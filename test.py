import requests
import json

data = {
    "k": 1,
    "v": "example-value"
}

URLS = [
    # "77.221.158.176:4500",
    # "79.137.248.187:4500"
    "94.228.115.6:8082"
]

# response = requests.post("http://0.0.0.0:80/api/info", data=json.dumps(data))

for url in URLS:
    response = requests.post(f"http://{url}/api/info", data=json.dumps(data), verify=False)
    print(response.status_code)
    print(response.json())
