from create_API import Create_API
import requests
import allure


class Delete_API(Create_API):
    def __init__(self):
        # Inherit attributes (base_url, header) from Create_API
        super().__init__()

    @allure.step("API: Delete resource ID {phone_id}")
    def delete_phone(self, phone_id):
        response = requests.delete(f"{self.base_url}/{phone_id}", headers=self.header)
        return response

    @allure.step("VALIDATION: Verify resource no longer exists (404)")
    def verify_is_gone(self, phone_id):
        # Attempt to delete again or perform a GET to confirm it's gone
        response = requests.delete(f"{self.base_url}/{phone_id}", headers=self.header)
        with allure.step(f"Status Code Check: Expected [404] | Actual [{response.status_code}]"):
            assert response.status_code == 404
        return response
