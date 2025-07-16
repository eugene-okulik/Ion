import allure


@allure.feature("Create Post")
def test_create_post_with_default_payload(create_post_endpoint):
    create_post_endpoint.create_new_post()
    create_post_endpoint.check_that_status_is_200()
    create_post_endpoint.check_response_title_is_correct("Default Title")


@allure.feature("Update Post")
def test_update_post_with_default_payload(create_post_endpoint, update_post_endpoint):
    create_post_endpoint.create_new_post()
    post_id = create_post_endpoint.post_id

    update_post_endpoint.make_changes_in_post(post_id)
    update_post_endpoint.check_that_status_is_200()
    update_post_endpoint.check_response_title_is_correct("Updated Title")


@allure.feature("Delete Post")
def test_delete_post_after_creation(create_post_endpoint, delete_post_endpoint):
    create_post_endpoint.create_new_post()
    post_id = create_post_endpoint.post_id

    response = delete_post_endpoint.delete_post(post_id)
    assert response.status_code in [200, 204], f"Unexpected status code: {response.status_code}"
