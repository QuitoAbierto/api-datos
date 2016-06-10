from test.helpers import *
from app.route_service import RouteService
from app.route_repository import RouteRepository
from app.scripts import get_db


class TestRouteService:

    def setup(self):
        db = get_db.run()
        repo = RouteRepository(db)
        self.service = RouteService(repo)
        delete_db()

    def test_adds_route_node_to_existing_route(self):
        name = random_alpha(10)
        new_location = {'lng': 200, 'lat': 200}
        self.__save_route_node(name=name)
        self.__save_route_node(name=name, location=new_location)
        saved_route = self.service.all()[0]

        assert_equal(2, len(saved_route['locations']))
        assert_equal([100, 100], saved_route['locations'][0])
        assert_equal([200, 200], saved_route['locations'][1])

    def test_groups_routes(self):
        self.__save_route_node(name='route1')
        self.__save_route_node(name='route1')
        self.__save_route_node(name='route2')

        saved_routes = self.service.all()

        assert_equal(2, len(saved_routes))

    def test_gets_route_by_name(self):
        self.__save_route_node(name='route1')
        self.__save_route_node(name='route1')
        self.__save_route_node(name='route2')

        route = self.service.by_name('route1')

        assert_equal('route1', route['name'])
        assert_equal(2, len(route['locations']))

    def __save_route_node(self, **kwargs):
        default_location = {
            'lng': 100,
            'lat': 100
        }
        route_node = {
            'name': kwargs.get('name') or 'some_name',
            'description': kwargs.get('description') or 'description',
            'location': kwargs.get('location') or default_location
        }
        self.service.save(route_node)
