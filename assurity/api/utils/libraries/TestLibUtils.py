import sys, os
import json
from robot.libraries.String import String
_here = os.path.dirname(__file__)
_string = String()
_here = _string.fetch_from_left(_here, "assurity")
sys.path.insert(0, os.path.abspath(os.path.join(_here)))


class TestLibUtils(object):
    def __init__(self):
        self.data = self.load_json()

    def get_base_url(self, app=None):
        return self.data['base_url'][app]

    def get_endpoints(self, endpoint=None):
        return self.data['endpoints'][endpoint]

    def get_expected_val(self, value=None):
        return self.data['expected_value'][value]

    def load_json(self):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, '../resources/test_data.json')
        data = json.load(open(file_path))
        return data

    #assertions
    def assert_equal(self, actual_val, expected_val):
        log = 'Actual Value = ' + str(actual_val) + '  :  Expected Value = ' + str(expected_val)
        assert(actual_val == expected_val), log
        print(log)

    def assert_text_contains(self, actual_val, expected_val):
        log = 'Actual Value = ' + str(actual_val) + '  :  Expected Value = ' + str(expected_val)
        assert(actual_val in expected_val), log
        print(log)