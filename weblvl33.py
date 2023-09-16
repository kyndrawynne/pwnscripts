import requests

base_url = "http://127.0.0.1:80"
url = f"{base_url}/redirecting-url"

# Disable automatic redirects
response = requests.get(url, allow_redirects=False)

while response.status_code == 302:
    redirect_url = response.headers['Location']
    # Concatenate the base URL if the location is a relative URL
    if redirect_url.startswith("/"):
        redirect_url = base_url + redirect_url
    print(f"Following redirect to {redirect_url}")
    response = requests.get(redirect_url, allow_redirects=False)

print(response.text)

