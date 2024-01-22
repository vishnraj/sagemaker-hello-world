import flask
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    """Determine if the container is working and healthy. In this sample container, we declare
    it healthy if we can load the model successfully."""
    return jsonify('pong')

@app.route('/invocations', methods=['POST'])
def transformation():
    return jsonify("Hello World")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
