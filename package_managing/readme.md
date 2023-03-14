# Publishing to Python Package Index

## Preparation:

- Ensure on most up-to-date `sedaro-app` branch and openapi container is running (check spec at `http://localhost:8081/redoc`)
- Use client generator to make sure `sedaro_base_client` is up to date by regenerating it (options > "python" > "x")
  - `$ python3 client_generator`
  - Make sure to check `README` in client generator for "Known Issues"
  - Make sure dependencies in `sedaro/src/pyproject.toml` are up to date (should include everything in `requirements.txt` and `requirements-base-client.txt`)
- Ensure `BlockClassClient` options are up-to-date in `tests/test_bcc_options.py` and in `sedaro/readme.md`
  - Run `$ python3 client_generator/bcc_options.py` and compare against what's in both of those files.
- Use `python_version_manager` to install **local sedaro** package and run tests using **dev server** in python 3.7 - 3.10
  - Make sure to comment back things that may have been commented out during client generator
- Sync release `version` in `sedaro/src/pyproject.toml` file with Sedaro site release version

## Build

Inside `sedaro-python/`:

- Deactivate current python environment (`$ deactivate`)
- Delete and create new virtual environment and install needed dependencies:
  - `$ rm -rf .venv && python3 -m venv ./.venv && source .venv/bin/activate && pip install --upgrade pip && pip install --upgrade setuptools build twine`
- Build:
  - `$ cd sedaro`
  - `$ rm -rf dist && python3 -m build`
- If doesn’t create `.tar.gz` and `.whl` in `sedaro/dist/`, wait a minute. Reload vs-code if doesn't show up.

## Publish to test.pypi

- Do everything under "Build" above
- In `sedaro/`:
  - `$ python3 -m twine upload --repository testpypi dist/\*`
  - enter username and password
- Use `python_version_manager` to install sedaro from **test.pypi** and run tests using **live server** in python 3.7 - 3.10

## Publish to pypi:

- Open pull request. After merged, switch to main branch with new changes pulled in
- Do everything under "Build" above
- In `sedaro/`:
  - `$ python3 -m twine upload dist/\*`
  - enter username and password
- Use `python_version_manager` to install sedaro from **pypi** and run tests using **live server** in python 3.7 - 3.10
