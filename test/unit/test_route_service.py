from test.helpers import *
from app.route_service import RouteService


class TestRouteService:

    def setup(self):
        self.mock_repo = Mock()
        self.mock_repo.save.side_effect = lambda route: route
        self.service = RouteService(self.mock_repo)

    def test_adds_type_to_route(self):
        route = {'name': 'some_name'}

        saved_route = self.service.save(route)

        assert_equal('route', saved_route['type'])

    def test_gets_route_by_name(self):
        route_name = 'route1'
        self.mock_repo.by_name.return_value = [
            {'name': route_name, 'location': {'lng': 1, 'lat': 1}},
            {'name': route_name, 'location': {'lng': 2, 'lat': 2}}
        ]

        route = self.service.by_name(route_name)

        assert_equal(route_name, route['name'])
        assert_equal(2, len(route['locations']))

    def test_returns_none_if_no_nodes_are_found(self):
        self.mock_repo.by_name.return_value = []

        route = self.service.by_name('invalid_name')

        assert_equal(None, route)
