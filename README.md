# Clients

## Sedaro OpenAPI Client Generator

An interactive tool for building clients for Sedaro Satellite based on our OpenAPI spec. Built on an **OpenAPI Generator** docker image: https://openapi-generator.tech/docs/installation#docker

In this folder run:

- Set up virtual environment if haven't done already:
  - Create virtual environment: `$ python3.9 -m venv ./.venv`
  - Active virtual environment: `source .venv/bin/activate`
  - Install dependencies: `$ pipenv install` to install dependencies and create virtual environment
  - Select the newly created python environment in vs-code (`cmd shift p` > "Python: Select Interpreter")
- Activate script:
  - `$ python3 generate.py` or `$ python3 generate.py`
  - You will be prompted on how to proceed.

_Note: requires python to be installed on the computer or a virtual environment to be created in the directory._
