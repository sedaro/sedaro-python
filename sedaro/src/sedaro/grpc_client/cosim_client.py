import asyncio
import itertools
import json
import logging
from typing import Any, Optional, Tuple, Coroutine

import aiohttp
import grpc

from ..utils import serdes
from . import cosim_pb2, cosim_pb2_grpc

class CosimClient:
    def __init__(self, grpc_host: str, api_key: str, address: str, job_id: str, host: str):
        self.grpc_host = grpc_host
        self.api_key = api_key
        self.address = address
        self.job_id = job_id
        self.host = host
        self.channel: Optional[grpc.aio.Channel] = None
        self.stub: Optional['cosim_pb2_grpc.CosimStub'] = None
        self.auth_payload = None
        self._stream_task = None
        self._stream = None
        self._response_queue = asyncio.Queue()

        self._produce_counter = itertools.count(start=1)
        self._consume_counter = itertools.count(start=1)

    async def __aenter__(self):
        await self.connect()
        authenticated = await self.authenticate()
        if not authenticated:
            await self.terminate()
            raise Exception("Authentication with CosimClient failed.")
        logging.info("Cosimulation session opened successfully.")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.terminate()

    async def connect(self):
        logging.info(f"Connecting to gRPC server at {self.grpc_host}")
        self.channel = grpc.aio.insecure_channel(self.grpc_host)
        await self.channel.channel_ready()
        self.stub = cosim_pb2_grpc.CosimStub(self.channel)
        logging.info("Connected to gRPC server.")

    async def _send_and_receive(
        self,
        request: cosim_pb2.CosimRequest,
        action_type: cosim_pb2.CosimActionType,
        identifier: Optional[str] = None,
        retry_on_expiry: bool = True
    ) -> Any:
        try:
            if action_type == cosim_pb2.CosimActionType.COSIM_ACTION_CONSUME:
                logging.info(f"Sending consume request: {request}")
            elif action_type == cosim_pb2.CosimActionType.COSIM_ACTION_PRODUCE:
                logging.info(f"Sending produce request: {request}")
            else:
                logging.warning(f"Sending request with unknown action type: {request}")
            
            response = await self.stub.CosimCall(request)

            if response.action != action_type:
                logging.warning(f"Ignoring unrelated response: {response}")
                raise Exception("Unrelated response received.")

            if identifier and response.external_state_block_id != identifier:
                logging.warning(f"Ignoring response with unmatched ID: {response.external_state_block_id}")
                raise Exception("Response ID does not match.")

            if response.state == "True":
                val = response.value if hasattr(response, 'value') else True
                if action_type == cosim_pb2.CosimActionType.COSIM_ACTION_CONSUME:
                    logging.info(f"Consumed ID: {identifier} and got value: {val}")
                if action_type == cosim_pb2.CosimActionType.COSIM_ACTION_PRODUCE:
                    logging.info(f"Produced ID: {identifier} and got value: {val}")
                return val

            elif response.state == "EXPIRED" and retry_on_expiry:
                logging.warning("Session expired. Re-authenticating and retrying call...")
                await self._handle_expiration()
                return await self._send_and_receive(request, action_type, identifier, retry_on_expiry=False)
            else:
                error_msg = response.value if hasattr(response, 'value') else "Unknown error"
                raise Exception(f"{action_type} failed: {error_msg}")

        except grpc.aio.AioRpcError as e:
            logging.error(f"RPC failed: {e}")
            raise ConnectionError(f"RPC failed: {e}")

    # FIXMETL This should be extracted into middleware

    async def authenticate(self) -> bool:
        async with aiohttp.ClientSession() as session:
            url = f"{self.host}/simulations/jobs/authorization/{self.job_id}"
            params = {"audience": "SimBed", "permission": "RUN_SIMULATION"}
            headers = {"X_API_KEY": self.api_key}
            logging.info(f"Authenticating with URL: {url} and params: {params}")

            async with session.get(url, params=params, headers=headers) as res:
                if res.status != 200:
                    logging.error(f"Authentication failed with status {res.status}")
                    return False
                data = await res.json()
                jwt_token = data.get('jwt')
                if not jwt_token:
                    logging.error("JWT token not found in authentication response")
                    return False

        auth_request = cosim_pb2.CosimRequest(
            auth_token=cosim_pb2.AuthMeta(auth_token=jwt_token),
            action=cosim_pb2.CosimActionType.COSIM_ACTION_AUTHENTICATE,
            cluster_handle_address=self.address,
            job_id=self.job_id
        )
        response = await self._send_and_receive(
            auth_request,
            cosim_pb2.CosimActionType.COSIM_ACTION_AUTHENTICATE
        )
        if response:
            self.auth_payload = {
                "api_key": self.api_key,
                "address": self.address,
                "job_id": self.job_id,
                "host": self.host
            }
            logging.info("Authentication successful.")
            return True
        logging.error("Authentication failed.")
        return False

    def produce(
        self, 
        external_state_id: str, 
        agent_id: str, 
        value: Any, 
        timestamp: float = 0.0
    ) -> Coroutine[Any, Any, Any]:
        index = next(self._produce_counter)
        produce_request = cosim_pb2.CosimRequest(
            action=cosim_pb2.CosimActionType.COSIM_ACTION_PRODUCE,
            external_state_block_id=external_state_id,
            agent_id=agent_id,
            value=json.dumps({"payload": serdes(value)}),
            time=timestamp,
            index=index
        )
        
        async def _produce_coroutine():
            try:
                response = await self._send_and_receive(
                    produce_request,
                    cosim_pb2.CosimActionType.COSIM_ACTION_PRODUCE,
                    identifier=external_state_id
                )
                logging.info(f"Produced message with index {index}: {value}")
                return index, response
            except Exception as e:
                logging.error(f"Produce operation failed for index {index}: {e}")
                raise

        return _produce_coroutine()

    def consume(
        self, 
        external_state_id: str, 
        agent_id: str, 
        time: float = 0.0
    ) -> Coroutine[Any, Any, Tuple[Any, Any]]:
        index = next(self._consume_counter)
        consume_request = cosim_pb2.CosimRequest(
            action=cosim_pb2.CosimActionType.COSIM_ACTION_CONSUME,
            external_state_block_id=external_state_id,
            agent_id=agent_id,
            time=time,
            index=index,
        )
        
        async def _consume_coroutine():
            try:
                response = await self._send_and_receive(
                    consume_request,
                    cosim_pb2.CosimActionType.COSIM_ACTION_CONSUME,
                    identifier=external_state_id,
                )
                logging.info(f"Consumed message with index {index}: {external_state_id}")
                return index, response
            except Exception as e:
                logging.error(f"Consume operation failed for index {index}: {e}")
                raise

        return _consume_coroutine()

    async def _handle_expiration(self):
        if not self.auth_payload:
            raise Exception("No authentication payload available for re-authentication.")

        success = await self.authenticate()
        if not success:
            raise Exception("Re-authentication failed after expiration.")

    async def terminate(self):
        if self._stream:
            await self._stream.done_writing()
        if self.channel:
            await self.channel.close()
            logging.info("gRPC channel closed.")
        logging.info("CosimClient terminated.")
