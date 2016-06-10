
class RouteRepository:

    def __init__(self, db):
        self.db = db

    def save(self, route_node):
        self.db.save(route_node)
        return route_node

    def all(self):
        map_function = '''
            function(doc) {
                if(doc.type === 'route') {
                    emit(doc._id, doc);
                }
            }'''
        return [route['value'] for route in self.db.query(map_function)]

    def by_name(self, name):
        map_function = '''
            function(doc) {{
                if(doc.type === 'route' && doc.name === '{}') {{
                    emit(doc._id, doc);
                }}
            }}'''.format(name)
        return [route['value'] for route in self.db.query(map_function)]
