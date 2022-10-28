# Sedaro Python Client (Beta)

A python client for interacting with the Sedaro Satellite API using intuitive classes and methods.

## Install

```bash
pip install sedaro
```

## Use

1. Instantiate the `SedaroApiClient` as a context manager. All code interacting with the API within the scope of that context manager.

   ```py
   from sedaro import SedaroApiClient

   API_KEY = 'my_api_key_generated_by_sedaro_satellite'
   BRANCH_ID = 1 # id of a Branch owned by my Sedaro account with the given api key

   with SedaroApiClient(api_key=API_KEY) as sedaro_client:
       ...
   ```

2. Use the client to instantiate a `BranchClient`.

   ```py
   ...

   with SedaroApiClient(api_key=API_KEY) as sedaro_client:
       branch_client = sedaro_client.get_branch(BRANCH_ID)
   ```

3. Use the `BranchClient` to access and utilize `BlockClassClient`s.

   ```py
   ...

       branch_client = sedaro_client.get_branch(BRANCH_ID)

       branch_client.Target

       tranch_client.Component

       branch_client.BatteryCell

       branch_client.Subsystem

       # ...etc.

   ```

4. A `BlockClassClient` has several methods:

   ```py
   ...
       branch_client.subsystem.create(
           name='One subsystem to rule them all',
           satellite='5'
       )

       branch_client.subsystem.get('5')
       branch_client.subsystem.get_all()
       branch_client.subsystem.get_first()
       branch_client.subsystem.get_last()
       branch_client.subsystem.get_all_ids()
   ```

5. Most `BlockClassClient` methods return a `BlockClient` which has several methods and properties.

   ```py
   ...
       subsystem_client = branch_client.subsystem.create(
           name='One subsystem to rule them all',
           satellite='5'
       )

       subsystem_client.update(name='One subsystem to find them')

       subsystem_client.delete()
   ```

   ```py
   ...
   # A `BlockClient` will always be equal to and in sync with any other `BlockClient` referencing the same Sedaro block:
       subsystem_client = branch_client.subsystem.create(
           name='One subsystem to bring them all',
           satellite='5'
       )

       subsystem_client_2 = subsystem_client.update(
        name='And in the darkness to bind them'
       )

       subsystem_client_3 = branch_client.subsystem.get(subsystem_client.id)

       assert subsystem_client == subsystem_client_2 == subsystem_client_3
   ```

   ```py
   ...
   # Printing a `BlockClient` will show you the corresponding Sedaro blocks data:
   print(subsystem_client)
   >>> Subsystem(
   >>>   id=27
   >>>   name=One subsystem to find them
   >>>   category=CUSTOM
   >>>   satellite=5
   >>>   components=()
   >>> )
   ```

   ```py
   # Keying into any property existing on the corresponding Sedaro block, will return that properties value.
   subsystem_client.name
   >>> 'And in the darkness to bind them'
   # Keying into a property that is a relationship field, will return a `BlockClient` corresponding to the related `Block` (or `list` of `BlockClient`s) if it's a many-side relationship field.
   subsystem.satellite
   >>> Satellite(
   >>>   id=5
   >>>   mass=1000
   >>>   ...etc
   >>> )
   ```

   ```py
   # This allows for traversing all the blocks in the branch via relationship fields:
   solar_panel_client = branch_client.solarPanel.get_first()
   solar_panel_client.cell.panels[-1].subsystem.satellite.components[0].thermal_interface_A[0].satellite.topology
   ```
