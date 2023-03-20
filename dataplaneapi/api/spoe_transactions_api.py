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


class SpoeTransactionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def commit_spoe_transaction(self, spoe, id, **kwargs):  # noqa: E501
        """Commit transaction  # noqa: E501

        Commit transaction, execute all operations in transaction and return msg  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.commit_spoe_transaction(spoe, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str spoe: Spoe file name (required)
        :param str id: Transaction id (required)
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: SpoeTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.commit_spoe_transaction_with_http_info(spoe, id, **kwargs)  # noqa: E501
        else:
            (data) = self.commit_spoe_transaction_with_http_info(spoe, id, **kwargs)  # noqa: E501
            return data

    def commit_spoe_transaction_with_http_info(self, spoe, id, **kwargs):  # noqa: E501
        """Commit transaction  # noqa: E501

        Commit transaction, execute all operations in transaction and return msg  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.commit_spoe_transaction_with_http_info(spoe, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str spoe: Spoe file name (required)
        :param str id: Transaction id (required)
        :param bool force_reload: If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration.
        :return: SpoeTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['spoe', 'id', 'force_reload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method commit_spoe_transaction" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'spoe' is set
        if ('spoe' not in params or
                params['spoe'] is None):
            raise ValueError("Missing the required parameter `spoe` when calling `commit_spoe_transaction`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `commit_spoe_transaction`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'spoe' in params:
            query_params.append(('spoe', params['spoe']))  # noqa: E501
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
            '/services/haproxy/spoe_transactions/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SpoeTransaction',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_spoe_transaction(self, spoe, id, **kwargs):  # noqa: E501
        """Delete a transaction  # noqa: E501

        Deletes a transaction.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_spoe_transaction(spoe, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str spoe: Spoe file name (required)
        :param str id: Transaction id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_spoe_transaction_with_http_info(spoe, id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_spoe_transaction_with_http_info(spoe, id, **kwargs)  # noqa: E501
            return data

    def delete_spoe_transaction_with_http_info(self, spoe, id, **kwargs):  # noqa: E501
        """Delete a transaction  # noqa: E501

        Deletes a transaction.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_spoe_transaction_with_http_info(spoe, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str spoe: Spoe file name (required)
        :param str id: Transaction id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['spoe', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_spoe_transaction" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'spoe' is set
        if ('spoe' not in params or
                params['spoe'] is None):
            raise ValueError("Missing the required parameter `spoe` when calling `delete_spoe_transaction`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_spoe_transaction`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'spoe' in params:
            query_params.append(('spoe', params['spoe']))  # noqa: E501

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
            '/services/haproxy/spoe_transactions/{id}', 'DELETE',
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

    def get_spoe_transaction(self, spoe, id, **kwargs):  # noqa: E501
        """Return one SPOE configuration transactions  # noqa: E501

        Returns one SPOE configuration transactions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_spoe_transaction(spoe, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str spoe: Spoe file name (required)
        :param str id: Transaction id (required)
        :return: SpoeTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_spoe_transaction_with_http_info(spoe, id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_spoe_transaction_with_http_info(spoe, id, **kwargs)  # noqa: E501
            return data

    def get_spoe_transaction_with_http_info(self, spoe, id, **kwargs):  # noqa: E501
        """Return one SPOE configuration transactions  # noqa: E501

        Returns one SPOE configuration transactions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_spoe_transaction_with_http_info(spoe, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str spoe: Spoe file name (required)
        :param str id: Transaction id (required)
        :return: SpoeTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['spoe', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_spoe_transaction" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'spoe' is set
        if ('spoe' not in params or
                params['spoe'] is None):
            raise ValueError("Missing the required parameter `spoe` when calling `get_spoe_transaction`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_spoe_transaction`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'spoe' in params:
            query_params.append(('spoe', params['spoe']))  # noqa: E501

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
            '/services/haproxy/spoe_transactions/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SpoeTransaction',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_spoe_transactions(self, spoe, **kwargs):  # noqa: E501
        """Return list of SPOE configuration transactions.  # noqa: E501

        Returns a list of SPOE configuration transactions. Transactions can be filtered by their status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_spoe_transactions(spoe, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str spoe: Spoe file name (required)
        :param str status: Filter by transaction status
        :return: SpoeTransactions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_spoe_transactions_with_http_info(spoe, **kwargs)  # noqa: E501
        else:
            (data) = self.get_spoe_transactions_with_http_info(spoe, **kwargs)  # noqa: E501
            return data

    def get_spoe_transactions_with_http_info(self, spoe, **kwargs):  # noqa: E501
        """Return list of SPOE configuration transactions.  # noqa: E501

        Returns a list of SPOE configuration transactions. Transactions can be filtered by their status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_spoe_transactions_with_http_info(spoe, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str spoe: Spoe file name (required)
        :param str status: Filter by transaction status
        :return: SpoeTransactions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['spoe', 'status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_spoe_transactions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'spoe' is set
        if ('spoe' not in params or
                params['spoe'] is None):
            raise ValueError("Missing the required parameter `spoe` when calling `get_spoe_transactions`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'spoe' in params:
            query_params.append(('spoe', params['spoe']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501

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
            '/services/haproxy/spoe_transactions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SpoeTransactions',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def start_spoe_transaction(self, spoe, version, **kwargs):  # noqa: E501
        """Start a new transaction  # noqa: E501

        Starts a new transaction and returns it's id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_spoe_transaction(spoe, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str spoe: Spoe file name (required)
        :param int version: Configuration version on which to work on (required)
        :return: SpoeTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.start_spoe_transaction_with_http_info(spoe, version, **kwargs)  # noqa: E501
        else:
            (data) = self.start_spoe_transaction_with_http_info(spoe, version, **kwargs)  # noqa: E501
            return data

    def start_spoe_transaction_with_http_info(self, spoe, version, **kwargs):  # noqa: E501
        """Start a new transaction  # noqa: E501

        Starts a new transaction and returns it's id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_spoe_transaction_with_http_info(spoe, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str spoe: Spoe file name (required)
        :param int version: Configuration version on which to work on (required)
        :return: SpoeTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['spoe', 'version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_spoe_transaction" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'spoe' is set
        if ('spoe' not in params or
                params['spoe'] is None):
            raise ValueError("Missing the required parameter `spoe` when calling `start_spoe_transaction`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `start_spoe_transaction`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'spoe' in params:
            query_params.append(('spoe', params['spoe']))  # noqa: E501
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
            '/services/haproxy/spoe_transactions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SpoeTransaction',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)