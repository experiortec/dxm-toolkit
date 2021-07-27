# coding: utf-8

"""
    Masking API

    Schema for the Masking Engine API  # noqa: E501

    OpenAPI spec version: 5.1.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from dxm.lib.masking_api.api_client import ApiClient


class JdbcDriverApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_jdbc_driver(self, body, **kwargs):  # noqa: E501
        """Create Jdbc Driver  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_jdbc_driver(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param JdbcDriver body: The jdbc driver details. (required)
        :return: JdbcDriver
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_jdbc_driver_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_jdbc_driver_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_jdbc_driver_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create Jdbc Driver  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_jdbc_driver_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param JdbcDriver body: The jdbc driver details. (required)
        :return: JdbcDriver
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_jdbc_driver" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `create_jdbc_driver`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/jdbc-drivers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JdbcDriver',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_jdbc_driver(self, jdbc_driver_id, **kwargs):  # noqa: E501
        """Delete JDBC driver by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_jdbc_driver(jdbc_driver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int jdbc_driver_id: The ID of the JDBC driver to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_jdbc_driver_with_http_info(jdbc_driver_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_jdbc_driver_with_http_info(jdbc_driver_id, **kwargs)  # noqa: E501
            return data

    def delete_jdbc_driver_with_http_info(self, jdbc_driver_id, **kwargs):  # noqa: E501
        """Delete JDBC driver by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_jdbc_driver_with_http_info(jdbc_driver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int jdbc_driver_id: The ID of the JDBC driver to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jdbc_driver_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_jdbc_driver" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jdbc_driver_id' is set
        if self.api_client.client_side_validation and ('jdbc_driver_id' not in params or
                                                       params['jdbc_driver_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `jdbc_driver_id` when calling `delete_jdbc_driver`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'jdbc_driver_id' in params:
            path_params['jdbcDriverId'] = params['jdbc_driver_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/jdbc-drivers/{jdbcDriverId}', 'DELETE',
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

    def get_all_jdbc_drivers(self, **kwargs):  # noqa: E501
        """Get all JDBC drivers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_jdbc_drivers(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool is_built_in: Get only drivers that are built in to the engine when this is true and only user uploaded drivers when this is false
        :param int page_number: The page number for which to get JDBC drivers. This will default to the first page if excluded
        :param int page_size: The maximum number of objects to return. This will default to the DEFAULT_API_PAGE_SIZE property if not provided
        :return: JdbcDriversList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_jdbc_drivers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_jdbc_drivers_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_jdbc_drivers_with_http_info(self, **kwargs):  # noqa: E501
        """Get all JDBC drivers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_jdbc_drivers_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool is_built_in: Get only drivers that are built in to the engine when this is true and only user uploaded drivers when this is false
        :param int page_number: The page number for which to get JDBC drivers. This will default to the first page if excluded
        :param int page_size: The maximum number of objects to return. This will default to the DEFAULT_API_PAGE_SIZE property if not provided
        :return: JdbcDriversList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['is_built_in', 'page_number', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_jdbc_drivers" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'is_built_in' in params:
            query_params.append(('is_built_in', params['is_built_in']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('page_number', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/jdbc-drivers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JdbcDriversList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_jdbc_driver_by_id(self, jdbc_driver_id, **kwargs):  # noqa: E501
        """Get JDBC driver by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_jdbc_driver_by_id(jdbc_driver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int jdbc_driver_id: The ID of the JDBC driver to get (required)
        :return: JdbcDriver
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_jdbc_driver_by_id_with_http_info(jdbc_driver_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_jdbc_driver_by_id_with_http_info(jdbc_driver_id, **kwargs)  # noqa: E501
            return data

    def get_jdbc_driver_by_id_with_http_info(self, jdbc_driver_id, **kwargs):  # noqa: E501
        """Get JDBC driver by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_jdbc_driver_by_id_with_http_info(jdbc_driver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int jdbc_driver_id: The ID of the JDBC driver to get (required)
        :return: JdbcDriver
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jdbc_driver_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_jdbc_driver_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jdbc_driver_id' is set
        if self.api_client.client_side_validation and ('jdbc_driver_id' not in params or
                                                       params['jdbc_driver_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `jdbc_driver_id` when calling `get_jdbc_driver_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'jdbc_driver_id' in params:
            path_params['jdbcDriverId'] = params['jdbc_driver_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/jdbc-drivers/{jdbcDriverId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JdbcDriver',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_jdbc_driver(self, jdbc_driver_id, body, **kwargs):  # noqa: E501
        """Update jdbc driver  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_jdbc_driver(jdbc_driver_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int jdbc_driver_id: The ID of the JDBC driver to update (required)
        :param JdbcDriver body: The jdbc driver details. (required)
        :return: JdbcDriver
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_jdbc_driver_with_http_info(jdbc_driver_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_jdbc_driver_with_http_info(jdbc_driver_id, body, **kwargs)  # noqa: E501
            return data

    def update_jdbc_driver_with_http_info(self, jdbc_driver_id, body, **kwargs):  # noqa: E501
        """Update jdbc driver  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_jdbc_driver_with_http_info(jdbc_driver_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int jdbc_driver_id: The ID of the JDBC driver to update (required)
        :param JdbcDriver body: The jdbc driver details. (required)
        :return: JdbcDriver
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jdbc_driver_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_jdbc_driver" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jdbc_driver_id' is set
        if self.api_client.client_side_validation and ('jdbc_driver_id' not in params or
                                                       params['jdbc_driver_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `jdbc_driver_id` when calling `update_jdbc_driver`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `update_jdbc_driver`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'jdbc_driver_id' in params:
            path_params['jdbcDriverId'] = params['jdbc_driver_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/jdbc-drivers/{jdbcDriverId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JdbcDriver',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
