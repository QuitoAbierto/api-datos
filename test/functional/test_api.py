from api import app
from test.helpers import *
import json
from random import randint


class TestApi:

    def setup(self):
        self.test_app = app.test_client()
        delete_db()

    def test_saves_new_stop(self):
        name = random_alpha(10)
        description = random_alpha(30)

        self.__save_stop(name=name, description=description)

        response = self.test_app.get('/api/parada')
        stored_stop = json.loads(response.data.decode("utf-8"))[0]

        assert_equal(name, stored_stop['name'])
        assert_equal(description, stored_stop['description'])
        assert_equal('parada', stored_stop['type'])
        assert_equal('Feature', stored_stop['geoJSON']['type'])

    def test_returns_error_when_required_fields_are_not_provided(self):
        invalid_stop = {'invalid_key': 'value'}

        response = self.test_app.post('/api/parada', data=json.dumps(invalid_stop))
        error = json.loads(response.data.decode("utf-8"))['error']

        assert_equal(400, response.status_code)
        assert_equal('JSON mal formateado', error)

    def test_returns_created_resources_location(self):
        some_value = random_alpha(10)
        response = self.__save_stop(name=some_value)
        response_body = json.loads(response.data.decode("utf-8"))
        resource_id = response_body['_id']
        assert_equal(response.status_code, 201)
        assert_true('/api/parada/{}'.format(response_body['_id']) in response.location)

    def test_returns_all_resources(self):
        self.__save_stop(name='some_name1')
        self.__save_stop(name='some_name2')

        response = self.test_app.get('/api/parada')
        response_body = json.loads(response.data.decode("utf-8"))
        document = response_body[randint(0,1)]

        assert_equal(response.status_code, 200)
        assert_equal(len(response_body), 2)
        assert_true('_id' in document)
        assert_true('_rev' in document)
        assert_true('geoJSON' in document)

    def test_returns_nearest_stop_to_the_given_coordinate(self):
        stops = [
            {'location': {'lat': -0.1842817466581577, 'lng': -78.48255157470703}, 'name': 'stop3'},
            {'location': {'lat': -0.18588909679818932, 'lng': -78.48271250724792}, 'name': 'stop2'},
            {'location': {'lat': -0.18161028009784438, 'lng': -78.48206877708435}, 'name': 'stop4'},
            {'location': {'lat': -0.17899245706132855, 'lng': -78.48127484321594}, 'name': 'stop5'}
        ]

        [self.__save_stop(name=stop['name'], location=stop['location'])
            for stop in stops]

        request = {'location': { 'lat': -0.18571743632385881, 'lng': -78.48230481147766 }}

        response = self.test_app.post('/api/parada/cercana', data=json.dumps(request))
        response_body = json.loads(response.data.decode("utf-8"))

        closest_stop = response_body['stop']

        assert_equal(response.status_code, 200)
        assert_equal('stop2', closest_stop['name'])

    def __save_stop(self, **kwargs):
        default_location = {'lat': 100, 'lng': 100}
        stop = {
            'name': kwargs.get('name') or 'default_name',
            'description': kwargs.get('description') or 'default_description',
            'location': kwargs.get('location') or default_location
        }
        return self.test_app.post('/api/parada', data=json.dumps(stop))
