import flatten_json
from fuzzywuzzy import fuzz

"""
This class is used to help discover agent model parameter paths for use with overrides in the Sedaro API.
"""
class AgentModelParametersOverridePaths():
    def __init__(self, wildfire_scenario_branch: str, wildfire_agent_branch:str, agent_name='Wildfire'):
        self.wildfire_scenario_branch = wildfire_scenario_branch
        self.wildfire_agent_branch    = wildfire_agent_branch
        self.agent_id_name_map, self.agent_name_id_map = self._create_agent_name_id_maps()
        self.path_to_agent_key = self._create_path_to_agent_dict(agent_name)

    def _create_agent_name_id_maps(self): 
        self.scenario_flat       = flatten_json.flatten( self.wildfire_scenario_branch.data, '.') 
        agent_id_name_map   = { key.split('.')[1]: value for (key,value) in self.scenario_flat.items() if key.endswith('name') } 
        agent_name_id_map   = { value: key.split('.')[1] for (key,value) in self.scenario_flat.items() if key.endswith('name') } 
        return agent_id_name_map, agent_name_id_map

    def _create_path_to_agent_dict(self, agent_name='Wildfire'):
        agent_flat = flatten_json.flatten( self.wildfire_agent_branch.data, '.') 

        self.agent_branches_flat = { f"{self.agent_name_id_map[agent_name]}.data.{key}": value for (key,value) in agent_flat.items() }

        agent_block_id_name = { tokens[-2]: value for (key, value) in self.agent_branches_flat.items() if key.endswith('.name') and  'blocks' in key for tokens in [key.split('.')] } 
        agent_block_id_type = { tokens[-2]: value for (key,value) in self.agent_branches_flat.items() if key.endswith('.type') and 'blocks' in key for tokens in [key.split('.')]}

        # block parameters
        agent_key_to_path   = { key: f"{ self.agent_id_name_map[ agentId ]}/{ agent_block_id_name[BlockId] if BlockId in agent_block_id_name else agent_block_id_type[BlockId]}/{'/'.join(key.split('.')[4:])}" 
                                    for (key,value) in self.agent_branches_flat.items() if 'blocks' in key
                                    for (agentId,BlockId) in [ (key.split('.')[0], key.split('.')[3] )]  }
        # agent non-block parameters
        agent_param_to_path = {  key: f"{ self.agent_id_name_map[ agentId[0]]}/{'/'.join(agentdata)}" 
                                    for (key,value) in self.agent_branches_flat.items() if 'data' in key and 'blocks' not in key and '._' not in key and 'index' not in key
                                    for (agentId,agentdata) in [ (key.split('.')[0:1], key.split('.')[1:]) ]}
        # Combine them
        agent_key_to_path  |= agent_param_to_path

        path_to_agent_key   = { value: key for (key,value) in agent_key_to_path.items() }
        return path_to_agent_key
    
    def listPaths(self) -> list[str]:
            return list(self.path_to_agent_key.keys())

    def findBestPathMatch(self, search_for_path:str) -> str:
            return max(self.path_to_agent_key.keys(), 
                       key=lambda path: fuzz.ratio(search_for_path, path ))
    
    # finds the top n best matches
    def findPathMatches(self, search_for_path:str, number_matches=5) -> list[str]:
            return sorted(self.path_to_agent_key.keys(), 
                          key=lambda path: fuzz.ratio(search_for_path, path ), reverse=True)[0:number_matches]

    def findValueOf(self, path:str) -> str | float | int | dict | list:
        if path in self.path_to_agent_key:
                return self.agent_branches_flat[ self.path_to_agent_key[path] ]
        else:
                return { "NotFoundPath": f"{path}", "Did you mean": self.findBestPathMatch(path) }

