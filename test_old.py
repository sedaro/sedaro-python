from urllib3.response import HTTPResponse
from sedaro import SedaroApiClient

# from sedaro_python_client.python_client.openapi_client.apis.tags import battery_cell_api
# from sedaro_python_client.python_client.openapi_client.model.battery_cell import BatteryCell
# from sedaro_python_client.python_client.openapi_client.model.battery_cell_create import BatteryCellCreate

from pprint import pprint

# NOTE: this is a temporary API key associated with Zach's dev environment
API_KEY = '2.6YnJx9FECI0_tweCHBVoDw1NpkqXpX0g2SbivoWk1js8tIigEcAFo9ebQ2pzSqpO-fHqzVikT2njA6xXNRTslw'


def test():
    with SedaroApiClient(api_key=API_KEY) as sedaro_client:

        res: HTTPResponse = sedaro_client.call_api('', 'GET')
        # res: HTTPResponse = sedaro_client.call_api('models/branches/14', 'GET',)
        print(f'\nres: {res.data}\n')

    # with SedaroApiClient(api_key=API_KEY) as sedaro_client:
    #     api_instance = battery_cell_api.BatteryCellApi(sedaro_client)

    #     path_parmas = {
    #         'branchId': 14
    #     }

    #     body = BatteryCellCreate(
    #         part_number='1234',
    #         manufacturer='abcd',
    #         esr='1.0',
    #         max_charge_current='100',
    #         max_discharge_current='100',
    #         min_soc='0.01',
    #         capacity='5000',
    #         topology='1'
    #     )

        # try:
        #     # Create Battery Cell
        #     api_response = api_instance.create_battery_cell(
        #         path_params=path_parmas,
        #         body=body,
        #     )
        #     pprint(api_response)
        # except sedaro_client.ApiException as e:
        #     print("Exception when calling BatteryCellApi->create_battery_cell: %s\n" % e)


if __name__ == "__main__":
    test()
