import platform
import time

import test_auth_handle
import test_bcc_options
import test_crud_and_traversal
import test_data_utils
import test_externals
import test_model_managers
import test_modsim
import test_plain_requests
import test_results
import test_scenario
import test_simulation
from config import HOST

############## IMPORT AND ADD TEST FILES HERE ##############
# All imports are expected to have a `run_tests` function


imported_test_files = [
    test_auth_handle,
    test_bcc_options,
    test_crud_and_traversal,
    test_data_utils,
    test_externals,
    test_model_managers,
    test_modsim,
    test_plain_requests,
    test_results,
    test_scenario,
    test_simulation,
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
