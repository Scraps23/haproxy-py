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

class GlobalDeviceAtlasOptions(object):
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
        'json_file': 'str',
        'log_level': 'str',
        'properties_cookie': 'str',
        'separator': 'str'
    }

    attribute_map = {
        'json_file': 'json_file',
        'log_level': 'log_level',
        'properties_cookie': 'properties_cookie',
        'separator': 'separator'
    }

    def __init__(self, json_file=None, log_level=None, properties_cookie=None, separator=None):  # noqa: E501
        """GlobalDeviceAtlasOptions - a model defined in Swagger"""  # noqa: E501
        self._json_file = None
        self._log_level = None
        self._properties_cookie = None
        self._separator = None
        self.discriminator = None
        if json_file is not None:
            self.json_file = json_file
        if log_level is not None:
            self.log_level = log_level
        if properties_cookie is not None:
            self.properties_cookie = properties_cookie
        if separator is not None:
            self.separator = separator

    @property
    def json_file(self):
        """Gets the json_file of this GlobalDeviceAtlasOptions.  # noqa: E501


        :return: The json_file of this GlobalDeviceAtlasOptions.  # noqa: E501
        :rtype: str
        """
        return self._json_file

    @json_file.setter
    def json_file(self, json_file):
        """Sets the json_file of this GlobalDeviceAtlasOptions.


        :param json_file: The json_file of this GlobalDeviceAtlasOptions.  # noqa: E501
        :type: str
        """

        self._json_file = json_file

    @property
    def log_level(self):
        """Gets the log_level of this GlobalDeviceAtlasOptions.  # noqa: E501


        :return: The log_level of this GlobalDeviceAtlasOptions.  # noqa: E501
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """Sets the log_level of this GlobalDeviceAtlasOptions.


        :param log_level: The log_level of this GlobalDeviceAtlasOptions.  # noqa: E501
        :type: str
        """

        self._log_level = log_level

    @property
    def properties_cookie(self):
        """Gets the properties_cookie of this GlobalDeviceAtlasOptions.  # noqa: E501


        :return: The properties_cookie of this GlobalDeviceAtlasOptions.  # noqa: E501
        :rtype: str
        """
        return self._properties_cookie

    @properties_cookie.setter
    def properties_cookie(self, properties_cookie):
        """Sets the properties_cookie of this GlobalDeviceAtlasOptions.


        :param properties_cookie: The properties_cookie of this GlobalDeviceAtlasOptions.  # noqa: E501
        :type: str
        """

        self._properties_cookie = properties_cookie

    @property
    def separator(self):
        """Gets the separator of this GlobalDeviceAtlasOptions.  # noqa: E501


        :return: The separator of this GlobalDeviceAtlasOptions.  # noqa: E501
        :rtype: str
        """
        return self._separator

    @separator.setter
    def separator(self, separator):
        """Sets the separator of this GlobalDeviceAtlasOptions.


        :param separator: The separator of this GlobalDeviceAtlasOptions.  # noqa: E501
        :type: str
        """

        self._separator = separator

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
        if issubclass(GlobalDeviceAtlasOptions, dict):
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
        if not isinstance(other, GlobalDeviceAtlasOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
