import pytest
import requests

api_url = 'http://167.172.172.115:52353/object'

@pytest.fixture(scope='session', autouse=True)
def session_start_end():
    print("Start testing")
    yield
    print("Testing completed")

@pytest.fixture(autouse=True)
def test_prints():
    print("before test")
    yield
    print("after test")


@pytest.mark.parametrize("data", [
    {"id": 101, "name": "Object One", "data": {"color": "red", "size": "small"}},
    {"id": 102, "name": "Object Two", "data": {"color": "green", "size": "medium"}},
    {"id": 103, "name": "Object Three", "data": {"color": "blue", "size": "large"}},
])
@pytest.mark.critical
def test_create_object(data):
    response = requests.post(api_url, json=data)
    assert response.status_code == 200
    assert response.json()["name"] == data["name"]
    requests.delete(f"{api_url}/{response.json()['id']}")


@pytest.mark.medium
def test_update_object():

    create_body = {"id": 104, "name": "To Update", "data": {"color": "yellow", "size": "big"}}
    create_resp = requests.post(api_url, json=create_body)
    obj_id = create_resp.json()["id"]


    update_body = {"id": obj_id, "name": "Updated Name", "data": {"color": "black", "size": "tiny"}}
    update_resp = requests.put(f"{api_url}/{obj_id}", json=update_body)
    assert update_resp.status_code == 200
    assert update_resp.json()["name"] == "Updated Name"


    requests.delete(f"{api_url}/{obj_id}")


def test_patch_object():
    create_body = {"id": 105, "name": "Patch Me", "data": {"color": "white", "size": "normal"}}
    create_resp = requests.post(api_url, json=create_body)
    obj_id = create_resp.json()["id"]

    patch_body = {"name": "Patched", "data": {"color": "pink", "size": "very small"}}
    patch_resp = requests.patch(f"{api_url}/{obj_id}", json=patch_body)
    assert patch_resp.status_code == 200
    assert patch_resp.json()["name"] == "Patched"

    requests.delete(f"{api_url}/{obj_id}")


def test_get_object_by_id():
    create_body = {"id": 106, "name": "Get Me", "data": {"color": "orange", "size": "medium"}}
    create_resp = requests.post(api_url, json=create_body)
    obj_id = create_resp.json()["id"]

    get_resp = requests.get(f"{api_url}/{obj_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == obj_id

    requests.delete(f"{api_url}/{obj_id}")


def test_delete_object():
    create_body = {"id": 107, "name": "To Delete", "data": {"color": "gray", "size": "large"}}
    create_resp = requests.post(api_url, json=create_body)
    obj_id = create_resp.json()["id"]

    delete_resp = requests.delete(f"{api_url}/{obj_id}")
    assert delete_resp.status_code == 200


    get_resp = requests.get(f"{api_url}/{obj_id}")
    assert get_resp.status_code == 404
