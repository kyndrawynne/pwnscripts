import requests

url = "http://127.0.0.1:80/api/data"

payload = {
    "a": "1db56423564adcc137ca21906c813710",
    "b": {
        "c": "6930c452",
        "d": ["6df748ae", "11ff73d8 d95f590b&0ddb5bae#96461b28"]
    }
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
