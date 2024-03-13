import pytest
from typing import Generator
from playwright.sync_api import Playwright, APIRequestContext

"""
This is the orginal test file I created, you can see my TODO list of where I wanted to break the steops out into
fictures and other utils to keep this code cleaner. The tutorial I was following takes my TODO's a step further.
"""

@pytest.fixture(scope="session")
# TODO add to a utility
def user_ids():
    ids = []
    yield ids

@pytest.fixture(scope="session")
# TODO explore breaking out the requests into a helper to increase readability and reduce complexity
def user_api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="https://reqres.in" # TODO Explore pulling this value from a config file
    )
    yield request_context
    request_context.dispose()

# Happy Path Tests
# TODO look into adding tags
def test_create_user(user_api_request_context: APIRequestContext, user_ids) -> None:
    payload = {
        "name": "First Last",
        "job": "QA Analyst"
    }

    response = user_api_request_context.post(url=f"/api/users", data=payload)
    assert response.ok

    json_response = response.json()
    print("Create User API Response:\n{}".format(json_response))
    assert json_response["name"] == payload.get("name")
    user_ids.append(json_response["id"])

# TODO look into adding tags
def test_get_user_happy_flow(user_api_request_context: APIRequestContext) -> None:
    response = user_api_request_context.get(url=f"/api/users/2")
    assert response.status == 200

    json_response = response.json()
    print("Get User API Response - Happy Flow:\n{}".format(json_response))
    assert json_response["data"]["id"] == 2

#Negative Tests
# TODO look into adding tags
def test_get_user_not_found(user_api_request_context: APIRequestContext, user_ids) -> None:
    response = user_api_request_context.get(url=f"/api/users/{user_ids[0]}")
    assert response.status == 404

    json_response = response.json()
    print("Get User API Response - User Not Found:\n{}".format(json_response))

