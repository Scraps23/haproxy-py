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
from dataplaneapi.api.userlist_api import UserlistApi  # noqa: E501
from dataplaneapi.rest import ApiException


class TestUserlistApi(unittest.TestCase):
    """UserlistApi unit test stubs"""

    def setUp(self):
        self.api = UserlistApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_userlist(self):
        """Test case for create_userlist

        Add a new userlist  # noqa: E501
        """
        pass

    def test_delete_userlist(self):
        """Test case for delete_userlist

        Delete a userlist  # noqa: E501
        """
        pass

    def test_get_userlist(self):
        """Test case for get_userlist

        Return one userlist  # noqa: E501
        """
        pass

    def test_get_userlists(self):
        """Test case for get_userlists

        Return an array of userlists  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
