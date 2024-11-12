# Sedaro Python Client

**For documentation on the use of the Sedaro Python Client, see the documentation [here](./sedaro/README.md).  This documentation is for client development, maintenance, and testing.**

## Usage:

See [Sedaro Python Client](./sedaro/README.md) for client usage instructions.  The rest of this documentation is for client development, maintenance, and testing.

## To run tests:

- For Sedaro devs testing in the local development environment: make sure `sedaro-app` container is running.
- Create a `tests/config.py` file based on the `tests/config_example.py` file:
  - For Sedaro devs testing in the live environment: update the `HOST` variable to `'http://localhost:80'`.
  - For non-Sedaro devs testing in a dedicated Sedaro instance: update the `HOST` to the url of your Sedaro server.
- Ensure `pytest` is installed in the python environment (`$ pip install pytest`). If you use the `python_version_manager` to create the virtual environment, it will be installed.

Run:

```zsh
python3 tests
```

## To switch python version in this directory's virtual environment:

Install the python version you want to use if it isn't already installed:

```zsh
brew install python@3.9
brew install python@3.10
...etc
```

To check curent python version:

```zsh
python3 -V
```

### Option #1 (custom script)

- Use the custom python version manager designed for use in this directory. You will be prompted on how to proceed.

  ```zsh
  python3 python_version_manager
  ```

### Option #2 (manual)

- Create and activate virtual environment (first `deactivate` current virtual environment and delete `.venv` directory if already exists):

  - Switch out "3.9" for desired version
  ```zsh
  python3.9 -m venv ./.venv
  source .venv/bin/activate
  ```

- Install sedaro python client:

  ```
  pip install -e sedaro
  pip install pytest
  ```

## To run client generator:

Note: this is designed and set up for Sedaro dev's use.

```zsh
python3 client_generator
```

## To generate protobufs for cosimulation:

Note: this is designed and set up for Sedaro dev's use.

```zsh
python3 -m grpc_tools.protoc --proto_path=<PATH_OF_cosim.proto>--python_out=./sedaro/src/sedaro/grpc_client --grpc_python_out=./sedaro/src/sedaro/grpc_client cosim.proto
```
