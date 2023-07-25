# Sedaro Python Client

A python client for interacting with the Sedaro API using intuitive classes and methods.

This client is intended to be used alongside our [OpenAPI Specification](https://sedaro.github.io/openapi/). Please refer to this documentation for detailed information on the names, attributes, and relationships of each Sedaro Block. See docstrings on classes and their methods for further instructions and explanations.

It is recommended that you are familiar with [Modeling in Sedaro](https://sedaro.github.io/openapi/#tag/Templates) as a prerequisite to using this client.

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
agent_template_branch = sedaro.agent_template('NShL_CIU9iuufSII49xm-')

# Get a scenario branch
scenario_branch = sedaro.scenario('NXKwd2xSSPo-V2ivlIr8k')
```

```py
# If using a dedicated enterprise Sedaro instance, overwrite the default `host` kwarg.
HOST = 'url-to-my-sedaro-instance.com'
sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)
```

## Block CRUD

Use the `AgentTemplateBranch` or `ScenarioBranch` to instantiate and utilize the `BlockType` class. A `BlockType` object is used to create and access Sedaro Blocks of the respective class.

```py
branch.BatteryCell
branch.Component
branch.Subsystem
# ...etc.
```

- Valid `BlockType`s for Agent Template Branches and Scenario Branches can be found in our redocs [OpenAPI Specification](https://sedaro.github.io/openapi/), by viewing the valid classes in the `blocks` key for the `Template` `PATCH` route. In code editors that support it, intellisense will suggest names for `BlockTypes`.

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
>>>   id='NShHxZwUh1JGRfZKDvqdA'
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
>>> SolarPanel(id='NShKPImRZHxGAXqkPsluk')
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
AGENT_TEMPLATE_ID = 'NShL_CIU9iuufSII49xm-'

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
    assert str(e) == f'The referenced "SolarCell" (id: {sc_id}) no longer exists.'
```

### Multi-Block CRUD

The `crud` method is also available for performing operations on multiple Sedaro blocks and/or root at the same time using kwargs as follows:

- `root`: update fields on the root by passing a dictionary
- `blocks`: create/update 1+ blocks by passing a list of dictionaries. If an `id` is present, the corresponding block will be updated. If an `id` isn't present, a new block will be created. The `type` is always required.
- `delete`: delete 1+ blocks by passing a list of their block `id`s.

In this method, relationship fields can point at existing `BlockID`'s or "ref id"s. A "ref id" is similar to a
json "reference" and is used as follows:
  - It is any string starting with `'$'`.
  - It must be in the `id` field of a single `Block` dictionary created in this transaction.
  - It can be referenced in any relationship field on root or any `Block` dictionary in this transaction.
  - All instances of the "ref id" will be resolved to the corresponding created `Block`'s id.


```py
branch.crud(
    root={ "field": "value" }, # update fields on root
    blocks=[
        { "id": "NXKzb4gSdLyThwudHSR4k", "type": "Modem", "field": "value" }, # update block
        { "type": "SolarCell",  "field": "value", ... }, # create block
    ],
    delete=["NTF8-90Sh93mPKxJkq6z-"] # delete block
)
```

The response from this method is used to update the blocks in the `Branch` the method was called on. The content of the response is also returned, as follows:

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
sim = sedaro.scenario('NShL7J0Rni63llTcEUp4F').simulation

# Start simulation
simulation_handle = sim.start()

# See simulation status
simulation_handle = sim.status()

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
simulation_handle.results_plain(...)
simulation_handle.terminate()
```

The `SimulationHandle` can also be used to access the attributes of the running simulation. For example:

```py
simulation_handle['id']
simulation_handle['status']
...
```

## Results

Any object in the results API will provide a descriptive summary of its contents when the `.summarize` method is called. See the `results_api_demo` notebook in the [modsim notebooks](https://github.com/sedaro/modsim-notebooks) repository for more examples.

## Fetch Raw Data

You may also fetch results directly as a plain dictionary with additional arguments to customize the result.

```py
sim = sedaro.scenario('NShL7J0Rni63llTcEUp4F').simulation

# Run simulation
sim.start()

# After finished... get raw data
selected_streams=[
    ('foo',),
    ('bar', 'Thermal'),
    ('bar', 'Power')
]
data = sim.results_plain(
  start=65000,
  stop=65001,
  limit=250,
  streams=selected_streams,
  axisOrder='TIME_MINOR'
)
### alternative:
data = sim.results_plain(
  start=65000,
  stop=65001,
  binWidth=0.004,
  streams=selected_streams,
  axisOrder='TIME_MINOR'
)
```

See doc string in the `results_plain` for details on use of the arguments.

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

Note that requests sent this way to CRUD Sedaro Blocks won't automatically update already instantiated `Branch` or `Block` objects.

## External Simulation State Dependencies

The following API is exposed to enable the integration of external software with a Sedaro simulation during runtime. Read more about "Cosimulation" in Sedaro [here](https://sedaro.github.io/openapi/#tag/Externals).

**Warning:** The following documentation is a work in progress as we continue to evolve this feature. It is recommended that you reach out to Sedaro Application Engineering for assistance using this capability while we mature the documentation for it.

### Setup

Define `ExternalState` block(s) on a `Scenario` to facilitate in-the-loop connections from external client(s) (i.e. [Cosimulation](https://sedaro.github.io/openapi/#tag/Externals)). The existance of these blocks determines whether or not the external interface is enabled and active during a simulation. These blocks will also be version controlled just as any other block in a Sedaro model.

```python
# Per Round External State Block
{
    "id": "NZ2SGPWRnmdJhwUT4GD5k",
    "type": "PerRoundExternalState",
    "produced": [{"root": "velocity"}], # Implicit QuantityKind
    "consumed": [{"prev.root.position.as": "Position.eci"}], # Explicit QuantityKind
    "engineIndex": 0, # 0: GNC, 1: C&DH, 2: Power, 3: Thermal
    "agents": ["NSghFfVT8ieam0ydeZGX-"]
}

# Spontaneous External State Block
{
    "id": "NZ2SHUkS95z1GtmMZ0CTk",
    "type": "SpontaneousExternalState",
    "produced": [{"root": "activeOpMode"}],
    "consumed": [{"prev.root.position.as": "Position.eci"}],
    "engineIndex": 0, # 0: GNC, 1: C&DH, 2: Power, 3: Thermal
    "agents": ["NSghFfVT8ieam0ydeZGX-"]
}
```

### Deploy (i.e. Initialize)

```python
sim_client = sedaro.scenario('NShL7J0Rni63llTcEUp4F').simulation

# Start the simulation
# Note that when `sim_client.start()` returns, the simulation is running and ready for external state production/consumption
simulation_handle = sim_client.start()
```

### Consume

```python
agent_id = ... # The ID of the relevant simulation Agent
per_round_external_state_id = ... # The ID of the relevant ExternalState block
spontaneous_external_state_id = ... # The ID of the relevant ExternalState block
time = 60050.0137 # Time in MJD

# Query the simulation for the state defined on the ExternalState block at the optionally given time
# This blocks until the state is available from the simulation
state = simulasimulation_handletion.consume(agent_id, per_round_external_state_id)
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
