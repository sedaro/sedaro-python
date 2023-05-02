Test.
# Sedaro Python Client

This is the repository that houses the [Sedaro Python Client](https://github.com/sedaro/sedaro-python/tree/main/sedaro) (stored in directory `sedaro/`). Other files and directories in this repository help with development and maintenance of the [Sedaro Python Client](https://github.com/sedaro/sedaro-python/tree/main/sedaro). See below for some helpful notes regarding those other files and directories.


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
brew install python@3.7
brew install python@3.8
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

  - Switch out "3.7" for desired version
  ```zsh
  python3.7 -m venv ./.venv
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
