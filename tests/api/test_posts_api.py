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

@pytest.mark.api
def test_get_posts_return_non_empty_list():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    # NEW validations
    first_item = data[0]

    assert "userId" in first_item
    assert "id" in first_item
    assert "title" in first_item
    assert "body" in first_item

@pytest.mark.api
def test_create_post_returns_201():
    client = APIClient()
    payload = {
        "title": "QA Test Post",
        "body": "This is a test payload",
        "userId": 1
    }

    response = client.post("/posts", payload)
    data = response.json()

    assert response.status_code == 201
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

@pytest.mark.api
def test_get_post_invalid_id_returns_empty():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/999999"
    )

    # API returns empty object
    data = response.json()

    assert response.status_code == 404 or data == {}