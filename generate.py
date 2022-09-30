import os

# TODO: change spec location to reference our live spec
SPEC_LOCATION = '/local/sedaro-satellite.json'
TARGET_DIR = 'generated_clients'


def start_generator():
    '''Begin basic interactive terminal to create a client.'''

    print('\n------< Sedaro OpenAPI Client Generator >------')

    # ----------------- get desired language -----------------
    language = None
    while language == None:
        language = input(
            '\nWhat coding language would you like to generate a client for? (Can also type "options")\n- ').lower()

        if language == "options":
            print('')
            print(os.system(
                'docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli list'))
            print(
                '\nNote: this is intended to be used for generating a client, scroll up to "CLIENT generators".')
            language = None

    client_dir = f'{TARGET_DIR}/{language}_client'

    # ------- check if exists and if want to overwrite -------
    proceed = False
    if not os.path.isdir(client_dir):
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

    # ----------------- remove dir if exists -----------------
    if os.path.isdir(client_dir):
        os.system(f'rm -r {client_dir}')

    # --------------------- generate new ---------------------
    generate_client_cmd = f'docker run --rm -v "${{PWD}}:/local" openapitools/openapi-generator-cli generate \
        -i {SPEC_LOCATION} \
        -g {language} \
        -o /local/{client_dir}'

    os.system(generate_client_cmd)


if __name__ == "__main__":
    start_generator()
