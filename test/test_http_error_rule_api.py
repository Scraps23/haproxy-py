# coding: utf-8

"""
    HAProxy Data Plane API

    API for editing and managing haproxy instances. Provides process information, configuration management, haproxy stats and logs.   # noqa: E501

    OpenAPI spec version: 2.7
    Contact: support@haproxy.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import dataplaneapi
from dataplaneapi.api.http_error_rule_api import HTTPErrorRuleApi  # noqa: E501
from dataplaneapi.rest import ApiException


class TestHTTPErrorRuleApi(unittest.TestCase):
    """HTTPErrorRuleApi unit test stubs"""

    def setUp(self):
        self.api = HTTPErrorRuleApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_http_error_rule(self):
        """Test case for create_http_error_rule

        Add a new HTTP Error Rule  # noqa: E501
        """
        pass

    def test_delete_http_error_rule(self):
        """Test case for delete_http_error_rule

        Delete a HTTP Error Rule  # noqa: E501
        """
        pass

    def test_get_http_error_rule(self):
        """Test case for get_http_error_rule

        Return one HTTP Error Rule  # noqa: E501
        """
        pass

    def test_get_http_error_rules(self):
        """Test case for get_http_error_rules

        Return an array of all HTTP Error Rules  # noqa: E501
        """
        pass

    def test_replace_http_error_rule(self):
        """Test case for replace_http_error_rule

        Replace a HTTP Error Rule  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
