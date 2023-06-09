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
from dataplaneapi.api.backend_api import BackendApi  # noqa: E501
from dataplaneapi.rest import ApiException


class TestBackendApi(unittest.TestCase):
    """BackendApi unit test stubs"""

    def setUp(self):
        self.api = BackendApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_backend(self):
        """Test case for create_backend

        Add a backend  # noqa: E501
        """
        pass

    def test_delete_backend(self):
        """Test case for delete_backend

        Delete a backend  # noqa: E501
        """
        pass

    def test_get_backend(self):
        """Test case for get_backend

        Return a backend  # noqa: E501
        """
        pass

    def test_get_backends(self):
        """Test case for get_backends

        Return an array of backends  # noqa: E501
        """
        pass

    def test_replace_backend(self):
        """Test case for replace_backend

        Replace a backend  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
