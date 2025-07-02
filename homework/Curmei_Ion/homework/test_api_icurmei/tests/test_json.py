import pytest

TEST_DATA = [
    {"title": "My specific title", "body": "my body", "userId": 1},
    {"title": "My specific title2", "body": "my body2", "userId": 2},
    {"title": "My title number 3", "body": "my body3", "userId": 3},
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_post_a_post(create_post_endpoint, data):
    create_post_endpoint.create_new_post(payload=data)
    create_post_endpoint.check_that_status_is_200()
    create_post_endpoint.check_response_title_is_correct(data['title'])


def test_put_a_post(update_post_endpoint, create_post_endpoint):
    payload = {
        "title": "My update title",
        "body": "my new body update",
        "userId": 1
    }
    create_post_endpoint.create_new_post(payload)
    post_id = create_post_endpoint.post_id
    update_post_endpoint.make_changes_in_post(post_id, payload)
    update_post_endpoint.check_that_status_is_200()
    update_post_endpoint.check_response_title_is_correct(payload['title'])


def test_delete_a_post(create_post_endpoint, delete_post_endpoint):
    payload = {
        "title": "Post for deletion",
        "body": "To be deleted",
        "userId": 1
    }
    create_post_endpoint.create_new_post(payload)
    post_id = create_post_endpoint.post_id
    response = delete_post_endpoint.delete_post(post_id)
    assert response.status_code == 200
