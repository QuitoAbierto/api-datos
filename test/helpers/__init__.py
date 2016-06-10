from nose.tools import *
from unittest.mock import *
import random
from app.scripts import get_db
from app.stop_repository import StopRepository
from app.route_repository import RouteRepository

def random_alpha(size):
    return ''.join(random.choice('0123456789ABCDEF') for i in range(size))

def delete_db():
    db = get_db.run()
    stop_repo = StopRepository(db)
    route_repo = RouteRepository(db)
    stops = stop_repo.all()
    routes = route_repo.all()
    documents = stops + routes
    [db.delete(doc) for doc in documents]
