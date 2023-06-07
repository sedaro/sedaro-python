# Sedaro Python Client

A python client for interacting with the Sedaro API using intuitive classes and methods.

This client is intended to be used alongside our redocs [OpenAPI Specification](https://sedaro.github.io/openapi/). Please refer to this documentation for detailed information on the names, attributes, and relationships of each Sedaro Block. See docstrings on classes and their methods for further instructions and explanations.

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

Use the `AgentTemplateBranch` or `ScenarioBranch` to access and utilize `BlockType`s. A `BlockType` is used to create and access Sedaro Blocks of the respective class.

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
solar_panel = subsystem.components[0]

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

sedaro = SedaroApiClient(api_key=API_KEY):

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
sim = sedaro.scenario_branch('NShL7J0Rni63llTcEUp4F').simulation

# Start simulation
sim.start()

# Poll simulation, and return when complete (progress will be printed until ready)
results = sim.poll_results()

# If you know it's complete, query for results directly
results = sim.results()

# Terminate simulation
sim.start()
sim.terminate()
```

- For `results` and `poll_results`, you may also provide the optional kwarg `streams`. This triggers narrowing results to fetch only specific streams that you specify. See doc strings for the `results` method for details on how to use the `strams` kwarg.

## Results

Any object in the results API will provide a descriptive summary of its contents when the `.summarize` method is called. See the `results_api_demo` notebook in the [modsim notebooks](https://github.com/sedaro/modsim-notebooks) repository for more examples.

## Fetch Raw Data

You also fetch raw results data directly with additional options to customize the result.

```py
sim = sedaro.scenario_branch('NShL7J0Rni63llTcEUp4F').simulation

# Run simulation
sim.start()

# Get simulation
job = sim.job()

# Get raw data
selected_streams=[
    ('foo',),
    ('bar', 'Thermal'),
    ('bar', 'Power')
]
data = sim.results_raw(
  job['dataArray'],
  start=65000,
  stop=65001,
  limit=250,
  streams=selected_streams,
  axisOrder='TIME_MINOR'
)
### alternative:
data = sim.results_raw(
  job['dataArray'],
  start=65000,
  stop=65001,
  binWidth=0.004,
  streams=selected_streams,
  axisOrder='TIME_MINOR'
)
```

All arguments except the first are optional. See doc string in the `results_raw` for details on use of the arguments.

## Send Requests

Use the built-in method to send requests to the host. See [OpenAPI Specification](https://sedaro.github.io/openapi/) for documentation on resource paths and body params.

```py
# get a branch
sedaro.send_request(
    f'/models/branches/{AGENT_TEMPLATE_ID}',
    'GET'
)

# create a celestial target in a branch
sun = {
    'name': 'Sun',
    'type': 'CelestialTarget'
}

sedaro.send_request(
    f'/models/branches/{self.id}/template/',
    'PATCH',
    { 'blocks': [sun] }
)
```

Note that requests sent this way to CRUD Sedaro Blocks won't automatically update already instantiated `Branch`s or `Block`s.

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
