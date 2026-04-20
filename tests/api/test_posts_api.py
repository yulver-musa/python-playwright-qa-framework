import requests
import pytest
from utils.api_client import APIClient

@pytest.mark.api
def test_get_posts_returns_200():
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        headers=headers
    )

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 1

@pytest.mark.api
def test_get_posts_return_non_empty_list():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    data = response.json()

    print(data[:1])

    import json
    print(json.dumps(data[0], indent=2))

    assert isinstance(data, list)
    assert len(data) > 0

@pytest.mark.api
def test_create_post_returns_201():
    payload = {
        "title": "QA Test Post",
        "body": "This is a test payload",
        "userId": 1
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )

    data = response.json()


    assert response.status_code == 201
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data

@pytest.mark.api
def test_get_post_invalid_id_returns_empty():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/999999"
    )

    # API returns empty object
    data = response.json()

    assert response.status_code == 404 or data == {}

@pytest.mark.api
def test_get_posts_by_user():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params={"userId": 1}
    )

    data = response.json()

    assert response.status_code == 200
    assert len(data) > 0

    for post in data:
        assert post["userId"] == 1

@pytest.mark.api
def test_create_and_get_post():
    payload = {
        "title": "QA Chain Test",
        "body": "Testing chaining",
        "userId": 1
    }

    post_response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )

    assert post_response.status_code == 201

    post_data = post_response.json()

    post_id = post_data["id"]

    get_response = requests.get(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    )

    assert get_response.status_code in [200, 404]

@pytest.mark.api
def test_create_post_missing_title():
    payload = {
        "body": "No title",
        "userId": 1
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )

    data = response.json()

    assert response.status_code == 201  # fake API behavior
    assert "title" not in payload

@pytest.mark.api
def test_create_post_with_script_like_input():
    payload = {
        "title": "<script>alert('x')</script>",
        "body": "Testing unsafe-like input handling",
        "userId": 1
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )

    data = response.json()

    assert response.status_code == 201
    assert data["title"] == payload["title"]

@pytest.mark.api
def test_create_post_with_empty_body():
    payload = {
        "title": "Valid title",
        "body": "",
        "userId": 1
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )

    data = response.json()

    assert response.status_code == 201
    assert data["body"] == payload["body"]