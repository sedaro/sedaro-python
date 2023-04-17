# Sedaro Python Client

A python client for interacting with the Sedaro Satellite API using intuitive classes and methods.

This client is intended to be used alongside our redocs [OpenAPI Specification](https://sedaro.github.io/openapi/). Please refer to this documentation for detailed information on the names, attributes, and relationships of each Sedaro Block.

Package release versions correspond to the Sedaro Satellite application version at the time of package updates.

## Install

```bash
pip install sedaro
```

## Use: Block CRUD

1.  Instantiate the `SedaroApiClient` as a context manager. All code interacting with the API should be within the scope of that context manager. Generate an API key in the Sedaro Satellite Management Console.

    ```py
    from sedaro import SedaroApiClient

    API_KEY = 'my_api_key' # Generated in Sedaro Satellite Management Console
    AGENT_TEMPLATE_BRANCH_ID = 'NShL_CIU9iuufSII49xm-' # id of a Branch owned by my Sedaro account with the given api key

    with SedaroApiClient(api_key=API_KEY) as sedaro:
        ...
    ```

    ```py
    # If using a dedicated enterprise Sedaro instance, overwrite the default `host` kwarg.
    HOST = 'url-to-my-sedaro-instance.com'

    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro:
        ...
    ```

2.  Use the client to instantiate a `BranchClient`.

    ```py
    with SedaroApiClient(api_key=API_KEY) as sedaro:
        branch = sedaro.get_branch(AGENT_TEMPLATE_BRANCH_ID)
    ```

3.  Use the `BranchClient` to access and utilize `BlockClassClient`s. A `BlockClassClient` is used to create and access Sedaro Blocks of the respective class.

    ```py
    branch.BatteryCell
    branch.Component
    branch.Subsystem

    # ...etc.
    ```

    Valid `BlockClassClient`s for Agent Template Branches and Scenario Branches can be found in our redocs [OpenAPI Specification](https://sedaro.github.io/openapi/), by viewing the valid classes in the `blocks` key for the `Template` `PATCH` route.

    In code editors that support it, intellisense will suggest names for `BlockClassClients`. Pay attention to what is valid for an Agent Template vs a Scenario branch. If you key into an invalid value, an error will be raised.

4.  A `BlockClassClient` has several methods:

    ```py
    branch.Subsystem.create(name='Structure')
    branch.Subsystem.get(block_id) # ID of desired Subsystem
    branch.Subsystem.get_all_ids()
    branch.Subsystem.get_all()
    branch.Subsystem.get_where()
    branch.Subsystem.get_first()
    branch.Subsystem.get_last()
    ```

5.  These methods (except for `get_all_ids`) return a single or list of `BlockClient`(s). A `BlockClassClient` has several methods and properties.

    ```py
    subsystem = branch.Subsystem.create(name='Structure')

    subsystem.update(name='Structure 2.0')

    subsystem.delete()
    ```

    A `BlockClient` will always be equal to and in sync with all other `BlockClient`s referencing the same Sedaro Block:

    ```py
    subsystem = branch.Subsystem.create(name='Structure')
    subsystem_2 = subsystem.update(name='Structure 2.0')
    subsystem_3 = branch.Subsystem.get(subsystem.id)

    assert subsystem == subsystem_2 == subsystem_3
    ```

    The `repr` of a `BlockClient` will show you the corresponding Sedaro Block's data:

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

    Keying into relationship fields returns `BlockClient`s corresponding to the related Sedaro `Block`s as follows:

    - `OneSide`: a `BlockClient`
    - `ManySide`: a `list` of `BlockClient`s
    - `DataSide`: a dictionary with `BlockClient`s as keys and relationship data as values

    ```py
    solar_panel = subsystem.components[0]

    >>> SolarPanel(id='NShKPImRZHxGAXqkPsluk')
    ```

    Note that this allows for traversing via chained relationship fields.

    ```py
    solar_panel.cell.panels[-1].subsystem.components[0].delete()
    ```

### Full Example

```py
from sedaro import SedaroApiClient
from sedaro.exceptions import NonexistantBlockError

API_KEY = 'api_key_generated_by_sedaro'
AGENT_TEMPLATE_BRANCH_ID = 'NShL_CIU9iuufSII49xm-'

with SedaroApiClient(api_key=API_KEY) as sedaro:
    branch = sedaro.get_branch(AGENT_TEMPLATE_BRANCH_ID)

    solar_cell = branch.SolarCell.create(
      partNumber="987654321",
      manufacturer='Sedaro Corporation',
      openCircuitVoltage=3.95,
      shortCircuitCurrent=0.36,
      maxPowerVoltage=3.54,
      maxPowerCurrent=0.345,
      numJunctions=3,
    )

    bc_id = solar_cell.id

    solar_cell.update(partNumber="123456789")

    solar_cell.delete()

    try:
        solar_cell.update(partNumber="987654321")
    except NonexistantBlockError as e:
        assert str(e) == f'The referenced "BatteryCell" (id: {bc_id}) no longer exists.'
```

### Multi-Block CRUD

The `crud` method is also available for performing CRUD operations on multiple Sedaro blocks and/or root at the same time using kwargs as follows:
- `root`: update fields on the root by passing a dictionary
- `blocks`: create/update 1+ blocks by passing a list of dictionaries. If an `id` is present, the corresponding block will be updated. If an `id` isn't present, a new block will be created. The `type` is always required.
- `delete`: delete 1+ blocks by passing a list of their block `id`s.

```py
with SedaroApiClient(api_key=API_KEY) as sedaro:
    branch = sedaro.get_branch(AGENT_TEMPLATE_BRANCH_ID)

    branch.crud(
        root={ "field": "value" }, # update fields on root
        blocks=[
            { "id": "NTF7...", "type": "Modem", "field": "value" }, # update block
            { "type": "SolarCell",  "field": "value", ... }, # create block
        ],
        delete=["NTF8-90Sh93mPKxJkq6z-"] # delete block
    )
```


## Use: Simulation

```py
SCENARIO_BRANCH_ID = 'NShL7J0Rni63llTcEUp4F'

with SedaroApiClient(api_key=API_KEY) as sedaro:

    # Instantiate sim client
    sim = sedaro.get_sim_client(SCENARIO_BRANCH_ID)

    # Start simulation
    sim.start()

    # Get simulation
    job_res = sim.get_latest()[0]

    # Check status & percentage complete
    assert job_res['status'] == 'RUNNING'
    print(job_res['progress']['percentComplete'])

    # Terminate simulation
    response = sim.terminate(job_res['id'])
    assert response['message'] == 'Successfully terminated simulation.'

```

## Use: View Results

The primary entrypoint of the results API is the `SedaroSimulationResult` class. This class offers a few methods for pulling data from scenarios. The most commonly-used method is `.get_scenario_latest` that pulls the latest results into a new result object. If the simulation is not complete, the resulting object will indicate the status is "Running" and not contain any results.

```py
results = SedaroSimulationResult.get_scenario_latest(api_key, scenario_branch_id)
```

Alternatively, use the `.poll_scenario_latest` method to wait for an in-progress simulation to complete and download results after.

```py
results = SedaroSimulationResult.poll_scenario_latest(api_key, scenario_branch_id)
```

Any object in the results API will provide a descriptive summary of its contents when the `.summarize` method is called. See the `results_api_demo` notebook in the [modsim notebooks](https://github.com/sedaro/modsim-notebooks) repository for more examples.

## Use: Send Requests

Use built-in method to send customized requests to the host. See [OpenAPI Specification](https://sedaro.github.io/openapi/) for documentation on resource paths and body params.

```py
with SedaroApiClient(api_key=API_KEY) as sedaro:
    # get a branch
    sedaro.send_request(
        f'/models/branches/{AGENT_TEMPLATE_BRANCH_ID}',
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

Note that requests sent this way to CRUD Sedaro Blocks won't automatically update already instantiated `BranchClient`s or `BlockClient`s.

## Further information

See docstrings on classes and their methods for further instructions and explanations.

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
