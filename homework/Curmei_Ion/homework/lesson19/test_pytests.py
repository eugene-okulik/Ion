import pytest
import allure
import requests

api_url = "http://167.172.172.115:52353/object"


# coment


@pytest.fixture(scope="session", autouse=True)
def session_start_end():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture(autouse=True)
def prints_between_tests():
    print("before test")
    yield
    print("after test")


@pytest.fixture
def create_post_id():
    body = {"name": "To Update", "data": {"color": "yellow", "size": "big"}}

    response = requests.post(f"{api_url}", json=body)
    post_id = response.json()["id"]
    print("creating the post id ")
    yield post_id
    print("deleting the post id ")
    delete_id = f"{api_url}/{post_id}"
    requests.delete(delete_id)


@pytest.mark.parametrize(
    "data",
    [
        {"id": 101, "name": "Object One", "data": {"color": "red", "size": "small"}},
        {"id": 102, "name": "Object Two", "data": {"color": "green", "size": "medium"}},
        {"id": 103, "name": "Object Three", "data": {"color": "blue", "size": "large"}},
    ],
)
def test_create_object(data):
    response = requests.post(api_url, json=data)
    assert response.status_code == 200
    response_data = response.json()
    # assert response_data.get('id') == data['id']
    assert response_data.get("name") == data["name"]
    assert response_data.get("data") == data["data"]


@allure.feature("Modify api")
@allure.story("put api")
@pytest.mark.critical
def test_put(create_post_id):
    with allure.step(f"get the url api:{api_url}"):
        put_url = f"{api_url}/{create_post_id}"
    with allure.step("Get test data:"):
        body = {
            {"id": 101, "name": "Object One", "data": {"color": "red", "size": "small"}}
        }

    response = requests.put(put_url, json=body)
    with allure.step("check the satus code is 200"):
        assert response.status_code == 200


@allure.feature("Modify api")
@allure.story("patch api")
@pytest.mark.medium
def test_patch():
    patch_url = f"{api_url}"
    with allure.step("Get test data:"):
        body = {"id": 101, "name": "Object One"}

    response = requests.patch(patch_url, json=body)
    data = response.json()
    with allure.step("check the satus code is 200"):
        assert response.status_code == 200
        assert data["name"] == body["name"]


@allure.feature("Modify api")
@allure.story("get api")
def test_get_object_by_id(create_post_id):
    post_id_to_patch = 1
    patch_url = f"{api_url}/{post_id_to_patch}"

    get_resp = requests.get(patch_url)
    with allure.step("check the satus code is 200"):
        assert get_resp.status_code == 200
    assert get_resp.json()["id"] == post_id_to_patch


@allure.feature("Delete api")
@allure.story("delete api")
def test_delete_object_by_id(create_post_id):
    post_it_to_delete = create_post_id
    with allure.step("delete api"):
        delete_url = f"{api_url}/{post_it_to_delete}"
    requests.delete(delete_url)

    get_response = requests.get(delete_url)

    with allure.step("check the satus code is 200"):
        assert get_response.status_code == 404
