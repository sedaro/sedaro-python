import time

import block_class_client_options
import block_crud_tests
import simulation_tests


def run_tests():
    for file in [
        block_class_client_options,
        block_crud_tests,
        simulation_tests
    ]:
        print(f'\n### "{file.__name__}" -- running tests')
        start_time = time.perf_counter()

        file.run_tests()

        print(
            f'\n### "{file.__name__}" -- done in {round(time.perf_counter() - start_time, 2)} seconds'
        )

    print('\n### Done!')


if __name__ == "__main__":
    run_tests()
