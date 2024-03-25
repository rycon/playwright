import pytest
from typing import Generator
from playwright.sync_api import Playwright, APIRequestContext
from utils.config_parser import get_baseurl


@pytest.fixture(scope='session')
def make_call(playwright: Playwright ) -> Generator[APIRequestContext, None, None]:

    """
    This function makes the PlayWright API call. 
    It supports all REST types. 
    You need to Pass in the endpoint
    Example GET: make_call.get(f"/objects/{id}")
    Example POST: make_call.post("/objects", data=payload)
    """

    url = get_baseurl()

    headers = {
        "Accept": "application/vnd.github.v3+json"
    }

    request_context = playwright.request.new_context(base_url= url, extra_http_headers=headers)

    yield request_context
    request_context.dispose()

