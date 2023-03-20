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

class BackendSwitchingRule(object):
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
        'cond': 'str',
        'cond_test': 'str',
        'index': 'int',
        'name': 'str'
    }

    attribute_map = {
        'cond': 'cond',
        'cond_test': 'cond_test',
        'index': 'index',
        'name': 'name'
    }

    def __init__(self, cond=None, cond_test=None, index=None, name=None):  # noqa: E501
        """BackendSwitchingRule - a model defined in Swagger"""  # noqa: E501
        self._cond = None
        self._cond_test = None
        self._index = None
        self._name = None
        self.discriminator = None
        if cond is not None:
            self.cond = cond
        if cond_test is not None:
            self.cond_test = cond_test
        self.index = index
        self.name = name

    @property
    def cond(self):
        """Gets the cond of this BackendSwitchingRule.  # noqa: E501


        :return: The cond of this BackendSwitchingRule.  # noqa: E501
        :rtype: str
        """
        return self._cond

    @cond.setter
    def cond(self, cond):
        """Sets the cond of this BackendSwitchingRule.


        :param cond: The cond of this BackendSwitchingRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["if", "unless"]  # noqa: E501
        if cond not in allowed_values:
            raise ValueError(
                "Invalid value for `cond` ({0}), must be one of {1}"  # noqa: E501
                .format(cond, allowed_values)
            )

        self._cond = cond

    @property
    def cond_test(self):
        """Gets the cond_test of this BackendSwitchingRule.  # noqa: E501


        :return: The cond_test of this BackendSwitchingRule.  # noqa: E501
        :rtype: str
        """
        return self._cond_test

    @cond_test.setter
    def cond_test(self, cond_test):
        """Sets the cond_test of this BackendSwitchingRule.


        :param cond_test: The cond_test of this BackendSwitchingRule.  # noqa: E501
        :type: str
        """

        self._cond_test = cond_test

    @property
    def index(self):
        """Gets the index of this BackendSwitchingRule.  # noqa: E501


        :return: The index of this BackendSwitchingRule.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this BackendSwitchingRule.


        :param index: The index of this BackendSwitchingRule.  # noqa: E501
        :type: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def name(self):
        """Gets the name of this BackendSwitchingRule.  # noqa: E501


        :return: The name of this BackendSwitchingRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BackendSwitchingRule.


        :param name: The name of this BackendSwitchingRule.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(BackendSwitchingRule, dict):
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
        if not isinstance(other, BackendSwitchingRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
