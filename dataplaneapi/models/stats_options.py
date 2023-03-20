# coding: utf-8

"""
    HAProxy Data Plane API

    API for editing and managing haproxy instances. Provides process information, configuration management, haproxy stats and logs.   # noqa: E501

    OpenAPI spec version: 2.7
    Contact: support@haproxy.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class StatsOptions(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'stats_admin': 'bool',
        'stats_admin_cond': 'str',
        'stats_admin_cond_test': 'str',
        'stats_auths': 'list[StatsAuth]',
        'stats_enable': 'bool',
        'stats_hide_version': 'bool',
        'stats_http_requests': 'list[StatsHttpRequest]',
        'stats_maxconn': 'int',
        'stats_realm': 'bool',
        'stats_realm_realm': 'str',
        'stats_refresh_delay': 'int',
        'stats_show_desc': 'str',
        'stats_show_legends': 'bool',
        'stats_show_modules': 'bool',
        'stats_show_node_name': 'str',
        'stats_uri_prefix': 'str'
    }

    attribute_map = {
        'stats_admin': 'stats_admin',
        'stats_admin_cond': 'stats_admin_cond',
        'stats_admin_cond_test': 'stats_admin_cond_test',
        'stats_auths': 'stats_auths',
        'stats_enable': 'stats_enable',
        'stats_hide_version': 'stats_hide_version',
        'stats_http_requests': 'stats_http_requests',
        'stats_maxconn': 'stats_maxconn',
        'stats_realm': 'stats_realm',
        'stats_realm_realm': 'stats_realm_realm',
        'stats_refresh_delay': 'stats_refresh_delay',
        'stats_show_desc': 'stats_show_desc',
        'stats_show_legends': 'stats_show_legends',
        'stats_show_modules': 'stats_show_modules',
        'stats_show_node_name': 'stats_show_node_name',
        'stats_uri_prefix': 'stats_uri_prefix'
    }

    def __init__(self, stats_admin=None, stats_admin_cond=None, stats_admin_cond_test=None, stats_auths=None, stats_enable=None, stats_hide_version=None, stats_http_requests=None, stats_maxconn=None, stats_realm=None, stats_realm_realm=None, stats_refresh_delay=None, stats_show_desc=None, stats_show_legends=None, stats_show_modules=None, stats_show_node_name=None, stats_uri_prefix=None):  # noqa: E501
        """StatsOptions - a model defined in Swagger"""  # noqa: E501
        self._stats_admin = None
        self._stats_admin_cond = None
        self._stats_admin_cond_test = None
        self._stats_auths = None
        self._stats_enable = None
        self._stats_hide_version = None
        self._stats_http_requests = None
        self._stats_maxconn = None
        self._stats_realm = None
        self._stats_realm_realm = None
        self._stats_refresh_delay = None
        self._stats_show_desc = None
        self._stats_show_legends = None
        self._stats_show_modules = None
        self._stats_show_node_name = None
        self._stats_uri_prefix = None
        self.discriminator = None
        if stats_admin is not None:
            self.stats_admin = stats_admin
        if stats_admin_cond is not None:
            self.stats_admin_cond = stats_admin_cond
        if stats_admin_cond_test is not None:
            self.stats_admin_cond_test = stats_admin_cond_test
        if stats_auths is not None:
            self.stats_auths = stats_auths
        if stats_enable is not None:
            self.stats_enable = stats_enable
        if stats_hide_version is not None:
            self.stats_hide_version = stats_hide_version
        if stats_http_requests is not None:
            self.stats_http_requests = stats_http_requests
        if stats_maxconn is not None:
            self.stats_maxconn = stats_maxconn
        if stats_realm is not None:
            self.stats_realm = stats_realm
        if stats_realm_realm is not None:
            self.stats_realm_realm = stats_realm_realm
        if stats_refresh_delay is not None:
            self.stats_refresh_delay = stats_refresh_delay
        if stats_show_desc is not None:
            self.stats_show_desc = stats_show_desc
        if stats_show_legends is not None:
            self.stats_show_legends = stats_show_legends
        if stats_show_modules is not None:
            self.stats_show_modules = stats_show_modules
        if stats_show_node_name is not None:
            self.stats_show_node_name = stats_show_node_name
        if stats_uri_prefix is not None:
            self.stats_uri_prefix = stats_uri_prefix

    @property
    def stats_admin(self):
        """Gets the stats_admin of this StatsOptions.  # noqa: E501


        :return: The stats_admin of this StatsOptions.  # noqa: E501
        :rtype: bool
        """
        return self._stats_admin

    @stats_admin.setter
    def stats_admin(self, stats_admin):
        """Sets the stats_admin of this StatsOptions.


        :param stats_admin: The stats_admin of this StatsOptions.  # noqa: E501
        :type: bool
        """

        self._stats_admin = stats_admin

    @property
    def stats_admin_cond(self):
        """Gets the stats_admin_cond of this StatsOptions.  # noqa: E501


        :return: The stats_admin_cond of this StatsOptions.  # noqa: E501
        :rtype: str
        """
        return self._stats_admin_cond

    @stats_admin_cond.setter
    def stats_admin_cond(self, stats_admin_cond):
        """Sets the stats_admin_cond of this StatsOptions.


        :param stats_admin_cond: The stats_admin_cond of this StatsOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["if", "unless"]  # noqa: E501
        if stats_admin_cond not in allowed_values:
            raise ValueError(
                "Invalid value for `stats_admin_cond` ({0}), must be one of {1}"  # noqa: E501
                .format(stats_admin_cond, allowed_values)
            )

        self._stats_admin_cond = stats_admin_cond

    @property
    def stats_admin_cond_test(self):
        """Gets the stats_admin_cond_test of this StatsOptions.  # noqa: E501


        :return: The stats_admin_cond_test of this StatsOptions.  # noqa: E501
        :rtype: str
        """
        return self._stats_admin_cond_test

    @stats_admin_cond_test.setter
    def stats_admin_cond_test(self, stats_admin_cond_test):
        """Sets the stats_admin_cond_test of this StatsOptions.


        :param stats_admin_cond_test: The stats_admin_cond_test of this StatsOptions.  # noqa: E501
        :type: str
        """

        self._stats_admin_cond_test = stats_admin_cond_test

    @property
    def stats_auths(self):
        """Gets the stats_auths of this StatsOptions.  # noqa: E501


        :return: The stats_auths of this StatsOptions.  # noqa: E501
        :rtype: list[StatsAuth]
        """
        return self._stats_auths

    @stats_auths.setter
    def stats_auths(self, stats_auths):
        """Sets the stats_auths of this StatsOptions.


        :param stats_auths: The stats_auths of this StatsOptions.  # noqa: E501
        :type: list[StatsAuth]
        """

        self._stats_auths = stats_auths

    @property
    def stats_enable(self):
        """Gets the stats_enable of this StatsOptions.  # noqa: E501


        :return: The stats_enable of this StatsOptions.  # noqa: E501
        :rtype: bool
        """
        return self._stats_enable

    @stats_enable.setter
    def stats_enable(self, stats_enable):
        """Sets the stats_enable of this StatsOptions.


        :param stats_enable: The stats_enable of this StatsOptions.  # noqa: E501
        :type: bool
        """

        self._stats_enable = stats_enable

    @property
    def stats_hide_version(self):
        """Gets the stats_hide_version of this StatsOptions.  # noqa: E501


        :return: The stats_hide_version of this StatsOptions.  # noqa: E501
        :rtype: bool
        """
        return self._stats_hide_version

    @stats_hide_version.setter
    def stats_hide_version(self, stats_hide_version):
        """Sets the stats_hide_version of this StatsOptions.


        :param stats_hide_version: The stats_hide_version of this StatsOptions.  # noqa: E501
        :type: bool
        """

        self._stats_hide_version = stats_hide_version

    @property
    def stats_http_requests(self):
        """Gets the stats_http_requests of this StatsOptions.  # noqa: E501


        :return: The stats_http_requests of this StatsOptions.  # noqa: E501
        :rtype: list[StatsHttpRequest]
        """
        return self._stats_http_requests

    @stats_http_requests.setter
    def stats_http_requests(self, stats_http_requests):
        """Sets the stats_http_requests of this StatsOptions.


        :param stats_http_requests: The stats_http_requests of this StatsOptions.  # noqa: E501
        :type: list[StatsHttpRequest]
        """

        self._stats_http_requests = stats_http_requests

    @property
    def stats_maxconn(self):
        """Gets the stats_maxconn of this StatsOptions.  # noqa: E501


        :return: The stats_maxconn of this StatsOptions.  # noqa: E501
        :rtype: int
        """
        return self._stats_maxconn

    @stats_maxconn.setter
    def stats_maxconn(self, stats_maxconn):
        """Sets the stats_maxconn of this StatsOptions.


        :param stats_maxconn: The stats_maxconn of this StatsOptions.  # noqa: E501
        :type: int
        """

        self._stats_maxconn = stats_maxconn

    @property
    def stats_realm(self):
        """Gets the stats_realm of this StatsOptions.  # noqa: E501


        :return: The stats_realm of this StatsOptions.  # noqa: E501
        :rtype: bool
        """
        return self._stats_realm

    @stats_realm.setter
    def stats_realm(self, stats_realm):
        """Sets the stats_realm of this StatsOptions.


        :param stats_realm: The stats_realm of this StatsOptions.  # noqa: E501
        :type: bool
        """

        self._stats_realm = stats_realm

    @property
    def stats_realm_realm(self):
        """Gets the stats_realm_realm of this StatsOptions.  # noqa: E501


        :return: The stats_realm_realm of this StatsOptions.  # noqa: E501
        :rtype: str
        """
        return self._stats_realm_realm

    @stats_realm_realm.setter
    def stats_realm_realm(self, stats_realm_realm):
        """Sets the stats_realm_realm of this StatsOptions.


        :param stats_realm_realm: The stats_realm_realm of this StatsOptions.  # noqa: E501
        :type: str
        """

        self._stats_realm_realm = stats_realm_realm

    @property
    def stats_refresh_delay(self):
        """Gets the stats_refresh_delay of this StatsOptions.  # noqa: E501


        :return: The stats_refresh_delay of this StatsOptions.  # noqa: E501
        :rtype: int
        """
        return self._stats_refresh_delay

    @stats_refresh_delay.setter
    def stats_refresh_delay(self, stats_refresh_delay):
        """Sets the stats_refresh_delay of this StatsOptions.


        :param stats_refresh_delay: The stats_refresh_delay of this StatsOptions.  # noqa: E501
        :type: int
        """

        self._stats_refresh_delay = stats_refresh_delay

    @property
    def stats_show_desc(self):
        """Gets the stats_show_desc of this StatsOptions.  # noqa: E501


        :return: The stats_show_desc of this StatsOptions.  # noqa: E501
        :rtype: str
        """
        return self._stats_show_desc

    @stats_show_desc.setter
    def stats_show_desc(self, stats_show_desc):
        """Sets the stats_show_desc of this StatsOptions.


        :param stats_show_desc: The stats_show_desc of this StatsOptions.  # noqa: E501
        :type: str
        """

        self._stats_show_desc = stats_show_desc

    @property
    def stats_show_legends(self):
        """Gets the stats_show_legends of this StatsOptions.  # noqa: E501


        :return: The stats_show_legends of this StatsOptions.  # noqa: E501
        :rtype: bool
        """
        return self._stats_show_legends

    @stats_show_legends.setter
    def stats_show_legends(self, stats_show_legends):
        """Sets the stats_show_legends of this StatsOptions.


        :param stats_show_legends: The stats_show_legends of this StatsOptions.  # noqa: E501
        :type: bool
        """

        self._stats_show_legends = stats_show_legends

    @property
    def stats_show_modules(self):
        """Gets the stats_show_modules of this StatsOptions.  # noqa: E501


        :return: The stats_show_modules of this StatsOptions.  # noqa: E501
        :rtype: bool
        """
        return self._stats_show_modules

    @stats_show_modules.setter
    def stats_show_modules(self, stats_show_modules):
        """Sets the stats_show_modules of this StatsOptions.


        :param stats_show_modules: The stats_show_modules of this StatsOptions.  # noqa: E501
        :type: bool
        """

        self._stats_show_modules = stats_show_modules

    @property
    def stats_show_node_name(self):
        """Gets the stats_show_node_name of this StatsOptions.  # noqa: E501


        :return: The stats_show_node_name of this StatsOptions.  # noqa: E501
        :rtype: str
        """
        return self._stats_show_node_name

    @stats_show_node_name.setter
    def stats_show_node_name(self, stats_show_node_name):
        """Sets the stats_show_node_name of this StatsOptions.


        :param stats_show_node_name: The stats_show_node_name of this StatsOptions.  # noqa: E501
        :type: str
        """

        self._stats_show_node_name = stats_show_node_name

    @property
    def stats_uri_prefix(self):
        """Gets the stats_uri_prefix of this StatsOptions.  # noqa: E501


        :return: The stats_uri_prefix of this StatsOptions.  # noqa: E501
        :rtype: str
        """
        return self._stats_uri_prefix

    @stats_uri_prefix.setter
    def stats_uri_prefix(self, stats_uri_prefix):
        """Sets the stats_uri_prefix of this StatsOptions.


        :param stats_uri_prefix: The stats_uri_prefix of this StatsOptions.  # noqa: E501
        :type: str
        """

        self._stats_uri_prefix = stats_uri_prefix

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(StatsOptions, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StatsOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other