import time

############## IMPORT AND ADD TEST FILES HERE ##############
# All imports are expected to have a `run_tests` function

import block_class_client_options
import block_crud_tests
import simulation_tests

test_imports = [
    block_class_client_options,
    block_crud_tests,
    simulation_tests
]
############################################################


def run_tests():
    '''Runs all tests from `test_imports` with name, progress, and time `print`s throughout.'''
    num_tests = len(test_imports)
    for i, imported_test_file in enumerate(test_imports):

        intro = f'### Test {i + 1}/{num_tests}: "{imported_test_file.__name__}" --'

        # print and start timer
        print(f'\n{intro} running...')
        start_time = time.perf_counter()

        # run tests
        imported_test_file.run_tests()

        # end timer and print
        total_time = round(time.perf_counter() - start_time, 2)
        print(f'{intro} done in {total_time} seconds')

        # delay so prints are easier to follow
        time.sleep(0.5)

    print('\n### Done!')


if __name__ == "__main__":
    run_tests()
