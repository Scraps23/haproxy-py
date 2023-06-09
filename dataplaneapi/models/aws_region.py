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

class AwsRegion(object):
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
        'access_key_id': 'str',
        'allowlist': 'list[AwsFilters]',
        'denylist': 'list[AwsFilters]',
        'description': 'str',
        'enabled': 'bool',
        'id': 'str',
        'ipv4_address': 'str',
        'name': 'str',
        'region': 'str',
        'retry_timeout': 'int',
        'secret_access_key': 'str',
        'server_slots_base': 'int',
        'server_slots_growth_increment': 'int',
        'server_slots_growth_type': 'str'
    }

    attribute_map = {
        'access_key_id': 'access_key_id',
        'allowlist': 'allowlist',
        'denylist': 'denylist',
        'description': 'description',
        'enabled': 'enabled',
        'id': 'id',
        'ipv4_address': 'ipv4_address',
        'name': 'name',
        'region': 'region',
        'retry_timeout': 'retry_timeout',
        'secret_access_key': 'secret_access_key',
        'server_slots_base': 'server_slots_base',
        'server_slots_growth_increment': 'server_slots_growth_increment',
        'server_slots_growth_type': 'server_slots_growth_type'
    }

    def __init__(self, access_key_id=None, allowlist=None, denylist=None, description=None, enabled=None, id=None, ipv4_address=None, name=None, region=None, retry_timeout=None, secret_access_key=None, server_slots_base=10, server_slots_growth_increment=None, server_slots_growth_type='exponential'):  # noqa: E501
        """AwsRegion - a model defined in Swagger"""  # noqa: E501
        self._access_key_id = None
        self._allowlist = None
        self._denylist = None
        self._description = None
        self._enabled = None
        self._id = None
        self._ipv4_address = None
        self._name = None
        self._region = None
        self._retry_timeout = None
        self._secret_access_key = None
        self._server_slots_base = None
        self._server_slots_growth_increment = None
        self._server_slots_growth_type = None
        self.discriminator = None
        if access_key_id is not None:
            self.access_key_id = access_key_id
        if allowlist is not None:
            self.allowlist = allowlist
        if denylist is not None:
            self.denylist = denylist
        if description is not None:
            self.description = description
        self.enabled = enabled
        if id is not None:
            self.id = id
        self.ipv4_address = ipv4_address
        self.name = name
        self.region = region
        self.retry_timeout = retry_timeout
        if secret_access_key is not None:
            self.secret_access_key = secret_access_key
        if server_slots_base is not None:
            self.server_slots_base = server_slots_base
        if server_slots_growth_increment is not None:
            self.server_slots_growth_increment = server_slots_growth_increment
        if server_slots_growth_type is not None:
            self.server_slots_growth_type = server_slots_growth_type

    @property
    def access_key_id(self):
        """Gets the access_key_id of this AwsRegion.  # noqa: E501

        AWS Access Key ID.  # noqa: E501

        :return: The access_key_id of this AwsRegion.  # noqa: E501
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """Sets the access_key_id of this AwsRegion.

        AWS Access Key ID.  # noqa: E501

        :param access_key_id: The access_key_id of this AwsRegion.  # noqa: E501
        :type: str
        """

        self._access_key_id = access_key_id

    @property
    def allowlist(self):
        """Gets the allowlist of this AwsRegion.  # noqa: E501

        Specify the AWS filters used to filter the EC2 instances to add  # noqa: E501

        :return: The allowlist of this AwsRegion.  # noqa: E501
        :rtype: list[AwsFilters]
        """
        return self._allowlist

    @allowlist.setter
    def allowlist(self, allowlist):
        """Sets the allowlist of this AwsRegion.

        Specify the AWS filters used to filter the EC2 instances to add  # noqa: E501

        :param allowlist: The allowlist of this AwsRegion.  # noqa: E501
        :type: list[AwsFilters]
        """

        self._allowlist = allowlist

    @property
    def denylist(self):
        """Gets the denylist of this AwsRegion.  # noqa: E501

        Specify the AWS filters used to filter the EC2 instances to ignore  # noqa: E501

        :return: The denylist of this AwsRegion.  # noqa: E501
        :rtype: list[AwsFilters]
        """
        return self._denylist

    @denylist.setter
    def denylist(self, denylist):
        """Sets the denylist of this AwsRegion.

        Specify the AWS filters used to filter the EC2 instances to ignore  # noqa: E501

        :param denylist: The denylist of this AwsRegion.  # noqa: E501
        :type: list[AwsFilters]
        """

        self._denylist = denylist

    @property
    def description(self):
        """Gets the description of this AwsRegion.  # noqa: E501


        :return: The description of this AwsRegion.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AwsRegion.


        :param description: The description of this AwsRegion.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this AwsRegion.  # noqa: E501


        :return: The enabled of this AwsRegion.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AwsRegion.


        :param enabled: The enabled of this AwsRegion.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this AwsRegion.  # noqa: E501

        Auto generated ID.  # noqa: E501

        :return: The id of this AwsRegion.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AwsRegion.

        Auto generated ID.  # noqa: E501

        :param id: The id of this AwsRegion.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ipv4_address(self):
        """Gets the ipv4_address of this AwsRegion.  # noqa: E501

        Select which IPv4 address the Service Discovery has to use for the backend server entry  # noqa: E501

        :return: The ipv4_address of this AwsRegion.  # noqa: E501
        :rtype: str
        """
        return self._ipv4_address

    @ipv4_address.setter
    def ipv4_address(self, ipv4_address):
        """Sets the ipv4_address of this AwsRegion.

        Select which IPv4 address the Service Discovery has to use for the backend server entry  # noqa: E501

        :param ipv4_address: The ipv4_address of this AwsRegion.  # noqa: E501
        :type: str
        """
        if ipv4_address is None:
            raise ValueError("Invalid value for `ipv4_address`, must not be `None`")  # noqa: E501
        allowed_values = ["private", "public"]  # noqa: E501
        if ipv4_address not in allowed_values:
            raise ValueError(
                "Invalid value for `ipv4_address` ({0}), must be one of {1}"  # noqa: E501
                .format(ipv4_address, allowed_values)
            )

        self._ipv4_address = ipv4_address

    @property
    def name(self):
        """Gets the name of this AwsRegion.  # noqa: E501


        :return: The name of this AwsRegion.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AwsRegion.


        :param name: The name of this AwsRegion.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def region(self):
        """Gets the region of this AwsRegion.  # noqa: E501


        :return: The region of this AwsRegion.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AwsRegion.


        :param region: The region of this AwsRegion.  # noqa: E501
        :type: str
        """
        if region is None:
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501

        self._region = region

    @property
    def retry_timeout(self):
        """Gets the retry_timeout of this AwsRegion.  # noqa: E501

        Duration in seconds in-between data pulling requests to the AWS region  # noqa: E501

        :return: The retry_timeout of this AwsRegion.  # noqa: E501
        :rtype: int
        """
        return self._retry_timeout

    @retry_timeout.setter
    def retry_timeout(self, retry_timeout):
        """Sets the retry_timeout of this AwsRegion.

        Duration in seconds in-between data pulling requests to the AWS region  # noqa: E501

        :param retry_timeout: The retry_timeout of this AwsRegion.  # noqa: E501
        :type: int
        """
        if retry_timeout is None:
            raise ValueError("Invalid value for `retry_timeout`, must not be `None`")  # noqa: E501

        self._retry_timeout = retry_timeout

    @property
    def secret_access_key(self):
        """Gets the secret_access_key of this AwsRegion.  # noqa: E501

        AWS Secret Access Key.  # noqa: E501

        :return: The secret_access_key of this AwsRegion.  # noqa: E501
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        """Sets the secret_access_key of this AwsRegion.

        AWS Secret Access Key.  # noqa: E501

        :param secret_access_key: The secret_access_key of this AwsRegion.  # noqa: E501
        :type: str
        """

        self._secret_access_key = secret_access_key

    @property
    def server_slots_base(self):
        """Gets the server_slots_base of this AwsRegion.  # noqa: E501


        :return: The server_slots_base of this AwsRegion.  # noqa: E501
        :rtype: int
        """
        return self._server_slots_base

    @server_slots_base.setter
    def server_slots_base(self, server_slots_base):
        """Sets the server_slots_base of this AwsRegion.


        :param server_slots_base: The server_slots_base of this AwsRegion.  # noqa: E501
        :type: int
        """

        self._server_slots_base = server_slots_base

    @property
    def server_slots_growth_increment(self):
        """Gets the server_slots_growth_increment of this AwsRegion.  # noqa: E501


        :return: The server_slots_growth_increment of this AwsRegion.  # noqa: E501
        :rtype: int
        """
        return self._server_slots_growth_increment

    @server_slots_growth_increment.setter
    def server_slots_growth_increment(self, server_slots_growth_increment):
        """Sets the server_slots_growth_increment of this AwsRegion.


        :param server_slots_growth_increment: The server_slots_growth_increment of this AwsRegion.  # noqa: E501
        :type: int
        """

        self._server_slots_growth_increment = server_slots_growth_increment

    @property
    def server_slots_growth_type(self):
        """Gets the server_slots_growth_type of this AwsRegion.  # noqa: E501


        :return: The server_slots_growth_type of this AwsRegion.  # noqa: E501
        :rtype: str
        """
        return self._server_slots_growth_type

    @server_slots_growth_type.setter
    def server_slots_growth_type(self, server_slots_growth_type):
        """Sets the server_slots_growth_type of this AwsRegion.


        :param server_slots_growth_type: The server_slots_growth_type of this AwsRegion.  # noqa: E501
        :type: str
        """
        allowed_values = ["linear", "exponential"]  # noqa: E501
        if server_slots_growth_type not in allowed_values:
            raise ValueError(
                "Invalid value for `server_slots_growth_type` ({0}), must be one of {1}"  # noqa: E501
                .format(server_slots_growth_type, allowed_values)
            )

        self._server_slots_growth_type = server_slots_growth_type

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
        if issubclass(AwsRegion, dict):
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
        if not isinstance(other, AwsRegion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
