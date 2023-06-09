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
from dataplaneapi.api.group_api import GroupApi  # noqa: E501
from dataplaneapi.rest import ApiException


class TestGroupApi(unittest.TestCase):
    """GroupApi unit test stubs"""

    def setUp(self):
        self.api = GroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_group(self):
        """Test case for create_group

        Add a new userlist group  # noqa: E501
        """
        pass

    def test_delete_group(self):
        """Test case for delete_group

        Delete a group  # noqa: E501
        """
        pass

    def test_get_group(self):
        """Test case for get_group

        Return one userlist group  # noqa: E501
        """
        pass

    def test_get_groups(self):
        """Test case for get_groups

        Return an array of userlist groups  # noqa: E501
        """
        pass

    def test_replace_group(self):
        """Test case for replace_group

        Replace a group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
