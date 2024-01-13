import requests
from concurrent.futures import ThreadPoolExecutor
from random import choices, randint
from string import ascii_lowercase, digits
from datetime import datetime, timedelta


def generate_data():
    traceId = "".join(choices(ascii_lowercase, k=3)) + "".join(choices(ascii_lowercase, k=3)) + "".join(choices(digits, k=3))
    spanId = "span-"+"".join(choices(digits, k=3))

    start_date = "2023-01-01"
    end_date = "2023-12-31"
    start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = datetime.strptime(end_date, "%Y-%m-%d")
    time_diff_seconds = (end_datetime - start_datetime).total_seconds()
    random_seconds = randint(0, int(time_diff_seconds))
    random_timestamp = start_datetime + timedelta(seconds=random_seconds)
    timestamp = random_timestamp.isoformat() + "Z"    
    
    data = {
        "level": "error",
        "message": "Failed to connect to DB",
        "resourceId": "server-1234",
        "timestamp": timestamp,
        "traceId": traceId,
        "spanId": spanId,
        "commit": "5e5342f",
        "metadata": {
            "parentResourceId": "server-0987"
        }
    }
    return data

def send_request(url):
    response = requests.get(url)
    print(f"Response from {url}: {response.status_code}")

# Local host URL to send requests to
base_url = "http://localhost:8000/"

# Generate a list of 1000 URLs
urls = [f"{base_url}" for i in range(1, 30000)]

# Use ThreadPoolExecutor to send 10000 requests simultaneously
with ThreadPoolExecutor() as executor:
    executor.map(send_request, urls)