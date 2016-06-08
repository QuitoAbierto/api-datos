from flask import Flask, request
import json
from app.scripts import get_db
from app.stop_repository import StopRepository
from app.stop_service import StopService
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)
db = get_db.run()

@app.route('/api/parada', methods=['POST'])
def insert_one():
    repo = StopRepository(db)
    doc = json.loads(request.data.decode("utf-8"))
    new_doc = repo.save(doc)
    location = '/api/parada/{}'.format(new_doc['_id'])
    return json.dumps(new_doc), 201, {'location': location}

@app.route('/api/parada', methods=['GET'])
def return_all():
    repo = StopRepository(db)
    stops = repo.all()
    return json.dumps(stops), 200

@app.route('/api/parada/cercana', methods=['POST'])
def closest_stop():
    repo = StopRepository(db)
    stop_service = StopService(repo)
    current_location = json.loads(request.data.decode("utf-8"))
    lat, lng = (current_location['location']['lat'],
        current_location['location']['lng'])
    stop = stop_service.get_closest(lat, lng)
    return json.dumps({'stop': stop})


if __name__ == '__main__':
    app.debug = True
    app.run()
