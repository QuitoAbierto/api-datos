from api import app
from test.helpers import *
import json
from random import randint


class TestApi:

    def setup(self):
        self.test_app = app.test_client()

    def test_returns_created_resources_location(self):
        some_value = random_alpha(10)
        response = self.__insert_document(some_value)
        response_body = json.loads(response.data.decode("utf-8"))
        resource_id = response_body['_id']
        assert_equal(response.status_code, 201)
        assert_true('/api/parada/{}'.format(response_body['_id']) in response.location)

    def test_returns_all_resources(self):
        self.__insert_document('some_value1')
        self.__insert_document('some_value2')

        response = self.test_app.get('/api/parada')
        response_body = json.loads(response.data.decode("utf-8"))
        document = response_body[randint(0,1)]

        assert_equal(response.status_code, 200)
        assert_equal(len(response_body), 2)
        assert_true('_id' in document)
        assert_true('_rev' in document)
        assert_true('some_key' in document)

    def __insert_document(self, value):
        data = {'some_key': value}
        return self.test_app.post('/api/parada', data=json.dumps(data))
