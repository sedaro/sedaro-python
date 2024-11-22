# Sedaro Python Client

A python client for interacting with the Sedaro API using intuitive classes and methods.

This client is intended to be used alongside our [OpenAPI Specification](https://sedaro.github.io/openapi/). Please refer to this documentation for detailed information on the names, attributes, and relationships of each Sedaro Block. See docstrings on classes and their methods for further instructions and explanations.

It is recommended that you are familiar with [Modeling in Sedaro](https://sedaro.github.io/openapi/#tag/MetaModel) as a prerequisite to using this client.

Package release versions correspond to the Sedaro application version at the time of package updates.

## Installation

```bash
pip install sedaro
```

## Getting Started

Instantiate `SedaroApiClient` and get a `Branch`

```py
# Generate an API key in the Sedaro Management Console.
sedaro = SedaroApiClient(api_key=API_KEY)

# Get an agent template branch
agent_template_branch = sedaro.agent_template('PP8kvyVt2DDv6Ds7HX85Ck')

# Get a scenario branch
scenario_branch = sedaro.scenario('PP8kmSz3ktmTChSCPnZl5H')

# Get any kind of branch
branch = sedaro.Branch.get('PP8kyFpQKrGbwcy4VBcnbQ')

```

```py
# If using a dedicated enterprise Sedaro instance, overwrite the default `host` kwarg.
HOST = 'url-to-my-sedaro-instance.com'
sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)
```

### Proxy Configuration

Depending on your networking, some use cases will require that your proxy be configured appropriately. This is done as follows:

```py
sedaro = SedaroApiClient(api_key=API_KEY, proxy_url='http://my-proxy.com:8080')
```

If your proxy requires authentication, you can pass the `proxy_headers` argument as follows:

```py
from urllib3 import make_headers

proxy_headers = make_headers(proxy_basic_auth='username:password')
sedaro = SedaroApiClient(api_key=API_KEY, proxy_url='http://my-proxy.com:8080', proxy_headers=proxy_headers)
```

If your proxy is HTTP and not HTTPS (i.e. the URL starts with `http://`), you may need to suppress warnings about insecure transport. This can be done by setting `suppress_insecure_transport_warnings` to `True`.

## Modeling

### Model Management

Workspaces, Projects, Repositories, and Branches can be managed directly on the `SedaroApiClient` object.

```py
sedaro = SedaroApiClient(api_key=API_KEY)

sedaro.Workspace
sedaro.Project
sedaro.Repository
sedaro.Branch
```

Each of these attributes has methods for creating instances of the corresponding Sedaro objects.

```py
workspace = sedaro.Workspace.create(name='My Workspace')

project = sedaro.Project.create(name='My Project', workspace=workspace.id)

repository = sedaro.Repository.create(name='My Repository', metamodelType='Scenario', workspace=workspace.id, project=project.id) # creates a single default branch as well; project id is optional

branch = sedaro.Branch.create(repository.branches[0].id, name='My Branch') # create a new branch based on the id of the branch passed as the first argument
```
Note that other kwargs can also be passed to these methods such as `description`.

Each of these attributes also have methods for retrieving instances of the corresponding Sedaro objects.

```py
workspaces = sedaro.Workspace.get() # Get all workspaces
workspaces =  sedaro.Workspace.get_all() # Get all workspaces
workspace = sedaro.Workspace.get(workspace_id) # Get a single workspace by ID

projects = sedaro.Project.get() # Get all projects
# ...etc.
```

Fetching via the `Workspace`, `Project`, and `Repository` attributes, return objects that each have an `update`, `refresh`, and `delete` method. They also allow for keying into relationship attributes and fetching corresponding objects. Note that the retrieved objects are cached until calling the `refresh` method.

```py
workspace.update(name='New Name') # Update the workspace
workspace.refresh() # Refresh the workspace object with the latest data from Sedaro
workspace.delete()  # Delete the workspace

workspace.projects # Fetch all projects in the workspace
repo.workspace # Fetch the workspace of the repository
project.repositories # Fetch all repositories in the project
# ...etc.
```

The object returned from the `Branch` attribute does not yet support `update`, `refresh`, and `delete` method, nor does it support keying into relationship attributes. These features will be added in a future release. It currently returns a `Branch` object with as described in the next section.

### Agent Modeling

[Models](https://docs.sedaro.com/models) in Sedaro can be modified via the `AgentTemplateBranch` and `ScenarioBranch` interfaces. Blocks of a particular type are created and retrieved via the following pattern, where `branch` is an instance of `AgentTemplateBranch` or `ScenarioBranch`:

```py
branch.BatteryCell
branch.Component
branch.Subsystem
# ...etc.
```

- Valid `BlockType`s for Agent Template Branches and Scenario Branches can be found in our [Model Docs](https://docs.sedaro.com/models). In code editors that support it, intellisense will suggest names for `BlockTypes`.

A `BlockType` has several methods:

```py
branch.Subsystem.create(name='Structure')
branch.Subsystem.get(block_id) # ID of desired Subsystem
branch.Subsystem.get_all_ids()
branch.Subsystem.get_all()
branch.Subsystem.get_where()
branch.Subsystem.get_first()
branch.Subsystem.get_last()
```

These methods (except for `get_all_ids`) return a single or list of `Block`(s). A `Block` has several methods and properties.

```py
subsystem = branch.Subsystem.create(name='Structure')

subsystem.update(name='Structure 2.0')

subsystem.delete()
```

A `Block` will always be equal to and in sync with all other `Block`s referencing the same Sedaro Block:

```py
subsystem = branch.Subsystem.create(name='Structure')
subsystem_2 = subsystem.update(name='Structure 2.0')
subsystem_3 = branch.Subsystem.get(subsystem.id)

assert subsystem == subsystem_2 == subsystem_3
```

The `repr` of a `Block` will show you the corresponding Sedaro Block's data:

```py
repr(subsystem)

>>> Subsystem(
>>>   category='CUSTOM'
>>>   components=[]
>>>   id='PP8kvbfczhXYk2kyhSm2gg'
>>>   name='Structure 2.0'
>>>   type='Subsystem'
>>> )
```

Keying into any field existing on the corresponding Sedaro Block will return the value.

```py
subsystem.name
>>> 'Structure 2.0'
```

Keying into relationship fields returns `Block`s corresponding to the related Sedaro `Block`s as follows:

- `OneSide`: a `Block`
- `ManySide`: a `list` of `Block`s
- `DataSide`: a dictionary with `Block`s as keys and relationship data as values

```py
subsystem.components[0]
>>> SolarPanel(id='PP8kvpQ78rgKSpqhM2r55k')
```

Note that this allows for traversing via chained relationship fields.

```py
solar_panel.cell.panels[-1].subsystem.components[0].delete()
```

### **Full Example**

```py
from sedaro import SedaroApiClient
from sedaro.exceptions import NonexistantBlockError

API_KEY = 'api_key_generated_by_sedaro'
AGENT_TEMPLATE_ID = 'PP8kvyVt2DDv6Ds7HX85Ck'

sedaro = SedaroApiClient(api_key=API_KEY)

branch = sedaro.agent_template(AGENT_TEMPLATE_ID)

solar_cell = branch.SolarCell.create(
  partNumber="987654321",
  manufacturer='Sedaro Corporation',
  openCircuitVoltage=3.95,
  shortCircuitCurrent=0.36,
  maxPowerVoltage=3.54,
  maxPowerCurrent=0.345,
  numJunctions=3,
)

sc_id = solar_cell.id

solar_cell.update(partNumber="123456789")

solar_cell.delete()

try:
    solar_cell.update(partNumber="987654321")
except NonexistantBlockError as e:
    assert str(e) == f'The referenced Block with ID: {sc_id} no longer exists.'
```

### Multi-Block Updates and Deletions

The `update` method is also available for performing operations on multiple Sedaro blocks and/or root at the same time using kwargs as follows:

- Update any number of fields on the root of the Model by passing the fields directly as additional kwargs to `update`
- `blocks`: create/update 1+ blocks by passing a list of dictionaries. If an `id` is present in a dictionary, the corresponding block will be updated in Sedaro. If an `id` isn't present, a new block will be created. The `type` is always required.
- `delete`: delete 1+ blocks by passing a list of their block `id`s.

In this method, relationship fields can point at existing `BlockID`'s or "ref id"s. A "ref id" is similar to a
json "reference" and is used as follows:

- It is any string starting with `'$'`.
- It must be in the `id` field of a single `Block` dictionary created in this transaction.
- It can be referenced in any relationship field on root or any `Block` dictionary in this transaction.
- All instances of the "ref id" will be resolved to the corresponding created `Block`'s id.

```py
branch.update(
    name="value", # update fields on root
    mass=12.1 # update fields on root
    blocks=[
        { "id": "PP8kwWKT2QZdr76LhCw6JS", "type": "Modem", "field": "value" }, # update block
        { "type": "SolarCell",  "field": "value", ... }, # create block
    ],
    delete=["PP8kwfFJZpzL87s5Q8qmlK"] # delete block
)
```

And additional truthy keyword argument `include_response` can be passed to `update` to return the response from the update operation, as follows:

```py
{
    "crud": {
        "blocks": [], # ids of all Blocks created or updated
        "delete": [], # ids of all Blocks deleted
    },
    "branch": {
        # whole branch dictionary
    }
}
```

## Simulation

Access a `Simulation` via the `simulation` attribute on a `ScenarioBranch`.

```py
sim = sedaro.scenario('PP8kwsb5wlzNT59jZYZkdt').simulation

# Start simulation
simulation_handle = sim.start(wait=True) # To wait for the simulation to enter the RUNNING state, pass `wait=True`
# simulation_handle = sim.start() # Alternatively, this will return immediately after the simulation job is queued for execution

# See simulation status
simulation_handle = sim.status() # simulation_handle can also be obtained by calling sim.status()

# Poll simulation, and return results when complete (progress will be printed until ready)
results = sim.results_poll()

# If you know it's complete, query for results directly
results = sim.results()

# Terminate running simulation
sim.terminate()
```

- The `status`, `results`, `results_poll`, and `terminate` methods can all optionally take a `job_id`, otherwise they operate on the latest (most recently started/finished) simulation.
- For `results` and `results_poll`, you may also provide the optional kwarg `streams`. This triggers narrowing results to fetch only specific streams that you specify. See doc strings for the `results` method for details on how to use the `streams` kwarg.

### Simulation Handle

The following `Simulation` methods are also available on the `SimulationHandle` returned by `sim.start()` and `sim.status()`:

```py
simulation_handle.status()
simulation_handle.results_poll()
simulation_handle.results()
simulation_handle.terminate()
```

The `SimulationHandle` can also be used to access the attributes of the running simulation. For example:

```py
simulation_handle['id']
simulation_handle['status']
...
```

### Context Manager

The `SimulationHandle` object can be used as a context manager to automatically terminate the simulation when the context is exited.

```py
with sim.start(wait=True) as simulation_handle:
    # Do something with the simulation
    pass
```

## Results

Any object in the results API will provide a descriptive summary of its contents when the `.summarize` method is called. See the `results_api_demo` notebook in the [modsim notebooks](https://github.com/sedaro/modsim-notebooks) repository for more examples.

### Selecting Results to Download

The `results` and `results_poll` methods take a number of arguments. These arguments can be used to specify which segments of the data should be downloaded, the resolution of the downloaded data, and more.

- `start`: start time of the data to fetch, in MJD. Defaults to the start of the simulation.
- `stop`: end time of the data to fetch, in MJD. Defaults to the end of the simulation.
- `streams`: a list of streams to fetch, following the format specified below. If no argument is provided, all streams are fetched.
- `sampleRate`: the resolution at which to fetch the data. Must be a positive integer power of two, or 0. The value `n` provided, if not 0, corresponds to data at `1/n` resolution. For instance, `1` means data is fetched at full resolution, `2` means every second data point is fetched, `4` means every fourth data point is fetched, and so on. If the value provided is 0, data is fetched at the lowest resolution available. If no argument is provided, data is fetched at full resolution (sampleRate 1).
- num_workers: `results` and `results_poll` use parallel downloaders to accelerate data fetching. The default number of downloaders is 2, but you can use this argument to set a different number.

#### Format of `streams`

If you pass an argument to `streams`, it
must be a list of tuples following particular rules:

- Each tuple in the list can contain either 1 or 2 items.
- If a tuple contains 1 item, that item must be the agent ID, as a string. Data for all engines of this agent\
   will be fetched. Remember that a 1-item tuple is written as `(foo,)`, not as `(foo)`.
- If a tuple contains 2 items, the first item must be the same as above. The second item must be one of the\
   following strings, specifying an engine: `'GNC`, `'CDH'`, `'Thermal'`, `'Power'`. Data for the specified\
   agent of this engine will be fetched.

For example, with the following code, `results` will only contain data for all engines of agent `foo` and the
`Power` and `Thermal` engines of agent `bar`.

```py
selected_streams=[
    ('foo',),
    ('bar', 'Thermal'),
    ('bar', 'Power')
]
results = sim.results(streams=selected_streams)
```

### Saving Downloaded Data

You may save downloaded simulation data to your machine via the following procedure:

```py
results = simulation_handle.results()
results.save('path/to/data')
```

This will save the data in a directory whose path is indicated by the argument to `results.save()`. The path given must be to an empty directory, or a directory which does not yet exist.

### Statistics

Summary statistics are calculated for certain state variables. They become available shortly after a simulation finishes running.

To fetch the statistics for a simulation, use `stats`:

```py
stats = simulation_handle.stats()
```

The above will raise an exception if the sim's stats are not yet ready. Use the optional `wait=True` argument to block until the stats are ready:

```py
stats = simulation_handle.stats(wait=True)
```

To fetch statistics only for certain streams, use the `streams` argument in the format previously described:

```py
selected_streams=[
    ('foo',),
    ('bar', 'Thermal'),
    ('bar', 'Power')
]
stats = sim.stats(streams=selected_streams)
```

## Loading Saved Data

Once data has been saved as above, it can be loaded again by using the `load` method of its class. For instance, `results` above, a SimulationResult, is loaded as follows:

```py
from sedaro.results.simulation_result import SimulationResult
results = SimulationResult.load('path/to/data')
```

Once loaded, the results can be interacted with as before.

To load a agent, block, or series result, one would use the `load` method of the `SedaroAgentResult`, `SedaroBlockResult`, or `SedaroSeries` class respectively.

## Send Requests

Use the built-in method to send custom requests to the host. See [OpenAPI Specification](https://sedaro.github.io/openapi/) for documentation on resource paths and body params.

Through the `request` property, you can access `get`, `post`, `put`, `patch`, and `delete` methods.

```py
# get a branch
sedaro.request.get(f'/models/branches/{AGENT_TEMPLATE_ID}')
```

```py
# create a celestial target in a branch
sun = {
    'name': 'Sun',
    'type': 'CelestialTarget'
}

sedaro.request.patch(
    f'/models/branches/{AGENT_TEMPLATE_ID}/template/',
    { 'blocks': [sun] }
)
```

Note that requests sent this way to create, read, update, or delete Sedaro Blocks won't automatically update already instantiated `Branch` or `Block` objects.

## External Simulation State Dependencies

The following API is exposed to enable the integration of external software with a Sedaro simulation during runtime. Read more about "Cosimulation" in Sedaro [here](https://sedaro.github.io/openapi/#tag/Externals). For detailed documentation on our Models, their Blocks, at the attributes and relationships of each, see our [model docs](https://docs.sedaro.com/models).

**Warning:** The following documentation is a work in progress as we continue to evolve this feature. It is recommended that you reach out to Sedaro Application Engineering for assistance using this capability while we mature the documentation for it.

### Setup

Define `ExternalState` block(s) on a `Scenario` to facilitate in-the-loop connections from external client(s) (i.e. [Cosimulation](https://sedaro.github.io/openapi/#tag/Externals)). The existance of these blocks determines whether or not the external interface is enabled and active during a simulation. These blocks will also be version controlled just as any other block in a Sedaro model.

```python
# Per Round External State Block
{
    "id": "PP8kxMDBklsdb8BMXGvggz",
    "type": "PerRoundExternalState",
    "produced": [{"root": "velocity"}], # Implicit QuantityKind
    "consumed": [{"prev.root.position.as": "Position.eci"}], # Explicit QuantityKind
    "engineIndex": 0, # 0: GNC, 1: C&DH, 2: Power, 3: Thermal
    "agents": ["PP8kxTYSBMngYh5vMDvTZn"]
}

# Spontaneous External State Block
{
    "id": "PP8kxjrXWzqSY22YqJs3Dd",
    "type": "SpontaneousExternalState",
    "produced": [{"root": "activeOpMode"}],
    "consumed": [{"prev.root.position.as": "Position.eci"}],
    "engineIndex": 0, # 0: GNC, 1: C&DH, 2: Power, 3: Thermal
    "agents": ["PP8kxTYSBMngYh5vMDvTZn"]
}
```

#### Deleting External State Blocks

If you'd like to clear/delete the `ExternalState` Blocks on a `Scenario` model, a shortcut method `delete_all_external_state_blocks` is available on any `ScenarioBranch`.

```python
scenario_branch.delete_all_external_state_blocks()
```

### Deploy (i.e. Initialize)

```python
sim_client = sedaro.scenario('PP8kwsb5wlzNT59jZYZkdt').simulation

# Start the simulation
# Note that when `sim_client.start()` returns, the simulation job has entered your Workspace queue to be built and run.
# Passing `wait=True` to start() will wait until the simulation has entered the RUNNING state before returning.
# At this time, the simulation is ready for external state production/consumption
with sim_client.start(wait=True) as simulation_handle:
  # External cosimulation transactions go here
```

### Consume

```python
  agent_id = ... # The ID of the relevant simulation Agent
  per_round_external_state_id = ... # The ID of the relevant ExternalState block
  spontaneous_external_state_id = ... # The ID of the relevant ExternalState block
  time = 60050.0137 # Time in MJD

  # Query the simulation for the state defined on the ExternalState block at the optionally given time
  # This blocks until the state is available from the simulation
  state = simulation_handle.consume(agent_id, per_round_external_state_id)
  print(state)

  state = simulation_handle.consume(agent_id, spontaneous_external_state_id, time=time) # Optionally provide time
  print(state)
```

**Note:** Calling `consume` with a `time` value that the simulation hasn't reached yet will block until the simulation catches up. This is currently subject to a 10 minute timeout. If the request fails after 10 minutes, it is recommended that it be reattempted.

Similarly, calling `consume` with a `time` that too far lags the current simulation might result in an error as the value has been garbage collected from the simulation caches and is no longer available for retrieval. If this is the case, please fetch the data from the Data Service (via the Results API) instead.

### Produce

```python
  state = (
    [7000, 0, 0], # Position as ECI (km)
    [12, 0, 14.1, 14.3, 7, 0], # Thruster thrusts
  )
  simulation_handle.produce(agent_id, per_round_external_state_id, state)

  state = (
    [0, 0, 0, 1], # Commanded Attitude as Quaternion
  )
  simulation_handle.produce(agent_id, spontaneous_external_state_id, state, timestamp=60050.2)
  # `timestamp` is optional.  If not provided, the `time` at which the simulation receives the spontaneous state is used
  # Note: `timestamp` can be used to intentionally inject latency between the time a command is sent and when it is to take effect.  This allows for more accurately modeling communications latency on various comms buses.
```

### Teardown

A simulation that terminates on its own will clean up all external state interfaces. Manually terminating the simulation will do the same:

```python
  simulation_handle.terminate()

  # Or if using the context manager, simply exit the context
```

### Asynchronous Interface

You can also communicate asynchronously with a simulation to take advantage of lower latencies and parallelism. 


```python
  agent_id = ... # The ID of the relevant simulation Agent
  per_round_external_state_id = ... # The ID of the relevant ExternalState block
  spontaneous_external_state_id = ... # The ID of the relevant ExternalState block
  time = 60050.0137 # Time in MJD

  async with simulation_handle.async_channel(url) as channel:
    state = await channel.consume(agent_id, per_round_external_state_id)
    print(state)

    state = await channel.consume(agent_id, spontaneous_external_state_id, time=time) # Optionally provide time
    print(state)
```

Over the async_channel, you can also spawn tasks asynchronously.

```python
  async with simulation_handle.async_channel(url) as channel:
    tasks = []
    for i in range(10):
      tasks.append(asyncio.create_task(channel.consume(agent_id, per_round_external_state_id)))

    await asyncio.gather(*tasks)
```

This code expects the async_channel to be used only within one async run loop.  If you mix async and threaded python, the functionality of the async channel is not defined.

## Modeling and Simulation Utilities

The following modeling and simuation utility methods are available for convenience. See the docstrings for each method for more information and usage.

```python
from sedaro import modsim as ms

ms.datetime_to_mjd(dt: datetime.datetime) -> float:
ms.mjd_to_datetime(mjd: float) -> datetime.datetime:
ms.read_csv_time_series(file_path: str, time_column_header: str = 'time', **kwargs):
ms.read_excel_time_series(file_path: str, time_column_header: str = 'time', **kwargs):
ms.search_time_series(time_dimension: np.ndarray | list, timestamp: float | datetime.datetime) -> int:
ms.quaternion2attitude_mat(quaternion: np.ndarray) -> np.ndarray:
ms.quaternion_rotate_frame(vectorIn: np.ndarray, quaternion: np.ndarray) -> np.ndarray:
ms.angle_between_quaternion(q1: np.ndarray, q2: np.ndarray) -> np.ndarray:
ms.difference_quaternion(q1: np.ndarray, q2: np.ndarray) -> np.ndarray:
ms.quaternion2rotmat(quaternion: np.ndarray) -> np.ndarray:
ms.orthogonal_vector(vector: np.ndarray) -> np.ndarray:
ms.quaternion_dot(q1: np.ndarray, q2: np.ndarray) -> np.ndarray:
ms.random_orthogonal_rotation(vector: np.ndarray, angle_1sigma: float, random: np.random.RandomState | None = None) -> np.ndarray:
ms.euler_axis_angle2quaternion(axis, angle):
ms.vectors2angle(vector1: np.ndarray, vector2: np.ndarray) -> float:
ms.eci_vector_to_body(vector_eci: np.ndarray, attitude_body_eci: np.ndarray) -> np.ndarray:
ms.body_vector_to_eci(vector_eci: np.ndarray, attitude_body_eci: np.ndarray) -> np.ndarray:
ms.quaternion_conjugate(quaternion: np.ndarray) -> np.ndarray:
ms.rotmat2quaternion(rot_mat: np.ndarray) -> np.ndarray:
ms.quaternions_to_rates(q1: np.ndarray, q2: np.ndarray, dt: float) -> np.ndarray:
ms.invert3(m: np.ndarray) -> np.ndarray:
ms.unit3(vec: np.ndarray) -> np.ndarray:
```

## Sedaro Base Client

The Sedaro client is a wrapper around the Swagger generated OpenAPI client. When this package is installed, the auto-generated, lower-level clients and methods are also available under `sedaro_base_client`.

```py
from sedaro_base_client import ...
```

## Community, Support, Discussion

If you have any issues using the package or any suggestions, please start by reaching out:

1. Open an issue on [GitHub](https://github.com/sedaro/sedaro-python/issues)
2. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow)
3. Email us at support@sedarotech.com

Please note that while emails are always welcome, we prefer the first two options as this allows for others to benefit from the discourse in the threads. That said, if the matter is specific to your use case or sensitive in nature, don't hesitate to shoot us an email instead.
