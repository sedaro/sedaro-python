import os
import tempfile
import shutil
import json
import urllib.request
import urllib.error

DOWNLOAD_SPEC_FROM = 'http://localhost:8081/sedaro-satellite.json'

# CONSTANTS
PYTHON = 'python'
CUSTOM = 'custom'
SEDARO = 'sedaro'
GENERATE_NEW = 'new'
DRY_RUN = 'dr'
MINIMAL_UPDATE = 'mu'
QUIT = 'q'
REGENERATE = 'x'
DIFFERENT_LANGUAGE = 'dl'


def run_generator(skip_intro=False):
    '''Begin basic interactive terminal to create a client.'''

    if not skip_intro:
        print('\n------< 🛰️  Sedaro OpenAPI Client Generator 🛰️  >------')

    # ----------------- get desired language for client -----------------
    language = None
    while language == None:
        print('\nWhat coding language would you like to generate a client for? (Can also type "options")')
        language = input('~ ').lower().strip()

        if language == "options":
            print('')
            print(os.system(
                'docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli list'))
            print(
                '\n*** Note: this is intended to be used for generating a client, scroll up to "CLIENT generators". ***')
            language = None

    CONFIG_FILE = f'/client_generator/{language}_config.json'
    config_dict = None
    if os.path.isfile('.' + CONFIG_FILE):
        config_dict = json.load(open(f'.{CONFIG_FILE}'))
        PROJECT_NAME = config_dict['projectName']
        PACKAGE_NAME = config_dict['packageName']
    else:
        PROJECT_NAME = f'{SEDARO}_base_client'
        PACKAGE_NAME = f'{SEDARO}_base_client'

    CLIENT_DIR_BUILD = f'build/{language}/{PROJECT_NAME}'

    # --------- check if client exists and if want to overwrite ---------
    how_to_proceed = None
    proceed_options = (
        GENERATE_NEW, DRY_RUN, MINIMAL_UPDATE, QUIT, DIFFERENT_LANGUAGE, REGENERATE
    )

    if not os.path.isdir(CLIENT_DIR_BUILD):
        how_to_proceed = GENERATE_NEW

    while how_to_proceed not in proceed_options:
        print(
            f'\nA client has already been generated for {language}. How would you like to proceed?')
        print(
            f'  + "{DRY_RUN}"    dry-run                try things out and report on potential changes (without actually making changes)')
        print(
            f'  + "{MINIMAL_UPDATE}"    minimal-update         only write output files that have changed')
        print(
            f'  + "{QUIT}"     quit                   abort generator')
        print(
            f'  + "{DIFFERENT_LANGUAGE}"    different language     restart and pick a different language')
        print(
            f'  + "{REGENERATE}"     regenerate             delete and regenerate client (use with caution)')
        how_to_proceed = input('~ ').lower().strip()

        if how_to_proceed not in proceed_options:
            print(f'\n"{how_to_proceed}" is not a valid choice')

    if how_to_proceed == REGENERATE:
        yn = None
        yn_options = ('y', 'n')
        while yn not in yn_options:
            print('\nAre you sure you would like to regenerate the client? Any customizations you made will be lost. (y/n)')
            yn = input('~ ').lower().strip()
            if yn not in yn_options:
                print(f'\n"{yn}" is not a valid choice')
            if yn == 'n':
                how_to_proceed = QUIT

    if how_to_proceed == QUIT:
        print('\n------------------< 🛰️  Aborted 🛰️  >------------------\n')
        return

    if how_to_proceed == DIFFERENT_LANGUAGE:
        run_generator(skip_intro=True)

    # ----------------------- generate new client -----------------------
    with tempfile.TemporaryDirectory(dir='./', prefix='.temp_dir_', suffix='_spec') as temp_dir:

        # ----- remove client if already exists -----
        if how_to_proceed == REGENERATE:
            # ----- delete old client dir -----
            os.system(f'rm -r {CLIENT_DIR_BUILD}')

        TEMP_SPEC_LOCATION = f'{temp_dir}/spec.json'
        try:
            urllib.request.urlretrieve(
                DOWNLOAD_SPEC_FROM, f'{TEMP_SPEC_LOCATION}')
        except urllib.error.URLError:
            print(
                f'\nError retrieving spec. Please ensure it is available at: "{DOWNLOAD_SPEC_FROM}".\n'
            )
            return

        # ----- generate client -----
        cmd = f'docker run --rm -v "${{PWD}}:/local" openapitools/openapi-generator-cli generate \
                -i /local{TEMP_SPEC_LOCATION[1:]} \
                -g {language} \
                -o /local/{CLIENT_DIR_BUILD}'

        # ----- exta options -----
        if config_dict is not None:
            cmd = cmd + f' -c /local{CONFIG_FILE}'
        if how_to_proceed == DRY_RUN:
            cmd += ' --dry-run'
        if how_to_proceed == MINIMAL_UPDATE:
            cmd += ' --minimal-update'

        os.system(cmd)

        if language == PYTHON and how_to_proceed != DRY_RUN:
            shutil.copytree(
                f'{CLIENT_DIR_BUILD}/{PACKAGE_NAME}',
                f'{SEDARO}/src/{PACKAGE_NAME}',
                dirs_exist_ok=True
            )
            shutil.copyfile(
                f'{CLIENT_DIR_BUILD}/requirements.txt',
                f'{SEDARO}/requirements-base-client.txt'
            )

        print('\n-------------< 🛰️  Closing Generator 🛰️  >-------------\n')


if __name__ == '__main__':
    run_generator()
