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


class UserApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_user(self, body, userlist, **kwargs):  # noqa: E501
        """Add a new userlist user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user(body, userlist, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param User body: (required)
        :param str userlist: Parent userlist name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_user_with_http_info(body, userlist, **kwargs)  # noqa: E501
        else:
            (data) = self.create_user_with_http_info(body, userlist, **kwargs)  # noqa: E501
            return data

    def create_user_with_http_info(self, body, userlist, **kwargs):  # noqa: E501
        """Add a new userlist user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_with_http_info(body, userlist, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param User body: (required)
        :param str userlist: Parent userlist name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'userlist', 'transaction_id', 'version', 'force_reload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_user`")  # noqa: E501
        # verify the required parameter 'userlist' is set
        if ('userlist' not in params or
                params['userlist'] is None):
            raise ValueError("Missing the required parameter `userlist` when calling `create_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'userlist' in params:
            query_params.append(('userlist', params['userlist']))  # noqa: E501
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
            '/services/haproxy/configuration/users', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_user(self, username, userlist, **kwargs):  # noqa: E501
        """Delete a user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user(username, userlist, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: User username (required)
        :param str userlist: Parent userlist name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_user_with_http_info(username, userlist, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_user_with_http_info(username, userlist, **kwargs)  # noqa: E501
            return data

    def delete_user_with_http_info(self, username, userlist, **kwargs):  # noqa: E501
        """Delete a user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_with_http_info(username, userlist, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: User username (required)
        :param str userlist: Parent userlist name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'userlist', 'transaction_id', 'version', 'force_reload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params or
                params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `delete_user`")  # noqa: E501
        # verify the required parameter 'userlist' is set
        if ('userlist' not in params or
                params['userlist'] is None):
            raise ValueError("Missing the required parameter `userlist` when calling `delete_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']  # noqa: E501

        query_params = []
        if 'userlist' in params:
            query_params.append(('userlist', params['userlist']))  # noqa: E501
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
            '/services/haproxy/configuration/users/{username}', 'DELETE',
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

    def get_user(self, username, userlist, **kwargs):  # noqa: E501
        """Return one userlist user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user(username, userlist, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: User username (required)
        :param str userlist: Parent userlist name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :return: InlineResponse20079
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_with_http_info(username, userlist, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_with_http_info(username, userlist, **kwargs)  # noqa: E501
            return data

    def get_user_with_http_info(self, username, userlist, **kwargs):  # noqa: E501
        """Return one userlist user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_with_http_info(username, userlist, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: User username (required)
        :param str userlist: Parent userlist name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :return: InlineResponse20079
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'userlist', 'transaction_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params or
                params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `get_user`")  # noqa: E501
        # verify the required parameter 'userlist' is set
        if ('userlist' not in params or
                params['userlist'] is None):
            raise ValueError("Missing the required parameter `userlist` when calling `get_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']  # noqa: E501

        query_params = []
        if 'userlist' in params:
            query_params.append(('userlist', params['userlist']))  # noqa: E501
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
            '/services/haproxy/configuration/users/{username}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20079',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_users(self, userlist, **kwargs):  # noqa: E501
        """Return an array of userlist users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_users(userlist, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str userlist: Parent userlist name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :return: InlineResponse20078
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_users_with_http_info(userlist, **kwargs)  # noqa: E501
        else:
            (data) = self.get_users_with_http_info(userlist, **kwargs)  # noqa: E501
            return data

    def get_users_with_http_info(self, userlist, **kwargs):  # noqa: E501
        """Return an array of userlist users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_users_with_http_info(userlist, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str userlist: Parent userlist name (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :return: InlineResponse20078
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['userlist', 'transaction_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'userlist' is set
        if ('userlist' not in params or
                params['userlist'] is None):
            raise ValueError("Missing the required parameter `userlist` when calling `get_users`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'userlist' in params:
            query_params.append(('userlist', params['userlist']))  # noqa: E501
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
            '/services/haproxy/configuration/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20078',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def replace_user(self, body, userlist, username, **kwargs):  # noqa: E501
        """Replace a user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.replace_user(body, userlist, username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param User body: (required)
        :param str userlist: Parent userlist name (required)
        :param str username: User username (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.replace_user_with_http_info(body, userlist, username, **kwargs)  # noqa: E501
        else:
            (data) = self.replace_user_with_http_info(body, userlist, username, **kwargs)  # noqa: E501
            return data

    def replace_user_with_http_info(self, body, userlist, username, **kwargs):  # noqa: E501
        """Replace a user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.replace_user_with_http_info(body, userlist, username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param User body: (required)
        :param str userlist: Parent userlist name (required)
        :param str username: User username (required)
        :param str transaction_id: ID of the transaction where we want to add the operation. Cannot be used when version is specified.
        :param int version: Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version.
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'userlist', 'username', 'transaction_id', 'version', 'force_reload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method replace_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `replace_user`")  # noqa: E501
        # verify the required parameter 'userlist' is set
        if ('userlist' not in params or
                params['userlist'] is None):
            raise ValueError("Missing the required parameter `userlist` when calling `replace_user`")  # noqa: E501
        # verify the required parameter 'username' is set
        if ('username' not in params or
                params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `replace_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']  # noqa: E501

        query_params = []
        if 'userlist' in params:
            query_params.append(('userlist', params['userlist']))  # noqa: E501
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
            '/services/haproxy/configuration/users/{username}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
