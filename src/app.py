# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)


def parse(message):
    pass

@app.post("/upload")
def receive_data():
    if request.is_json:
        message = request.get_json()
        try:
            parse(message)
            return "Ok!", 200
        except Exception as e:
            print(e)
            return "Data could not be parsed!", 400
    return "Data not in JSON format!", 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
