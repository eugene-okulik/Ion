import requests
import allure


class Create_API:
    base_url = "http://127.0.0.1:5000/api/v1/phones"
    header = {"Content-Type": "application/json"}
    payload = {
        "modelul": "Test Phone", "submodelul": "Automation",
        "anul": 2024, "CPU": "Snapdragon", "RAM": "12GB"
    }

    @allure.step("API: Create resource (POST)")
    def create_phone(self, payload=None, expected_status=None):  # Added expected_status
        target_payload = payload if payload else self.payload
        response = requests.post(self.base_url, json=target_payload, headers=self.header)

        allure.attach(response.text, name="Creation Response", attachment_type=allure.attachment_type.JSON)

        # INTERNAL VALIDATION LOGIC
        if expected_status:
            with allure.step(f"VALIDATION: Status {expected_status}"):
                assert response.status_code == expected_status

        # Return JSON only on success, otherwise return the response object for other optional checks
        return response.json() if response.status_code in [200, 201] else response
