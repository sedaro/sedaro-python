import os
import shutil
import time

QUIT = "q"
SWITCH = "sl"
SWITCH_PYPI = "sp"
SWITCH_PYPI_TEST = "st"
RUN_TESTS = 't'

PY_VERSIONS_TESTS = ['3.7', '3.8', '3.9', '3.10']

SWITCH_INSTR = 'Switch python version, install sedaro from: '

OPTIONS_MAIN = {
    QUIT: 'Quit',
    SWITCH: f'{SWITCH_INSTR}local sedaro directory',
    SWITCH_PYPI: f'{SWITCH_INSTR}pypi',
    SWITCH_PYPI_TEST: f'{SWITCH_INSTR}test.pypi',
    RUN_TESTS: f'Run tests in python versions {PY_VERSIONS_TESTS}'
}
# TODO: python version wasn't switching in tests, so disabled RUN_TESTS for now
# Add that option back in and test it then follow the print outputs to see if works
VENV = '.venv'


def get_cur_python_version():
    return os.popen("python3 -V").read().split("Python")[1][1:]


def switch_current_python_virtual_environment(new_version=None, run_tests=False, pypi_sedaro=False, test_pypi_sedaro=False):
    if new_version is None:
        print('\nAvailable python versions:')
        os.system('pyenv versions')
        print('Note: use `$ pyenv install <version>` if don\'t see desired version.')
        new_version = input(
            '\nWhich python version would you like to switch to? (see above)\n~ '
        )

    if os.path.isdir(VENV):
        shutil.rmtree(VENV)

    print_msg = f'\n🛰️  Creating virtual environment for Python {new_version} and installing sedaro'
    if pypi_sedaro:
        print_msg += ' from pypi'
    elif test_pypi_sedaro:
        print_msg += ' from test.pypi'
    else:
        print_msg += ' from local sedaro directory'
    print(print_msg + '...\n')

    try:
        command = f'pyenv local {new_version} && python3 -m venv ./.venv && source .venv/bin/activate && pip install --upgrade pip && pip install -U autopep8'
        if pypi_sedaro:
            command += ' && pip install sedaro'
        elif test_pypi_sedaro:
            # see S.O. answer for context on command below: https://stackoverflow.com/a/59495166/16448566
            command += ' pip install --index-url https://test.pypi.org/simple/ --upgrade --no-cache-dir --extra-index-url=https://pypi.org/simple/ sedaro'
        else:
            command += ' && pip install -e sedaro'
        os.system(command)
        print(
            f'\n🛰️  Virtual environment created/activated with Python {new_version} and sedaro installed'
        )
        if run_tests:
            os.system('python3 tests')

    except Exception as e:
        print('')
        print('='*50)
        print(e)
        print('='*50)
        print('')
        switch_current_python_virtual_environment()


def sedaro_client_python_version_manager():

    print('\n---------< Sedero Client - python version manager >---------')

    print('\nCurrent python environment:')
    os.system('pip -V')

    print(f'\nCurrent python version:')
    print(get_cur_python_version())

    how_proceed = ''
    while how_proceed not in OPTIONS_MAIN:
        print('Options:')
        print('  (note, "Switch" options deletes/recreates venv)')
        for k, v in OPTIONS_MAIN.items():
            command = f'  - "{k}"'
            for _ in range(8 - len(k)):
                command += ' '
            print(command + v)

        how_proceed = input('~ ')

        if how_proceed not in OPTIONS_MAIN:
            print(f'\nInvalid option: "{how_proceed}"\n')

    if how_proceed == QUIT:
        print('\nClosing manager\n')

    elif how_proceed == SWITCH:
        switch_current_python_virtual_environment()

    elif how_proceed == SWITCH_PYPI:
        switch_current_python_virtual_environment(pypi_sedaro=True)

    elif how_proceed == SWITCH_PYPI_TEST:
        switch_current_python_virtual_environment(test_pypi_sedaro=True)

    elif how_proceed == RUN_TESTS:
        for version in PY_VERSIONS_TESTS:
            switch_current_python_virtual_environment(
                new_version=version,
                run_tests=True
            )
            print(f'\n🛰️  Finished running tests for version {version}')
            # short pause needed here to make sure next venv is created and used properly
            time.sleep(1)
        print(f'\n🛰️  Finished running tests for versions {PY_VERSIONS_TESTS}')

    return


if __name__ == '__main__':
    sedaro_client_python_version_manager()
