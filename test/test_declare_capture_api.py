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
from dataplaneapi.api.declare_capture_api import DeclareCaptureApi  # noqa: E501
from dataplaneapi.rest import ApiException


class TestDeclareCaptureApi(unittest.TestCase):
    """DeclareCaptureApi unit test stubs"""

    def setUp(self):
        self.api = DeclareCaptureApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_declare_capture(self):
        """Test case for create_declare_capture

        Add a new declare capture  # noqa: E501
        """
        pass

    def test_delete_declare_capture(self):
        """Test case for delete_declare_capture

        Delete a declare capture  # noqa: E501
        """
        pass

    def test_get_declare_capture(self):
        """Test case for get_declare_capture

        Return one declare capture  # noqa: E501
        """
        pass

    def test_get_declare_captures(self):
        """Test case for get_declare_captures

        Return an array of declare captures  # noqa: E501
        """
        pass

    def test_replace_declare_capture(self):
        """Test case for replace_declare_capture

        Replace a declare capture  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
