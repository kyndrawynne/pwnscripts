import requests

# Create a session object to handle cookies
session = requests.Session()

# Define the URL and headers
url = 'http://127.0.0.1:80/'
headers = {'Host': '127.0.0.1'}

# Define the initial cookies
cookies = {'cookie': 'eb70d95de4a993e410c664b0b79454ad'}

# Make the initial GET request with the cookies, and disable automatic redirection
response = session.get(url, headers=headers, cookies=cookies, allow_redirects=False)

# Extract the new cookie and Location for redirect
new_cookie = response.cookies['cookie']
location = response.headers['Location']

# Build the full URL for the redirect location
redirect_url = url.rstrip('/') + location

# Make a new request to the redirect location, including the new cookie
response = session.get(redirect_url, headers=headers, cookies={'cookie': new_cookie}, allow_redirects=False)

# Print the final response
print(response.text)

