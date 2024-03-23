from playwright.sync_api import APIRequestContext

from utils.config_parser import get_endpoint
from utils.yaml_parser import load_test_data

from jsonschema import validate

def test_get_object(make_call: APIRequestContext) -> None:
    """
    Uses a static ID to fetch a record, and then validate that the response matches the schema
    For get requests, we cannot always control the data, and I don't always want to create new records when testing.
    For that reason, I write a test to validate the json structure, and the POST test can further test the GET endpoint.
    Due to this being a public API, the record I used could change
    """

    id = load_test_data("schemas/get_object.yaml")["id"]
    endpoint = get_endpoint("endpoint_objects")
    get_object = make_call.get(endpoint + f"/{id}")

    assert get_object.ok
    get_response = get_object.json()

    # Load the schema from file
    schema = load_test_data("schemas/get_object.yaml")["schema"]

    # Schema Validation
    validate(instance=get_response, schema=schema)

def test_get_object_negative(make_call: APIRequestContext) -> None:
    # A negative test case where an incorrect ID is sent
    id = "test"
    endpoint = get_endpoint("endpoint_objects")
    get_object = make_call.get(endpoint + f"/{id}")

    assert get_object.status == 404
    assert get_object.json()["error"] == "Oject with id=test was not found."
