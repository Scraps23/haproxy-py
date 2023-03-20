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

class DgramBind(object):
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
        'address': 'str',
        'interface': 'str',
        'name': 'str',
        'namespace': 'str',
        'port': 'int',
        'port_range_end': 'int',
        'transparent': 'bool'
    }

    attribute_map = {
        'address': 'address',
        'interface': 'interface',
        'name': 'name',
        'namespace': 'namespace',
        'port': 'port',
        'port_range_end': 'port-range-end',
        'transparent': 'transparent'
    }

    def __init__(self, address=None, interface=None, name=None, namespace=None, port=None, port_range_end=None, transparent=None):  # noqa: E501
        """DgramBind - a model defined in Swagger"""  # noqa: E501
        self._address = None
        self._interface = None
        self._name = None
        self._namespace = None
        self._port = None
        self._port_range_end = None
        self._transparent = None
        self.discriminator = None
        if address is not None:
            self.address = address
        if interface is not None:
            self.interface = interface
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if port is not None:
            self.port = port
        if port_range_end is not None:
            self.port_range_end = port_range_end
        if transparent is not None:
            self.transparent = transparent

    @property
    def address(self):
        """Gets the address of this DgramBind.  # noqa: E501


        :return: The address of this DgramBind.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this DgramBind.


        :param address: The address of this DgramBind.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def interface(self):
        """Gets the interface of this DgramBind.  # noqa: E501


        :return: The interface of this DgramBind.  # noqa: E501
        :rtype: str
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """Sets the interface of this DgramBind.


        :param interface: The interface of this DgramBind.  # noqa: E501
        :type: str
        """

        self._interface = interface

    @property
    def name(self):
        """Gets the name of this DgramBind.  # noqa: E501


        :return: The name of this DgramBind.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DgramBind.


        :param name: The name of this DgramBind.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this DgramBind.  # noqa: E501


        :return: The namespace of this DgramBind.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this DgramBind.


        :param namespace: The namespace of this DgramBind.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def port(self):
        """Gets the port of this DgramBind.  # noqa: E501


        :return: The port of this DgramBind.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this DgramBind.


        :param port: The port of this DgramBind.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def port_range_end(self):
        """Gets the port_range_end of this DgramBind.  # noqa: E501


        :return: The port_range_end of this DgramBind.  # noqa: E501
        :rtype: int
        """
        return self._port_range_end

    @port_range_end.setter
    def port_range_end(self, port_range_end):
        """Sets the port_range_end of this DgramBind.


        :param port_range_end: The port_range_end of this DgramBind.  # noqa: E501
        :type: int
        """

        self._port_range_end = port_range_end

    @property
    def transparent(self):
        """Gets the transparent of this DgramBind.  # noqa: E501


        :return: The transparent of this DgramBind.  # noqa: E501
        :rtype: bool
        """
        return self._transparent

    @transparent.setter
    def transparent(self, transparent):
        """Sets the transparent of this DgramBind.


        :param transparent: The transparent of this DgramBind.  # noqa: E501
        :type: bool
        """

        self._transparent = transparent

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
        if issubclass(DgramBind, dict):
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
        if not isinstance(other, DgramBind):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
