import asyncio
import base64
import itertools
import json
import logging
import os
import uuid
from typing import Any, Coroutine, Optional, Tuple

import aiohttp
import grpc

from ..utils import serdes
from . import cosim_pb2, cosim_pb2_grpc

REFRESH_INTERVAL = 60 * 4


class MetadataClientInterceptor(grpc.aio.UnaryUnaryClientInterceptor):
    def __init__(self):
        self.metadata_to_add = None

    def set_uuid(self, uuid: str):
        self.metadata_to_add = [("session-uuid", uuid)]

    def _add_metadata(self, client_call_details):
        metadata = list(client_call_details.metadata) if client_call_details.metadata else []
        if self.metadata_to_add:
            metadata.extend(self.metadata_to_add)
        return client_call_details._replace(metadata=metadata)

    async def intercept_unary_unary(self, continuation, client_call_details, request):
        new_details = self._add_metadata(client_call_details)
        return await continuation(new_details, request)


class CosimClient:
    def __init__(self, grpc_host: str, api_key: str, address: str, job_id: str, host: str, insecure: bool = False):
        self.grpc_host = grpc_host
        self.api_key = api_key
        self.address = address
        self.job_id = job_id
        self.host = host
        self.insecure = insecure

        self.channel: Optional[grpc.aio.Channel] = None
        self.cosim_stub: Optional['cosim_pb2_grpc.CosimStub'] = None
        self.auth_stub: Optional['cosim_pb2_grpc.CosimStub'] = None

        self._produce_counter = itertools.count(start=1)
        self._consume_counter = itertools.count(start=1)

        self._metadata_interceptor = MetadataClientInterceptor()
        self._refresh_task: Optional[asyncio.Task] = None
        self._stop_refresh = asyncio.Event()

    async def __aenter__(self):
        await self.connect()
        authorized, uuid = await self.authorize()
        self._metadata_interceptor.set_uuid(uuid)
        if not authorized:
            await self.terminate()
            raise Exception("Authentication with CosimClient failed.")

        self._refresh_task = asyncio.create_task(self._refresh_loop())
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.terminate()

    def create_channel(self):
        if self.insecure:
            logging.warning("Using insecure gRPC connection.")
            return grpc.aio.insecure_channel(self.grpc_host, interceptors=(self._metadata_interceptor,))
        
        logging.info("Using SSL/TLS for gRPC connection.")
        if os.environ.get("COSIM_TLS_CERTIFICATE"):
            certificate_chain = base64.b64decode(os.environ['COSIM_TLS_CERTIFICATE'])
            credentials = grpc.ssl_channel_credentials(root_certificates=certificate_chain)
            channel = grpc.aio.secure_channel(self.grpc_host, credentials, interceptors=(self._metadata_interceptor,))
        else:
            credentials = grpc.ssl_channel_credentials()
            channel = grpc.aio.secure_channel(self.grpc_host, credentials, interceptors=(self._metadata_interceptor,))
            
        return channel

    async def connect(self):
        logging.info(f"Connecting to gRPC server at {self.grpc_host}")
        self.channel = self.create_channel()
        await self.channel.channel_ready()
        self.cosim_stub = cosim_pb2_grpc.CosimStub(self.channel)
        self.auth_stub = cosim_pb2_grpc.CosimStub(self.channel)
        logging.info("Connected to gRPC server.")

    async def _refresh_loop(self):
        while not self._stop_refresh.is_set():
            try:
                try:
                    await asyncio.wait_for(self._stop_refresh.wait(), timeout=REFRESH_INTERVAL)
                    break
                except asyncio.TimeoutError:
                    pass

                if not self._stop_refresh.is_set():
                    logging.info("Refreshing authorization token...")
                    authorized, new_uuid = await self.authorize()
                    if authorized:
                        self._metadata_interceptor.set_uuid(new_uuid)
                        logging.info("Authorization token refreshed successfully.")
                    else:
                        logging.error("Failed to refresh authorization token.")
                        self._stop_refresh.set()
                        await self.terminate()
            except Exception as e:
                logging.error(f"Error in refresh loop: {e}")
                continue

    async def get_auth_token(self) -> Optional[str]:
        """Get a fresh JWT token from the django server."""
        async with aiohttp.ClientSession() as session:
            url = f"{self.host}/simulations/jobs/authorization/{self.job_id}"
            params = {"audience": "SimBed", "permission": "RUN_SIMULATION"}
            headers = {"X_API_KEY": self.api_key}

            try:
                async with session.get(url, params=params, headers=headers) as res:
                    if res.status != 200:
                        logging.error(f"Authentication failed with status {res.status}")
                        return None
                    data = await res.json()
                    return data.get('jwt')
            except aiohttp.ClientError as e:
                logging.error(f"Failed to get auth token: {e}")
                return None

    async def authorize(self) -> Tuple[bool, Optional[str]]:
        jwt_token = await self.get_auth_token()
        if not jwt_token:
            return False, None

        auth_request = cosim_pb2.Authorize(
            auth_token=jwt_token,
            cluster_handle_address=self.address,
        )
        try:
            response: cosim_pb2.AuthorizeResponse = await self.auth_stub.AuthorizeCall(auth_request)
            if response.success:
                logging.info("Authentication successful.")
                return True, response.session_uuid
            else:
                logging.error(f"Authentication failed: {response.message}")
                return False, None
        except grpc.aio.AioRpcError as e:
            logging.error(f"Authentication RPC failed: {e}")
            return False, None

    async def _send_simulation_action(
        self,
        action: cosim_pb2.SimulationAction,
        retry_on_expiry: bool = True
    ) -> Any:
        try:
            logging.debug(f"Sending SimulationAction: {action}")
            response: cosim_pb2.SimulationResponse = await self.cosim_stub.SimulationCall(action)

            if response.state != cosim_pb2.State.SUCCESS:
                logging.error(f"Unexpected response state: {response.state}")
                raise Exception("Unexpected response state.")

            # TODO-tindell we can assume mismatches won't happen, and panic if they do elsewhere
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

    async def terminate(self):
        """Cleanup resources and stop the refresh loop."""
        if self._refresh_task is not None:
            self._stop_refresh.set()
            await self._refresh_task
            self._refresh_task = None

        if self.channel:
            await self.channel.close()
            logging.info("gRPC channel closed.")
        logging.info("CosimClient terminated.")

    async def produce(
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

        try:
            response = await self._send_simulation_action(
                simulation_action,
            )
            logging.info(f"Produced message with index {index}: {value}")
            return index, response
        except Exception as e:
            logging.error(f"Produce operation failed for index {index}: {e}")
            raise e

    async def consume(
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
        try:
            response = await self._send_simulation_action(
                simulation_action,
            )
            logging.info(f"Consumed message with index {index}: {response}")
            return index, response
        except Exception as e:
            logging.error(f"Consume operation failed for index {index}: {e}")
            raise e
