from flask import Flask, request


app = Flask(__name__)


@app.route('/api/ejemplo', methods=['POST'])
def ejemplo_post():
    return request.data
