import requests
from utils.api_config import API_BASE_URL


class APIClient:
    def __init__(self):
        self.base_url = API_BASE_URL

    def get(self, endpoint: str):
        return requests.get(f"{self.base_url}{endpoint}")
    
    def post(self, endpoint: str, payload: dict):
        return requests.post(f"{self.base_url}{endpoint}", json=payload)