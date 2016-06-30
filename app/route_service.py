from itertools import groupby

class RouteService:

    def __init__(self, repo):
        self.repo = repo

    def save(self, route):
        route['type'] = 'route'
        return self.repo.save(route)

    def all(self):
        nodes = self.repo.all()
        routes = []
        for key, group in groupby(nodes, lambda x: x['name']):
            routes.append({
                'name': key,
                'locations': self.__get_locations(group)})
        return routes

    def by_name(self, route_name):
        route_nodes = self.repo.by_name(route_name)
        if not route_nodes:
            return None
        route = {
            'name': route_nodes[0]['name'],
            'locations': self.__get_locations(route_nodes)
        }

        return route

    def __get_locations(self, route_nodes):
        return [[node['location']['lng'], node['location']['lat']]
            for node in route_nodes]
