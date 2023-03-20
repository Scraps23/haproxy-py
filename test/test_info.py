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
from dataplaneapi.models.info import Info  # noqa: E501
from dataplaneapi.rest import ApiException


class TestInfo(unittest.TestCase):
    """Info unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInfo(self):
        """Test Info"""
        # FIXME: construct object with mandatory attributes with example values
        # model = dataplaneapi.models.info.Info()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
