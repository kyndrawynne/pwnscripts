import urllib.parse
import requests

# The path with spaces
path = "/02f92ca8 92dcd1d9/f71b0541 a76f08bc"

# URL-encode the path
encoded_path = urllib.parse.quote(path)

# The full URL
url = "http://127.0.0.1:80" + encoded_path

# Send the GET request
response = requests.get(url)

# Print the response
print(response.text)
