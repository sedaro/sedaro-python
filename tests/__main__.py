import time
import platform
from config import HOST

############## IMPORT AND ADD TEST FILES HERE ##############
# All imports are expected to have a `run_tests` function

import block_class_client_options
import block_crud_tests
import simulation_tests

imported_test_files = [
    block_class_client_options,
    block_crud_tests,
    simulation_tests
]
############################################################


def run_tests():
    '''Runs all tests from `imported_test_files` with name, progress, and time `print`s throughout.'''
    print(f'\n### Test Info:')
    print(f'### - Running in Python: {platform.python_version()}')
    print(f'### - Running with server: {HOST}')
    # delay so prints are easier to follow
    time.sleep(0.5)

    for i, test_file in enumerate(imported_test_files):

        intro = f'### Test {i + 1}/{len(imported_test_files)}: "{test_file.__name__}" --'

        # print and start timer
        print(f'\n{intro} running...')
        start_time = time.perf_counter()

        # run tests
        test_file.run_tests()

        # end timer and print
        total_time = round(time.perf_counter() - start_time, 2)
        print(f'{intro} done in {total_time} seconds')

        # delay so prints are easier to follow
        time.sleep(0.5)

    print('\n### Done!')


if __name__ == "__main__":
    run_tests()
