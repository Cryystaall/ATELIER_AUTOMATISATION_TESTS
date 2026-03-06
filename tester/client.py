import requests
import time

BASE_URL = "https://dog.ceo/api"

TIMEOUT = 3
MAX_RETRY = 1


def get(endpoint):
    url = BASE_URL + endpoint

    for attempt in range(MAX_RETRY + 1):
        start = time.time()

        try:
            response = requests.get(url, timeout=TIMEOUT)

            latency = (time.time() - start) * 1000

            return {
                "status_code": response.status_code,
                "json": response.json(),
                "latency_ms": latency,
                "error": None
            }

        except requests.exceptions.Timeout:

            if attempt == MAX_RETRY:
                return {
                    "status_code": None,
                    "json": None,
                    "latency_ms": None,
                    "error": "timeout"
                }