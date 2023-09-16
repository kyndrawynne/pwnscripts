import requests

# Starting URL
url = "http://127.0.0.1:80"

# Start a session to handle cookies
session = requests.Session()

# Initial request
response = session.get(url)
print(response.text) # Print the response

# Make further requests maintaining the session
for _ in range(4): # Adjust the range based on your needs
    response = session.get(url)
    print(response.text) # Print the response

# You can also access cookies if needed
cookies = session.cookies.get_dict()
print("Cookies:", cookies)
