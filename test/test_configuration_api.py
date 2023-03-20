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
from dataplaneapi.api.configuration_api import ConfigurationApi  # noqa: E501
from dataplaneapi.rest import ApiException


class TestConfigurationApi(unittest.TestCase):
    """ConfigurationApi unit test stubs"""

    def setUp(self):
        self.api = ConfigurationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_configuration_version(self):
        """Test case for get_configuration_version

        Return a configuration version  # noqa: E501
        """
        pass

    def test_get_ha_proxy_configuration(self):
        """Test case for get_ha_proxy_configuration

        Return HAProxy configuration  # noqa: E501
        """
        pass

    def test_post_ha_proxy_configuration(self):
        """Test case for post_ha_proxy_configuration

        Push new haproxy configuration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
