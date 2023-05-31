import concurrent.futures
import json
import os
import pathlib
from random import choice
import shutil
from string import ascii_letters
from typing import Dict, List, Optional, Tuple
from zipfile import ZipFile, ZIP_DEFLATED

from sedaro_base_client import Configuration
from sedaro_base_client.api_client import ApiClient
from sedaro_base_client.apis.tags import branches_api

from .branch_client import BranchClient
from .exceptions import SedaroApiException
from .settings import COMMON_API_KWARGS
from .sim_client import SimClient
from .utils import body_from_res, parse_urllib_response


class SedaroApiClient(ApiClient):
    """A client to interact with the Sedaro API"""

    def __init__(self, api_key, host='https://api.sedaro.com', *args, **kwargs):
        return super().__init__(
            configuration=Configuration(host=host),
            *args,
            **kwargs,
            header_name='X_API_KEY',
            header_value=api_key
        )

    def get_branch(self, id: int) -> BranchClient:
        """Gets a Sedaro Branch based on the given `id` and creates a `BranchClient` from the response. The branch must
        be accessible to this `SedaroApiClient` via the `api_key`.

        Args:
            id (int): the id of the desired Sedaro Branch

        Returns:
            BranchClient: A `BranchClient` object used to interact with the data attached to the corresponding Sedaro
            Branch.
        """
        branches_api_instance = branches_api.BranchesApi(self)
        # res = branches_api_instance.get_branch(path_params={'branchId': id}) # TODO: temp_crud
        # return BranchClient(res.body, self)
        res = branches_api_instance.get_branch(
            path_params={'branchId': id}, **COMMON_API_KWARGS)
        return BranchClient(body_from_res(res), self)

    def download_data_in_parallel(self, agents, id, dirname: str):
        for agent in agents:
            agentData = self.get_data(id, limit=None, streams=[(agent,)], bulktool=True)
            with open(f'{dirname}/{agent}.json', 'w') as fd:
                json.dump(agentData, fd)
        return agents

    def download_data(self, branch, id, filename: str):
        # check if filename already exists
        path = pathlib.Path(filename)
        if path.exists():
            raise FileExistsError('Provided file name is already in use. Please try again with a different file name.')

        # create temp directory in which to build zip
        dirname = ''.join(choice(ascii_letters) for _ in range(32)) # random 32-char string
        assert '/' not in dirname # extra level of protection against bad removes later
        try:
            os.mkdir(dirname, mode=0o777)
            archive = ZipFile(filename, 'w')

            # get list of agents
            agents = []
            for agent in branch.Agent.get_all():
                agents.append(agent.id)
            
            # get data for one agent at a time
            MAX_CHUNKS = 4
            if len(agents) < MAX_CHUNKS:
                NUM_CHUNKS = len(agents)
            else:
                NUM_CHUNKS = MAX_CHUNKS
            chunks = []
            for _ in range(NUM_CHUNKS):
                chunks.append([])
            for i in range(len(agents)):
                chunks[i % NUM_CHUNKS].append(agents[i])
            with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_CHUNKS) as executor:
                _id = [id for _ in range(NUM_CHUNKS)]
                _dirname = [dirname for _ in range(NUM_CHUNKS)]
                done = executor.map(self.download_data_in_parallel, chunks, _id, _dirname)
            for chunk in done:
                for agent in chunk:
                    archive.write(f'{dirname}/{agent}.json', f'{agent}.json', ZIP_DEFLATED)
        
        except Exception:
            # clean up
            try:
                archive.close()
            except Exception:
                pass
            if pathlib.Path(filename).exists():
                os.remove(filename)
            if pathlib.Path(dirname).exists():
                shutil.rmtree(dirname, ignore_errors=True)
        
        # save zip file and delete temp directory
        archive.close()
        shutil.rmtree(dirname, ignore_errors=True)

        print(f'ZIP file created: {filename}')

    def get_data(self,
            id,
            start: float = None,
            stop: float = None,
            binWidth: float = None,
            limit: float = None,
            axisOrder: str = None,
            bulktool: bool = False,
            streams: Optional[List[Tuple[str, ...]]] = None
        ):
        """Simplified Data Service getter with significantly higher performance over the Swagger-generated client."""
        url = f'/data/{id}?'
        if start is not None:
            url += f'&start={start}'
        if stop is not None:
            url += f'&stop={stop}'
        if binWidth is not None:
            url += f'&binWidth={binWidth}'
        elif limit is not None:
            url += f'&limit={limit}'
        elif bulktool == True:
            url += f'&bulktool={bulktool}'
        streams = streams or []
        if len(streams) > 0:
            encodedStreams = ','.join(['.'.join(x) for x in streams])
            url += f'&streams={encodedStreams}'
        if axisOrder is not None:
            if axisOrder not in {'TIME_MAJOR',  'TIME_MINOR'}:
                raise ValueError(
                    'axisOrder must be either "TIME_MAJOR" or "TIME_MINOR"')
            url += f'&axisOrder={axisOrder}'
        response = self.call_api(url, 'GET')
        _response = None
        try:
            _response = parse_urllib_response(response)
            if response.status != 200:
                raise Exception()
        except:
            reason = _response['error']['message'] if _response and 'error' in _response else 'An unknown error occurred.'
            raise SedaroApiException(status=response.status, reason=reason)
        return _response

    def get_sim_client(self, branch_id: int):
        """Creates and returns a Sedaro SimClient

        Args:
            branch_id (int): id of the desired Sedaro Scenario Branch to interact with its simulations (jobs)

        Returns:
            SimClient: a Sedaro SimClient
        """
        return SimClient(self, branch_id)

    def send_request(self, resource_path: str, method: str, body: Optional[Dict] = None):
        """Send a request to the Sedaro server

        Args:
            resource_path (str): url path (everything after the host) for desired route
            method (str): HTTP method ('GET', 'POST', 'DELETE'...etc)
            body (Optional[Union[str, bytes]], optional): Body of the request. Defaults to None.

        Returns:
            Dict: dictionary from the response body
        """
        headers = {}
        if body is not None:
            body = json.dumps(body)
            headers['Content-Type'] = 'application/json'
        res = self.call_api(
            resource_path,
            method.upper(),
            headers=headers,
            body=body
        )
        return parse_urllib_response(res)
