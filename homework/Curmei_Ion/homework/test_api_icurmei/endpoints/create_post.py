import requests
import allure
from endpoints.endpoint import Endpoint


class CreatePost(Endpoint):
    post_id = None

    @allure.step('Create new post')
    def create_new_post(self, payload, headers=None):
        if len(payload.get('body', '')) > 1000:
            self.url = f'{self.url}/dlinnopost'
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        try:
            self.json = self.response.json()
            self.post_id = self.json.get('id')
        except ValueError:
            self.json = None
            self.post_id = None
        return self.response
