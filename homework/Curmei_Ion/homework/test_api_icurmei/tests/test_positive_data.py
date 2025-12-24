import pytest
import allure

# Test Data
bulk_phones = [
    {"modelul": "iPhone", "submodelul": "15", "anul": 2023, "CPU": "A16", "RAM": "6GB"},
    {"modelul": "Samsung", "submodelul": "S24", "anul": 2024, "CPU": "Exynos", "RAM": "8GB"}
]


@allure.feature("Phone Management - Positive")
@allure.story("Create & Read")
def test_create_and_read(get_api, phone_setup):
    """Verifies the create and read flow."""
    allure.dynamic.title("Flow: Automatic Creation -> Automatic Read")

    # Get_API internally validates status 200 and structure
    get_api.get_all()
    get_api.get_by_id(expected_model=phone_setup['modelul'])


@allure.feature("Phone Management - Positive")
@allure.story("Update (PUT)")
@pytest.mark.parametrize("phone_data", bulk_phones)
def test_update_put(update_api, phone_data):
    """Verifies full update. Validation is handled within Update_API."""
    allure.dynamic.title(f"PUT: Update to {phone_data['modelul']}")
    # Update_API internally validates status 200 and returned payload
    update_api.execute_update(phone_data, method="PUT")


@allure.feature("Phone Management - Positive")
@allure.story("Update (PATCH)")
def test_update_patch(update_api):
    """Verifies partial update."""
    allure.dynamic.title("PATCH: RAM Modification")
    # Internal validation
    update_api.execute_update({"RAM": "32GB"}, method="PATCH")


@allure.feature("Phone Management - Positive")
@allure.story("Delete")
def test_delete_resource(delete_api, phone_setup):
    """Verifies deletion."""
    allure.dynamic.title("DELETE: Phone Deletion")
    # Delete_API returns response, but complex validation is in negative tests
    delete_api.delete_phone(phone_setup['id'])

    # The verify_is_gone method in Delete_API class already includes the 404 assertion.
    delete_api.verify_is_gone(phone_setup['id'])