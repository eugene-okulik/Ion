import pytest
import requests

api_url = 'http://167.172.172.115:52353/object'


@pytest.fixture(scope='session', autouse=True)
def session_start_end():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture
def create_delete_object():
    created_ids = []

    def _create_object(data):
        response = requests.post(api_url, json=data)
        assert response.status_code == 200
        assert response.json()["name"] == data["name"]
        object_id = response.json()['id']
        created_ids.append(object_id)
        return object_id

    yield _create_object

    for obj_id in created_ids:
        requests.delete(f"{api_url}/{obj_id}")


@pytest.mark.parametrize("data", [
    {"id": 101, "name": "Object One", "data": {"color": "red", "size": "small"}},
    {"id": 102, "name": "Object Two", "data": {"color": "green", "size": "medium"}},
    {"id": 103, "name": "Object Three", "data": {"color": "blue", "size": "large"}},
])
def test_create_object(create_delete_object, data):
    create_delete_object(data)


@pytest.fixture(autouse=True)
def test_prints():
    print("before test")
    yield
    print("after test")


@pytest.mark.critical
def test_update_object(create_delete_object):
    create_body = {"name": "To Update", "data": {"color": "yellow", "size": "big"}}
    obj_id = create_delete_object(create_body)

    update_body = {"name": "Updated Name", "data": {"color": "black", "size": "tiny"}}
    update_resp = requests.put(f"{api_url}/{obj_id}", json=update_body)
    assert update_resp.status_code == 200
    assert update_resp.json()["name"] == "Updated Name"


@pytest.mark.medium
def test_patch_object(create_delete_object):
    create_body = {"name": "Patch Me", "data": {"color": "white", "size": "normal"}}
    obj_id = create_delete_object(create_body)

    patch_body = {"name": "Patched", "data": {"color": "pink", "size": "very small"}}
    patch_resp = requests.patch(f"{api_url}/{obj_id}", json=patch_body)
    assert patch_resp.status_code == 200
    assert patch_resp.json()["name"] == "Patched"


def test_get_object_by_id(create_delete_object):
    create_body = {"name": "Get Me", "data": {"color": "orange", "size": "medium"}}
    obj_id = create_delete_object(create_body)

    get_resp = requests.get(f"{api_url}/{obj_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == obj_id


def test_delete_object(create_delete_object):
    create_body = {"name": "To Delete", "data": {"color": "gray", "size": "large"}}
    obj_id = create_delete_object(create_body)

    delete_resp = requests.delete(f"{api_url}/{obj_id}")
    assert delete_resp.status_code == 200

    get_resp = requests.get(f"{api_url}/{obj_id}")
    assert get_resp.status_code == 404
