from playwright.sync_api import APIRequestContext

from utils.yaml_parser import load_test_data
from utils.config_parser import get_endpoint


def test_put_object(make_call: APIRequestContext) -> None:

    # Get the request payload from the test data
    payload = load_test_data("put_object.yaml")[0]["payload"]
    endpoint = get_endpoint("endpoint_objects")
    
    create_object = make_call.post(endpoint, data=payload)
    assert create_object.ok

    # Save id for patch request
    id = create_object.json()['id']

    put_payload = load_test_data("put_object.yaml")[0]["put"]
    put_object = make_call.put(endpoint + f"/{id}", data=put_payload)
    assert put_object.ok

    get_object = make_call.get(endpoint + f"/{id}")
    assert get_object.ok

    get_response = get_object.json()
    #Validate response values from test data file against input
    expected = load_test_data("put_object.yaml")[0]["response"]
    assert get_response["name"] == expected["name"]
    assert get_response["data"]["year"] == expected["data"]["year"]
    assert get_response["data"]["price"] == expected["data"]["price"] 
    assert get_response["data"]["CPU model"] == expected["data"]["CPU model"]
    assert get_response["data"]["Hard disk size"] == expected["data"]["Hard disk size"]


def test_put_object_negative_invalid_id(make_call: APIRequestContext) -> None:
    # A negative test case where an incorrect ID is sent
    id = "test"
    put_payload = load_test_data("put_object.yaml")[0]["put"]
    endpoint = get_endpoint("endpoint_objects")

    put_object = make_call.put(endpoint + f"/{id}", data=put_payload)

    assert put_object.status == 404
    assert put_object.json()["error"] == "The Object with id = test doesn't exist. Please provide an object id which exists or generate a new Object using POST request and capture the id of it to use it as part of PUT request after that."


def test_put_object_negative_missing_payload(make_call: APIRequestContext) -> None:
    # A negative test case where an incorrect ID is sent
    id = "7"
    put_payload = ""
    endpoint = get_endpoint("endpoint_objects")

    put_object = make_call.put(endpoint + f"/{id}", data=put_payload)

    assert put_object.status == 400
    assert put_object.json()["error"] == "400 Bad Request. If you are trying to create or update the data, potential issue is that you are sending incorrect body json or it is missing at all."
