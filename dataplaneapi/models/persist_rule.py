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

class PersistRule(object):
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
        'rdp_cookie_name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'rdp_cookie_name': 'rdp_cookie_name',
        'type': 'type'
    }

    def __init__(self, rdp_cookie_name=None, type=None):  # noqa: E501
        """PersistRule - a model defined in Swagger"""  # noqa: E501
        self._rdp_cookie_name = None
        self._type = None
        self.discriminator = None
        if rdp_cookie_name is not None:
            self.rdp_cookie_name = rdp_cookie_name
        self.type = type

    @property
    def rdp_cookie_name(self):
        """Gets the rdp_cookie_name of this PersistRule.  # noqa: E501


        :return: The rdp_cookie_name of this PersistRule.  # noqa: E501
        :rtype: str
        """
        return self._rdp_cookie_name

    @rdp_cookie_name.setter
    def rdp_cookie_name(self, rdp_cookie_name):
        """Sets the rdp_cookie_name of this PersistRule.


        :param rdp_cookie_name: The rdp_cookie_name of this PersistRule.  # noqa: E501
        :type: str
        """

        self._rdp_cookie_name = rdp_cookie_name

    @property
    def type(self):
        """Gets the type of this PersistRule.  # noqa: E501


        :return: The type of this PersistRule.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PersistRule.


        :param type: The type of this PersistRule.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["rdp-cookie"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(PersistRule, dict):
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
        if not isinstance(other, PersistRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
