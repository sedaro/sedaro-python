import os
import shutil

QUIT = "q"
SWITCH = "s"
RUN_TESTS = 't'
OPTIONS_MAIN = [QUIT, SWITCH]
# OPTIONS_MAIN = [QUIT, SWITCH, RUN_TESTS]
# TODO: python version wasn't switching in tests, so disabled RUN_TESTS for now
# Add that option back in and test it then follow the print outputs to see if works
VENV = '.venv'
PYTHON_VERSIONS = ['3.7', '3.8', '3.9', '3.10']


def get_cur_python_version():
    return os.popen("python3 -V").read().split("Python")[1][1:]


def switch_current_python_virtual_environment(new_version=None, run_tests=False):
    if new_version is None:
        print('\nAvailable python versions:')
        os.system('pyenv versions')
        print('Note: use `$ pyenv install <version>` if don\'t see desired version.')
        new_version = input(
            '\nWhich python version would you like to switch to? (see above)\n~ '
        )

    if os.path.isdir(VENV):
        shutil.rmtree(VENV)

    print(
        f'\n🛰️  Creating virtual environment for Python {new_version} and installing sedaro...\n'
    )

    try:
        command = f'pyenv local {new_version} && python3 -m venv ./.venv && source .venv/bin/activate && pip install -e sedaro'
        if run_tests:
            command += ' && python3 tests'
        os.system(command)
        print(
            f'\n🛰️  Virtual environment created/activated with Python {new_version} and sedaro installed'
        )

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
        if QUIT in OPTIONS_MAIN:
            print(
                f'  - "{QUIT}"   Quit'
            )
        if SWITCH in OPTIONS_MAIN:
            print(
                f'  - "{SWITCH}"   Switch to a new python virtual environment (deletes current one if exists)'
            )
        if RUN_TESTS in OPTIONS_MAIN:
            print(
                f'  - "{RUN_TESTS}"   Run tests in python versions {PYTHON_VERSIONS}'
            )

        how_proceed = input('~ ')

        if how_proceed not in OPTIONS_MAIN:
            print(f'\nInvalid option: "{how_proceed}"\n')

    if how_proceed == QUIT:
        print('\nClosing manager\n')
        return

    if how_proceed == SWITCH:
        switch_current_python_virtual_environment()
        return

    if how_proceed == RUN_TESTS:
        for version in PYTHON_VERSIONS:
            switch_current_python_virtual_environment(version, run_tests=True)
            print(f'\n🛰️  Finished running tests for version {version}')
        print(f'\n🛰️  Finished running tests for versions {PYTHON_VERSIONS}')
        return


if __name__ == '__main__':
    sedaro_client_python_version_manager()
