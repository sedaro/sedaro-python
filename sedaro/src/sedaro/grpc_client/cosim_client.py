from concurrent.futures import ThreadPoolExecutor
import logging
import threading
from typing import Iterator
import grpc
from google.protobuf.json_format import MessageToJson
from . import cosim_pb2 
from . import cosim_pb2_grpc
import json
import numpy as np
import requests
import settings


def deser(v):
    return json.loads(v)["payload"]


def serdes(v):
    if type(v) is dict and 'ndarray' in v:
        return np.array(v['ndarray'])
    if type(v) is np.ndarray:
        return {'ndarray': v.tolist()}
    if type(v) is dict:
        return {k: serdes(v) for k, v in v.items()}
    if type(v) is list or type(v) is tuple:
        return [serdes(v) for v in v]
    return v


class MessageGenerator:

    def __init__(self, executor, channel):
        self._executor = executor
        self._channel = channel
        self._stub = cosim_pb2_grpc.CosimStub(channel)
        self.close_stream = threading.Event()
        self._variable_consume_blocker = {}
        self._variable_produce_blocker = {}
        self._variable_blocker = {}
        self._local_storage = {}
        self._auth_payload = None
        self._expired = False
        self.queue = []

    def _response_watcher(self, response_iterator):

        for response in response_iterator:
            if response.action == cosim_pb2.CosimActionType.COSIM_ACTION_AUTHENTICATE:
                logging.info("Received auth response: %s",
                             MessageToJson(response)
                             )
                self._local_storage["auth"] = response
                self._variable_blocker["auth"].set()
            else:
                if response.state == "EXPIRED":
                    self._expired = True
                if response.action == cosim_pb2.CosimActionType.COSIM_ACTION_CONSUME:
                    self._local_storage[response.external_state_block_id] = response
                    logging.info("Received response: %s",
                                 MessageToJson(response))
                    self._variable_consume_blocker[response.external_state_block_id].set(
                    )
                if response.action == cosim_pb2.CosimActionType.COSIM_ACTION_PRODUCE:
                    logging.info("Received response: %s",
                                 MessageToJson(response))
                    self._variable_produce_blocker[response.external_state_block_id].set(
                    )

        print("END")

    def consume(self, x, agent_id):
        if x not in self._variable_consume_blocker:
            self._variable_consume_blocker[x] = threading.Event()
        else:
            self._variable_consume_blocker[x].clear()
        self._send(cosim_pb2.CosimRequest(action=cosim_pb2.CosimActionType.COSIM_ACTION_CONSUME,
                                          external_state_block_id=x, agent_id=agent_id))
        self._variable_consume_blocker[x].wait()
        consumed_value = self._local_storage[x]
        if self._expired:
            if self._auth_payload:
                refresh = self.authenticate(self._auth_payload["api_key"], self._auth_payload["address"], self._auth_payload["job_id"])
                if refresh:
                    self._expired = True
                    return self.consume(x, agent_id)
                else:
                    raise Exception("Authentication failed")
            else:
                    raise Exception("Authentication failed")
        print()
        return serdes(deser(consumed_value.value))

    def produce(self, x, agent_id, value):
        if x not in self._variable_produce_blocker:
            self._variable_produce_blocker[x] = threading.Event()
        else:
            self._variable_produce_blocker[x].clear()
        new_value = json.dumps({"payload": serdes(value)})
        self._send(cosim_pb2.CosimRequest(action=cosim_pb2.CosimActionType.COSIM_ACTION_PRODUCE,
                   external_state_block_id=x, agent_id=agent_id, value=new_value))
        self._variable_produce_blocker[x].wait()
        if self._expired:
            if self._auth_payload:
                refresh = self.authenticate(self._auth_payload["api_key"], self._auth_payload["address"], self._auth_payload["job_id"])
                if refresh:
                    self._expired = True
                    return self.produce(x, agent_id, value)
                else:
                    raise Exception("Authentication failed")
            else:
                raise Exception("Authentication failed")
        return value

    def authenticate(self, api_key, address, job_id, host):
        self._variable_blocker["auth"] = threading.Event()
        res = requests.get(f"http://{host}/simulations/jobs/{job_id}/authorization?audience={"SimBed"}&permission=RUN_SIMULATION", headers={"X_API_KEY": api_key})
        print(res.json())
        self._send(cosim_pb2.CosimRequest(
            auth_token=cosim_pb2.AuthMETA(api_key=api_key, auth_token=res.json()['jwt']), action=cosim_pb2.CosimActionType.COSIM_ACTION_AUTHENTICATE, cluster_handle_address=address, job_id=job_id))
        self._variable_blocker["auth"].wait()
        success = self._local_storage["auth"]
        valid = (success.state == "True")
        if valid:
            self._auth_payload = {"api_key": api_key, "address": address, "job_id": job_id}
        return valid
    
    def terminate(self):
        self.close_stream.set()
        self.queue = []
        print("TERMINATING...")
        return

    def _send(self, message):
        print("SENDING")
        self.queue.append(message)

    def _stream(self):
        while not self.close_stream.is_set():
            if self.queue:
                print("SENDING MESSAGE")
                new_message = self.queue.pop(0)
                yield new_message

    def open_stream(self):
        responses = self._stub.CosimCall(self._stream())
        self._executor.submit(self._response_watcher, responses)

class CosimRunner:
    def __init__(self):
        self.message_generator = None
        self._hold_stream = threading.Event()
        self._error = None
        
    def _open(self, api_key, address, job_id):
        try:
            root_certs = settings.CLIENT_ROOT_CERT
            if not root_certs:
                self._error = e
                self._hold_stream.set()
                raise Exception("No root certificate provided")
            credentials = grpc.ssl_channel_credentials(root_certs)
        except Exception as e:
            print("Error loading CA certificate: " + str(e))
            self._error = e
            self._hold_stream.set()
            raise Exception("Error loading CA certificate: " + str(e))
        try:
            with grpc.secure_channel('localhost:50049', credentials) as channel:
                message_generator = MessageGenerator(
                    ThreadPoolExecutor(max_workers=10), channel)
                message_generator.open_stream()
                print("Stream opened")
                success = message_generator.authenticate(
                    api_key, address, job_id)
                if not success:
                    print("Authentication failed")
                    message_generator.terminate()
                    raise Exception("Authentication failed")
                self.message_generator = message_generator
                self._hold_stream.set()
                message_generator.close_stream.wait(timeout=None)
        except Exception as e:
            self._error = e
            self._hold_stream.set()
            raise Exception("Error opening stream: " + str(e))
            
            
    def open(self, api_key, address, job_id):
        try:
            ThreadPoolExecutor(max_workers=5).submit(self._open, api_key, address, job_id)
            self._hold_stream.wait()
            return
        except Exception as e:
            raise e
    
        
