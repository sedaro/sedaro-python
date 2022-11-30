# Publishing to Python Package Index

## Preparation:

- Ensure on most up-to-date `sedaro-app` branch and openapi container is running (check spec at `http://localhost:8081/redoc`)
- Use client generator to make sure `sedaro_base_client` is up to date (options > "python" > "mu")
  - Make sure dependencies in `sedaro/src/pyproject.toml` are up to date (should include everything in `requirements.txt` and `requirements-base-client.txt`)
- Ensure `BlockClassClient` options are up-to-date in `tests/block_class_client_options.py` and in `sedaro/readme.md`
- Use `python_version_manager` to install **local sedaro** package and run tests using **dev server** in python 3.7 - 3.10
- Sync release `version` in `sedaro/src/pyproject.toml` file with Sedaro site release version

## Build

Inside `sedaro-python/`:

- Deactivate current python environment (`$ deactivate`)
- `$ rm -rf .venv && python3 -m venv ./.venv && source .venv/bin/activate && pip install --upgrade pip && pip install --upgrade setuptools build twine`
- `$ cd sedaro`
- `$ rm -rf dist && python3 -m build`
- If doesn’t create `.tar.gz` and `.whl`, wait a minute. Can re-run ^^^ if needed.

## Publish to test.pypi

- Do everything under "Build"
- `$ python3 -m twine upload --repository testpypi dist/\*`
  - requires username and password
- Use `python_version_manager` to install sedaro from **test.pypi** and run tests using **live server** in python 3.7 - 3.10

## Publish to pypi:

- Open pull request. After merged, switch to main branch with new changes pulled in
- Do everything under "Build"
- `$ python -m twine upload dist/\*`
  - requires username and password
- Use `python_version_manager` to install sedaro from **pypi** and run tests using **live server** in python 3.7 - 3.10
