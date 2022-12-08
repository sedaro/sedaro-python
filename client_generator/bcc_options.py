import os
from pydash.strings import pascal_case


def get_block_class_client_options():
    all_tags = os.listdir('./sedaro/src/sedaro_base_client/apis/tags')
    all_tags.sort()
    for t in all_tags:
        if t.startswith('__'):
            continue

        option = pascal_case(t.replace('api.py', ''))
        if option in {'Branches', 'Data', 'Jobs'}:
            continue

        print(option)


if __name__ == '__main__':
    get_block_class_client_options()
