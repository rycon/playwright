import pytest
from allure import description, epic, story, step
from utils.logger_config import get_logger
from utils.user_client import user_client
from assertpy.assertpy import assert_that
from http import HTTPStatus

"""
This is the only test that I followed from the tutorial I followed. All test files were written by me.
"""

@epic("User Acquisition")
@story("Test User Modules")
@description("Scenarios: user creation & result verification")
class TestUserModules:
    logger = get_logger(module_name=__name__)

    # creates an ID for use in the tests below
    @pytest.fixture(scope="module") # TODO add to conftest??
    def user_ids(self):
        ids: list = []
        yield ids

    # 
    @pytest.fixture
    def user_client(self, request_context):
        user_client_context = user_client(request_context=request_context)
        yield user_client_context

    @step("Create a user")
    @pytest.mark.dependency()
    def test_create_user(self, user_client, user_ids):
        status_code, response = user_client.create_user()
        assert_that(status_code).is_equal_to(HTTPStatus.CREATED)
        assert_that(response.id).is_not_none()
        user_ids.append(response.id)

    @step("Get a user profile which doesn't exist")
    @pytest.mark.dependency(depends=['TestUserModules::test_create_user']) # I see this is use in this tutorial, but I don't like having test rely on others. 
    def test_get_user_not_found(self, user_client, user_ids):
        status_code = user_client.get_user(user_id=user_ids[0])
        assert_that(status_code).is_equal_to(HTTPStatus.NOT_FOUND)

    @step("Get a valid user profile")
    @pytest.mark.dependency()
    def test_get_user_happy_flow(self, user_client):
        status_code, response = user_client.get_user(user_id="2")
        assert_that(status_code).is_equal_to(HTTPStatus.OK)
        assert_that(response.data.id).is_equal_to(2)