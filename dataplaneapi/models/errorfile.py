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

class Errorfile(object):
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
        'code': 'int',
        'file': 'str'
    }

    attribute_map = {
        'code': 'code',
        'file': 'file'
    }

    def __init__(self, code=None, file=None):  # noqa: E501
        """Errorfile - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._file = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if file is not None:
            self.file = file

    @property
    def code(self):
        """Gets the code of this Errorfile.  # noqa: E501


        :return: The code of this Errorfile.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Errorfile.


        :param code: The code of this Errorfile.  # noqa: E501
        :type: int
        """
        allowed_values = [200, 400, 401, 403, 404, 405, 407, 408, 410, 413, 425, 429, 500, 501, 502, 503, 504]  # noqa: E501
        if code not in allowed_values:
            raise ValueError(
                "Invalid value for `code` ({0}), must be one of {1}"  # noqa: E501
                .format(code, allowed_values)
            )

        self._code = code

    @property
    def file(self):
        """Gets the file of this Errorfile.  # noqa: E501


        :return: The file of this Errorfile.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this Errorfile.


        :param file: The file of this Errorfile.  # noqa: E501
        :type: str
        """

        self._file = file

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
        if issubclass(Errorfile, dict):
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
        if not isinstance(other, Errorfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
