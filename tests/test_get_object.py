from typing import Generator

import pytest
from playwright.sync_api import Playwright, APIRequestContext

from utils.yaml_parser import load_test_data
from utils.config_parser import get_baseurl

from jsonschema import validate

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


def test_get_object(api_request_context: APIRequestContext) -> None:
    """
    Uses a static ID to fetch a record, and then validate that the response matches the schema
    For get requests, we cannot always control the data, and I don't always want to create new records when testing.
    For that reason, I write a test to validate the json structure, and the POST test can further test the GET endpoint.
    Due to this being a public API, the record I used could change
    """
    id = load_test_data("schemas/get_object.yaml")["id"]
    get_object = api_request_context.get(f"/objects/{id}")
    print(get_object)

    assert get_object.ok
    get_response = get_object.json()

    # Load the schema from file
    schema = load_test_data("schemas/get_object.yaml")["schema"]

    # Schema Validation
    validate(instance=get_response, schema=schema)

def test_get_object_negative(api_request_context: APIRequestContext) -> None:
    # A negative test case where an incorrect ID is sent
    id = "test"
    get_object = api_request_context.get(f"/objects/{id}")

    assert get_object.status == 404
    assert get_object.json()["error"] == "Oject with id=test was not found."
