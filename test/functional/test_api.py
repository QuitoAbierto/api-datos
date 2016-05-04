from app.api import app
from test.helpers import *
import json


class TestApi:

    def setup(self):
        self.test_app = app.test_client()

    def test_returns_created_object(self):
        some_value = random_alpha(10)
        data = {'some_key': some_value}
        response = self.test_app.post('/api/ejemplo', data=json.dumps(data))
        expected_data_response = json.dumps(data)
        assert_equal(response.status_code, 200)
        assert_equal(response.data.decode("utf-8"), expected_data_response)
