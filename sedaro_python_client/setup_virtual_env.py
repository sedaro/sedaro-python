import os


def make_virtual_env():
    os.system('python3.9 -m venv ./.venv')
    os.system('source .venv/bin/activate')
    os.system('pipenv install -r sedaro_python_client/requirements.txt')


if __name__ == '__main__':
    make_virtual_env()
