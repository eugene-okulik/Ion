import pytest
import allure

from endpoints.create_API import Create_API
from endpoints.update_API import Update_API
from endpoints.get_API import Get_API
from endpoints.delete_API import Delete_API


@pytest.fixture(scope="function")
def phone_setup():
    api = Create_API()
    with allure.step("PRECONDITION: Environment Setup (Create phone)"):
        data = api.create_phone()
    yield data
    with allure.step("POSTCONDITION: Environment Cleanup (Delete phone)"):
        Delete_API().delete_phone(data['id'])


@pytest.fixture
def create_api():
    """Simple fixture for creation tests (POST), without prior setup.
    Specifically used for negative tests involving invalid IDs.
    """
    with allure.step("CONFIGURATION: Initialize Create_API"):
        return Create_API()


@pytest.fixture
def update_api(phone_setup):
    with allure.step("CONFIGURATION: Prepare Update_API"):
        api = Update_API()
        api.target_id = phone_setup['id']
        return api


@pytest.fixture
def get_api(phone_setup):
    with allure.step("CONFIGURATION: Prepare Get_API"):
        api = Get_API()
        # Verify if phone_setup contains the 'id' key (retrieved from response.json() during creation)
        api.target_id = phone_setup['id']
        return api


@pytest.fixture
def delete_api():
    with allure.step("CONFIGURATION: Prepare Delete_API"):
        return Delete_API()
