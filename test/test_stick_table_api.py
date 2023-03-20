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
from dataplaneapi.api.stick_table_api import StickTableApi  # noqa: E501
from dataplaneapi.rest import ApiException


class TestStickTableApi(unittest.TestCase):
    """StickTableApi unit test stubs"""

    def setUp(self):
        self.api = StickTableApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_stick_table(self):
        """Test case for get_stick_table

        Return Stick Table  # noqa: E501
        """
        pass

    def test_get_stick_table_entries(self):
        """Test case for get_stick_table_entries

        Return Stick Table Entries  # noqa: E501
        """
        pass

    def test_get_stick_tables(self):
        """Test case for get_stick_tables

        Return Stick Tables  # noqa: E501
        """
        pass

    def test_set_stick_table_entries(self):
        """Test case for set_stick_table_entries

        Set Entry to Stick Table  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()