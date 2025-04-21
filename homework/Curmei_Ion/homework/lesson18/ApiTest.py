import requests


def my_post():
    body = {
        "data": {"color": "blue", "size": "medium"},
        "id": 100,
        "name": "My object"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)

    print(f"my post is: {response.json()}")
    print(f"status code: {response.status_code}")
    return response.json()['id']


post_id = my_post()


def put_my_post():
    body = {
        "data": {"color": "black", "size": "small"},
        "id": 100,
        "name": "My new object"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.put(f'http://167.172.172.115:52353/object/{post_id}', json=body, headers=headers)

    print(f"my new post is: {response.json()}")
    print(f"status code: {response.status_code}")


def patch_my_post():
    body = {
        "data": {"color": "pink", "size": "very small"},
        "name": "My update object"
    }
    headers = {'Content-Type': 'application/json'}

    response = (requests.patch(f'http://167.172.172.115:52353/object/{post_id}', json=body, headers=headers))

    print(f"my update post is: {response.json()}")
    print(f"status code: {response.status_code}")


def delete_my_post():
    response = requests.delete(f'http://167.172.172.115:52353/object/{post_id}')
    print("Delete function is execute")
    print(f"status code: {response.status_code}")


put_my_post()
patch_my_post()
delete_my_post()
