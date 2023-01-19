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

    print('\nNote:')
    print('- All of the options should be listed above, but some of them may not have all letters in the correct case.')
    print('- They should correspond to `Block` names as defined in satellite-app (ex. "GpsAlgorithm" should be "GPSAlgorithm").')
    print('- Please confirm case.')
    print('')


if __name__ == '__main__':
    get_block_class_client_options()
