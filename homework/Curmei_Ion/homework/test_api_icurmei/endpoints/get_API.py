import requests
import allure
import json
from create_API import Create_API


class Get_API(Create_API):

    def __init__(self):
        super().__init__()
        self.target_id = None

    @allure.step("API Call: GET ALL - Retrieve complete list")
    def get_all(self):
        response = requests.get(self.base_url, headers=self.header)

        # Attach response in Allure for quick debugging
        allure.attach(
            json.dumps(response.json(), indent=4) if response.status_code == 200 else response.text,
            name="Server Response (List)",
            attachment_type=allure.attachment_type.JSON
        )

        with allure.step("VALIDATION: Status 200 and Structure"):
            with allure.step(f"Status Code Check: Expected [200] | Actual [{response.status_code}]"):
                assert response.status_code == 200

            with allure.step("Verify: Response is a list"):
                assert isinstance(response.json(),
                                  list), f"Error: Expected a list, received {type(response.json())}"

        return response

    @allure.step("API Call: GET BY ID - Retrieve specific resource")
    def get_by_id(self, specific_id=None, expected_model=None, expected_status=200):
        # Choose ID: either passed manually (for negative tests) or injected by fixture
        id_to_use = specific_id if specific_id is not None else self.target_id

        url = f"{self.base_url}/{id_to_use}"
        response = requests.get(url, headers=self.header)

        # Attach response body in Allure
        allure.attach(
            response.text,
            name=f"Server Response for ID {id_to_use}",
            attachment_type=allure.attachment_type.JSON
        )

        with allure.step(f"AUTOMATIC VALIDATION: ID {id_to_use}"):
            # 1. Status Code Validation
            with allure.step(f"Status Code: Expected [{expected_status}] | Actual [{response.status_code}]"):
                assert response.status_code == expected_status

            # 2. Model Validation (only if status is success and model verification was requested)
            if response.status_code == 200 and expected_model is not None:
                response_json = response.json()
                actual_model = response_json.get('modelul')

                with allure.step(f"Verify 'modelul' field: [{expected_model}] == [{actual_model}]"):
                    assert actual_model == expected_model, f"Error! Expected: {expected_model}, Received: {actual_model}"

                # Optional: Verify that the ID in JSON is correct
                with allure.step(f"Verify ID integrity in JSON: [{id_to_use}]"):
                    assert str(response_json.get('id')) == str(id_to_use)

        return response