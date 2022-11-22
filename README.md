# Sedaro Python Client

This is the repository that houses the [Sedaro Python Client](sedaro/README.md) (stored in directory `sedaro/`). Other files and directories in this repository help with development and maintenance of the [Sedaro Python Client](sedaro/README.md). See below for some helpful notes regarding those other files and directories.

## To run tests:

- For Sedaro devs testing in the local development environment: make sure `sedaro-app` container is running.

- For non-Sedaro devs testing in the live environment: update the `HOST` variable in `tests/config.py` to `'https://api.sedaro.com'`.

- For non-Sedaro devs testing in a dedicated Sedaro instance: update the `HOST` variable in `tests/config.py` to the url of your Sedaro server.

- For everyone: update the remaining variables in `tests/config.py` to reflect an API key for a `user` in your environment and for branch ID's that correspond to that user.

Run:

```zsh
python3 tests
```

## To switch python version in this directory's virtual environment:

Have `pyenv` installed:

```zsh
brew install pyenv
```

Install the python version you want to use if it isn't already installed:

```zsh
pyenv install <version>
```

Other helpful commands

```zsh
# List available python versions:
pyenv versions

# Check curent python version:
python3 -V
```

Note: see section ".zshrc or .bashrc" for potential necessary updates to those files.

### Option #1 (custom script)

- Use the custom python version manager designed for use in this directory. You will be prompted on how to proceed.

  ```zsh
  python3 python_version_manager
  ```

### Option #2 (manual)

- Select version for current directory (this will update the `.python-version` file):

  ```zsh
  pyenv local <version>
  ```

- Create and activate virtual environment (first `deactivate` current virtual environment and delete `.venv` directory if already exists):

  ```zsh
  python3 -m venv ./.venv
  source .venv/bin/activate
  ```

- Install sedaro python client:

  ```
  pip install -e sedaro
  ```

### .zshrc or .bashrc

You may need to add the following to your `.zshrc` or `.bashrc` file. See S.O. answer [here](https://stackoverflow.com/a/71364553/16448566).

```zsh
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
export PIPENV_PYTHON="$PYENV_ROOT/shims/python"
plugin=(
  pyenv
)
eval "$(pyenv init -)"
eval "$(command pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```

## To run client generator:

Note: this is designed and set up for Sedaro dev's use.

```zsh
python3 client_generator
```
