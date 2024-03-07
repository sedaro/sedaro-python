import time
from pytest import approx

from config import API_KEY, HOST, WILDFIRE_SCENARIO_ID, WILDFIRE_A_T_ID

from sedaro import SedaroApiClient, AgentModelParametersOverridePaths


sedaroAPI = SedaroApiClient(api_key=API_KEY, host=HOST)


tradespace_overrides_dict = {
  "name": "Test Example",
  "variables": [
    {
      "name": "Baseline_mass",
      "path": "Wildfire/root/mass"
    },
    {
      "name": "SAR-10237_mass_delta",
      "equals": 2.20
    },
    {
      "name": "SAR-10239_mass_delta",
      "equals": 3.20
    },
    {
      "name": "P33081_mass_delta",
      "equals": -0.702
    },
    {
      "name": "Baseline_dry_inertia_X.X",
      "path": "Wildfire/root/inertia/0/0"
    },
    {
      "name": "Baseline_dry_inertia_Y.Y",
      "path": "Wildfire/root/inertia/1/1"
    },
    {
      "name": "Baseline_dry_inertia_Z.Z",
      "path": "Wildfire/root/inertia/2/2"
    }
  ],
  "overrides": [
    {
      "path": "Wildfire/root/mass",
      "sim_index": [ 
                      {"fn": "=", "arg": "Baseline_mass"}, 
                      {"fn": "+", "arg": "SAR-10237_mass_delta"}, 
                      {"fn": "+", "arg": "SAR-10239_mass_delta"}, 
                      {"fn": "+", "arg": "P33081_mass_delta"}, 
                  ]
    },
    {
      "agent_key": "NT06aqHUT5djI1_JPAsck.data.inertia.0.0",
      "sim_index": [ 
                      {"fn": "=", "arg": "Baseline_dry_inertia_X.X"}, 
                      { "fn_chain": [
                          {"fn": "/", "arg": "Baseline_mass"}, 
                          {"fn": "*", "arg": "SAR-10237_mass_delta"}, 
                          {"fn": "+", "arg": "Baseline_dry_inertia_X.X" } ] 
                      },
                      { "fn_chain": [
                          {"fn": "/", "arg": "Baseline_mass"}, 
                          {"fn": "*", "arg": "SAR-10239_mass_delta"}, 
                          {"fn": "+", "arg": "Baseline_dry_inertia_X.X" } ] 
                      },
                      { "fn_chain": [
                          {"fn": "/", "arg": "Baseline_mass"}, 
                          {"fn": "*", "arg": "P33081_mass_delta"}, 
                          {"fn": "+", "arg": "Baseline_dry_inertia_X.X" } ] 
                      },
                  ]
    },
    {
      "agent_key": "NT06aqHUT5djI1_JPAsck.data.inertia.1.1",
      "sim_index": [ 
                      {"fn": "=", "arg": "Baseline_dry_inertia_Y.Y"}, 
                      { "fn_chain": [
                          {"fn": "/", "arg": "Baseline_mass"}, 
                          {"fn": "*", "arg": "SAR-10237_mass_delta"}, 
                          {"fn": "+", "arg": "Baseline_dry_inertia_Y.Y" } ] 
                      },
                      { "fn_chain": [
                          {"fn": "/", "arg": "Baseline_mass"}, 
                          {"fn": "*", "arg": "SAR-10239_mass_delta"}, 
                          {"fn": "+", "arg": "Baseline_dry_inertia_Y.Y" } ] 
                      },
                      { "fn_chain": [
                          {"fn": "/", "arg": "Baseline_mass"}, 
                          {"fn": "*", "arg": "P33081_mass_delta"}, 
                          {"fn": "+", "arg": "Baseline_dry_inertia_Y.Y" } ] 
                      },
                  ]
    },
    {
      "agent_key": "NT06aqHUT5djI1_JPAsck.data.inertia.2.2",
      "sim_index": [ 
                      {"fn": "=", "arg": "Baseline_dry_inertia_Z.Z"}, 
                      { "fn_chain": [
                          {"fn": "/", "arg": "Baseline_mass"}, 
                          {"fn": "*", "arg": "SAR-10237_mass_delta"}, 
                          {"fn": "+", "arg": "Baseline_dry_inertia_Z.Z" } ] 
                      },
                      { "fn_chain": [
                          {"fn": "/", "arg": "Baseline_mass"}, 
                          {"fn": "*", "arg": "SAR-10239_mass_delta"}, 
                          {"fn": "+", "arg": "Baseline_dry_inertia_Z.Z" } ] 
                      },
                      { "fn_chain": [
                          {"fn": "/", "arg": "Baseline_mass"}, 
                          {"fn": "*", "arg": "P33081_mass_delta"}, 
                          {"fn": "+", "arg": "Baseline_dry_inertia_Z.Z" } ] 
                      },
                  ]
    },
  ]
}

def getStudyStatus(scenario_branch_id, study_id):
     study_control_resource = f'/simulations/branches/{scenario_branch_id}/control/study/{study_id}'
     study_status = sedaroAPI.request.get(study_control_resource)
     return study_status

def getStudySimJobsStatus(scenario_branch_id, study_id):
     study_status = getStudyStatus(scenario_branch_id, study_id)
     study_job_ids = study_status['jobs']
     return [ ( f"SimJob ID: {job['id']}", f"Status: {job['status']}", f"Progress:", job['progress']) 
        for job_id in study_job_ids 
        for job in [sedaroAPI.request.get(f'/simulations/branches/{scenario_branch_id}/control/{job_id}')] ]


def runStudy(scenario_branch_id, iterations, overridesID):
    create_study_resource_url = f'/simulations/branches/{scenario_branch_id}/control/study/'
    new_studyjob = sedaroAPI.request.post(  create_study_resource_url,
                                            body={
                                                "iterations": iterations,
                                                "overrideID": overridesID
                                                })
    return new_studyjob

def create_override(wildfire_scenario_branch):
    overrides_block = wildfire_scenario_branch.OverrideSet.create(**tradespace_overrides_dict)

    return overrides_block

def test_run_studies():
    iterations = 2
    wildfire_scenario_branch = sedaroAPI.scenario(WILDFIRE_SCENARIO_ID)
    wildfire_agent_branch   = sedaroAPI.agent_template(WILDFIRE_A_T_ID)

    overrides = create_override(wildfire_scenario_branch)
    assert overrides != None
    assert overrides.name == "Test Example"
    print(f"Override id: {overrides.id}")
    
    assert len(overrides.variables) == 7
    assert overrides.variables[0]["name"] == "Baseline_mass"
    
    assert len(overrides.overrides) == 4
    assert overrides.overrides[0]["path"] == "Wildfire/root/mass"

    wildfire_agent_paths = AgentModelParametersOverridePaths(wildfire_scenario_branch, wildfire_agent_branch, agent_name='Wildfire')
    assert wildfire_agent_paths != None
    assert len(wildfire_agent_paths.listPaths()) > 0
    assert wildfire_agent_paths.findBestPathMatch('mass') == 'Wildfire/root/mass'
    assert len(wildfire_agent_paths.findPathMatches('inertia', 3)) == 3

    test_study = runStudy(WILDFIRE_SCENARIO_ID, iterations, overrides.id)
    print(f"Study id: {test_study['id']}")
    assert test_study != None
    assert test_study["status"] in  [ 'RUNNING', 'PENDING' ]
    
    print('Wait for the study to finish')


    start_time = time.perf_counter()
    max_seconds = 30*60
    while test_study.status() in ['RUNNING', 'PENDING']:
        time.sleep(10)
        test_study = wildfire_scenario_branch.study.results(test_study['id'])
        study_simjob_statuses = getStudySimJobsStatus(WILDFIRE_SCENARIO_ID, test_study.id)
        print(study_simjob_statuses)
        if time.perf_counter() - start_time > max_seconds:
            raise TimeoutError(f'Simulation did not start within {max_seconds} seconds')

    
    assert test_study.status() == 'COMPLETED'

    study_simjob_statuses = getStudySimJobsStatus(WILDFIRE_SCENARIO_ID, test_study.id)
    assert len(study_simjob_statuses) == iterations
    assert study_simjob_statuses[0][1] == 'Status: COMPLETED'
    assert study_simjob_statuses[1][1] == 'Status: COMPLETED'


    study_results = sedaroAPI.simulation.study(test_study['id']).results()
    assert study_results != None

    # some helper variables
    agent_id='NT06aqHUT5djI1_JPAsck' 
    engine_name='GNC' 
    agent_name='Wildfire'

    # get all the study simulation results
    study_simID_to_results_dict = study_results.study_results_dict()
    assert study_simID_to_results_dict != None
    assert len(study_simID_to_results_dict) == iterations

    study_wildfire_agents = test_study.agent(agent_name)
    assert study_wildfire_agents != None

    # test study blocks
    root_variables = study_wildfire_agents.blocks("root").variables
    assert len(root_variables) >= 50 # there are more than 50 variables in the root block

    # test study series study stats
    study_root_time_series_stats = study_wildfire_agents.blocks("root").time.study_stats()
    assert study_root_time_series_stats != None
    assert len(study_root_time_series_stats) == iterations

    # test study time series start time (Should never change)
    study_root_time_series_stats['min'][0] == approx(60053.354167, 0.0001)

    




def run_tests():
    test_run_studies()
    

           