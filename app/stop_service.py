from geopy import Point, distance


class StopService:
    def __init__(self, repo):
        self.repo = repo

    def save(self, stop):
        latitude = stop['location']['lat']
        longitude = stop['location']['lng']
        stop['type'] = 'parada'
        stop['geoJSON'] = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [longitude, latitude]},
            'properties': {
                'name': stop['name'],
                'description': stop['description']
            }
        }
        return self.repo.save(stop)

    def get_closest(self, lat, lng):
        stops = self.repo.all()
        stops_with_coordinates = self.__get_coordinates(stops)
        current_location = Point(lat, lng)
        distances = self.__calculate_distances(stops_with_coordinates,
            current_location)
        if not distances:
            return None
        closest_stop = min(distances, key=lambda x: x[1])[0]
        closest_stop.pop('point')
        return closest_stop

    def __get_coordinates(self, stops):
        def add_point(stop):
            stop['point'] = Point(stop['location']['lat'],
                stop['location']['lng'])
            return stop

        return [add_point(stop) for stop in stops]

    def __calculate_distances(self, stops, current_location):
        return [(stop, distance.distance(stop['point'], current_location).km)\
            for stop in stops]
