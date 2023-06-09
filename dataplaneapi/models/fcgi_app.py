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

class FcgiApp(object):
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
        'docroot': 'str',
        'get_values': 'str',
        'index': 'str',
        'keep_conn': 'str',
        'log_stderrs': 'list[FcgiLogStderr]',
        'max_reqs': 'int',
        'mpxs_conns': 'str',
        'name': 'str',
        'pass_headers': 'list[FcgiPassHeader]',
        'path_info': 'str',
        'set_params': 'list[FcgiSetParam]'
    }

    attribute_map = {
        'docroot': 'docroot',
        'get_values': 'get_values',
        'index': 'index',
        'keep_conn': 'keep_conn',
        'log_stderrs': 'log_stderrs',
        'max_reqs': 'max_reqs',
        'mpxs_conns': 'mpxs_conns',
        'name': 'name',
        'pass_headers': 'pass_headers',
        'path_info': 'path_info',
        'set_params': 'set_params'
    }

    def __init__(self, docroot=None, get_values=None, index=None, keep_conn=None, log_stderrs=None, max_reqs=1, mpxs_conns=None, name=None, pass_headers=None, path_info=None, set_params=None):  # noqa: E501
        """FcgiApp - a model defined in Swagger"""  # noqa: E501
        self._docroot = None
        self._get_values = None
        self._index = None
        self._keep_conn = None
        self._log_stderrs = None
        self._max_reqs = None
        self._mpxs_conns = None
        self._name = None
        self._pass_headers = None
        self._path_info = None
        self._set_params = None
        self.discriminator = None
        self.docroot = docroot
        if get_values is not None:
            self.get_values = get_values
        if index is not None:
            self.index = index
        if keep_conn is not None:
            self.keep_conn = keep_conn
        if log_stderrs is not None:
            self.log_stderrs = log_stderrs
        if max_reqs is not None:
            self.max_reqs = max_reqs
        if mpxs_conns is not None:
            self.mpxs_conns = mpxs_conns
        self.name = name
        if pass_headers is not None:
            self.pass_headers = pass_headers
        if path_info is not None:
            self.path_info = path_info
        if set_params is not None:
            self.set_params = set_params

    @property
    def docroot(self):
        """Gets the docroot of this FcgiApp.  # noqa: E501

        Defines the document root on the remote host. The parameter serves to build the default value of FastCGI parameters SCRIPT_FILENAME and PATH_TRANSLATED. It is a mandatory setting.  # noqa: E501

        :return: The docroot of this FcgiApp.  # noqa: E501
        :rtype: str
        """
        return self._docroot

    @docroot.setter
    def docroot(self, docroot):
        """Sets the docroot of this FcgiApp.

        Defines the document root on the remote host. The parameter serves to build the default value of FastCGI parameters SCRIPT_FILENAME and PATH_TRANSLATED. It is a mandatory setting.  # noqa: E501

        :param docroot: The docroot of this FcgiApp.  # noqa: E501
        :type: str
        """
        if docroot is None:
            raise ValueError("Invalid value for `docroot`, must not be `None`")  # noqa: E501

        self._docroot = docroot

    @property
    def get_values(self):
        """Gets the get_values of this FcgiApp.  # noqa: E501

        Enables or disables the retrieval of variables related to connection management.  # noqa: E501

        :return: The get_values of this FcgiApp.  # noqa: E501
        :rtype: str
        """
        return self._get_values

    @get_values.setter
    def get_values(self, get_values):
        """Sets the get_values of this FcgiApp.

        Enables or disables the retrieval of variables related to connection management.  # noqa: E501

        :param get_values: The get_values of this FcgiApp.  # noqa: E501
        :type: str
        """
        allowed_values = ["enabled", "disabled"]  # noqa: E501
        if get_values not in allowed_values:
            raise ValueError(
                "Invalid value for `get_values` ({0}), must be one of {1}"  # noqa: E501
                .format(get_values, allowed_values)
            )

        self._get_values = get_values

    @property
    def index(self):
        """Gets the index of this FcgiApp.  # noqa: E501

        Defines the script name to append after a URI that ends with a slash (\"/\") to set the default value for the FastCGI parameter SCRIPT_NAME. It is an optional setting.  # noqa: E501

        :return: The index of this FcgiApp.  # noqa: E501
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this FcgiApp.

        Defines the script name to append after a URI that ends with a slash (\"/\") to set the default value for the FastCGI parameter SCRIPT_NAME. It is an optional setting.  # noqa: E501

        :param index: The index of this FcgiApp.  # noqa: E501
        :type: str
        """

        self._index = index

    @property
    def keep_conn(self):
        """Gets the keep_conn of this FcgiApp.  # noqa: E501

        Tells the FastCGI application whether or not to keep the connection open after it sends a response. If disabled, the FastCGI application closes the connection after responding to this request.  # noqa: E501

        :return: The keep_conn of this FcgiApp.  # noqa: E501
        :rtype: str
        """
        return self._keep_conn

    @keep_conn.setter
    def keep_conn(self, keep_conn):
        """Sets the keep_conn of this FcgiApp.

        Tells the FastCGI application whether or not to keep the connection open after it sends a response. If disabled, the FastCGI application closes the connection after responding to this request.  # noqa: E501

        :param keep_conn: The keep_conn of this FcgiApp.  # noqa: E501
        :type: str
        """
        allowed_values = ["enabled", "disabled"]  # noqa: E501
        if keep_conn not in allowed_values:
            raise ValueError(
                "Invalid value for `keep_conn` ({0}), must be one of {1}"  # noqa: E501
                .format(keep_conn, allowed_values)
            )

        self._keep_conn = keep_conn

    @property
    def log_stderrs(self):
        """Gets the log_stderrs of this FcgiApp.  # noqa: E501


        :return: The log_stderrs of this FcgiApp.  # noqa: E501
        :rtype: list[FcgiLogStderr]
        """
        return self._log_stderrs

    @log_stderrs.setter
    def log_stderrs(self, log_stderrs):
        """Sets the log_stderrs of this FcgiApp.


        :param log_stderrs: The log_stderrs of this FcgiApp.  # noqa: E501
        :type: list[FcgiLogStderr]
        """

        self._log_stderrs = log_stderrs

    @property
    def max_reqs(self):
        """Gets the max_reqs of this FcgiApp.  # noqa: E501

        Defines the maximum number of concurrent requests this application can accept. If the FastCGI application retrieves the variable FCGI_MAX_REQS during connection establishment, it can override this option. Furthermore, if the application does not do multiplexing, it will ignore this option.  # noqa: E501

        :return: The max_reqs of this FcgiApp.  # noqa: E501
        :rtype: int
        """
        return self._max_reqs

    @max_reqs.setter
    def max_reqs(self, max_reqs):
        """Sets the max_reqs of this FcgiApp.

        Defines the maximum number of concurrent requests this application can accept. If the FastCGI application retrieves the variable FCGI_MAX_REQS during connection establishment, it can override this option. Furthermore, if the application does not do multiplexing, it will ignore this option.  # noqa: E501

        :param max_reqs: The max_reqs of this FcgiApp.  # noqa: E501
        :type: int
        """

        self._max_reqs = max_reqs

    @property
    def mpxs_conns(self):
        """Gets the mpxs_conns of this FcgiApp.  # noqa: E501

        Enables or disables the support of connection multiplexing. If the FastCGI application retrieves the variable FCGI_MPXS_CONNS during connection establishment, it can override this option.  # noqa: E501

        :return: The mpxs_conns of this FcgiApp.  # noqa: E501
        :rtype: str
        """
        return self._mpxs_conns

    @mpxs_conns.setter
    def mpxs_conns(self, mpxs_conns):
        """Sets the mpxs_conns of this FcgiApp.

        Enables or disables the support of connection multiplexing. If the FastCGI application retrieves the variable FCGI_MPXS_CONNS during connection establishment, it can override this option.  # noqa: E501

        :param mpxs_conns: The mpxs_conns of this FcgiApp.  # noqa: E501
        :type: str
        """
        allowed_values = ["enabled", "disabled"]  # noqa: E501
        if mpxs_conns not in allowed_values:
            raise ValueError(
                "Invalid value for `mpxs_conns` ({0}), must be one of {1}"  # noqa: E501
                .format(mpxs_conns, allowed_values)
            )

        self._mpxs_conns = mpxs_conns

    @property
    def name(self):
        """Gets the name of this FcgiApp.  # noqa: E501

        Declares a FastCGI application  # noqa: E501

        :return: The name of this FcgiApp.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FcgiApp.

        Declares a FastCGI application  # noqa: E501

        :param name: The name of this FcgiApp.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def pass_headers(self):
        """Gets the pass_headers of this FcgiApp.  # noqa: E501


        :return: The pass_headers of this FcgiApp.  # noqa: E501
        :rtype: list[FcgiPassHeader]
        """
        return self._pass_headers

    @pass_headers.setter
    def pass_headers(self, pass_headers):
        """Sets the pass_headers of this FcgiApp.


        :param pass_headers: The pass_headers of this FcgiApp.  # noqa: E501
        :type: list[FcgiPassHeader]
        """

        self._pass_headers = pass_headers

    @property
    def path_info(self):
        """Gets the path_info of this FcgiApp.  # noqa: E501

        Defines a regular expression to extract the script-name and the path-info from the URI. Thus, <regex> must have two captures: the first to capture the script name, and the second to capture the path- info. If not defined, it does not perform matching on the URI, and does not fill the FastCGI parameters PATH_INFO and PATH_TRANSLATED.  # noqa: E501

        :return: The path_info of this FcgiApp.  # noqa: E501
        :rtype: str
        """
        return self._path_info

    @path_info.setter
    def path_info(self, path_info):
        """Sets the path_info of this FcgiApp.

        Defines a regular expression to extract the script-name and the path-info from the URI. Thus, <regex> must have two captures: the first to capture the script name, and the second to capture the path- info. If not defined, it does not perform matching on the URI, and does not fill the FastCGI parameters PATH_INFO and PATH_TRANSLATED.  # noqa: E501

        :param path_info: The path_info of this FcgiApp.  # noqa: E501
        :type: str
        """

        self._path_info = path_info

    @property
    def set_params(self):
        """Gets the set_params of this FcgiApp.  # noqa: E501


        :return: The set_params of this FcgiApp.  # noqa: E501
        :rtype: list[FcgiSetParam]
        """
        return self._set_params

    @set_params.setter
    def set_params(self, set_params):
        """Sets the set_params of this FcgiApp.


        :param set_params: The set_params of this FcgiApp.  # noqa: E501
        :type: list[FcgiSetParam]
        """

        self._set_params = set_params

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
        if issubclass(FcgiApp, dict):
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
        if not isinstance(other, FcgiApp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
