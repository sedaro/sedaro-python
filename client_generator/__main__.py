import os
import urllib.request
import tempfile

DOWNLOAD_SPEC_FROM = 'http://localhost:8081/sedaro-satellite.json'

GO = 'go'
DRY_RUN = 'dr'
MINIMAL_UPDATE = 'mu'
QUIT = 'q'
DELETE = 'x'
DIFFERENT_LANGUAGE = 'dl'

def run_generator(skip_intro = False):
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

    # PARENT_DIR = f'sedaro'
    # if language != 'python':
    #     PARENT_DIR = PARENT_DIR + f'_{language}'
    # CLIENT_DIR = f'{PARENT_DIR}/src/sedaro/{language}_client'
    CLIENT_DIR = f'sedaro'
    if language != 'python':
        CLIENT_DIR = CLIENT_DIR + f'_{language}'

    # --------- check if client exists and if want to overwrite ---------
    how_to_proceed = None
    proceed_options = (GO, DRY_RUN, MINIMAL_UPDATE, QUIT, DIFFERENT_LANGUAGE, DELETE)

    if not os.path.isdir(CLIENT_DIR):
        how_to_proceed = GO

    while how_to_proceed not in proceed_options:
        print(f'\nA client has already been generated for {language}. How would you like to proceed?')
        print(f'  + "{DRY_RUN}" (dry-run) -- try things out and report on potential changes (without actually making changes)')
        print(f'  + "{MINIMAL_UPDATE}" (minimal-update) -- only write output files that have changed')
        print(f'  + "{QUIT}"  (quit) -- abort generator')
        print(f'  + "{DIFFERENT_LANGUAGE}"  (different language) -- restart and pick a different language')
        print(f'  + "{DELETE}"  (delete) -- delete and regenerate old client')
        how_to_proceed = input(f'~ ').lower().strip()

        if how_to_proceed not in proceed_options:
            print(f'\n"{how_to_proceed}" is not a valid choice')

    if how_to_proceed == QUIT:
        print('\n------------------< 🛰️  Aborted 🛰️  >------------------\n')
        return

    if how_to_proceed == DIFFERENT_LANGUAGE:
        run_generator(skip_intro=True)

    # ----------------- remove client if already exists -----------------
    if how_to_proceed == DELETE:
        os.system(f'rm -r {CLIENT_DIR}')

    # ----------------------- generate new client -----------------------
    with tempfile.TemporaryDirectory(dir='./', prefix='.temp_dir_', suffix='_spec') as TEMP_DIR_FOR_SPEC:

        TEMP_SPEC_LOCATION = f'{TEMP_DIR_FOR_SPEC}/spec.json'
        urllib.request.urlretrieve(DOWNLOAD_SPEC_FROM, f'{TEMP_SPEC_LOCATION}')

        # ----- generate client -----
        cmd = f'docker run --rm -v "${{PWD}}:/local" openapitools/openapi-generator-cli generate \
                -i /local{TEMP_SPEC_LOCATION[1:]} \
                -g {language} \
                -o /local/{CLIENT_DIR}'

        config_file = f'/client_generator/{language}_config.yaml'
        if os.path.isfile('.' + config_file):
            cmd = cmd + f' -c /local{config_file}'

        if how_to_proceed == DRY_RUN:
            cmd += ' --dry-run'
        if how_to_proceed == MINIMAL_UPDATE:
            cmd += ' --minimal-update'

        os.system(cmd)

        print('\n-------------< 🛰️  Closing Generator 🛰️  >-------------\n')

if __name__ == "__main__":
    run_generator()
