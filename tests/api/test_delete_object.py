from playwright.sync_api import APIRequestContext

from utils.yaml_parser import load_test_data
from utils.config_parser import get_endpoint


def test_create_and_delete_new_object(make_call: APIRequestContext) -> None:
    # Create a new object in the DB, then perform a GET to validate
    
    # Get the request payload from the test data
    payload = load_test_data("delete_object.yaml")[0]["payload"]
    endpoint = get_endpoint("endpoint_objects")
    create_object = make_call.post(endpoint, data=payload)
    assert create_object.ok

    # Save id for other requests
    id = create_object.json()['id']
    get_object = make_call.get(endpoint + f"/{id}")
    assert get_object.ok

    get_response = get_object.json()
    # Only asserting that the body is not empty, full tests are handles in other test cases
    assert get_response is not None

    delete_object = make_call.delete(endpoint + f"/{id}")
    assert delete_object.ok
    assert delete_object.json()["message"] == "Object with id = " + id + " has been deleted."

    # Final GET to verify record was deleted
    get_object = make_call.get(endpoint + f"/{id}")
    assert get_object.json()["error"] == "Oject with id=" + id + " was not found."


def test_delete_object_negative_invalid_id(make_call: APIRequestContext) -> None:
    # A negative test case where an incorrect ID is sent
    id = "test"
    endpoint = get_endpoint("endpoint_objects")
    delete_object = make_call.delete(endpoint + f"/{id}")

    assert delete_object.status == 404
    assert delete_object.json()["error"] == "Object with id = test doesn't exist."
