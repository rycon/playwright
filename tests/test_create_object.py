from playwright.sync_api import APIRequestContext

from utils.yaml_parser import load_test_data
from utils.config_parser import get_endpoint


# TODO figure out if we can iterate through a test data file to execute test cases
def test_create_new_object(make_call: APIRequestContext) -> None:
    
    # Get the request payload from the test data
    payload = load_test_data("create_object.yaml")[0]["payload"]
    # Get the endpoint from the config file
    endpoint = get_endpoint("endpoint_objects")

    create_object = make_call.post(endpoint, data=payload)
    assert create_object.ok

    # Save id for get request
    id = create_object.json()['id']
    get_object = make_call.get(endpoint + f"/{id}")

    assert get_object.ok
    get_response = get_object.json()
    
    #Validate response values from test data file against input
    expected = load_test_data("create_object.yaml")[0]["response"]
    assert get_response["name"] == expected["name"]
    assert get_response["data"]["year"] == expected["data"]["year"]
    assert get_response["data"]["price"] == expected["data"]["price"] 
    assert get_response["data"]["CPU model"] == expected["data"]["CPU model"]
    assert get_response["data"]["Hard disk size"] == expected["data"]["Hard disk size"]

def test_create_object_negative_missing_payload(make_call: APIRequestContext) -> None:
    # A negative test case where an incorrect ID is sent
    payload = ""
    endpoint = get_endpoint("endpoint_objects")
    create_object = make_call.post(endpoint, data=payload)

    assert create_object.status == 400
    assert create_object.json()["error"] == "400 Bad Request. If you are trying to create or update the data, potential issue is that you are sending incorrect body json or it is missing at all."
