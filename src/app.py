# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)


def parse(message):
    pass

@app.route("/upload")
def receive_data():
    if request.is_json:
        message = request.get_json()
        try:
            parse(message)
            return None, 200
        except Exception as e:
            print(e)
            return None, 400
    return None, 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
