ENVIRONMENTS = {
    "dev": "https://the-internet.herokuapp.com",
    "staging": "https://the-internet.herokuapp.com",
    "prod": "https://the-internet.herokuapp.com",
}

import os

ENV = os.getenv("ENV", "dev")

BASE_URL = ENVIRONMENTS.get(ENV)