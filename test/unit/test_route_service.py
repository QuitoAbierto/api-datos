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
        expected_locations = [[1, 1], [2, 2]]

        assert_equal(route_name, route['name'])
        assert_equal(2, len(route['locations']))
        assert_equal(expected_locations, route['locations'])

    def test_returns_none_if_no_nodes_are_found(self):
        self.mock_repo.by_name.return_value = []

        route = self.service.by_name('invalid_name')

        assert_equal(None, route)

    def test_returns_all_routes(self):
        self.mock_repo.all.return_value = [
            {'name': 'route1', 'location': {'lng': 1, 'lat': 1}},
            {'name': 'route1', 'location': {'lng': 2, 'lat': 2}},
            {'name': 'route2', 'location': {'lng': 3, 'lat': 3}},
            {'name': 'route3', 'location': {'lng': 4, 'lat': 4}}
        ]

        expected_routes = [
            {'name': 'route1', 'locations': [[1, 1], [2, 2]]},
            {'name': 'route2', 'locations': [[3, 3]]},
            {'name': 'route3', 'locations': [[4, 4]]}
        ]

        routes = self.service.all()

        assert_equal(expected_routes, routes)
