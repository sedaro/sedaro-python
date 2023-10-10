import inspect
from pathlib import Path

from sedaro import SedaroApiClient

API_KEY = 'API_KEY'
AGENT_TEMPLATE_ID = 'SIMPLESAT_A_T_ID'
SCENARIO_ID = 'SIMPLESAT_SCENARIO_ID'

HOST = 'http://localhost:80'

sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)


def update_branch_bcc_annotations():
    EDIT_START = '$AUTO_EDIT_START$'

    for get_method, branch_id in (
        (sedaro.agent_template, AGENT_TEMPLATE_ID),
        (sedaro.scenario, SCENARIO_ID)
    ):
        branch = get_method(branch_id)
        branch_kls = branch.__class__
        class_file = inspect.getfile(branch_kls)
        class_path = Path(class_file).relative_to(Path.cwd())

        with class_path.open('r+') as f:
            while line := f.readline():
                if EDIT_START in line:
                    f.seek(0, 1)
                    f.truncate()
                    break
            else:
                raise ValueError(f'Unable to find {EDIT_START} in file')

            f.write('\n')
            a_or_an = 'an' if branch_kls.__name__[0].lower() in 'aeiou' else 'a'
            doc_string = f'A Sedaro `Block` class on {a_or_an} `{branch_kls.__name__}`'
            for block_name in sorted(branch.data['_blockNames']):
                f.write(f'    {block_name}: BlockType\n')
                f.write(f'    """{doc_string}"""\n')


if __name__ == '__main__':
    update_branch_bcc_annotations()
