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


class MapsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_map_entry(self, body, map, **kwargs):  # noqa: E501
        """Adds an entry into the map file  # noqa: E501

        Adds an entry into the map file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_map_entry(body, map, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MapEntry body: (required)
        :param str map: Mapfile attribute storage_name (required)
        :param bool force_sync: If true, immediately syncs changes to disk
        :return: MapEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_map_entry_with_http_info(body, map, **kwargs)  # noqa: E501
        else:
            (data) = self.add_map_entry_with_http_info(body, map, **kwargs)  # noqa: E501
            return data

    def add_map_entry_with_http_info(self, body, map, **kwargs):  # noqa: E501
        """Adds an entry into the map file  # noqa: E501

        Adds an entry into the map file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_map_entry_with_http_info(body, map, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MapEntry body: (required)
        :param str map: Mapfile attribute storage_name (required)
        :param bool force_sync: If true, immediately syncs changes to disk
        :return: MapEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'map', 'force_sync']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_map_entry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_map_entry`")  # noqa: E501
        # verify the required parameter 'map' is set
        if ('map' not in params or
                params['map'] is None):
            raise ValueError("Missing the required parameter `map` when calling `add_map_entry`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'map' in params:
            query_params.append(('map', params['map']))  # noqa: E501
        if 'force_sync' in params:
            query_params.append(('force_sync', params['force_sync']))  # noqa: E501

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
            '/services/haproxy/runtime/maps_entries', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MapEntry',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def add_payload_runtime_map(self, body, name, **kwargs):  # noqa: E501
        """Add a new map payload  # noqa: E501

        Adds a new map payload.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_payload_runtime_map(body, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[MapEntry] body: (required)
        :param str name: Map file name (required)
        :param bool force_sync: If true, immediately syncs changes to disk
        :return: MapEntries
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_payload_runtime_map_with_http_info(body, name, **kwargs)  # noqa: E501
        else:
            (data) = self.add_payload_runtime_map_with_http_info(body, name, **kwargs)  # noqa: E501
            return data

    def add_payload_runtime_map_with_http_info(self, body, name, **kwargs):  # noqa: E501
        """Add a new map payload  # noqa: E501

        Adds a new map payload.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_payload_runtime_map_with_http_info(body, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[MapEntry] body: (required)
        :param str name: Map file name (required)
        :param bool force_sync: If true, immediately syncs changes to disk
        :return: MapEntries
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'name', 'force_sync']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_payload_runtime_map" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_payload_runtime_map`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `add_payload_runtime_map`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []
        if 'force_sync' in params:
            query_params.append(('force_sync', params['force_sync']))  # noqa: E501

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
            '/services/haproxy/runtime/maps/{name}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MapEntries',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def clear_runtime_map(self, name, **kwargs):  # noqa: E501
        """Remove all map entries from the map file  # noqa: E501

        Remove all map entries from the map file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clear_runtime_map(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Map file name (required)
        :param bool force_delete: If true, deletes file from disk
        :param bool force_sync: If true, immediately syncs changes to disk
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.clear_runtime_map_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.clear_runtime_map_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def clear_runtime_map_with_http_info(self, name, **kwargs):  # noqa: E501
        """Remove all map entries from the map file  # noqa: E501

        Remove all map entries from the map file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clear_runtime_map_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Map file name (required)
        :param bool force_delete: If true, deletes file from disk
        :param bool force_sync: If true, immediately syncs changes to disk
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'force_delete', 'force_sync']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clear_runtime_map" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `clear_runtime_map`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []
        if 'force_delete' in params:
            query_params.append(('forceDelete', params['force_delete']))  # noqa: E501
        if 'force_sync' in params:
            query_params.append(('force_sync', params['force_sync']))  # noqa: E501

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
            '/services/haproxy/runtime/maps/{name}', 'DELETE',
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

    def delete_runtime_map_entry(self, id, map, **kwargs):  # noqa: E501
        """Deletes all the map entries from the map by its id  # noqa: E501

        Delete all the map entries from the map by its id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_runtime_map_entry(id, map, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Map id (required)
        :param str map: Mapfile attribute storage_name (required)
        :param bool force_sync: If true, immediately syncs changes to disk
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_runtime_map_entry_with_http_info(id, map, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_runtime_map_entry_with_http_info(id, map, **kwargs)  # noqa: E501
            return data

    def delete_runtime_map_entry_with_http_info(self, id, map, **kwargs):  # noqa: E501
        """Deletes all the map entries from the map by its id  # noqa: E501

        Delete all the map entries from the map by its id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_runtime_map_entry_with_http_info(id, map, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Map id (required)
        :param str map: Mapfile attribute storage_name (required)
        :param bool force_sync: If true, immediately syncs changes to disk
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'map', 'force_sync']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_runtime_map_entry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_runtime_map_entry`")  # noqa: E501
        # verify the required parameter 'map' is set
        if ('map' not in params or
                params['map'] is None):
            raise ValueError("Missing the required parameter `map` when calling `delete_runtime_map_entry`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'map' in params:
            query_params.append(('map', params['map']))  # noqa: E501
        if 'force_sync' in params:
            query_params.append(('force_sync', params['force_sync']))  # noqa: E501

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
            '/services/haproxy/runtime/maps_entries/{id}', 'DELETE',
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

    def get_all_runtime_map_files(self, **kwargs):  # noqa: E501
        """Return runtime map files  # noqa: E501

        Returns runtime map files.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_runtime_map_files(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool include_unmanaged: If true, also show unmanaged map files loaded in haproxy
        :return: Maps
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_runtime_map_files_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_runtime_map_files_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_runtime_map_files_with_http_info(self, **kwargs):  # noqa: E501
        """Return runtime map files  # noqa: E501

        Returns runtime map files.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_runtime_map_files_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool include_unmanaged: If true, also show unmanaged map files loaded in haproxy
        :return: Maps
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['include_unmanaged']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_runtime_map_files" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'include_unmanaged' in params:
            query_params.append(('include_unmanaged', params['include_unmanaged']))  # noqa: E501

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
            '/services/haproxy/runtime/maps', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Maps',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_one_runtime_map(self, name, **kwargs):  # noqa: E501
        """Return one runtime map file  # noqa: E501

        Returns one runtime map file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_one_runtime_map(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Map file name (required)
        :return: dict
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_one_runtime_map_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_one_runtime_map_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def get_one_runtime_map_with_http_info(self, name, **kwargs):  # noqa: E501
        """Return one runtime map file  # noqa: E501

        Returns one runtime map file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_one_runtime_map_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Map file name (required)
        :return: dict
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_one_runtime_map" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_one_runtime_map`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

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
            '/services/haproxy/runtime/maps/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_runtime_map_entry(self, id, map, **kwargs):  # noqa: E501
        """Return one map runtime setting  # noqa: E501

        Returns one map runtime setting by it's id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_runtime_map_entry(id, map, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Map id (required)
        :param str map: Mapfile attribute storage_name (required)
        :return: MapEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_runtime_map_entry_with_http_info(id, map, **kwargs)  # noqa: E501
        else:
            (data) = self.get_runtime_map_entry_with_http_info(id, map, **kwargs)  # noqa: E501
            return data

    def get_runtime_map_entry_with_http_info(self, id, map, **kwargs):  # noqa: E501
        """Return one map runtime setting  # noqa: E501

        Returns one map runtime setting by it's id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_runtime_map_entry_with_http_info(id, map, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Map id (required)
        :param str map: Mapfile attribute storage_name (required)
        :return: MapEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'map']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_runtime_map_entry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_runtime_map_entry`")  # noqa: E501
        # verify the required parameter 'map' is set
        if ('map' not in params or
                params['map'] is None):
            raise ValueError("Missing the required parameter `map` when calling `get_runtime_map_entry`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'map' in params:
            query_params.append(('map', params['map']))  # noqa: E501

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
            '/services/haproxy/runtime/maps_entries/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MapEntry',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def replace_runtime_map_entry(self, body, map, id, **kwargs):  # noqa: E501
        """Replace the value corresponding to each id in a map  # noqa: E501

        Replaces the value corresponding to each id in a map.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.replace_runtime_map_entry(body, map, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MapsEntriesIdBody body: (required)
        :param str map: Mapfile attribute storage_name (required)
        :param str id: Map id (required)
        :param bool force_sync: If true, immediately syncs changes to disk
        :return: MapEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.replace_runtime_map_entry_with_http_info(body, map, id, **kwargs)  # noqa: E501
        else:
            (data) = self.replace_runtime_map_entry_with_http_info(body, map, id, **kwargs)  # noqa: E501
            return data

    def replace_runtime_map_entry_with_http_info(self, body, map, id, **kwargs):  # noqa: E501
        """Replace the value corresponding to each id in a map  # noqa: E501

        Replaces the value corresponding to each id in a map.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.replace_runtime_map_entry_with_http_info(body, map, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MapsEntriesIdBody body: (required)
        :param str map: Mapfile attribute storage_name (required)
        :param str id: Map id (required)
        :param bool force_sync: If true, immediately syncs changes to disk
        :return: MapEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'map', 'id', 'force_sync']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method replace_runtime_map_entry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `replace_runtime_map_entry`")  # noqa: E501
        # verify the required parameter 'map' is set
        if ('map' not in params or
                params['map'] is None):
            raise ValueError("Missing the required parameter `map` when calling `replace_runtime_map_entry`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `replace_runtime_map_entry`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'map' in params:
            query_params.append(('map', params['map']))  # noqa: E501
        if 'force_sync' in params:
            query_params.append(('force_sync', params['force_sync']))  # noqa: E501

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
            '/services/haproxy/runtime/maps_entries/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MapEntry',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def show_runtime_map(self, map, **kwargs):  # noqa: E501
        """Return one map runtime entries  # noqa: E501

        Returns an array of all entries in a given runtime map file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.show_runtime_map(map, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str map: Mapfile attribute storage_name (required)
        :return: MapEntries
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.show_runtime_map_with_http_info(map, **kwargs)  # noqa: E501
        else:
            (data) = self.show_runtime_map_with_http_info(map, **kwargs)  # noqa: E501
            return data

    def show_runtime_map_with_http_info(self, map, **kwargs):  # noqa: E501
        """Return one map runtime entries  # noqa: E501

        Returns an array of all entries in a given runtime map file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.show_runtime_map_with_http_info(map, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str map: Mapfile attribute storage_name (required)
        :return: MapEntries
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['map']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method show_runtime_map" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'map' is set
        if ('map' not in params or
                params['map'] is None):
            raise ValueError("Missing the required parameter `map` when calling `show_runtime_map`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'map' in params:
            query_params.append(('map', params['map']))  # noqa: E501

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
            '/services/haproxy/runtime/maps_entries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MapEntries',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
