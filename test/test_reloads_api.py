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
from dataplaneapi.api.reloads_api import ReloadsApi  # noqa: E501
from dataplaneapi.rest import ApiException


class TestReloadsApi(unittest.TestCase):
    """ReloadsApi unit test stubs"""

    def setUp(self):
        self.api = ReloadsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_reload(self):
        """Test case for get_reload

        Return one HAProxy reload status  # noqa: E501
        """
        pass

    def test_get_reloads(self):
        """Test case for get_reloads

        Return list of HAProxy Reloads.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()