from flask import Flask, request
import json
from app.scripts import get_db
from app.stop_repository import StopRepository
from app.route_repository import RouteRepository
from app.stop_service import StopService
from app.route_service import RouteService
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)
db = get_db.run()

@app.route('/api/parada', methods=['POST'])
def save_stop():
    stop = json.loads(request.data.decode("utf-8"))
    if not stop_valid(stop):
        return '{"error": "JSON mal formateado"}', 400
    repo = StopRepository(db)
    service = StopService(repo)
    new_stop = service.save(stop)
    location = '/api/parada/{}'.format(new_stop['_id'])
    return json.dumps(new_stop), 201, {'location': location}

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

@app.route('/api/ruta', methods=['POST'])
def save_route_node():
    route_node = json.loads(request.data.decode("utf-8"))
    repo = RouteRepository(db)
    route_service = RouteService(repo)
    route_service.save(route_node)
    return 'success', 201

@app.route('/api/ruta', methods=['GET'])
def get_all_routes():
    repo = RouteRepository(db)
    route_service = RouteService(repo)
    routes = route_service.all()
    return json.dumps(routes), 200

@app.route('/api/ruta/<route_name>', methods=['GET'])
def get_route_by_name(route_name):
    repo = RouteRepository(db)
    route_service = RouteService(repo)
    route = route_service.by_name(route_name)
    if not route:
        return json.dumps({'error': 'No such route.'}), 404
    return json.dumps({'route' :route}), 200

def stop_valid(stop):
    required_keys = ['name', 'description', 'location']
    return all([stop.get(key) for key in required_keys])

if __name__ == '__main__':
    app.debug = True
    app.run()
