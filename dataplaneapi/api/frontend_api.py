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


class FrontendApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_frontend(self, body, **kwargs):  # noqa: E501
        """Add a frontend  # noqa: E501

        Adds a new frontend to the configuration file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_frontend(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Frontend body: (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: Frontend
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_frontend_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_frontend_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_frontend_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add a frontend  # noqa: E501

        Adds a new frontend to the configuration file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_frontend_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Frontend body: (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: Frontend
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'transaction_id', 'version', 'force_reload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_frontend" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_frontend`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
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
            '/services/haproxy/configuration/frontends', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Frontend',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_frontend(self, name, **kwargs):  # noqa: E501
        """Delete a frontend  # noqa: E501

        Deletes a frontend from the configuration by it's name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_frontend(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Frontend name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_frontend_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_frontend_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def delete_frontend_with_http_info(self, name, **kwargs):  # noqa: E501
        """Delete a frontend  # noqa: E501

        Deletes a frontend from the configuration by it's name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_frontend_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Frontend name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'transaction_id', 'version', 'force_reload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_frontend" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `delete_frontend`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []
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
            '/services/haproxy/configuration/frontends/{name}', 'DELETE',
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

    def get_frontend(self, name, **kwargs):  # noqa: E501
        """Return a frontend  # noqa: E501

        Returns one frontend configuration by it's name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_frontend(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Frontend name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :return: InlineResponse20024
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_frontend_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_frontend_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def get_frontend_with_http_info(self, name, **kwargs):  # noqa: E501
        """Return a frontend  # noqa: E501

        Returns one frontend configuration by it's name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_frontend_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Frontend name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :return: InlineResponse20024
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'transaction_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_frontend" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_frontend`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

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
            '/services/haproxy/configuration/frontends/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20024',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_frontends(self, **kwargs):  # noqa: E501
        """Return an array of frontends  # noqa: E501

        Returns an array of all configured frontends.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_frontends(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :return: InlineResponse20023
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_frontends_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_frontends_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_frontends_with_http_info(self, **kwargs):  # noqa: E501
        """Return an array of frontends  # noqa: E501

        Returns an array of all configured frontends.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_frontends_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :return: InlineResponse20023
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
                    " to method get_frontends" % key
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
            '/services/haproxy/configuration/frontends', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20023',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def replace_frontend(self, body, name, **kwargs):  # noqa: E501
        """Replace a frontend  # noqa: E501

        Replaces a frontend configuration by it's name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.replace_frontend(body, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Frontend body: (required)
        :param str name: Frontend name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: Frontend
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.replace_frontend_with_http_info(body, name, **kwargs)  # noqa: E501
        else:
            (data) = self.replace_frontend_with_http_info(body, name, **kwargs)  # noqa: E501
            return data

    def replace_frontend_with_http_info(self, body, name, **kwargs):  # noqa: E501
        """Replace a frontend  # noqa: E501

        Replaces a frontend configuration by it's name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.replace_frontend_with_http_info(body, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Frontend body: (required)
        :param str name: Frontend name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: Frontend
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'name', 'transaction_id', 'version', 'force_reload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method replace_frontend" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `replace_frontend`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `replace_frontend`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []
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
            '/services/haproxy/configuration/frontends/{name}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Frontend',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
