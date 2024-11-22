import os
import requests
from flask import Flask

app = Flask(__name__)

WORKER_URI = os.environ.get("WORKER_URI")

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/dowork")
def do_work():
    return requests.get(f'{WORKER_URI}/hello').content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
