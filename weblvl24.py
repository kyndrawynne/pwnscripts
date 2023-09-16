import requests

# The URL to send the request to
url = "http://127.0.0.1:80/api/data"

# The form data to include in the request
form_data = {
    "a": "5879d890c13c71dd16c8228ae2a955e4",
    "b": "6ff1a988 a49a34ec&cabd9531#7cb306bc",
}

# Send the POST request with the form data
response = requests.post(url, data=form_data)

# Print the response
print(response.text)
