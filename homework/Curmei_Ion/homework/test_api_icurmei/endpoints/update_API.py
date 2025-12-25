import requests
import allure
from create_API import Create_API


class Update_API(Create_API):
    def __init__(self):
        super().__init__()
        self.target_id = None
        self.response = None
        self.response_json = None

    def execute_update(self, payload, method="PUT", expected_status=200):
        url = f"{self.base_url}/{self.target_id}"

        with allure.step(
            f"Execution {method} on ID {self.target_id} (Expected: {expected_status})"
        ):
            if method.upper() == "PUT":
                self.response = requests.put(url, json=payload, headers=self.header)
            else:
                self.response = requests.patch(url, json=payload, headers=self.header)

            allure.attach(
                self.response.text,
                name="Server Response",
                attachment_type=allure.attachment_type.JSON,
            )

            # INTERNAL VALIDATION
            with allure.step(f"Status Code Check: Expected [{expected_status}]"):
                assert self.response.status_code == expected_status

            # Validate body only if status is success (200)
            if expected_status == 200:
                self.response_json = self.response.json()
                self._auto_validate(payload)

            return self.response

    def _auto_validate(self, expected_payload):
        with allure.step("AUTOMATIC VALIDATION: Received Data"):
            for key, expected_value in expected_payload.items():
                actual_value = self.response_json.get(key)
                with allure.step(
                    f"Verifying '{key}': [{expected_value}] == [{actual_value}]"
                ):
                    assert actual_value == expected_value
