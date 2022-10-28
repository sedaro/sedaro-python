# Sedaro Python Client (Beta)

A python client for interacting with the Sedaro Satellite API using intuitive classes and methods.

## Install

```bash
pip install sedaro
```

## Use

1. Instantiate the `SedaroApiClient` as a context manager.

```py
from sedaro import SedaroApiClient

API_KEY = 'my_api_key_generated_by_sedaro_satellite'
BRANCH_ID = 1 # id of a Branch owned by my Sedaro account with the given api key

with SedaroApiClient(api_key=API_KEY) as sedaro_client:
    ...
```

2. Use the client to instantiate a `BranchClient`.

```py
with SedaroApiClient(api_key=API_KEY) as sedaro_client:
    branch_client = sedaro_client.get_branch(BRANCH_ID)
```

3. Use the `BranchClient` to access and utilize `BlockClassClient`s.

```py
with SedaroApiClient(api_key=API_KEY) as sedaro_client:
    branch_client = sedaro_client.get_branch(BRANCH_ID)

    branch_client.BatteryCell

    branch_client.Target

    branch_client.Subsystem

    tranch_client.Component

    # ...etc.

```

4. A `BlockClassClient` have several methods that all return 1+ `BlockClient`s:

```py

```
