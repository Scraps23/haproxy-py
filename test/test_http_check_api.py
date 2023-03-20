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
from dataplaneapi.api.http_check_api import HTTPCheckApi  # noqa: E501
from dataplaneapi.rest import ApiException


class TestHTTPCheckApi(unittest.TestCase):
    """HTTPCheckApi unit test stubs"""

    def setUp(self):
        self.api = HTTPCheckApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_http_check(self):
        """Test case for create_http_check

        Add a new HTTP check  # noqa: E501
        """
        pass

    def test_delete_http_check(self):
        """Test case for delete_http_check

        Delete a HTTP check  # noqa: E501
        """
        pass

    def test_get_http_check(self):
        """Test case for get_http_check

        Return one HTTP check  # noqa: E501
        """
        pass

    def test_get_http_checks(self):
        """Test case for get_http_checks

        Return an array of HTTP checks  # noqa: E501
        """
        pass

    def test_replace_http_check(self):
        """Test case for replace_http_check

        Replace a HTTP check  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
