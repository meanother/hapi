import requests
import json

data = {
    "k": 1,
    "v": "example-value"
}

response = requests.post("http://0.0.0.0:80/api/info", data=json.dumps(data))
print(response.status_code)
print(response.json())
