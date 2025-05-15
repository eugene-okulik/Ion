import pytest
import requests

api_url = 'http://167.172.172.115:52353/object'


@pytest.fixture(scope='session', autouse=True)
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
    body = {
        "name": "To Update",
        "data": {"color": "yellow", "size": "big"}
    }

    response = requests.post(f'{api_url}', json=body)
    post_id = response.json()['id']
    print("creating the post id ")
    yield post_id
    print("deleting the post id ")
    delete_id = f'{api_url}/{post_id}'
    requests.delete(delete_id)


@pytest.mark.parametrize("data", [
    {"id": 101, "name": "Object One", "data": {"color": "red", "size": "small"}},
    {"id": 102, "name": "Object Two", "data": {"color": "green", "size": "medium"}},
    {"id": 103, "name": "Object Three", "data": {"color": "blue", "size": "large"}},
])
def test_create_object(create_post_id, data):
    create_post_id(data)


@pytest.mark.critical
def test_put_a_post(create_post_id):
    put_url = f'{api_url}/{create_post_id}'
    body = {
        {"id": 101, "name": "Object One",
         "data": {"color": "red", "size": "small"}}
    }

    response = requests.put(put_url, json=body)

    assert response.status_code == 200


@pytest.mark.medium
def test_patch_a_post():
    post_id_to_patch = 1
    patch_url = f'{api_url}/{post_id_to_patch}'
    body = {
        "id": 101, "name": "Object One"
    }

    response = requests.patch(patch_url, json=body)
    data = response.json()

    assert response.status_code == 200
    assert data['name'] == body['name']


def test_get_object_by_id(create_post_id):
    create_body = {"name": "Get Me", "data": {"color": "orange", "size": "medium"}}
    obj_id = create_post_id(create_body)

    get_resp = requests.get(f"{api_url}/{obj_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == obj_id


def test_delete_post_id(create_post_id):
    post_it_to_delete = create_post_id
    delete_url = f'{api_url}/{post_it_to_delete}'
    requests.delete(delete_url)

    get_response = requests.get(delete_url)

    assert get_response.status_code == 404
