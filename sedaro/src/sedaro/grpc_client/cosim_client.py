import asyncio
import itertools
import json
import logging
import uuid
from typing import Any, Coroutine, Optional, Tuple

import aiohttp
import grpc

from ..utils import serdes
from . import cosim_pb2, cosim_pb2_grpc


class MetadataClientInterceptor(grpc.aio.UnaryUnaryClientInterceptor):
    def __init__(self, metadata_to_add):
        self.metadata_to_add = metadata_to_add

    def _add_metadata(self, client_call_details):
        metadata = list(client_call_details.metadata) if client_call_details.metadata else []
        metadata.extend(self.metadata_to_add)
        return client_call_details._replace(metadata=metadata)

    async def intercept_unary_unary(self, continuation, client_call_details, request):
        new_details = self._add_metadata(client_call_details)
        return await continuation(new_details, request)


class CosimClient:
    def __init__(self, grpc_host: str, api_key: str, address: str, job_id: str, host: str):
        self.grpc_host = grpc_host
        self.api_key = api_key
        self.address = address
        self.job_id = job_id
        self.host = host
        self.uuid = uuid.uuid4()  # FIXMETL this needs to change to a secrets.token_hex call on the server on the first authenticate

        self.channel: Optional[grpc.aio.Channel] = None
        self.cosim_stub: Optional['cosim_pb2_grpc.CosimStub'] = None
        self.auth_stub: Optional['cosim_pb2_grpc.CosimStub'] = None

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
        metadata_interceptor = MetadataClientInterceptor([("session-uuid", self.uuid.hex)])
        logging.info(f"Connecting to gRPC server at {self.grpc_host} with session UUID: {self.uuid}")
        self.channel = grpc.aio.insecure_channel(self.grpc_host, interceptors=(metadata_interceptor,))
        await self.channel.channel_ready()
        self.cosim_stub = cosim_pb2_grpc.CosimStub(self.channel)
        self.auth_stub = cosim_pb2_grpc.CosimStub(self.channel)
        logging.info("Connected to gRPC server.")

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

        auth_request = cosim_pb2.Authenticate(
            auth_token=jwt_token,
            cluster_handle_address=self.address,
        )
        try:
            response: cosim_pb2.AuthenticateResponse = await self.auth_stub.AuthenticateCall(auth_request)
            if response.success:
                logging.info("Authentication successful.")
                return True
            else:
                logging.error(f"Authentication failed: {response.message}")
                return False
        except grpc.aio.AioRpcError as e:
            logging.error(f"Authentication RPC failed: {e}")
            return False

    async def _send_simulation_action(
        self,
        action: cosim_pb2.SimulationAction,
        expected_state: cosim_pb2.State,
        retry_on_expiry: bool = True
    ) -> Any:
        try:
            logging.debug(f"Sending SimulationAction: {action}")
            response: cosim_pb2.SimulationResponse = await self.cosim_stub.SimulationCall(action)

            if response.state != expected_state:
                # FIXMETL remove reauthentication logic from here and put it into a long running task.  This is not async safe.
                if response.state == cosim_pb2.State.FAILURE and retry_on_expiry and expected_state == cosim_pb2.State.SUCCESS:
                    logging.warning("Session expired. Re-authenticating and retrying call...")
                    if await self.authenticate():
                        return await self._send_simulation_action(action, expected_state, retry_on_expiry=False)
                logging.error(f"Unexpected response state: {response.state}")
                raise Exception("Unexpected response state.")

            # FIXMETL we can assume mismatches won't happen, and panic if they do elsewhere
            if action.WhichOneof("request") == "consume":
                consume_resp = response.WhichOneof("response")
                if consume_resp != "consume_response":
                    raise Exception("Expected ConsumeResponse.")
                return response.consume_response.value

            elif action.WhichOneof("request") == "produce":
                produce_resp = response.WhichOneof("response")
                if produce_resp != "produce_response":
                    raise Exception("Expected ProduceResponse.")
                return response.produce_response.index

            else:
                raise Exception("Unknown action type.")

        except grpc.aio.AioRpcError as e:
            logging.error(f"Simulation RPC failed: {e}")
            raise ConnectionError(f"Simulation RPC failed: {e}")

    def produce(
        self,
        external_state_id: str,
        agent_id: str,
        value: Any,
        timestamp: float = 0.0
    ) -> Coroutine[Any, Any, Tuple[int, Any]]:
        index = next(self._produce_counter)
        produce_action = cosim_pb2.Produce(
            index=index,
            value=json.dumps({"payload": serdes(value)})
        )
        simulation_action = cosim_pb2.SimulationAction(
            cluster_handle_address=self.address,
            job_id=self.job_id,
            agent_id=agent_id,
            external_state_block_id=external_state_id,
            time=timestamp,
        )
        simulation_action.produce.CopyFrom(produce_action)

        async def _produce_coroutine():
            try:
                response = await self._send_simulation_action(
                    simulation_action,
                    expected_state=cosim_pb2.State.SUCCESS
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
        time: float = None
    ) -> Coroutine[Any, Any, Tuple[int, Any]]:
        index = next(self._consume_counter)
        consume_action = cosim_pb2.Consume(
            index=index
        )
        simulation_action = cosim_pb2.SimulationAction(
            cluster_handle_address=self.address,
            job_id=self.job_id,
            agent_id=agent_id,
            external_state_block_id=external_state_id,
            time=time,
        )
        simulation_action.consume.CopyFrom(consume_action)

        async def _consume_coroutine():  # FIXMETL get around to removing these
            try:
                response = await self._send_simulation_action(
                    simulation_action,
                    expected_state=cosim_pb2.State.SUCCESS
                )
                logging.info(f"Consumed message with index {index}: {response}")
                return index, response
            except Exception as e:
                logging.error(f"Consume operation failed for index {index}: {e}")
                raise

        return _consume_coroutine()

    async def terminate(self):
        if self.channel:
            await self.channel.close()
            logging.info("gRPC channel closed.")
        logging.info("CosimClient terminated.")
