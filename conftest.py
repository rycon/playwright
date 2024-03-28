from playwright.sync_api._generated import Page
import pytest
from typing import Generator
from playwright.sync_api import Playwright, APIRequestContext
from utils.config_parser import get_baseurl, get_graphql_url, get_webpage


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


@pytest.fixture(scope='session')
def gql_query(playwright: Playwright ) -> Generator[APIRequestContext, None, None]:

    """
    Queries the Media Resolver.
    You need to Pass in the endpoint
    Example POST: make_call.post("/objects", data=payload)
    """

    url = get_graphql_url()

    headers = {
        "Accept": "application/vnd.github.v3+json"
    }

    request_context = playwright.request.new_context(base_url= url, extra_http_headers=headers)

    yield request_context
    request_context.dispose()


@pytest.fixture()
def setup_tear_down(page: Page):

    """
    Used at the beginning of test execution. It will set some PlayWright parameters, and gets the test start page.
    """

    # browser = Playwright.chromium.launch(headless=False, slowMo=500)
    # context = browser.new_context()
    # page = context.new_page()
    url = get_webpage()
    page.set_viewport_size({"width": 1536, "height": 800})
    page.goto(url)
    yield page
