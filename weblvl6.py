import requests

url = 'http://127.0.0.1:80/'
headers = {'Host': 'a0d306763b130b99e31204bc48e0c60b'}

response = requests.get(url, headers=headers)

print(response.text)
