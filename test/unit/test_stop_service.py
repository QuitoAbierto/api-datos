from test.helpers import *
from app.stop_service import StopService


class TestStopService:

    def setup(self):
        self.repo = Mock()
        self.repo.save.side_effect = lambda stop: stop
        self.service = StopService(self.repo)

    def test_adds_type_to_document(self):
        stop = {
            'name': 'some_name',
            'description': 'some_description',
            'location': {
                'lat': 100,
                'lng': 100
            }
        }
        new_stop = self.service.save(stop)
        assert_equal(new_stop['type'], 'parada')

    def test_adds_geo_json_before_save(self):
        name = random_alpha(10)
        description = random_alpha(30)
        stop = {
            'name': name,
            'description': description,
            'location': {
                'lat': 100,
                'lng': 100
            }
        }
        self.service.save(stop)

        stop_with_geo_json = stop.copy()
        stop_with_geo_json['geoJSON'] = {
            'type': 'Feature',
            'geometry': {'type': 'Point', 'coordinates': [100, 100]},
            'properties': {
                'name': name,
                'description': description
            }
        }

        self.repo.save.assert_called_once_with(stop_with_geo_json)

    def test_calculates_closest_stop(self):
        stop_name = random_alpha(10)
        self.repo.all.return_value = [
            {
            'location': {'lat': -0.1862216889624625, 'lng': -78.48278224468231},
            'name': 'some_other_stop'
            },
            {
            'location': {'lat': -0.1850629807501721, 'lng': -78.48256230354309},
            'name': stop_name
            },
            {
            'location': {'lat': -0.18161028009784438, 'lng': -78.48206877708435},
            'name': 'stop4'},
        ]

        lat, lng = (-0.18506834514020962, -78.48234236240387)
        closest_stop = self.service.get_closest(lat, lng)

        assert_equal(stop_name, closest_stop['name'])

    def test_removes_point_when_closest_stop_is_found(self):
        self.repo.all.return_value = [
            {'location': {'lat': 100, 'lng': 100}}
        ]

        closest_stop = self.service.get_closest(100, 100)

        assert_false('point' in closest_stop,
            msg='Key point should not be present')

    def test_returns_none_when_there_is_no_stop_stored(self):
        self.repo.all.return_value = []

        closest_stop = self.service.get_closest(100, 100)

        assert_true(closest_stop is None,
            msg='closest stop should be none')
