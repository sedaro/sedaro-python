# Clients

## Sedaro OpenAPI Client Generator

An interactive tool for building clients for Sedaro Satellite based on our OpenAPI spec. Built on an **OpenAPI Generator** docker image: https://openapi-generator.tech/docs/installation#docker

If you are generating a client based on the dev open api spec, make sure the open api docker container is running. If you want to make it based on the live spec, upload the `DOWNLOAD_SPEC_FROM` accordingly variable in `__main__.py`.

In the directory containing this directory run:

- `$ python client_generator.py` or `$ python3 client_generator.py`

You will be prompted on how to proceed.

_Note: requires python to be installed on the computer or a virtual environment to be created in the directory._
