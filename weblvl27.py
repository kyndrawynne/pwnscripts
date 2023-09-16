import requests

url = "http://127.0.0.1:80/api/data"
data = {
    "a": "cd63d127f0e047cad3d0c484a6b4a65f"
}

response = requests.post(url, json=data)

print(response.text)
