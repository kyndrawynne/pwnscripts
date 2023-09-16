import requests

url = 'http://127.0.0.1:80/553c75b5a6c1c4672f4e5c5fdd3bb5bd'
response = requests.get(url)

print(response.text)
