import sys
import os
import requests
import json
import jsonschema
from robot.libraries.String import String
from robot.api.deco import keyword

_here = os.path.dirname(__file__)
string = String()
_here = string.fetch_from_left(_here, "assurity")
sys.path.insert(0, os.path.abspath(os.path.join(_here)))

from assurity.api.utils.libraries.TestLibUtils import TestLibUtils

class Categories(object):
    def __init__(self):
        super(Categories, self).__init__()
        self.utils = TestLibUtils()
        self.application = 'tmsandbox'
        self.request_url = ''
        self.response = ''
        self.category_name = ''
        self.can_relist = ''
        self.promo_description = ''
        self.schema = jsonschema
        ## File format using Windows
        with open(_here + 'assurity-test-automation\\assurity\\api\\utils\\resources\\schema_response_get.json') as schema_obj:
            self.schema_exp = json.load(schema_obj)['Categories']

        ## File format using Mac OS
        # with open(_here + '/assurity/api/utils/resources/schema_response_get.json') as schema_obj:
        #     self.schema_exp = json.load(schema_obj)['Categories']

# A user should be able to check if category name is equal to Carbon credits
    @keyword("A user wants to retrieve the category details")
    def prepare_category_details(self):
        self.request_url = self.utils.get_base_url(self.application) + self.utils.get_endpoints('get_category')
        print("Request URL: " + self.request_url)

    @keyword("A request was made to retrieve Name in Category details")
    def get_category_name(self):
        self.response = requests.get(self.request_url, headers=None)
        payload = json.loads(self.response.text)
        self.category_name = payload['Name']
        print("Category Name: " + self.category_name)

    @keyword("Return a successful status response if Name is set to Carbon credits")
    def assert_name_and_response(self):
        self.utils.assert_equal(self.category_name, self.utils.get_expected_val('name'))
        self.utils.assert_equal(self.response.headers['Content-Type'], "application/json")
        self.utils.assert_equal(self.response.status_code, 200)
        self.validate_get_response_schema()

# A user should be able to check if a category can be relisted
    @keyword("A request was made to check if category can be relisted")
    def get_category_relist(self):
        self.response = requests.get(self.request_url, headers=None)
        payload = json.loads(self.response.text)
        self.can_relist = payload['CanRelist']
        print("CanRelist: " + str(self.can_relist))

    @keyword("Return a successful status response if category can be relisted")
    def assert_relist_and_response(self):
        self.utils.assert_equal(str(self.can_relist), self.utils.get_expected_val('can_relist'))
        self.utils.assert_equal(self.response.headers['Content-Type'], "application/json")
        self.utils.assert_equal(self.response.status_code, 200)
        self.validate_get_response_schema()

# A user should be able to check if the description of the promo contains 2x larger image
    @keyword("A request was made to retrieve the description of the Gallery under Promotions")
    def get_category_promotions(self):
        self.response = requests.get(self.request_url, headers=None)
        payload = json.loads(self.response.text)
        for each in payload['Promotions']:
            if each['Name'] == "Gallery":
                self.promo_description = each['Description']
                break
        print("Promo Gallery Description: " + self.promo_description)

    @keyword("Return a successful status response if the promo description contains 2x larger image")
    def assert_promotions_description_and_response(self):
        self.utils.assert_text_contains(self.utils.get_expected_val('promotions'), self.promo_description)
        self.utils.assert_equal(self.response.headers['Content-Type'], "application/json")
        self.utils.assert_equal(self.response.status_code, 200)
        self.validate_get_response_schema()

# Schema Checking
    @keyword("Validate Get Categories Response Schema")
    def validate_get_response_schema(self):
        if self.response.status_code == 200:
            expected_schema = self.schema_exp['get_details']
            self.schema.validate(self.response.json(), expected_schema)
            print("Schema validation passed")
        else:
            print("Schema validation will not be performed due to response status " + str(self.response.status_code))

## Negative Scenario

# A user should be able to get '400 Bad Request' error response when entering invalid query
    @keyword("A user wants to retrieve the category details using an invalid query")
    def prepare_category_details_invalid_syntax(self):
        self.request_url = self.utils.get_base_url(self.application) + self.utils.get_endpoints('get_category_invalid400')
        print("Request URL: " + self.request_url)

    @keyword("A request was made to retrieve Category details")
    def get_category_details(self):
        self.response = requests.get(self.request_url, headers=None)
        print(self.response)

    @keyword("Then Return an error status 400 Bad Request")
    def assert_400_error_response(self):
        self.utils.assert_equal(self.response.status_code, 400)

# A user should be able to get '401 Unauthorized' error response when entering invalid login credentials
    @keyword("A request was made to retrieve Category details with invalid login credentials")
    def get_category_details_unauthorized(self):
        invalid_header = {
            'Authorization': "Bearer InvalidHeader",
        }
        self.response = requests.get(self.request_url, headers=invalid_header)
        print(self.response)

    @keyword("Return an error status 401 Unauthorized")
    def assert_401_error_response(self):
        self.utils.assert_equal(self.response.status_code, 401)

# A user should be able to get '404 Not Found' error when entering broken or not existing link
    @keyword("A user wants to retrieve the category details from a broken links")
    def prepare_category_details_broken_links(self):
        self.request_url = self.utils.get_base_url(self.application) + self.utils.get_endpoints('get_category_invalid404')
        print("Request URL: " + self.request_url)

    @keyword("Return an error status 404 Not Found")
    def assert_404_error_response(self):
        self.utils.assert_equal(self.response.status_code, 404)

