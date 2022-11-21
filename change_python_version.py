import os
import shutil
import subprocess

QUIT = "q"
SWITCH = "s"
RUN_TESTS = 't'
OPTIONS_MAIN = [QUIT, SWITCH, RUN_TESTS]
VENV = '.venv'

def get_cur_python_version():
    return os.popen("python3 -V").read().split("Python")[1][1:]

def switch_current_python_virtual_environment():
    new_version = input(
        '\nWhich python version would you like to switch to?\n~ '
    )

    if os.path.isdir(VENV):
        shutil.rmtree(VENV)

    try:
        subprocess.check_output(f"pyenv local {new_version}", shell=True)
        os.system('python3 -m venv ./.venv')
        os.system('source .venv/bin/activate')
        print(f'\nVirtual environment created and activated with Python {get_cur_python_version()}')
    except:
        switch_current_python_virtual_environment()

def sedaro_client_python_version_manager():

    print('\n---------< Sedero Client - python version manager >---------')

    print('\nCurrent python environment:')
    os.system('pip -V')

    print(f'\nCurrent python version: {get_cur_python_version()}')

    how_proceed = ''
    while how_proceed not in OPTIONS_MAIN:
        print('\nOptions:')
        print(
            f'  - "{QUIT}"   Quit'
        )
        print(
            f'  - "{SWITCH}"   Switch to a new python virtual environment (deletes current one if exists)'
        )
        print(
            f'  - "{RUN_TESTS}"   Run tests in python 3.7 - 3.10'
        )

        how_proceed = input('~ ')

        if how_proceed not in OPTIONS_MAIN:
            print(f'\nInvalid option: "{how_proceed}"')

    if how_proceed == QUIT:
        print('\nClosing manager\n')
        return

    if how_proceed == SWITCH:
        switch_current_python_virtual_environment()
        return

    if how_proceed == RUN_TESTS:
        print('run tests!!')
        return

if __name__ == '__main__':
    sedaro_client_python_version_manager()
