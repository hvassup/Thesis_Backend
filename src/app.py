# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)


def parse(message):
    pass

@app.route("/")
def get_test():
    return 200

@app.route("/upload")
def receive_data():
    if request.is_json:
        message = request.get_json()
        try:
            parse(message)
            return 200
        except Exception as e:
            print(e)
            return 400
    return 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
