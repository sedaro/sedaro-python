import time

############ IMPORT AND ADD TESTS HERE ############
import block_class_client_options
import block_crud_tests
import simulation_tests

test_imports = [
    block_class_client_options,
    block_crud_tests,
    simulation_tests
]
###################################################


def run_tests():
    num_tests = len(test_imports)
    for i, t in enumerate(test_imports):

        cur_t_num = f'{i + 1}/{num_tests}'

        print(f'\n### Test {cur_t_num}: "{t.__name__}" -- running...')
        start_time = time.perf_counter()

        t.run_tests()

        print(
            f'\n### Test {cur_t_num}: "{t.__name__}" -- done in {round(time.perf_counter() - start_time, 2)} seconds'
        )
        time.sleep(.5)

    print('\n### Done!')


if __name__ == "__main__":
    run_tests()
