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

class RuntimeStickTableEntriesBody(object):
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
        'data_type': 'StickTableEntry',
        'key': 'str'
    }

    attribute_map = {
        'data_type': 'data_type',
        'key': 'key'
    }

    def __init__(self, data_type=None, key=None):  # noqa: E501
        """RuntimeStickTableEntriesBody - a model defined in Swagger"""  # noqa: E501
        self._data_type = None
        self._key = None
        self.discriminator = None
        self.data_type = data_type
        self.key = key

    @property
    def data_type(self):
        """Gets the data_type of this RuntimeStickTableEntriesBody.  # noqa: E501


        :return: The data_type of this RuntimeStickTableEntriesBody.  # noqa: E501
        :rtype: StickTableEntry
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this RuntimeStickTableEntriesBody.


        :param data_type: The data_type of this RuntimeStickTableEntriesBody.  # noqa: E501
        :type: StickTableEntry
        """
        if data_type is None:
            raise ValueError("Invalid value for `data_type`, must not be `None`")  # noqa: E501

        self._data_type = data_type

    @property
    def key(self):
        """Gets the key of this RuntimeStickTableEntriesBody.  # noqa: E501


        :return: The key of this RuntimeStickTableEntriesBody.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this RuntimeStickTableEntriesBody.


        :param key: The key of this RuntimeStickTableEntriesBody.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

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
        if issubclass(RuntimeStickTableEntriesBody, dict):
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
        if not isinstance(other, RuntimeStickTableEntriesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
