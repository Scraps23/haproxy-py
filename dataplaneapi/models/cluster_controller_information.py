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

class ClusterControllerInformation(object):
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
        'api_base_path': 'str',
        'cluster_id': 'str',
        'description': 'str',
        'log_targets': 'list[ClusterControllerInformationLogTargets]',
        'name': 'str',
        'port': 'int'
    }

    attribute_map = {
        'address': 'address',
        'api_base_path': 'api_base_path',
        'cluster_id': 'cluster_id',
        'description': 'description',
        'log_targets': 'log_targets',
        'name': 'name',
        'port': 'port'
    }

    def __init__(self, address=None, api_base_path=None, cluster_id=None, description=None, log_targets=None, name=None, port=None):  # noqa: E501
        """ClusterControllerInformation - a model defined in Swagger"""  # noqa: E501
        self._address = None
        self._api_base_path = None
        self._cluster_id = None
        self._description = None
        self._log_targets = None
        self._name = None
        self._port = None
        self.discriminator = None
        if address is not None:
            self.address = address
        if api_base_path is not None:
            self.api_base_path = api_base_path
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if description is not None:
            self.description = description
        if log_targets is not None:
            self.log_targets = log_targets
        if name is not None:
            self.name = name
        if port is not None:
            self.port = port

    @property
    def address(self):
        """Gets the address of this ClusterControllerInformation.  # noqa: E501


        :return: The address of this ClusterControllerInformation.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ClusterControllerInformation.


        :param address: The address of this ClusterControllerInformation.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def api_base_path(self):
        """Gets the api_base_path of this ClusterControllerInformation.  # noqa: E501


        :return: The api_base_path of this ClusterControllerInformation.  # noqa: E501
        :rtype: str
        """
        return self._api_base_path

    @api_base_path.setter
    def api_base_path(self, api_base_path):
        """Sets the api_base_path of this ClusterControllerInformation.


        :param api_base_path: The api_base_path of this ClusterControllerInformation.  # noqa: E501
        :type: str
        """

        self._api_base_path = api_base_path

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ClusterControllerInformation.  # noqa: E501


        :return: The cluster_id of this ClusterControllerInformation.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ClusterControllerInformation.


        :param cluster_id: The cluster_id of this ClusterControllerInformation.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def description(self):
        """Gets the description of this ClusterControllerInformation.  # noqa: E501


        :return: The description of this ClusterControllerInformation.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ClusterControllerInformation.


        :param description: The description of this ClusterControllerInformation.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def log_targets(self):
        """Gets the log_targets of this ClusterControllerInformation.  # noqa: E501


        :return: The log_targets of this ClusterControllerInformation.  # noqa: E501
        :rtype: list[ClusterControllerInformationLogTargets]
        """
        return self._log_targets

    @log_targets.setter
    def log_targets(self, log_targets):
        """Sets the log_targets of this ClusterControllerInformation.


        :param log_targets: The log_targets of this ClusterControllerInformation.  # noqa: E501
        :type: list[ClusterControllerInformationLogTargets]
        """

        self._log_targets = log_targets

    @property
    def name(self):
        """Gets the name of this ClusterControllerInformation.  # noqa: E501


        :return: The name of this ClusterControllerInformation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterControllerInformation.


        :param name: The name of this ClusterControllerInformation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def port(self):
        """Gets the port of this ClusterControllerInformation.  # noqa: E501


        :return: The port of this ClusterControllerInformation.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ClusterControllerInformation.


        :param port: The port of this ClusterControllerInformation.  # noqa: E501
        :type: int
        """

        self._port = port

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
        if issubclass(ClusterControllerInformation, dict):
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
        if not isinstance(other, ClusterControllerInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
