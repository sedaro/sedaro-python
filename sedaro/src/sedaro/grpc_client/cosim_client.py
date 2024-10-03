import asyncio
import json
import logging
from typing import Any, Optional, Tuple

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
        self.expired = False
        self._stream_task = None
        self._stream = None
        self._response_queue = asyncio.Queue()

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
        self._stream = self.stub.CosimCall()
        self._stream_task = asyncio.create_task(self._receive_messages())
        logging.info("Connected and stream task started.")

    async def _receive_messages(self):
        try:
            async for response in self._stream:
                await self._response_queue.put(response)
        except grpc.aio.AioRpcError as e:
            logging.error(f"Stream closed with error: {e}")
        finally:
            await self._response_queue.put(None)

    async def _send_message(self, message: 'cosim_pb2.CosimRequest'):
        if not self._stream:
            raise ConnectionError("Stream is not initialized. Call connect() first.")
        await self._stream.write(message)
        logging.debug(f"Sent message: {message}")

    async def _send_and_receive(
        self,
        request: 'cosim_pb2.CosimRequest',
        action_type: 'cosim_pb2.CosimActionType',
        identifier: Optional[str] = None,
        retry_on_expiry: bool = True
    ) -> Any:
        await self._send_message(request)
        logging.info(f"Sent {action_type} request")

        while True:
            response = await self._response_queue.get()
            if response is None:
                raise ConnectionError("Stream closed unexpectedly.")

            # FIXMETL This shouldn't ever happen
            if response.action != action_type:
                logging.warning(f"Ignoring unrelated response: {response}")
                continue

            # FIXMETL This shouldn't ever happen
            if identifier and response.external_state_block_id != identifier:
                logging.warning(f"Ignoring response with unmatched ID: {response.external_state_block_id}")
                continue

            logging.debug(f"Received response: {response}")

            if response.state == "True":
                logging.info(f"{action_type} successful for ID: {identifier}")
                return response.value if hasattr(response, 'value') else True

            # FIXMETL This should be extracted with authenticate into middleware
            elif response.state == "EXPIRED" and retry_on_expiry:
                logging.warning("Session expired. Re-authenticating...")
                await self._handle_expiration()
                return await self._send_and_receive(request, action_type, identifier, retry_on_expiry=False)
            else:
                error_msg = response.value if hasattr(response, 'value') else "Unknown error"
                raise Exception(f"{action_type} failed: {error_msg}")

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

    async def produce(self, external_state_id: str, agent_id: str, value: Any, timestamp: float = 0.0) -> Any:
        produce_request = cosim_pb2.CosimRequest(
            action=cosim_pb2.CosimActionType.COSIM_ACTION_PRODUCE,
            external_state_block_id=external_state_id,
            agent_id=agent_id,
            value=json.dumps({"payload": serdes(value)}),
            time=timestamp
        )
        response = await self._send_and_receive(
            produce_request,
            cosim_pb2.CosimActionType.COSIM_ACTION_PRODUCE,
            identifier=external_state_id
        )
        return response

    async def consume(self, external_state_id: str, agent_id: str, time: float = 0.0) -> Tuple[Any, Any]:
        consume_request = cosim_pb2.CosimRequest(
            action=cosim_pb2.CosimActionType.COSIM_ACTION_CONSUME,
            external_state_block_id=external_state_id,
            agent_id=agent_id,
            time=time
        )
        response = await self._send_and_receive(
            consume_request,
            cosim_pb2.CosimActionType.COSIM_ACTION_CONSUME,
            identifier=external_state_id
        )
        # return serdes(json.loads(response)["payload"]), response
        return response, response

    async def run(self, fn_strings: str | list, args: list) -> list:
        """
        Executes a list of consume/produce operations concurrently.
        """
        if isinstance(fn_strings, list):
            fns = fn_strings
        else:
            fns = [
                (self.consume if a == "c" else self.produce) for a in fn_strings
            ]

        paired_fns = []
        for fn, arg in zip(fns, args):
            if arg is None:
                paired_fns.append(fn())
            elif isinstance(arg, Iterable) and not isinstance(arg, (str, bytes)):
                paired_fns.append(fn(*arg))
            else:
                paired_fns.append(fn(arg))

        results = await asyncio.gather(*paired_fns, return_exceptions=True)

        for result in results:
            if isinstance(result, Exception):
                logging.error(f"Function execution failed: {result}")
                raise result

        return results

    async def _handle_expiration(self):
        if not self.auth_payload:
            raise Exception("No authentication payload available for re-authentication.")

        success = await self.authenticate()
        if not success:
            raise Exception("Re-authentication failed after expiration.")
        self.expired = False

    async def terminate(self):
        if self._stream:
            await self._stream.done_writing()
        if self.channel:
            await self.channel.close()
            logging.info("gRPC channel closed.")
        if self._stream_task:
            self._stream_task.cancel()
            try:
                await self._stream_task
            except asyncio.CancelledError:
                logging.info("Stream task cancelled.")
        logging.info("CosimClient terminated.")
