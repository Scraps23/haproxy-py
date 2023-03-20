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


class TCPRequestRuleApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_tcp_request_rule(self, body, parent_name, parent_type, **kwargs):  # noqa: E501
        """Add a new TCP Request Rule  # noqa: E501

        Adds a new TCP Request Rule of the specified type in the specified parent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_tcp_request_rule(body, parent_name, parent_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TcpRequestRule body: (required)
        :param str parent_name: Parent name (required)
        :param str parent_type: Parent type (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: TcpRequestRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_tcp_request_rule_with_http_info(body, parent_name, parent_type, **kwargs)  # noqa: E501
        else:
            (data) = self.create_tcp_request_rule_with_http_info(body, parent_name, parent_type, **kwargs)  # noqa: E501
            return data

    def create_tcp_request_rule_with_http_info(self, body, parent_name, parent_type, **kwargs):  # noqa: E501
        """Add a new TCP Request Rule  # noqa: E501

        Adds a new TCP Request Rule of the specified type in the specified parent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_tcp_request_rule_with_http_info(body, parent_name, parent_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TcpRequestRule body: (required)
        :param str parent_name: Parent name (required)
        :param str parent_type: Parent type (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: TcpRequestRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'parent_name', 'parent_type', 'transaction_id', 'version', 'force_reload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_tcp_request_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_tcp_request_rule`")  # noqa: E501
        # verify the required parameter 'parent_name' is set
        if ('parent_name' not in params or
                params['parent_name'] is None):
            raise ValueError("Missing the required parameter `parent_name` when calling `create_tcp_request_rule`")  # noqa: E501
        # verify the required parameter 'parent_type' is set
        if ('parent_type' not in params or
                params['parent_type'] is None):
            raise ValueError("Missing the required parameter `parent_type` when calling `create_tcp_request_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'parent_name' in params:
            query_params.append(('parent_name', params['parent_name']))  # noqa: E501
        if 'parent_type' in params:
            query_params.append(('parent_type', params['parent_type']))  # noqa: E501
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
            '/services/haproxy/configuration/tcp_request_rules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TcpRequestRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_tcp_request_rule(self, index, parent_name, parent_type, **kwargs):  # noqa: E501
        """Delete a TCP Request Rule  # noqa: E501

        Deletes a TCP Request Rule configuration by it's index from the specified parent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_tcp_request_rule(index, parent_name, parent_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int index: TCP Request Rule Index (required)
        :param str parent_name: Parent name (required)
        :param str parent_type: Parent type (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_tcp_request_rule_with_http_info(index, parent_name, parent_type, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_tcp_request_rule_with_http_info(index, parent_name, parent_type, **kwargs)  # noqa: E501
            return data

    def delete_tcp_request_rule_with_http_info(self, index, parent_name, parent_type, **kwargs):  # noqa: E501
        """Delete a TCP Request Rule  # noqa: E501

        Deletes a TCP Request Rule configuration by it's index from the specified parent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_tcp_request_rule_with_http_info(index, parent_name, parent_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int index: TCP Request Rule Index (required)
        :param str parent_name: Parent name (required)
        :param str parent_type: Parent type (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['index', 'parent_name', 'parent_type', 'transaction_id', 'version', 'force_reload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_tcp_request_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'index' is set
        if ('index' not in params or
                params['index'] is None):
            raise ValueError("Missing the required parameter `index` when calling `delete_tcp_request_rule`")  # noqa: E501
        # verify the required parameter 'parent_name' is set
        if ('parent_name' not in params or
                params['parent_name'] is None):
            raise ValueError("Missing the required parameter `parent_name` when calling `delete_tcp_request_rule`")  # noqa: E501
        # verify the required parameter 'parent_type' is set
        if ('parent_type' not in params or
                params['parent_type'] is None):
            raise ValueError("Missing the required parameter `parent_type` when calling `delete_tcp_request_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'index' in params:
            path_params['index'] = params['index']  # noqa: E501

        query_params = []
        if 'parent_name' in params:
            query_params.append(('parent_name', params['parent_name']))  # noqa: E501
        if 'parent_type' in params:
            query_params.append(('parent_type', params['parent_type']))  # noqa: E501
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
            '/services/haproxy/configuration/tcp_request_rules/{index}', 'DELETE',
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

    def get_tcp_request_rule(self, index, parent_name, parent_type, **kwargs):  # noqa: E501
        """Return one TCP Request Rule  # noqa: E501

        Returns one TCP Request Rule configuration by it's index in the specified parent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tcp_request_rule(index, parent_name, parent_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int index: TCP Request Rule Index (required)
        :param str parent_name: Parent name (required)
        :param str parent_type: Parent type (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :return: InlineResponse20073
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tcp_request_rule_with_http_info(index, parent_name, parent_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tcp_request_rule_with_http_info(index, parent_name, parent_type, **kwargs)  # noqa: E501
            return data

    def get_tcp_request_rule_with_http_info(self, index, parent_name, parent_type, **kwargs):  # noqa: E501
        """Return one TCP Request Rule  # noqa: E501

        Returns one TCP Request Rule configuration by it's index in the specified parent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tcp_request_rule_with_http_info(index, parent_name, parent_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int index: TCP Request Rule Index (required)
        :param str parent_name: Parent name (required)
        :param str parent_type: Parent type (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :return: InlineResponse20073
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['index', 'parent_name', 'parent_type', 'transaction_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tcp_request_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'index' is set
        if ('index' not in params or
                params['index'] is None):
            raise ValueError("Missing the required parameter `index` when calling `get_tcp_request_rule`")  # noqa: E501
        # verify the required parameter 'parent_name' is set
        if ('parent_name' not in params or
                params['parent_name'] is None):
            raise ValueError("Missing the required parameter `parent_name` when calling `get_tcp_request_rule`")  # noqa: E501
        # verify the required parameter 'parent_type' is set
        if ('parent_type' not in params or
                params['parent_type'] is None):
            raise ValueError("Missing the required parameter `parent_type` when calling `get_tcp_request_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'index' in params:
            path_params['index'] = params['index']  # noqa: E501

        query_params = []
        if 'parent_name' in params:
            query_params.append(('parent_name', params['parent_name']))  # noqa: E501
        if 'parent_type' in params:
            query_params.append(('parent_type', params['parent_type']))  # noqa: E501
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
            '/services/haproxy/configuration/tcp_request_rules/{index}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20073',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tcp_request_rules(self, parent_name, parent_type, **kwargs):  # noqa: E501
        """Return an array of all TCP Request Rules  # noqa: E501

        Returns all TCP Request Rules that are configured in specified parent and parent type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tcp_request_rules(parent_name, parent_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str parent_name: Parent name (required)
        :param str parent_type: Parent type (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :return: InlineResponse20072
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tcp_request_rules_with_http_info(parent_name, parent_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tcp_request_rules_with_http_info(parent_name, parent_type, **kwargs)  # noqa: E501
            return data

    def get_tcp_request_rules_with_http_info(self, parent_name, parent_type, **kwargs):  # noqa: E501
        """Return an array of all TCP Request Rules  # noqa: E501

        Returns all TCP Request Rules that are configured in specified parent and parent type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tcp_request_rules_with_http_info(parent_name, parent_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str parent_name: Parent name (required)
        :param str parent_type: Parent type (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :return: InlineResponse20072
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['parent_name', 'parent_type', 'transaction_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tcp_request_rules" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'parent_name' is set
        if ('parent_name' not in params or
                params['parent_name'] is None):
            raise ValueError("Missing the required parameter `parent_name` when calling `get_tcp_request_rules`")  # noqa: E501
        # verify the required parameter 'parent_type' is set
        if ('parent_type' not in params or
                params['parent_type'] is None):
            raise ValueError("Missing the required parameter `parent_type` when calling `get_tcp_request_rules`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'parent_name' in params:
            query_params.append(('parent_name', params['parent_name']))  # noqa: E501
        if 'parent_type' in params:
            query_params.append(('parent_type', params['parent_type']))  # noqa: E501
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
            '/services/haproxy/configuration/tcp_request_rules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20072',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def replace_tcp_request_rule(self, body, parent_name, parent_type, index, **kwargs):  # noqa: E501
        """Replace a TCP Request Rule  # noqa: E501

        Replaces a TCP Request Rule configuration by it's index in the specified parent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.replace_tcp_request_rule(body, parent_name, parent_type, index, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TcpRequestRule body: (required)
        :param str parent_name: Parent name (required)
        :param str parent_type: Parent type (required)
        :param int index: TCP Request Rule Index (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: TcpRequestRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.replace_tcp_request_rule_with_http_info(body, parent_name, parent_type, index, **kwargs)  # noqa: E501
        else:
            (data) = self.replace_tcp_request_rule_with_http_info(body, parent_name, parent_type, index, **kwargs)  # noqa: E501
            return data

    def replace_tcp_request_rule_with_http_info(self, body, parent_name, parent_type, index, **kwargs):  # noqa: E501
        """Replace a TCP Request Rule  # noqa: E501

        Replaces a TCP Request Rule configuration by it's index in the specified parent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.replace_tcp_request_rule_with_http_info(body, parent_name, parent_type, index, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TcpRequestRule body: (required)
        :param str parent_name: Parent name (required)
        :param str parent_type: Parent type (required)
        :param int index: TCP Request Rule Index (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: TcpRequestRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'parent_name', 'parent_type', 'index', 'transaction_id', 'version', 'force_reload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method replace_tcp_request_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `replace_tcp_request_rule`")  # noqa: E501
        # verify the required parameter 'parent_name' is set
        if ('parent_name' not in params or
                params['parent_name'] is None):
            raise ValueError("Missing the required parameter `parent_name` when calling `replace_tcp_request_rule`")  # noqa: E501
        # verify the required parameter 'parent_type' is set
        if ('parent_type' not in params or
                params['parent_type'] is None):
            raise ValueError("Missing the required parameter `parent_type` when calling `replace_tcp_request_rule`")  # noqa: E501
        # verify the required parameter 'index' is set
        if ('index' not in params or
                params['index'] is None):
            raise ValueError("Missing the required parameter `index` when calling `replace_tcp_request_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'index' in params:
            path_params['index'] = params['index']  # noqa: E501

        query_params = []
        if 'parent_name' in params:
            query_params.append(('parent_name', params['parent_name']))  # noqa: E501
        if 'parent_type' in params:
            query_params.append(('parent_type', params['parent_type']))  # noqa: E501
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
            '/services/haproxy/configuration/tcp_request_rules/{index}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TcpRequestRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
