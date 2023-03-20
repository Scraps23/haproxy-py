# coding: utf-8

"""
    HAProxy Data Plane API

    API for editing and managing haproxy instances. Provides process information, configuration management, haproxy stats and logs.   # noqa: E501

    OpenAPI spec version: 2.7
    Contact: support@haproxy.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from dataplaneapi.api_client import ApiClient


class ConfigurationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_configuration_version(self, **kwargs):  # noqa: E501
        """Return a configuration version  # noqa: E501

        Returns configuration version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_configuration_version(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_configuration_version_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_configuration_version_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_configuration_version_with_http_info(self, **kwargs):  # noqa: E501
        """Return a configuration version  # noqa: E501

        Returns configuration version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_configuration_version_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['transaction_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_configuration_version" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'transaction_id' in params:
            query_params.append(('transaction_id', params['transaction_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_auth']  # noqa: E501

        return self.api_client.call_api(
            '/services/haproxy/configuration/version', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_ha_proxy_configuration(self, **kwargs):  # noqa: E501
        """Return HAProxy configuration  # noqa: E501

        Returns HAProxy configuration file in plain text  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ha_proxy_configuration(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :return: InlineResponse20057
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ha_proxy_configuration_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_ha_proxy_configuration_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_ha_proxy_configuration_with_http_info(self, **kwargs):  # noqa: E501
        """Return HAProxy configuration  # noqa: E501

        Returns HAProxy configuration file in plain text  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ha_proxy_configuration_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :return: InlineResponse20057
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['transaction_id', 'version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ha_proxy_configuration" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'transaction_id' in params:
            query_params.append(('transaction_id', params['transaction_id']))  # noqa: E501
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_auth']  # noqa: E501

        return self.api_client.call_api(
            '/services/haproxy/configuration/raw', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20057',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_ha_proxy_configuration(self, body, **kwargs):  # noqa: E501
        """Push new haproxy configuration  # noqa: E501

        Push a new haproxy configuration file in plain text  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_ha_proxy_configuration(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: (required)
        :param str x_runtime_actions: List of Runtime API commands with parameters separated by ';'
        :param bool skip_version: If set, no version check will be done and the pushed config will be enforced
        :param bool skip_reload: If set, no reload will be initiated and runtime actions from X-Runtime-Actions will be applied
        :param bool only_validate: If set, only validates configuration, without applying it
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_ha_proxy_configuration_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_ha_proxy_configuration_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def post_ha_proxy_configuration_with_http_info(self, body, **kwargs):  # noqa: E501
        """Push new haproxy configuration  # noqa: E501

        Push a new haproxy configuration file in plain text  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_ha_proxy_configuration_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: (required)
        :param str x_runtime_actions: List of Runtime API commands with parameters separated by ';'
        :param bool skip_version: If set, no version check will be done and the pushed config will be enforced
        :param bool skip_reload: If set, no reload will be initiated and runtime actions from X-Runtime-Actions will be applied
        :param bool only_validate: If set, only validates configuration, without applying it
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_runtime_actions', 'skip_version', 'skip_reload', 'only_validate', 'version', 'force_reload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_ha_proxy_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_ha_proxy_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip_version' in params:
            query_params.append(('skip_version', params['skip_version']))  # noqa: E501
        if 'skip_reload' in params:
            query_params.append(('skip_reload', params['skip_reload']))  # noqa: E501
        if 'only_validate' in params:
            query_params.append(('only_validate', params['only_validate']))  # noqa: E501
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501
        if 'force_reload' in params:
            query_params.append(('force_reload', params['force_reload']))  # noqa: E501

        header_params = {}
        if 'x_runtime_actions' in params:
            header_params['X-Runtime-Actions'] = params['x_runtime_actions']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_auth']  # noqa: E501

        return self.api_client.call_api(
            '/services/haproxy/configuration/raw', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)