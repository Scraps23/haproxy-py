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
from dataplaneapi.api.filter_api import FilterApi  # noqa: E501
from dataplaneapi.rest import ApiException


class TestFilterApi(unittest.TestCase):
    """FilterApi unit test stubs"""

    def setUp(self):
        self.api = FilterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_filter(self):
        """Test case for create_filter

        Add a new Filter  # noqa: E501
        """
        pass

    def test_delete_filter(self):
        """Test case for delete_filter

        Delete a Filter  # noqa: E501
        """
        pass

    def test_get_filter(self):
        """Test case for get_filter

        Return one Filter  # noqa: E501
        """
        pass

    def test_get_filters(self):
        """Test case for get_filters

        Return an array of all Filters  # noqa: E501
        """
        pass

    def test_replace_filter(self):
        """Test case for replace_filter

        Replace a Filter  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()