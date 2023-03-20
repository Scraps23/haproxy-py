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


class TCPResponseRuleApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_tcp_response_rule(self, body, backend, **kwargs):  # noqa: E501
        """Add a new TCP Response Rule  # noqa: E501

        Adds a new TCP Response Rule of the specified type in the specified backend.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_tcp_response_rule(body, backend, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TcpResponseRule body: (required)
        :param str backend: Parent backend name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: TcpResponseRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_tcp_response_rule_with_http_info(body, backend, **kwargs)  # noqa: E501
        else:
            (data) = self.create_tcp_response_rule_with_http_info(body, backend, **kwargs)  # noqa: E501
            return data

    def create_tcp_response_rule_with_http_info(self, body, backend, **kwargs):  # noqa: E501
        """Add a new TCP Response Rule  # noqa: E501

        Adds a new TCP Response Rule of the specified type in the specified backend.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_tcp_response_rule_with_http_info(body, backend, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TcpResponseRule body: (required)
        :param str backend: Parent backend name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: TcpResponseRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'backend', 'transaction_id', 'version', 'force_reload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_tcp_response_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_tcp_response_rule`")  # noqa: E501
        # verify the required parameter 'backend' is set
        if ('backend' not in params or
                params['backend'] is None):
            raise ValueError("Missing the required parameter `backend` when calling `create_tcp_response_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'backend' in params:
            query_params.append(('backend', params['backend']))  # noqa: E501
        if 'transaction_id' in params:
            query_params.append(('transaction_id', params['transaction_id']))  # noqa: E501
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501
        if 'force_reload' in params:
            query_params.append(('force_reload', params['force_reload']))  # noqa: E501

        header_params = {}

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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_auth']  # noqa: E501

        return self.api_client.call_api(
            '/services/haproxy/configuration/tcp_response_rules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TcpResponseRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_tcp_response_rule(self, index, backend, **kwargs):  # noqa: E501
        """Delete a TCP Response Rule  # noqa: E501

        Deletes a TCP Response Rule configuration by it's index from the specified backend.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_tcp_response_rule(index, backend, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int index: TCP Response Rule Index (required)
        :param str backend: Parent backend name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_tcp_response_rule_with_http_info(index, backend, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_tcp_response_rule_with_http_info(index, backend, **kwargs)  # noqa: E501
            return data

    def delete_tcp_response_rule_with_http_info(self, index, backend, **kwargs):  # noqa: E501
        """Delete a TCP Response Rule  # noqa: E501

        Deletes a TCP Response Rule configuration by it's index from the specified backend.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_tcp_response_rule_with_http_info(index, backend, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int index: TCP Response Rule Index (required)
        :param str backend: Parent backend name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['index', 'backend', 'transaction_id', 'version', 'force_reload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_tcp_response_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'index' is set
        if ('index' not in params or
                params['index'] is None):
            raise ValueError("Missing the required parameter `index` when calling `delete_tcp_response_rule`")  # noqa: E501
        # verify the required parameter 'backend' is set
        if ('backend' not in params or
                params['backend'] is None):
            raise ValueError("Missing the required parameter `backend` when calling `delete_tcp_response_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'index' in params:
            path_params['index'] = params['index']  # noqa: E501

        query_params = []
        if 'backend' in params:
            query_params.append(('backend', params['backend']))  # noqa: E501
        if 'transaction_id' in params:
            query_params.append(('transaction_id', params['transaction_id']))  # noqa: E501
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501
        if 'force_reload' in params:
            query_params.append(('force_reload', params['force_reload']))  # noqa: E501

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
            '/services/haproxy/configuration/tcp_response_rules/{index}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tcp_response_rule(self, index, backend, **kwargs):  # noqa: E501
        """Return one TCP Response Rule  # noqa: E501

        Returns one TCP Response Rule configuration by it's index in the specified backend.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tcp_response_rule(index, backend, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int index: TCP Response Rule Index (required)
        :param str backend: Parent backend name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :return: InlineResponse20075
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tcp_response_rule_with_http_info(index, backend, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tcp_response_rule_with_http_info(index, backend, **kwargs)  # noqa: E501
            return data

    def get_tcp_response_rule_with_http_info(self, index, backend, **kwargs):  # noqa: E501
        """Return one TCP Response Rule  # noqa: E501

        Returns one TCP Response Rule configuration by it's index in the specified backend.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tcp_response_rule_with_http_info(index, backend, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int index: TCP Response Rule Index (required)
        :param str backend: Parent backend name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :return: InlineResponse20075
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['index', 'backend', 'transaction_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tcp_response_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'index' is set
        if ('index' not in params or
                params['index'] is None):
            raise ValueError("Missing the required parameter `index` when calling `get_tcp_response_rule`")  # noqa: E501
        # verify the required parameter 'backend' is set
        if ('backend' not in params or
                params['backend'] is None):
            raise ValueError("Missing the required parameter `backend` when calling `get_tcp_response_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'index' in params:
            path_params['index'] = params['index']  # noqa: E501

        query_params = []
        if 'backend' in params:
            query_params.append(('backend', params['backend']))  # noqa: E501
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
            '/services/haproxy/configuration/tcp_response_rules/{index}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20075',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tcp_response_rules(self, backend, **kwargs):  # noqa: E501
        """Return an array of all TCP Response Rules  # noqa: E501

        Returns all TCP Response Rules that are configured in specified backend.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tcp_response_rules(backend, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str backend: Parent backend name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :return: InlineResponse20074
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tcp_response_rules_with_http_info(backend, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tcp_response_rules_with_http_info(backend, **kwargs)  # noqa: E501
            return data

    def get_tcp_response_rules_with_http_info(self, backend, **kwargs):  # noqa: E501
        """Return an array of all TCP Response Rules  # noqa: E501

        Returns all TCP Response Rules that are configured in specified backend.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tcp_response_rules_with_http_info(backend, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str backend: Parent backend name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :return: InlineResponse20074
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['backend', 'transaction_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tcp_response_rules" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'backend' is set
        if ('backend' not in params or
                params['backend'] is None):
            raise ValueError("Missing the required parameter `backend` when calling `get_tcp_response_rules`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'backend' in params:
            query_params.append(('backend', params['backend']))  # noqa: E501
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
            '/services/haproxy/configuration/tcp_response_rules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20074',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def replace_tcp_response_rule(self, body, backend, index, **kwargs):  # noqa: E501
        """Replace a TCP Response Rule  # noqa: E501

        Replaces a TCP Response Rule configuration by it's Index in the specified backend.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.replace_tcp_response_rule(body, backend, index, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TcpResponseRule body: (required)
        :param str backend: Parent backend name (required)
        :param int index: TCP Response Rule Index (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: TcpResponseRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.replace_tcp_response_rule_with_http_info(body, backend, index, **kwargs)  # noqa: E501
        else:
            (data) = self.replace_tcp_response_rule_with_http_info(body, backend, index, **kwargs)  # noqa: E501
            return data

    def replace_tcp_response_rule_with_http_info(self, body, backend, index, **kwargs):  # noqa: E501
        """Replace a TCP Response Rule  # noqa: E501

        Replaces a TCP Response Rule configuration by it's Index in the specified backend.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.replace_tcp_response_rule_with_http_info(body, backend, index, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TcpResponseRule body: (required)
        :param str backend: Parent backend name (required)
        :param int index: TCP Response Rule Index (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: TcpResponseRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'backend', 'index', 'transaction_id', 'version', 'force_reload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method replace_tcp_response_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `replace_tcp_response_rule`")  # noqa: E501
        # verify the required parameter 'backend' is set
        if ('backend' not in params or
                params['backend'] is None):
            raise ValueError("Missing the required parameter `backend` when calling `replace_tcp_response_rule`")  # noqa: E501
        # verify the required parameter 'index' is set
        if ('index' not in params or
                params['index'] is None):
            raise ValueError("Missing the required parameter `index` when calling `replace_tcp_response_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'index' in params:
            path_params['index'] = params['index']  # noqa: E501

        query_params = []
        if 'backend' in params:
            query_params.append(('backend', params['backend']))  # noqa: E501
        if 'transaction_id' in params:
            query_params.append(('transaction_id', params['transaction_id']))  # noqa: E501
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501
        if 'force_reload' in params:
            query_params.append(('force_reload', params['force_reload']))  # noqa: E501

        header_params = {}

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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_auth']  # noqa: E501

        return self.api_client.call_api(
            '/services/haproxy/configuration/tcp_response_rules/{index}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TcpResponseRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
