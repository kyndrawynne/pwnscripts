import requests

url = 'http://127.0.0.1:80/'

# Send a GET request
response = requests.get(url)

# Print the HTTP status code
print(f"Status Code: {response.status_code}")

# Print the response text
print(response.text)
