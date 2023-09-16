import requests

url = "http://127.0.0.1:80"

params = {
    "a": "17bf7dde32c821b24bc646097f615780",
    "b": "0fed8056 16993573&11f3fc88#5081f60a"
}

response = requests.get(url, params=params)

print(response.text)
