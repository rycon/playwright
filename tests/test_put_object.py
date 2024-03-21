from typing import Generator

import pytest
from playwright.sync_api import Playwright, APIRequestContext

from utils.yaml_parser import load_test_data
from utils.config_parser import get_baseurl


# TODO figure out how to move this to util, I'm currently stuck
@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright,) -> Generator[APIRequestContext, None, None]:
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    url = get_baseurl()
    request_context = playwright.request.new_context(base_url=url, extra_http_headers=headers)
    yield request_context
    request_context.dispose()


def test_put_object(api_request_context: APIRequestContext) -> None:
    # Create a new object in the DB, then perform a GET to validate
    
    # Get the request payload from the test data
    payload = load_test_data("put_object.yaml")[0]["payload"]

    create_object = api_request_context.post(f"/objects", data=payload)
    assert create_object.ok

    # Save id for patch request
    id = create_object.json()['id']

    put_payload = load_test_data("put_object.yaml")[0]["put"]
    put_object = api_request_context.put(f"/objects/{id}", data=put_payload)
    assert put_object.ok

    get_object = api_request_context.get(f"/objects/{id}")
    assert get_object.ok

    get_response = get_object.json()
    #Validate response values from test data file against input
    expected = load_test_data("put_object.yaml")[0]["response"]
    assert get_response["name"] == expected["name"]
    assert get_response["data"]["year"] == expected["data"]["year"]
    assert get_response["data"]["price"] == expected["data"]["price"] 
    assert get_response["data"]["CPU model"] == expected["data"]["CPU model"]
    assert get_response["data"]["Hard disk size"] == expected["data"]["Hard disk size"]


def test_put_object_negative_invalid_id(api_request_context: APIRequestContext) -> None:
    # A negative test case where an incorrect ID is sent
    id = "test"
    put_payload = load_test_data("put_object.yaml")[0]["put"]
    put_object = api_request_context.put(f"/objects/{id}", data=put_payload)

    assert put_object.status == 404
    assert put_object.json()["error"] == "The Object with id = test doesn't exist. Please provide an object id which exists or generate a new Object using POST request and capture the id of it to use it as part of PUT request after that."


def test_put_object_negative_missing_payload(api_request_context: APIRequestContext) -> None:
    # A negative test case where an incorrect ID is sent
    id = "7"
    put_payload = ""
    put_object = api_request_context.put(f"/objects/{id}", data=put_payload)

    assert put_object.status == 400
    assert put_object.json()["error"] == "400 Bad Request. If you are trying to create or update the data, potential issue is that you are sending incorrect body json or it is missing at all."
