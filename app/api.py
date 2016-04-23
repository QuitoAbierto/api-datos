from flask import Flask, request


app = Flask(__name__)


@app.route('/api/v1/ejemplo', methods=['POST'])
def ejemplo_post():
    return request.data
