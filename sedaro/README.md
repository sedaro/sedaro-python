# Sedaro Python Client (Beta)

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
    AGENT_TEMPLATE_BRANCH_ID = 1 # id of a Branch owned by my Sedaro account with the given api key

    with SedaroApiClient(api_key=API_KEY) as sedaro_client:
        ...
    ```

    ```py
    # If using a dedicated enterprise Sedaro instance, overwrite the default `host` kwarg.
    ...
    HOST = 'url-to-my-sedaro-server-instance.com'

    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro_client:
        ...
    ```

2.  Use the client to instantiate a `BranchClient`.

    ```py
    ...

    with SedaroApiClient(api_key=API_KEY) as sedaro_client:
        branch_client = sedaro_client.get_branch(AGENT_TEMPLATE_BRANCH_ID)
    ```

3.  Use the `BranchClient` to access and utilize `BlockClassClient`s. A `BlockClassClient` is used to create and access Sedaro Blocks of the respective class.

    ```py
    ...

        branch_client = sedaro_client.get_branch(AGENT_TEMPLATE_BRANCH_ID)

        branch_client.BatteryCell

        branch_client.Component

        branch_client.Subsystem

        # ...etc.

    ```

    - Valid `BlockClassClient`s for an Agent Template Branch are as follows:

      - AngularVelocitySensor
      - AveragingAlgorithm
      - Battery
      - BatteryCell
      - BatteryPack
      - BodyFrameVector
      - BusRegulator
      - CelestialTarget
      - CelestialVector
      - CircularFieldOfView
      - Component
      - Condition
      - ConOps
      - ConstantLoad
      - Cooler
      - DirectionSensor
      - EKFAlgorithm
      - FOVConstraint
      - FuelReservoir
      - GPSAlgorithm
      - GroundTarget
      - GroupCondition
      - Heater
      - LoadState
      - LocalVector
      - LockPointingMode
      - Magnetorquer
      - MaxAlignPointingMode
      - MEKFAlgorithm
      - OperationalMode
      - OpticalAttitudeSensor
      - PassivePointingMode
      - PIDAlgorithm
      - PositionSensor
      - ReactionWheel
      - RectangularFieldOfView
      - Satellite
      - SlidingModeAlgorithm
      - SolarArray
      - SolarCell
      - SolarPanel
      - SpaceTarget
      - SphericalFuelTank
      - SpherocylinderFuelTank
      - StaticThrustControlAlgorithm
      - Subsystem
      - Surface
      - SurfaceMaterial
      - TargetGroup
      - TargetGroupVector
      - TargetVector
      - TempControllerState
      - ThermalInterface
      - ThermalInterfaceMaterial
      - Thruster
      - Topology
      - TriadAlgorithm
      - VectorSensor

    - Valid `BlockClassClient`s for an Scenario Branch are as follows:
      - Agent
      - ClockConfig
      - Orbit

4.  A `BlockClassClient` has several methods:

    ```py
    ...
        branch_client.Subsystem.create(
            name='Structure',
            satellite='3'  # The ID of the related Satellite Block
        )

        branch_client.Subsystem.get(block_id) # ID of desired Subsystem
        branch_client.Subsystem.get_all()
        branch_client.Subsystem.get_first()
        branch_client.Subsystem.get_last()
        branch_client.Subsystem.get_all_ids()
    ```

5.  Most `BlockClassClient` methods return a `BlockClient` which has several methods and properties.

    ```py
    ...
        subsystem_client = branch_client.Subsystem.create(
            name='Structure',
            satellite='3'
        )

        subsystem_client.update(name='Structure 2.0')

        subsystem_client.delete()
    ```

    ```py
    ...
    # A `BlockClient` will always be equal to and in sync with all other `BlockClient`s referencing the same Sedaro Block:
        subsystem_client = branch_client.Subsystem.create(
            name='Structure',
            satellite='3'
        )

        subsystem_client_2 = subsystem_client.update(
         name='Structure 2.0'
        )

        subsystem_client_3 = branch_client.Subsystem.get(subsystem_client.id)

        assert subsystem_client == subsystem_client_2 == subsystem_client_3
    ```

    ```py
    ...
    # Printing a `BlockClient` will show you the corresponding Sedaro Block's data:
        print(subsystem_client)

    >>> Subsystem(
    >>>   id=27
    >>>   name=Structure 2.0
    >>>   category=CUSTOM
    >>>   satellite=3
    >>>   components=()
    >>> )
    ```

    ```py
    # Keying into any property existing on the corresponding Sedaro Block will return that properties value.
        subsystem_client.name

    >>> 'Structure 2.0'
    # Keying into a property that is a relationship field, will return a `BlockClient` corresponding to the related `Block` (or `list` of `BlockClient`s if it's a many-side relationship field).
        subsystem.satellite

    >>> Satellite(
    >>>   id=3
    >>>   mass=1000
    >>>   ...etc
    >>> )
    ```

    ```py
    # This allows for traversing Blocks in the model via relationship fields:
        solar_panel_client = branch_client.SolarPanel.get_first()

        solar_panel_client.cell.panels[-1].subsystem.satellite.components[0].delete()
    ```

### Full Example

```py
from sedaro import SedaroApiClient
from sedaro.exceptions import NonexistantBlockError

API_KEY = 'my_api_key_generated_by_sedaro_satellite'
AGENT_TEMPLATE_BRANCH_ID = 1

with SedaroApiClient(api_key=API_KEY) as sedaro_client:
    branch_client = sedaro_client.get_branch(AGENT_TEMPLATE_BRANCH_ID)

    battery_cell_client = branch_client.BatteryCell.create(
        partNumber='987654321',
        manufacturer='Sedaro Corporation',
        esr=0.01,
        maxChargeCurrent=15,
        maxDischargeCurrent=100,
        minSoc=0.2,
        capacity=500,
        curve=[[0, 0.5, 1], [12.2, 14.1, 16.8]],
        topology='5',
    )

    bc_id = battery_cell_client.id

    battery_cell_client.update(partNumber="123456789")

    battery_cell_client.delete()

    try:
        battery_cell_client.update(partNumber="987654321")
    except NonexistantBlockError as e:
        assert str(e) == f'The referenced "BatteryCell" (id: {bc_id}) no longer exists.'
```

## Use: Simulation

```py
SCENARIO_BRANCH_ID = 2

with SedaroApiClient(api_key=API_KEY) as sedaro_client:

    # Instantiate sim client
    sim_client = sedaro_client.get_sim_client(SCENARIO_BRANCH_ID)

    # Start simulation
    sim_client.start()

    # Get simulation
    response = sim_client.get_latest()

    # Check status & percentage complete
    job = response.body[0]
    assert job['status'] == 'RUNNING'
    print(job['progress']['percentComplete'])

    # Terminate simulation
    response = sim_client.terminate(job['id'])
    assert response.body['message'] == 'Successfully terminated simulation.'

```

## Use: Send Requests

Use built-in method to send customized requests to the host. See [OpenAPI Specification](https://sedaro.github.io/openapi/) for documentation on resource paths and body params.

```py
with SedaroApiClient(api_key=API_KEY) as sedaro_client:
    # get a branch
    sedaro_client.send_request(
        f'/models/branches/{AGENT_TEMPLATE_BRANCH_ID}',
        'GET'
    )

    # create a celestial target in a branch
    sedaro_client.send_request(
        f'/models/branches/{AGENT_TEMPLATE_BRANCH_ID}/cdh/conops/celestial-targets/',
        'POST',
        body={
            'name': 'Sun',
            'polynomialEphemerisBody': 'SUN',
            'conOps': 2
        }
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
