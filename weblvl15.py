import requests

url = "http://127.0.0.1:80"
params = {'a': '165bfb6cf0c67019412fe105b0a3f4eb'}

response = requests.get(url, params=params)

print(response.text)
