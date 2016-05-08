from flask import Flask, request
import json
from app.scripts import create_db
from app.repository import Repository


app = Flask(__name__)
db = create_db.run()

@app.route('/api/recurso', methods=['POST'])
def ejemplo_post():
    repo = Repository(db)
    doc = json.loads(request.data.decode("utf-8"))
    new_doc = repo.save(doc)
    location = '/api/recurso/{}'.format(new_doc['_id'])
    return json.dumps(new_doc), 201, {'location': location}

if __name__ == '__main__':
    app.debug = True
    app.run()