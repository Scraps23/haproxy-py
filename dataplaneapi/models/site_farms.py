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

class SiteFarms(object):
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
        'balance': 'Balance',
        'cond': 'str',
        'cond_test': 'str',
        'forwardfor': 'Forwardfor',
        'mode': 'str',
        'name': 'str',
        'servers': 'list[Server]',
        'use_as': 'str'
    }

    attribute_map = {
        'balance': 'balance',
        'cond': 'cond',
        'cond_test': 'cond_test',
        'forwardfor': 'forwardfor',
        'mode': 'mode',
        'name': 'name',
        'servers': 'servers',
        'use_as': 'use_as'
    }

    def __init__(self, balance=None, cond=None, cond_test=None, forwardfor=None, mode=None, name=None, servers=None, use_as=None):  # noqa: E501
        """SiteFarms - a model defined in Swagger"""  # noqa: E501
        self._balance = None
        self._cond = None
        self._cond_test = None
        self._forwardfor = None
        self._mode = None
        self._name = None
        self._servers = None
        self._use_as = None
        self.discriminator = None
        if balance is not None:
            self.balance = balance
        if cond is not None:
            self.cond = cond
        if cond_test is not None:
            self.cond_test = cond_test
        if forwardfor is not None:
            self.forwardfor = forwardfor
        if mode is not None:
            self.mode = mode
        self.name = name
        if servers is not None:
            self.servers = servers
        self.use_as = use_as

    @property
    def balance(self):
        """Gets the balance of this SiteFarms.  # noqa: E501


        :return: The balance of this SiteFarms.  # noqa: E501
        :rtype: Balance
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this SiteFarms.


        :param balance: The balance of this SiteFarms.  # noqa: E501
        :type: Balance
        """

        self._balance = balance

    @property
    def cond(self):
        """Gets the cond of this SiteFarms.  # noqa: E501


        :return: The cond of this SiteFarms.  # noqa: E501
        :rtype: str
        """
        return self._cond

    @cond.setter
    def cond(self, cond):
        """Sets the cond of this SiteFarms.


        :param cond: The cond of this SiteFarms.  # noqa: E501
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
        """Gets the cond_test of this SiteFarms.  # noqa: E501


        :return: The cond_test of this SiteFarms.  # noqa: E501
        :rtype: str
        """
        return self._cond_test

    @cond_test.setter
    def cond_test(self, cond_test):
        """Sets the cond_test of this SiteFarms.


        :param cond_test: The cond_test of this SiteFarms.  # noqa: E501
        :type: str
        """

        self._cond_test = cond_test

    @property
    def forwardfor(self):
        """Gets the forwardfor of this SiteFarms.  # noqa: E501


        :return: The forwardfor of this SiteFarms.  # noqa: E501
        :rtype: Forwardfor
        """
        return self._forwardfor

    @forwardfor.setter
    def forwardfor(self, forwardfor):
        """Sets the forwardfor of this SiteFarms.


        :param forwardfor: The forwardfor of this SiteFarms.  # noqa: E501
        :type: Forwardfor
        """

        self._forwardfor = forwardfor

    @property
    def mode(self):
        """Gets the mode of this SiteFarms.  # noqa: E501


        :return: The mode of this SiteFarms.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this SiteFarms.


        :param mode: The mode of this SiteFarms.  # noqa: E501
        :type: str
        """
        allowed_values = ["http", "tcp"]  # noqa: E501
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def name(self):
        """Gets the name of this SiteFarms.  # noqa: E501


        :return: The name of this SiteFarms.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SiteFarms.


        :param name: The name of this SiteFarms.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def servers(self):
        """Gets the servers of this SiteFarms.  # noqa: E501


        :return: The servers of this SiteFarms.  # noqa: E501
        :rtype: list[Server]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this SiteFarms.


        :param servers: The servers of this SiteFarms.  # noqa: E501
        :type: list[Server]
        """

        self._servers = servers

    @property
    def use_as(self):
        """Gets the use_as of this SiteFarms.  # noqa: E501


        :return: The use_as of this SiteFarms.  # noqa: E501
        :rtype: str
        """
        return self._use_as

    @use_as.setter
    def use_as(self, use_as):
        """Sets the use_as of this SiteFarms.


        :param use_as: The use_as of this SiteFarms.  # noqa: E501
        :type: str
        """
        if use_as is None:
            raise ValueError("Invalid value for `use_as`, must not be `None`")  # noqa: E501
        allowed_values = ["default", "conditional"]  # noqa: E501
        if use_as not in allowed_values:
            raise ValueError(
                "Invalid value for `use_as` ({0}), must be one of {1}"  # noqa: E501
                .format(use_as, allowed_values)
            )

        self._use_as = use_as

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
        if issubclass(SiteFarms, dict):
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
        if not isinstance(other, SiteFarms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
