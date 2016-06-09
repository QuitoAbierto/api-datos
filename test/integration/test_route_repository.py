from app.route_repository import RouteRepository
from app.scripts import get_db
from test.helpers import *


class TestRouteRepository:

    def setup(self):
        self.db = get_db.run()
        self.repo = RouteRepository(self.db)
        delete_db()

    def test_saves_new_route(self):
        route = {'some_key': 'some_value'}

        saved_route = self.repo.save(route)
        assert_true('_rev' in saved_route)
        assert_true('_id' in saved_route)

    def test_returns_all_route_nodes(self):
        route1 = {'some_key': 'some_value', 'type': 'route'}
        route2 = {'some_other_key': 'some_other_value', 'type': 'route'}
        self.repo.save(route1)
        self.repo.save(route2)

        routes = self.repo.all()

        assert_equal(2, len(routes))
