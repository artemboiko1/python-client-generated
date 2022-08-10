# coding: utf-8

"""
    Alertmanager API

    API of the Prometheus Alertmanager (https://github.com/prometheus/alertmanager)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SilenceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_silence(self, silence_id, **kwargs):  # noqa: E501
        """delete_silence  # noqa: E501

        Delete a silence by its ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_silence(silence_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str silence_id: ID of the silence to get (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_silence_with_http_info(silence_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_silence_with_http_info(silence_id, **kwargs)  # noqa: E501
            return data

    def delete_silence_with_http_info(self, silence_id, **kwargs):  # noqa: E501
        """delete_silence  # noqa: E501

        Delete a silence by its ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_silence_with_http_info(silence_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str silence_id: ID of the silence to get (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['silence_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_silence" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'silence_id' is set
        if ('silence_id' not in params or
                params['silence_id'] is None):
            raise ValueError("Missing the required parameter `silence_id` when calling `delete_silence`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'silence_id' in params:
            path_params['silenceID'] = params['silence_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/silence/{silenceID}', 'DELETE',
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

    def get_silence(self, silence_id, **kwargs):  # noqa: E501
        """get_silence  # noqa: E501

        Get a silence by its ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_silence(silence_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str silence_id: ID of the silence to get (required)
        :return: GettableSilence
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_silence_with_http_info(silence_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_silence_with_http_info(silence_id, **kwargs)  # noqa: E501
            return data

    def get_silence_with_http_info(self, silence_id, **kwargs):  # noqa: E501
        """get_silence  # noqa: E501

        Get a silence by its ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_silence_with_http_info(silence_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str silence_id: ID of the silence to get (required)
        :return: GettableSilence
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['silence_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_silence" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'silence_id' is set
        if ('silence_id' not in params or
                params['silence_id'] is None):
            raise ValueError("Missing the required parameter `silence_id` when calling `get_silence`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'silence_id' in params:
            path_params['silenceID'] = params['silence_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/silence/{silenceID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GettableSilence',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_silences(self, **kwargs):  # noqa: E501
        """get_silences  # noqa: E501

        Get a list of silences  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_silences(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] filter: A list of matchers to filter silences by
        :return: GettableSilences
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_silences_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_silences_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_silences_with_http_info(self, **kwargs):  # noqa: E501
        """get_silences  # noqa: E501

        Get a list of silences  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_silences_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] filter: A list of matchers to filter silences by
        :return: GettableSilences
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_silences" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/silences', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GettableSilences',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_silences(self, body, **kwargs):  # noqa: E501
        """post_silences  # noqa: E501

        Post a new silence or update an existing one  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_silences(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostableSilence body: The silence to create (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_silences_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_silences_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def post_silences_with_http_info(self, body, **kwargs):  # noqa: E501
        """post_silences  # noqa: E501

        Post a new silence or update an existing one  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_silences_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostableSilence body: The silence to create (required)
        :return: InlineResponse200
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
                    " to method post_silences" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_silences`")  # noqa: E501

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

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/silences', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
