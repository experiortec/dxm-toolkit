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


class SyncApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def async_export(self, body, **kwargs):  # noqa: E501
        """Export masking object  # noqa: E501

        Export masking objects  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.async_export(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[ExportObjectMetadata] body: The identifier for the masking object to export (required)
        :return: AsyncTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.async_export_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.async_export_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def async_export_with_http_info(self, body, **kwargs):  # noqa: E501
        """Export masking object  # noqa: E501

        Export masking objects  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.async_export_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[ExportObjectMetadata] body: The identifier for the masking object to export (required)
        :return: AsyncTask
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
                    " to method async_export" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `async_export`")  # noqa: E501

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
            '/export-async', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncTask',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def async_import_object(self, file, force_overwrite, **kwargs):  # noqa: E501
        """Import masking objects  # noqa: E501

        WARNING: The generated curl command is incorrect, so please refer to the Masking API guide for instructions on how to upload files through the API  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.async_import_object(file, force_overwrite, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file file: The identifier for the masking object to import (required)
        :param bool force_overwrite: Specify whether the import should fail if an object already exists with the same ID or the existing object should be overwritten. (required)
        :param int environment_id: The ID of the environment to import objects into
        :param int source_environment_id: The ID of the source environment to import on-the-fly connectors into
        :return: AsyncTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.async_import_object_with_http_info(file, force_overwrite, **kwargs)  # noqa: E501
        else:
            (data) = self.async_import_object_with_http_info(file, force_overwrite, **kwargs)  # noqa: E501
            return data

    def async_import_object_with_http_info(self, file, force_overwrite, **kwargs):  # noqa: E501
        """Import masking objects  # noqa: E501

        WARNING: The generated curl command is incorrect, so please refer to the Masking API guide for instructions on how to upload files through the API  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.async_import_object_with_http_info(file, force_overwrite, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file file: The identifier for the masking object to import (required)
        :param bool force_overwrite: Specify whether the import should fail if an object already exists with the same ID or the existing object should be overwritten. (required)
        :param int environment_id: The ID of the environment to import objects into
        :param int source_environment_id: The ID of the source environment to import on-the-fly connectors into
        :return: AsyncTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'force_overwrite', 'environment_id', 'source_environment_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method async_import_object" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if self.api_client.client_side_validation and ('file' not in params or
                                                       params['file'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `file` when calling `async_import_object`")  # noqa: E501
        # verify the required parameter 'force_overwrite' is set
        if self.api_client.client_side_validation and ('force_overwrite' not in params or
                                                       params['force_overwrite'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `force_overwrite` when calling `async_import_object`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'force_overwrite' in params:
            query_params.append(('force_overwrite', params['force_overwrite']))  # noqa: E501
        if 'environment_id' in params:
            query_params.append(('environment_id', params['environment_id']))  # noqa: E501
        if 'source_environment_id' in params:
            query_params.append(('source_environment_id', params['source_environment_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/import-async', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncTask',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def export(self, body, **kwargs):  # noqa: E501
        """Export masking object  # noqa: E501

        Export masking objects  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.export(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[ExportObjectMetadata] body: The identifier for the masking object to export (required)
        :return: ExportObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.export_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.export_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def export_with_http_info(self, body, **kwargs):  # noqa: E501
        """Export masking object  # noqa: E501

        Export masking objects  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.export_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[ExportObjectMetadata] body: The identifier for the masking object to export (required)
        :return: ExportObject
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
                    " to method export" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `export`")  # noqa: E501

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
            '/export', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExportObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_syncable_objects(self, **kwargs):  # noqa: E501
        """Get all syncable objects  # noqa: E501

        Get all syncable objects  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_syncable_objects(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_number: The page number for which to get syncable objects. This will default to the first page if excluded
        :param int page_size: The maximum number of objects to return. This will default to the DEFAULT_API_PAGE_SIZE property if not provided
        :param str object_type: The type of syncable object to filter for
        :return: ExportObjectMetadataList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_syncable_objects_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_syncable_objects_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_syncable_objects_with_http_info(self, **kwargs):  # noqa: E501
        """Get all syncable objects  # noqa: E501

        Get all syncable objects  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_syncable_objects_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_number: The page number for which to get syncable objects. This will default to the first page if excluded
        :param int page_size: The maximum number of objects to return. This will default to the DEFAULT_API_PAGE_SIZE property if not provided
        :param str object_type: The type of syncable object to filter for
        :return: ExportObjectMetadataList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_number', 'page_size', 'object_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_syncable_objects" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_number' in params:
            query_params.append(('page_number', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'object_type' in params:
            query_params.append(('object_type', params['object_type']))  # noqa: E501

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
            '/syncable-objects', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExportObjectMetadataList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_syncable_object_by_environment_id(self, environment_id, **kwargs):  # noqa: E501
        """Get syncable object for environment  # noqa: E501

        Get syncable object for environment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_syncable_object_by_environment_id(environment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int environment_id: The ID of the environment to retrieve syncable object of (required)
        :return: ExportObjectMetadataList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_syncable_object_by_environment_id_with_http_info(environment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_syncable_object_by_environment_id_with_http_info(environment_id, **kwargs)  # noqa: E501
            return data

    def get_syncable_object_by_environment_id_with_http_info(self, environment_id, **kwargs):  # noqa: E501
        """Get syncable object for environment  # noqa: E501

        Get syncable object for environment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_syncable_object_by_environment_id_with_http_info(environment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int environment_id: The ID of the environment to retrieve syncable object of (required)
        :return: ExportObjectMetadataList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['environment_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_syncable_object_by_environment_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'environment_id' is set
        if self.api_client.client_side_validation and ('environment_id' not in params or
                                                       params['environment_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `environment_id` when calling `get_syncable_object_by_environment_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'environment_id' in params:
            path_params['environmentId'] = params['environment_id']  # noqa: E501

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
            '/syncable-objects/environments/{environmentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExportObjectMetadataList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def import_object(self, body, force_overwrite, **kwargs):  # noqa: E501
        """Import masking objects  # noqa: E501

        Import masking objects  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.import_object(body, force_overwrite, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ExportObject body: The identifier for the masking object to import (required)
        :param bool force_overwrite: Specify whether the import should fail if an object already exists with the same ID or the existing object should be overwritten. (required)
        :param int environment_id: The ID of the environment to import objects into
        :param int source_environment_id: The ID of the source environment to import on-the-fly connectors into
        :return: list[ImportObjectMetadata]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.import_object_with_http_info(body, force_overwrite, **kwargs)  # noqa: E501
        else:
            (data) = self.import_object_with_http_info(body, force_overwrite, **kwargs)  # noqa: E501
            return data

    def import_object_with_http_info(self, body, force_overwrite, **kwargs):  # noqa: E501
        """Import masking objects  # noqa: E501

        Import masking objects  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.import_object_with_http_info(body, force_overwrite, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ExportObject body: The identifier for the masking object to import (required)
        :param bool force_overwrite: Specify whether the import should fail if an object already exists with the same ID or the existing object should be overwritten. (required)
        :param int environment_id: The ID of the environment to import objects into
        :param int source_environment_id: The ID of the source environment to import on-the-fly connectors into
        :return: list[ImportObjectMetadata]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'force_overwrite', 'environment_id', 'source_environment_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_object" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `import_object`")  # noqa: E501
        # verify the required parameter 'force_overwrite' is set
        if self.api_client.client_side_validation and ('force_overwrite' not in params or
                                                       params['force_overwrite'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `force_overwrite` when calling `import_object`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'force_overwrite' in params:
            query_params.append(('force_overwrite', params['force_overwrite']))  # noqa: E501
        if 'environment_id' in params:
            query_params.append(('environment_id', params['environment_id']))  # noqa: E501
        if 'source_environment_id' in params:
            query_params.append(('source_environment_id', params['source_environment_id']))  # noqa: E501

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
            '/import', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ImportObjectMetadata]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def purge_export_directory(self, **kwargs):  # noqa: E501
        """Delete all export documents from /async-export tasks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purge_export_directory(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.purge_export_directory_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.purge_export_directory_with_http_info(**kwargs)  # noqa: E501
            return data

    def purge_export_directory_with_http_info(self, **kwargs):  # noqa: E501
        """Delete all export documents from /async-export tasks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purge_export_directory_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method purge_export_directory" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/export-async', 'DELETE',
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

    def purge_import_directory(self, **kwargs):  # noqa: E501
        """Delete all import documents from /async-import tasks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purge_import_directory(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.purge_import_directory_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.purge_import_directory_with_http_info(**kwargs)  # noqa: E501
            return data

    def purge_import_directory_with_http_info(self, **kwargs):  # noqa: E501
        """Delete all import documents from /async-import tasks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purge_import_directory_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method purge_import_directory" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/import-async', 'DELETE',
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
