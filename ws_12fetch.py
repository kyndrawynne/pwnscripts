import requests
params= {
            "user" : "1"
            }
response = requests.post("http://challenge.localhost/info", params=params)
response.content
