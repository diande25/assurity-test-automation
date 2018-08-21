*** Settings ***
Documentation  Feature: A user should be able to retrieve category details supplying requested parameters
Library  ../utils/keywords/Categories.py

*** Test Cases ***

A user should be able to check if category name is equal to Carbon credits
    [Documentation]  As a user I should be able to check if category name is equal to Carbon credits supplying a valid information
    [Tags]  positive    acceptance-test     category    name
    Given A user wants to retrieve the category details
    When A request was made to retrieve Name in Category details
    Then Return a successful status response if Name is set to Carbon credits

A user should be able to check if a category can be relisted
    [Documentation]  As a user I should be able to go into category details if it is can be relisted
    [Tags]  positive    acceptance-test     category    canrelist
    Given A user wants to retrieve the category details
    When A request was made to check if category can be relisted
    Then Return a successful status response if category can be relisted

A user should be able to check if the description of the promo contains 2x larger image
    [Documentation]  As a user I should be able to go into category details if the description of the promo contains 2x larger image
    [Tags]  positive    acceptance-test     category    promotions      gallery     2x larger image
    Given A user wants to retrieve the category details
    When A request was made to retrieve the description of the Gallery under Promotions
    Then Return a successful status response if the promo description contains 2x larger image

A user should be able to get '400 Bad Request' error response when entering invalid query
    [Documentation]  As a user I should be able to get '400 Bad Request' error when entering invalid query
    [Tags]  negative    acceptance-test     category    bad request     invalid syntax
    Given A user wants to retrieve the category details using an invalid query
    When A request was made to retrieve Category details
    Then Return an error status 400 Bad Request

A user should be able to get '401 Unauthorized' error response when entering invalid login credentials
    [Documentation]  As a user I should be able to get '401 Unauthorize' error when entering invalid query
    [Tags]  negative    acceptance-test     category    unauthorized    invalid login
    Given A user wants to retrieve the category details
    When A request was made to retrieve Category details with invalid login credentials
    Then Return an error status 401 Unauthorized

A user should be able to get '404 Not Found' error when entering broken or not existing link
    [Documentation]  As a user I should be able to get '400 Bad Request' error when entering invalid query
    [Tags]  negative    acceptance-test     category    broken link    not existing link
    Given A user wants to retrieve the category details from a broken links
    When A request was made to retrieve Category details
    Then Return an error status 404 Not Found