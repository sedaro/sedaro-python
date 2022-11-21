import os

QUIT = "q"
SWITCH = "s"


def delete_current_python_virtual_environment():
    print('')


def sedaro_client_python_version_manager():

    print('\n---------< Sedero Client python version manager >---------')

    print('\nCurrent python environment:')
    os.system('pip -V')

    cur_version = os.popen("python3 -V").read().split("Python")[1][1:]
    print('\nCurrent python version:')
    print(cur_version)

    choice = ''

    while choice not in [QUIT, SWITCH]:
        print('\nOptions:')
        print(
            f'  - "{QUIT}"   Quit'
        )
        print(
            f'  - "{SWITCH}"   Switch to a new python virtual environment (will delete current one if exists)'
        )

        choice = input('~ ')

    if choice == QUIT:
        print('\nClosing manager\n')
        return

    if choice == SWITCH:
        new_version = input(
            '\nWhich python version would you like to switch to?\n~ ')
        print(new_version, cur_version)


if __name__ == '__main__':
    sedaro_client_python_version_manager()
