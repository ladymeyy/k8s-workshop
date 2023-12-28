# sender.py

from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def send_request():
    # Send a request to App 2
    response = requests.get("http://localhost:5000")
    return f"Request sent to App 2, Response: {response.text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)