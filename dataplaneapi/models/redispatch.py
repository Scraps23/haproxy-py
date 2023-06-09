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

class Redispatch(object):
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
        'enabled': 'str',
        'interval': 'int'
    }

    attribute_map = {
        'enabled': 'enabled',
        'interval': 'interval'
    }

    def __init__(self, enabled=None, interval=None):  # noqa: E501
        """Redispatch - a model defined in Swagger"""  # noqa: E501
        self._enabled = None
        self._interval = None
        self.discriminator = None
        self.enabled = enabled
        if interval is not None:
            self.interval = interval

    @property
    def enabled(self):
        """Gets the enabled of this Redispatch.  # noqa: E501


        :return: The enabled of this Redispatch.  # noqa: E501
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Redispatch.


        :param enabled: The enabled of this Redispatch.  # noqa: E501
        :type: str
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501
        allowed_values = ["enabled", "disabled"]  # noqa: E501
        if enabled not in allowed_values:
            raise ValueError(
                "Invalid value for `enabled` ({0}), must be one of {1}"  # noqa: E501
                .format(enabled, allowed_values)
            )

        self._enabled = enabled

    @property
    def interval(self):
        """Gets the interval of this Redispatch.  # noqa: E501


        :return: The interval of this Redispatch.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this Redispatch.


        :param interval: The interval of this Redispatch.  # noqa: E501
        :type: int
        """

        self._interval = interval

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
        if issubclass(Redispatch, dict):
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
        if not isinstance(other, Redispatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
