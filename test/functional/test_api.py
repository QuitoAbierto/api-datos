from api import app
from test.helpers import *
import json
from random import randint


class TestApi:

    def setup(self):
        self.test_app = app.test_client()
        delete_db()

    def test_returns_created_resources_location(self):
        some_value = random_alpha(10)
        response = self.__insert_document({'some_key': some_value})
        response_body = json.loads(response.data.decode("utf-8"))
        resource_id = response_body['_id']
        assert_equal(response.status_code, 201)
        assert_true('/api/parada/{}'.format(response_body['_id']) in response.location)

    def test_returns_all_resources(self):
        self.__insert_document({'some_key': 'some_value1'})
        self.__insert_document({'some_key': 'some_value2'})

        response = self.test_app.get('/api/parada')
        response_body = json.loads(response.data.decode("utf-8"))
        document = response_body[randint(0,1)]

        assert_equal(response.status_code, 200)
        assert_equal(len(response_body), 2)
        assert_true('_id' in document)
        assert_true('_rev' in document)
        assert_true('some_key' in document)

    def test_returns_nearest_stop_to_the_given_coordinate(self):
        stops = [
            {'location': {'lat': -0.1842817466581577, 'lng': -78.48255157470703}, 'name': 'stop3'},
            {'location': {'lat': -0.18588909679818932, 'lng': -78.48271250724792}, 'name': 'stop2'},
            {'location': {'lat': -0.18161028009784438, 'lng': -78.48206877708435}, 'name': 'stop4'},
            {'location': {'lat': -0.17899245706132855, 'lng': -78.48127484321594}, 'name': 'stop5'}
        ]

        [self.__insert_document(stop) for stop in stops]

        request = {'location': { 'lat': -0.18571743632385881, 'lng': -78.48230481147766 }}

        response = self.test_app.post('/api/parada/cercana', data=json.dumps(request))
        response_body = json.loads(response.data.decode("utf-8"))

        closest_stop = response_body['stop']

        assert_equal(response.status_code, 200)
        assert_equal('stop2', closest_stop['name'])

    def __insert_document(self, document):
        return self.test_app.post('/api/parada', data=json.dumps(document))
