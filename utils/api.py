from typing import Generator
from utils.config_parser import get_baseurl
from playwright.sync_api import Playwright, APIRequestContext

def call_object_endpoint(playwright: Playwright,) -> Generator[APIRequestContext, None, None]:
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    url = get_baseurl()
    request_context = playwright.request.new_context(base_url=url, extra_http_headers=headers)
    return request_context.dispose()

def create_new_repository(endpoint, data, api_request_context: APIRequestContext):
    payload = data
    return api_request_context.post(
        endpoint,
        headers={
            "Accept": "application/vnd.github.v3+json",
        },
        data=payload,
    )