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

class SslCertEntry(object):
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
        'algorithm': 'str',
        'chain_issuer': 'str',
        'chain_subject': 'str',
        'issuer': 'str',
        'not_after': 'date',
        'not_before': 'date',
        'serial': 'str',
        'sha1_finger_print': 'str',
        'status': 'str',
        'storage_name': 'str',
        'subject': 'str',
        'subject_alternative_names': 'list[str]'
    }

    attribute_map = {
        'algorithm': 'algorithm',
        'chain_issuer': 'chain_issuer',
        'chain_subject': 'chain_subject',
        'issuer': 'issuer',
        'not_after': 'not_after',
        'not_before': 'not_before',
        'serial': 'serial',
        'sha1_finger_print': 'sha1_finger_print',
        'status': 'status',
        'storage_name': 'storage_name',
        'subject': 'subject',
        'subject_alternative_names': 'subject_alternative_names'
    }

    def __init__(self, algorithm=None, chain_issuer=None, chain_subject=None, issuer=None, not_after=None, not_before=None, serial=None, sha1_finger_print=None, status=None, storage_name=None, subject=None, subject_alternative_names=None):  # noqa: E501
        """SslCertEntry - a model defined in Swagger"""  # noqa: E501
        self._algorithm = None
        self._chain_issuer = None
        self._chain_subject = None
        self._issuer = None
        self._not_after = None
        self._not_before = None
        self._serial = None
        self._sha1_finger_print = None
        self._status = None
        self._storage_name = None
        self._subject = None
        self._subject_alternative_names = None
        self.discriminator = None
        if algorithm is not None:
            self.algorithm = algorithm
        if chain_issuer is not None:
            self.chain_issuer = chain_issuer
        if chain_subject is not None:
            self.chain_subject = chain_subject
        if issuer is not None:
            self.issuer = issuer
        if not_after is not None:
            self.not_after = not_after
        if not_before is not None:
            self.not_before = not_before
        if serial is not None:
            self.serial = serial
        if sha1_finger_print is not None:
            self.sha1_finger_print = sha1_finger_print
        if status is not None:
            self.status = status
        if storage_name is not None:
            self.storage_name = storage_name
        if subject is not None:
            self.subject = subject
        if subject_alternative_names is not None:
            self.subject_alternative_names = subject_alternative_names

    @property
    def algorithm(self):
        """Gets the algorithm of this SslCertEntry.  # noqa: E501


        :return: The algorithm of this SslCertEntry.  # noqa: E501
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this SslCertEntry.


        :param algorithm: The algorithm of this SslCertEntry.  # noqa: E501
        :type: str
        """

        self._algorithm = algorithm

    @property
    def chain_issuer(self):
        """Gets the chain_issuer of this SslCertEntry.  # noqa: E501


        :return: The chain_issuer of this SslCertEntry.  # noqa: E501
        :rtype: str
        """
        return self._chain_issuer

    @chain_issuer.setter
    def chain_issuer(self, chain_issuer):
        """Sets the chain_issuer of this SslCertEntry.


        :param chain_issuer: The chain_issuer of this SslCertEntry.  # noqa: E501
        :type: str
        """

        self._chain_issuer = chain_issuer

    @property
    def chain_subject(self):
        """Gets the chain_subject of this SslCertEntry.  # noqa: E501


        :return: The chain_subject of this SslCertEntry.  # noqa: E501
        :rtype: str
        """
        return self._chain_subject

    @chain_subject.setter
    def chain_subject(self, chain_subject):
        """Sets the chain_subject of this SslCertEntry.


        :param chain_subject: The chain_subject of this SslCertEntry.  # noqa: E501
        :type: str
        """

        self._chain_subject = chain_subject

    @property
    def issuer(self):
        """Gets the issuer of this SslCertEntry.  # noqa: E501


        :return: The issuer of this SslCertEntry.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this SslCertEntry.


        :param issuer: The issuer of this SslCertEntry.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def not_after(self):
        """Gets the not_after of this SslCertEntry.  # noqa: E501


        :return: The not_after of this SslCertEntry.  # noqa: E501
        :rtype: date
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        """Sets the not_after of this SslCertEntry.


        :param not_after: The not_after of this SslCertEntry.  # noqa: E501
        :type: date
        """

        self._not_after = not_after

    @property
    def not_before(self):
        """Gets the not_before of this SslCertEntry.  # noqa: E501


        :return: The not_before of this SslCertEntry.  # noqa: E501
        :rtype: date
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        """Sets the not_before of this SslCertEntry.


        :param not_before: The not_before of this SslCertEntry.  # noqa: E501
        :type: date
        """

        self._not_before = not_before

    @property
    def serial(self):
        """Gets the serial of this SslCertEntry.  # noqa: E501


        :return: The serial of this SslCertEntry.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this SslCertEntry.


        :param serial: The serial of this SslCertEntry.  # noqa: E501
        :type: str
        """

        self._serial = serial

    @property
    def sha1_finger_print(self):
        """Gets the sha1_finger_print of this SslCertEntry.  # noqa: E501


        :return: The sha1_finger_print of this SslCertEntry.  # noqa: E501
        :rtype: str
        """
        return self._sha1_finger_print

    @sha1_finger_print.setter
    def sha1_finger_print(self, sha1_finger_print):
        """Sets the sha1_finger_print of this SslCertEntry.


        :param sha1_finger_print: The sha1_finger_print of this SslCertEntry.  # noqa: E501
        :type: str
        """

        self._sha1_finger_print = sha1_finger_print

    @property
    def status(self):
        """Gets the status of this SslCertEntry.  # noqa: E501


        :return: The status of this SslCertEntry.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SslCertEntry.


        :param status: The status of this SslCertEntry.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def storage_name(self):
        """Gets the storage_name of this SslCertEntry.  # noqa: E501


        :return: The storage_name of this SslCertEntry.  # noqa: E501
        :rtype: str
        """
        return self._storage_name

    @storage_name.setter
    def storage_name(self, storage_name):
        """Sets the storage_name of this SslCertEntry.


        :param storage_name: The storage_name of this SslCertEntry.  # noqa: E501
        :type: str
        """

        self._storage_name = storage_name

    @property
    def subject(self):
        """Gets the subject of this SslCertEntry.  # noqa: E501


        :return: The subject of this SslCertEntry.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this SslCertEntry.


        :param subject: The subject of this SslCertEntry.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def subject_alternative_names(self):
        """Gets the subject_alternative_names of this SslCertEntry.  # noqa: E501


        :return: The subject_alternative_names of this SslCertEntry.  # noqa: E501
        :rtype: list[str]
        """
        return self._subject_alternative_names

    @subject_alternative_names.setter
    def subject_alternative_names(self, subject_alternative_names):
        """Sets the subject_alternative_names of this SslCertEntry.


        :param subject_alternative_names: The subject_alternative_names of this SslCertEntry.  # noqa: E501
        :type: list[str]
        """

        self._subject_alternative_names = subject_alternative_names

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
        if issubclass(SslCertEntry, dict):
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
        if not isinstance(other, SslCertEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other