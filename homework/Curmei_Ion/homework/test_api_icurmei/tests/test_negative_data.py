import pytest
import allure

@allure.feature("Phone Management - Negative")
@allure.story("Create (POST) - Invalid Data")
@pytest.mark.parametrize("bad_payload", [
    {"modelul": "OnlyModel"},  # Incomplete
    {"anul": "NotANumber", "RAM": "4GB"}  # Wrong data type
])
def test_create_invalid(create_api, bad_payload):
    """Tests creation with invalid data. Assertion is handled in Create_API."""
    allure.dynamic.title("POST: Validate 400 Error (Bad Request)")

    # The create_api fixture must be defined in conftest to return the Create_API() instance
    # The method performs an internal status == 400 assertion
    create_api.create_phone(payload=bad_payload, expected_status=400)


@allure.feature("Phone Management - Negative")
@allure.story("Update (PUT) - Non-existent ID")
def test_update_non_existent(update_api):
    """Tests update on a non-existent ID. Assertion is handled in Update_API."""
    allure.dynamic.title("PUT: Validate 404 Error (Not Found)")

    # Set an invalid ID
    update_api.target_id = 999999
    payload = {"modelul": "Ghost", "anul": 2025}

    # The method performs an internal status == 404 assertion
    update_api.execute_update(payload, method="PUT", expected_status=404)


@allure.feature("Phone Management - Negative")
@allure.story("Get - Non-existent ID")
def test_get_non_existent(get_api):
    """Tests retrieval with a non-existent ID."""
    allure.dynamic.title("GET: Validate 404 Error")

    # The method performs an internal status == 404 assertion
    get_api.get_by_id(specific_id=999999, expected_status=404)


@allure.feature("Phone Management - Negative")
@allure.story("Delete - Double Deletion")
def test_delete_twice_check(delete_api, phone_setup):
    """Tests double deletion scenario."""
    allure.dynamic.title("DELETE: Validate 404 on Second Deletion")

    # 1. Normal deletion
    delete_api.delete_phone(phone_setup['id'])

    # 2. Verify it no longer exists (The method performs an internal 404 assertion)
    delete_api.verify_is_gone(phone_setup['id'])