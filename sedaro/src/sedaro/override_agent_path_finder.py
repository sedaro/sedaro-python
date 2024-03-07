import flatten_json
from fuzzywuzzy import fuzz

"""
This class is used to help discover agent model parameter paths for use with overrides in the Sedaro API.
"""
class AgentModelParametersOverridePaths():
    def __init__(self, scenario_branch: str, agent_branch:str, agent_name:str):
        self.scenario_branch = scenario_branch
        self.agent_branch    = agent_branch
        self.agent_id_name_map, self.agent_name_id_map = self._create_agent_name_id_maps()
        self.path_to_agent_key = self._create_path_to_agent_dict(agent_name)

    def _create_agent_name_id_maps(self): 
        self.scenario_flat       = flatten_json.flatten( self.scenario_branch.data, '.') 
        agent_id_name_map   = { key.split('.')[1]: value for (key,value) in self.scenario_flat.items() if key.endswith('name') } 
        agent_name_id_map   = { value: key.split('.')[1] for (key,value) in self.scenario_flat.items() if key.endswith('name') } 
        return agent_id_name_map, agent_name_id_map

    def _create_path_to_agent_dict(self, agent_name):
        agent_flat = flatten_json.flatten( self.agent_branch.data, '.') 

        self.agent_branches_flat = { f"{self.agent_name_id_map[agent_name]}.data.{key}": value for (key,value) in agent_flat.items() }

        agent_block_id_name  = { blockID: block['name'] for (blockID, block) in self.agent_branch.data['blocks'].items() 
                                                                if 'name' in block }
        agent_block_id_type  = { blockID: block['type'] for (blockID, block) in self.agent_branch.data['blocks'].items() 
                                                                if 'type' in block }
        
        # Block Parameters
        agent_block_param_paths =  { f"{agent_name}/{block_label}/{parameter_key}": parameter_value 
                        for (block_key, block_parameters) in self.agent_branch.data['blocks'].items() 
                        for block_label in [agent_block_id_name[block_key] if block_key in agent_block_id_name else agent_block_id_type[block_key]] 
                        for (parameter_key, parameter_value ) in flatten_json.flatten(block_parameters, "/").items() } 

        # agent non-block parameters
        filter_list = ('blocks', 'index', '_')
        agent_root_param_paths = { f"{ agent_name }/root/{parameter_key}": parameter_value
                                    for (parameter_key, parameter_value) in flatten_json.flatten(self.agent_branch.data, '/').items() 
                                    if not parameter_key.startswith(filter_list) }
        # Combine them
        agent_block_param_paths  |= agent_root_param_paths

        return agent_block_param_paths
    
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
                return  self.path_to_agent_key[path] 
        else:
                return { "NotFoundPath": f"{path}", "Did you mean": self.findBestPathMatch(path) }

