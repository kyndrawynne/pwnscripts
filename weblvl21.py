import requests

url = "http://127.0.0.1:80"
form_data = {
    'a': '23c7ab065212f3d98aa85e60280a5123'
}

response = requests.post(url, data=form_data)

print(response.text)
