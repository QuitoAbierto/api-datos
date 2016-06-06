from flask import Flask, request
import json
from app.scripts import get_db
from app.repository import Repository
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)
db = get_db.run()

@app.route('/api/parada', methods=['POST'])
def insert_one():
    repo = Repository(db)
    doc = json.loads(request.data.decode("utf-8"))
    new_doc = repo.save(doc)
    location = '/api/parada/{}'.format(new_doc['_id'])
    return json.dumps(new_doc), 201, {'location': location}

@app.route('/api/parada', methods=['GET'])
def return_all():
    repo = Repository(db)
    documents = [doc['value'] for doc in repo.all()]
    return json.dumps(documents), 200

if __name__ == '__main__':
    app.debug = True
    app.run()
