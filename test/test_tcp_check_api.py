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
from dataplaneapi.api.tcp_check_api import TCPCheckApi  # noqa: E501
from dataplaneapi.rest import ApiException


class TestTCPCheckApi(unittest.TestCase):
    """TCPCheckApi unit test stubs"""

    def setUp(self):
        self.api = TCPCheckApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_tcp_check(self):
        """Test case for create_tcp_check

        Add a new TCP check  # noqa: E501
        """
        pass

    def test_delete_tcp_check(self):
        """Test case for delete_tcp_check

        Delete a TCP check  # noqa: E501
        """
        pass

    def test_get_tcp_check(self):
        """Test case for get_tcp_check

        Return one TCP check  # noqa: E501
        """
        pass

    def test_get_tcp_checks(self):
        """Test case for get_tcp_checks

        Return an array of TCP checks  # noqa: E501
        """
        pass

    def test_replace_tcp_check(self):
        """Test case for replace_tcp_check

        Replace a TCP check  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
