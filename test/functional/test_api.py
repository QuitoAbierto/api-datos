from api import app
from test.helpers import *
import json


class TestApi:

    def setup(self):
        self.test_app = app.test_client()

    def test_returns_created_resources_location(self):
        some_value = random_alpha(10)
        data = {'some_key': some_value}
        response = self.test_app.post('/api/recurso', data=json.dumps(data))
        response_body = json.loads(response.data.decode("utf-8"))
        resource_id = response_body['_id']
        assert_equal(response.status_code, 201)
        assert_true('/api/recurso/{}'.format(response_body['_id']) in response.location)
