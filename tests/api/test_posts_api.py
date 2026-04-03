from utils.api_client import APIClient


def test_get_posts_returns_200():
    client = APIClient()
    response = client.get("/posts")

    assert response.status_code == 200


def test_get_posts_return_non_empty_list():
    client = APIClient()
    response = client.get("/posts")

    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


def test_create_post_returns_201():
    client = APIClient()
    payload = {
        "title": "QA Test Post",
        "body": "This is a test payload",
        "userId": 1
    }

    response = client.post("/posts", payload)

    assert response.status_code == 201