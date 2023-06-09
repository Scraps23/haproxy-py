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
from dataplaneapi.api.server_switching_rule_api import ServerSwitchingRuleApi  # noqa: E501
from dataplaneapi.rest import ApiException


class TestServerSwitchingRuleApi(unittest.TestCase):
    """ServerSwitchingRuleApi unit test stubs"""

    def setUp(self):
        self.api = ServerSwitchingRuleApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_server_switching_rule(self):
        """Test case for create_server_switching_rule

        Add a new Server Switching Rule  # noqa: E501
        """
        pass

    def test_delete_server_switching_rule(self):
        """Test case for delete_server_switching_rule

        Delete a Server Switching Rule  # noqa: E501
        """
        pass

    def test_get_server_switching_rule(self):
        """Test case for get_server_switching_rule

        Return one Server Switching Rule  # noqa: E501
        """
        pass

    def test_get_server_switching_rules(self):
        """Test case for get_server_switching_rules

        Return an array of all Server Switching Rules  # noqa: E501
        """
        pass

    def test_replace_server_switching_rule(self):
        """Test case for replace_server_switching_rule

        Replace a Server Switching Rule  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
