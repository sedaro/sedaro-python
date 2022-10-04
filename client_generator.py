import os
import urllib.request
import tempfile

DOWNLOAD_SPEC_FROM = 'http://localhost:8081/sedaro-satellite.json'


def start_generator():
    '''Begin basic interactive terminal to create a client.'''

    print('\n------< Sedaro OpenAPI Client Generator >------')

    # ----------------- get desired language for client -----------------
    language = None
    while language == None:
        language = input(
            '\nWhat coding language would you like to generate a client for? (Can also type "options")\n- ').lower()

        if language == "options":
            print('')
            print(os.system(
                'docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli list'))
            print(
                '\n*** Note: this is intended to be used for generating a client, scroll up to "CLIENT generators". ***')
            language = None

    PARENT_DIR = f'sedaro'
    if language != 'python':
        PARENT_DIR = PARENT_DIR + f'_{language}'
    CLIENT_DIR = f'{PARENT_DIR}/src/sedaro/{language}_client'

    # --------- check if client exists and if want to overwrite ---------
    proceed = False
    if not os.path.isdir(CLIENT_DIR):
        proceed = True
    else:
        want_to_proceed = None
        while want_to_proceed not in ('y', 'n'):
            want_to_proceed = input(
                f'\nA client has already been generated for {language}.\nWould you like to delete that client and regenerate it? (y/n)\n- ').lower()
            if want_to_proceed == 'y':
                proceed = True
            elif want_to_proceed != 'n':
                print(f'\n"{want_to_proceed}" is not a valid choice')

    if not proceed:
        print('\nCancelled\n')
        return

    # ----------------- remove client if already exists -----------------
    if os.path.isdir(CLIENT_DIR):
        os.system(f'rm -r {CLIENT_DIR}')

    # ----------------------- generate new client -----------------------
    with tempfile.TemporaryDirectory(dir='./', prefix='.temp_dir_', suffix='_spec') as TEMP_DIR_FOR_SPEC:

        TEMP_SPEC_LOCATION = f'{TEMP_DIR_FOR_SPEC}/spec.json'
        urllib.request.urlretrieve(DOWNLOAD_SPEC_FROM, f'{TEMP_SPEC_LOCATION}')

        # ----- generate client -----
        os.system(
            f'docker run --rm -v "${{PWD}}:/local" openapitools/openapi-generator-cli generate \
                -i /local{TEMP_SPEC_LOCATION[1:]} \
                -g {language} \
                -o /local/{CLIENT_DIR}'
        )


if __name__ == "__main__":
    start_generator()
