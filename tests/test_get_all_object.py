from playwright.sync_api import APIRequestContext

from utils.yaml_parser import load_test_data
from utils.config_parser import get_endpoint

def test_get_all_object(make_call: APIRequestContext) -> None:
    # Returns all objects from the endpoint, we'll just assert the status code and that some data is returned
    endpoint = get_endpoint("endpoint_objects")
    get_object = make_call.get(endpoint)
    
    assert get_object.ok
    get_response = get_object.json()
    assert get_response is not None
