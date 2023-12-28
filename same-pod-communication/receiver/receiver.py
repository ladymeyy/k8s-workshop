# receiver.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def respond():
    # Respond to the request from App 1
    return "Response from App 2"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
