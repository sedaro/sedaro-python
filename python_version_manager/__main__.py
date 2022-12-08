import os
import shutil
import time

QUIT = 'q'
SWITCH_LOCAL = 'sl'
TESTS_LOCAL = 'tl'
SWITCH_PYPI_TEST = 'st'
TESTS_PYPI_TEST = 'tt'
SWITCH_PYPI = 'sp'
TESTS_PYPI = 'tp'

PY_VERSIONS_TESTS = ['3.7', '3.8', '3.9', '3.10']

SWITCH_INSTR = 'Switch python version, install sedaro from: '
TEST_INSTR = f'Run tests in python versions {PY_VERSIONS_TESTS} using sedaro from: '

OPTIONS_MAIN = {
    QUIT: ('quit', ''),
    SWITCH_LOCAL: ('switch local', f'{SWITCH_INSTR}local sedaro directory'),
    TESTS_LOCAL: ('test local', f'{TEST_INSTR}local sedaro directory'),
    SWITCH_PYPI_TEST: ('switch test.pypi', f'{SWITCH_INSTR}test.pypi'),
    TESTS_PYPI_TEST: ('test test.pypi', f'{TEST_INSTR}test.pypi'),
    SWITCH_PYPI: ('switch pypi', f'{SWITCH_INSTR}pypi'),
    TESTS_PYPI: ('test pypi', f'{TEST_INSTR}pypi'),
}

VENV = '.venv'


def get_cur_python_version():
    return os.popen('python3 -V').read().split('Python')[1][1:]


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

    if pypi_sedaro:
        print_msg_end = 'from pypi'
    elif test_pypi_sedaro:
        print_msg_end = 'from test.pypi'
    else:
        print_msg_end = 'from local sedaro directory'

    print(
        f'\n🛰️  Creating virtual environment for Python {new_version} and installing sedaro {print_msg_end}...'
    )

    PIP_INSTALL = 'pip install'
    if run_tests:
        # Don't show whole pip output ("quiet" flag) when running tests
        PIP_INSTALL += ' -q'
    else:
        # Print empty line before pip output when it's not "quiet"
        print('')

    try:
        command = f'pyenv local {new_version} && python3 -m venv ./.venv && source .venv/bin/activate && {PIP_INSTALL} --upgrade pip && {PIP_INSTALL} -U autopep8'
        if pypi_sedaro:
            command += f' && {PIP_INSTALL} sedaro'
        elif test_pypi_sedaro:
            # see S.O. answer for context on command below: https://stackoverflow.com/a/59495166/16448566
            command += f' {PIP_INSTALL} --index-url https://test.pypi.org/simple/ --upgrade --no-cache-dir --extra-index-url=https://pypi.org/simple/ sedaro'
        else:
            command += f' && {PIP_INSTALL} -e sedaro'
        os.system(command)
        print(
            f'\n🛰️  Virtual environment created/activated with Python {new_version} and sedaro installed {print_msg_end}'
        )

        time.sleep(0.5)
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
            stands_for, description = v
            command = f'  - "{k}"'
            for _ in range(7 - len(k)):
                command += ' '
            command += stands_for
            for _ in range(33 - len(command)):
                command += ' '
            command += description
            print(command)

        how_proceed = input('~ ')

        if how_proceed not in OPTIONS_MAIN:
            print(f'\nInvalid option: "{how_proceed}"\n')

    kwargs = {}

    if how_proceed == QUIT:
        print('\nClosing manager\n')
    elif how_proceed in [SWITCH_PYPI, TESTS_PYPI]:
        kwargs['pypi_sedaro'] = True
    elif how_proceed in [SWITCH_PYPI_TEST, TESTS_PYPI_TEST]:
        kwargs['test_pypi_sedaro'] = True

    # just switch or switch and run tests
    if how_proceed in [SWITCH_LOCAL, SWITCH_PYPI, SWITCH_PYPI_TEST]:
        switch_current_python_virtual_environment(**kwargs)

    elif how_proceed in [TESTS_LOCAL, TESTS_PYPI, TESTS_PYPI_TEST]:
        for version in PY_VERSIONS_TESTS:
            switch_current_python_virtual_environment(
                new_version=version,
                run_tests=True,
                **kwargs
            )
            print(f'\n🛰️  Finished running tests for python version {version}')
            # short pause needed here to make sure next venv is created and used properly
            time.sleep(1)

        print(
            f'\n🛰️  Finished running tests for python versions {PY_VERSIONS_TESTS}'
        )

    return


if __name__ == '__main__':
    sedaro_client_python_version_manager()
