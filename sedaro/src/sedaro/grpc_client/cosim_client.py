import asyncio
import json
import logging
from typing import Dict

import aiohttp  # Asynchronous HTTP client
import grpc
from google.protobuf.json_format import MessageToJson

from ..utils import serdes
from . import cosim_pb2, cosim_pb2_grpc


def deser(v):
    return json.loads(v)["payload"]


class MessageGenerator:
    def __init__(self, channel: grpc.aio.Channel):
        self._channel = channel
        self._stub = cosim_pb2_grpc.CosimStub(channel)
        self.close_stream = asyncio.Event()
        self._variable_consume_blocker: Dict[str, asyncio.Event] = {}
        self._variable_produce_blocker: Dict[str, asyncio.Event] = {}
        self._variable_blocker: Dict[str, asyncio.Event] = {}
        self._local_storage: Dict[str, cosim_pb2.CosimResponse] = {}
        self._auth_payload = None
        self._expired = False
        self.queue = asyncio.Queue()
        self._response_task = None

    async def _response_watcher(self, response_iterator):
        async for response in response_iterator:
            if response.action == cosim_pb2.CosimActionType.COSIM_ACTION_AUTHENTICATE:
                logging.info("Received auth response: %s",
                             MessageToJson(response))
                self._local_storage["auth"] = response
                event = self._variable_blocker.get("auth")
                if event:
                    event.set()
            else:
                if response.state == "False":
                    raise Exception("Error: " + response.value)
                if response.state == "EXPIRED":
                    self._expired = True
                if response.action == cosim_pb2.CosimActionType.COSIM_ACTION_CONSUME:
                    self._local_storage[response.external_state_block_id] = response
                    logging.info("Received response: %s",
                                 MessageToJson(response))
                    event = self._variable_consume_blocker.get(response.external_state_block_id)
                    if event:
                        event.set()
                if response.action == cosim_pb2.CosimActionType.COSIM_ACTION_PRODUCE:
                    logging.info("Received response: %s",
                                 MessageToJson(response))
                    event = self._variable_produce_blocker.get(response.external_state_block_id)
                    if event:
                        event.set()

    async def consume(self, x: str, agent_id: str, time: float = None):
        if x not in self._variable_consume_blocker:
            self._variable_consume_blocker[x] = asyncio.Event()
        else:
            self._variable_consume_blocker[x].clear()

        request = cosim_pb2.CosimRequest(
            action=cosim_pb2.CosimActionType.COSIM_ACTION_CONSUME,
            external_state_block_id=x,
            agent_id=agent_id,
            time=time
        )
        await self._send(request)

        await self._variable_consume_blocker[x].wait()

        consumed_value = self._local_storage[x]
        if self._expired:
            if self._auth_payload:
                refresh = await self.authenticate(
                    self._auth_payload["api_key"],
                    self._auth_payload["address"],
                    self._auth_payload["job_id"],
                    self._auth_payload["host"]
                )
                if refresh:
                    self._expired = False
                    return await self.consume(x, agent_id, time)
                else:
                    raise Exception("Authentication failed")
            else:
                raise Exception("Authentication failed")
        return serdes(deser(consumed_value.value))

    async def produce(self, x: str, agent_id: str, value, time: float = None):
        if x not in self._variable_produce_blocker:
            self._variable_produce_blocker[x] = asyncio.Event()
        else:
            self._variable_produce_blocker[x].clear()

        new_value = json.dumps({"payload": serdes(value)})

        request = cosim_pb2.CosimRequest(
            action=cosim_pb2.CosimActionType.COSIM_ACTION_PRODUCE,
            external_state_block_id=x,
            agent_id=agent_id,
            value=new_value,
            time=time if time else 0.0
        )
        await self._send(request)

        await self._variable_produce_blocker[x].wait()

        if self._expired:
            if self._auth_payload:
                refresh = await self.authenticate(
                    self._auth_payload["api_key"],
                    self._auth_payload["address"],
                    self._auth_payload["job_id"],
                    self._auth_payload["host"]
                )
                if refresh:
                    self._expired = False
                    return await self.produce(x, agent_id, value, time)
                else:
                    raise Exception("Authentication failed")
            else:
                raise Exception("Authentication failed")
        return value

    async def authenticate(self, api_key: str, address: str, job_id: str, host: str):
        self._variable_blocker["auth"] = asyncio.Event()
        async with aiohttp.ClientSession() as session:
            url = f"{host}/simulations/jobs/authorization/{job_id}"
            params = {"audience": "SimBed", "permission": "RUN_SIMULATION"}
            headers = {"X_API_KEY": api_key}
            print(f"@=-=-=-=-Connecting to {host} to authenticate job {job_id} with url {url} and params {params}")
            async with session.get(url, params=params, headers=headers) as res:
                print(f"@=-=-=-=- Response status: {res.status}")
                if res.status != 200:
                    logging.error(f"Authentication HTTP request failed with status {res.status}")
                    return False
                data = await res.json()
                jwt_token = data.get('jwt')
                if not jwt_token:
                    logging.error("JWT token not found in authentication response")
                    return False

        request = cosim_pb2.CosimRequest(
            auth_token=cosim_pb2.AuthMeta(auth_token=jwt_token),
            action=cosim_pb2.CosimActionType.COSIM_ACTION_AUTHENTICATE,
            cluster_handle_address=address,
            job_id=job_id
        )
        await self._send(request)
        await self._variable_blocker["auth"].wait()

        success = self._local_storage.get("auth")
        if not success:
            logging.error("Authentication response not received")
            return False

        valid = (success.state == "True")
        if valid:
            self._auth_payload = {
                "api_key": api_key,
                "address": address,
                "job_id": job_id,
                "host": host
            }
        return valid

    async def terminate(self):
        self.close_stream.set()
        while not self.queue.empty():
            await self.queue.get()
        logging.debug("TERMINATING...")

    async def _send(self, message: cosim_pb2.CosimRequest):
        logging.debug("SENDING")
        await self.queue.put(message)

    async def _stream(self):
        while not self.close_stream.is_set():
            try:
                message = await asyncio.wait_for(self.queue.get(), timeout=1.0)
                yield message
            except asyncio.TimeoutError:
                continue

    async def open_stream(self):
        response_iterator = self._stub.CosimCall(self._stream())
        self._response_task = asyncio.create_task(self._response_watcher(response_iterator))


class CosimRunner:
    def __init__(self):
        self.message_generator: MessageGenerator = None
        self._hold_stream = asyncio.Event()
        self._error = None

    async def _open(self, api_key: str, address: str, job_id: str, host: str, grpc_host: str):
        try:
            logging.info(f"Using insecure channel to connect to {grpc_host}")
            channel = grpc.aio.insecure_channel(grpc_host)
            print("Channel created")
            await channel.channel_ready()
            print("Channel ready")
            message_generator = MessageGenerator(channel)

            await message_generator.open_stream()
            logging.debug("Stream opened")

            success = await message_generator.authenticate(api_key, address, job_id, host)
            if not success:
                logging.debug("Authentication failed")
                await message_generator.terminate()
                raise Exception("Authentication failed")

            self.message_generator = message_generator
            self._hold_stream.set()

            await message_generator.close_stream.wait()
        except Exception as e:
            logging.error(f"Error opening stream: {e}")
            self._error = e
            self._hold_stream.set()
            raise Exception("Error opening stream: " + str(e))

    async def open(self, api_key: str, address: str, job_id: str, host: str, grpc_host: str):
        try:
            self._hold_stream.clear()
            asyncio.create_task(self._open(api_key, address, job_id, host, grpc_host))
            await self._hold_stream.wait()
        except Exception as e:
            raise e

    async def terminate(self):
        if self.message_generator:
            await self.message_generator.terminate()
