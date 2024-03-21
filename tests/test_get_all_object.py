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


def test_get_all_object(api_request_context: APIRequestContext) -> None:
    # Returns all objects from the endpoint, we'll just assert the status code and that some data is returned
    get_object = api_request_context.get(f"/objects")
    print(get_object)

    assert get_object.ok
    get_response = get_object.json()
    assert len(get_response) > 10
