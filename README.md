# Sedaro Clients

See below for some helpful notes

## To run tests:

Make sure `sedaro-app` container is running. Update the variables in `tests/config.py` to reflect an API key for a `user` in your dev environment and branch ID's that correspond to that user. Then run:

```zsh
python3 tests
```

## To run client generator:

```zsh
python3 client_generator
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

## .zshrc or .bashrc

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
