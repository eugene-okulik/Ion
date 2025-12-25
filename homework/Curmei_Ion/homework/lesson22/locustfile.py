import random
from locust import HttpUser, task, between


class PhoneFullCRUDUser(HttpUser):
    wait_time = between(1, 4)
    endpoint = "/api/v1/phones"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_phone_id = None

    def on_start(self):
        # Initialization: set headers and create a base resource.
        self.client.headers.update({"Content-Type": "application/json"})

        setup_payload = {
            "anul": 2024,
            "modelul": "Initial_Device",
            "submodelul": "Setup_Version",
            "CPU": "Standard",
            "RAM": "8GB",
        }

        response = self.client.post(
            self.endpoint, json=setup_payload, name="Setup: Create Phone"
        )
        if response.status_code == 201:
            self.my_phone_id = response.json().get("id")
        else:
            # If setup fails, mark the user as unconfigured
            self.my_phone_id = None

    @task(10)
    def read_all(self):
        # [READ] - Retrieve the entire list.
        self.client.get(self.endpoint, name="GET /phones (All)")

    @task(5)
    def read_one(self):
        # [READ] - Retrieve details of the owned resource.
        if self.my_phone_id:
            self.client.get(
                f"{self.endpoint}/{self.my_phone_id}", name="GET /phones/[id]"
            )

    @task(2)
    def update_full(self):
        # [UPDATE] - PUT: Full data replacement.
        if self.my_phone_id:
            payload = {
                "anul": 2025,
                "modelul": "Updated_Model",
                "submodelul": "Ultra_Edition",
                "CPU": "Snapdragon Gen 4",
                "RAM": "16GB",
            }
            self.client.put(
                f"{self.endpoint}/{self.my_phone_id}",
                json=payload,
                name="PUT /phones/[id]",
            )

    @task(3)
    def update_partial(self):
        # [UPDATE] - PATCH: Modify only the RAM field."
        if self.my_phone_id:
            payload = {"RAM": f"{random.choice([12, 24, 32])}GB"}
            self.client.patch(
                f"{self.endpoint}/{self.my_phone_id}",
                json=payload,
                name="PATCH /phones/[id]",
            )

    @task(1)
    def delete_and_recreate(self):
        # [DELETE & CREATE] - Simulates a full resource lifecycle.
        if self.my_phone_id:
            # Delete current resource
            self.client.delete(
                f"{self.endpoint}/{self.my_phone_id}", name="DELETE /phones/[id]"
            )

            # Create a new one to maintain the workflow for subsequent tasks
            payload = {
                "anul": 2025,
                "modelul": "New_Device_After_Delete",
                "submodelul": "V2",
            }
            res = self.client.post(
                self.endpoint, json=payload, name="POST /phones (Recreate)"
            )
            if res.status_code == 201:
                self.my_phone_id = res.json().get("id")

    def on_stop(self):
        # Cleanup: Delete the resource when the test stops.
        if self.my_phone_id:
            self.client.delete(
                f"{self.endpoint}/{self.my_phone_id}", name="Cleanup: Delete on Stop"
            )
