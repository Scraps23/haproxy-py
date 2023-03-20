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

class AclFile(object):
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
        'description': 'str',
        'id': 'str',
        'storage_name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'storage_name': 'storage_name'
    }

    def __init__(self, description=None, id=None, storage_name=None):  # noqa: E501
        """AclFile - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._id = None
        self._storage_name = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if storage_name is not None:
            self.storage_name = storage_name

    @property
    def description(self):
        """Gets the description of this AclFile.  # noqa: E501


        :return: The description of this AclFile.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AclFile.


        :param description: The description of this AclFile.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this AclFile.  # noqa: E501


        :return: The id of this AclFile.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AclFile.


        :param id: The id of this AclFile.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def storage_name(self):
        """Gets the storage_name of this AclFile.  # noqa: E501


        :return: The storage_name of this AclFile.  # noqa: E501
        :rtype: str
        """
        return self._storage_name

    @storage_name.setter
    def storage_name(self, storage_name):
        """Sets the storage_name of this AclFile.


        :param storage_name: The storage_name of this AclFile.  # noqa: E501
        :type: str
        """

        self._storage_name = storage_name

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
        if issubclass(AclFile, dict):
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
        if not isinstance(other, AclFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other