# coding: utf-8

"""
    My Project

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class VersionerServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_versioner_v1_ancestry_date_title_title_json_get(self, _date, title, **kwargs):  # noqa: E501
        """Ancestors route returns all ancestors (including self) from a given level through the top title node.  # noqa: E501

        The Ancestry service can be used to determine the complete ancestry to a leaf node at a specific point in time. ### Example The complete hierarchy for **2 CFR 1532.137** is ``` Title 2   Subtitle B     Chapter XV       Part 1532         Subpart A           Section 1532.137 ``` To retrieve this complete hierarchy you can use the ancestry endpoint and provide a Title, Part and Section (you can provide additional layers of the hierarchy) to retrieve a full ancestry. See sample json responses below.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_versioner_v1_ancestry_date_title_title_json_get(_date, title, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date _date: YYYY-MM-DD (required)
        :param str title: Title Number: '1', '2', '50', etc (required)
        :param str subtitle: Uppercase letter. 'A', 'B', 'C'
        :param str chapter: Roman Numerals and digits 0-9. 'I', 'X', '1'
        :param str subchapter: A SUBCHAPTER REQUIRES A CHAPTER. Uppercase letters with optional underscore or dash. 'A', 'B', 'I'
        :param str part: Uppercase letters with optional underscore or dash. 'A', 'B', 'I'
        :param str subpart: A SUBPART REQUIRES A PART. Generally an uppercase letter. 'A', 'B', 'C'
        :param str section: A SECTION REQUIRES A PART. Generally a number followed by a dot and another number. '121.1', '13.4', '1.9'
        :param str appendix: AN APPENDIX REQUIRES A SUBTITLE, CHAPTER or PART. Multiple formats. 'A', 'III', 'App. A'
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_versioner_v1_ancestry_date_title_title_json_get_with_http_info(_date, title, **kwargs)  # noqa: E501
        else:
            (data) = self.api_versioner_v1_ancestry_date_title_title_json_get_with_http_info(_date, title, **kwargs)  # noqa: E501
            return data

    def api_versioner_v1_ancestry_date_title_title_json_get_with_http_info(self, _date, title, **kwargs):  # noqa: E501
        """Ancestors route returns all ancestors (including self) from a given level through the top title node.  # noqa: E501

        The Ancestry service can be used to determine the complete ancestry to a leaf node at a specific point in time. ### Example The complete hierarchy for **2 CFR 1532.137** is ``` Title 2   Subtitle B     Chapter XV       Part 1532         Subpart A           Section 1532.137 ``` To retrieve this complete hierarchy you can use the ancestry endpoint and provide a Title, Part and Section (you can provide additional layers of the hierarchy) to retrieve a full ancestry. See sample json responses below.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_versioner_v1_ancestry_date_title_title_json_get_with_http_info(_date, title, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date _date: YYYY-MM-DD (required)
        :param str title: Title Number: '1', '2', '50', etc (required)
        :param str subtitle: Uppercase letter. 'A', 'B', 'C'
        :param str chapter: Roman Numerals and digits 0-9. 'I', 'X', '1'
        :param str subchapter: A SUBCHAPTER REQUIRES A CHAPTER. Uppercase letters with optional underscore or dash. 'A', 'B', 'I'
        :param str part: Uppercase letters with optional underscore or dash. 'A', 'B', 'I'
        :param str subpart: A SUBPART REQUIRES A PART. Generally an uppercase letter. 'A', 'B', 'C'
        :param str section: A SECTION REQUIRES A PART. Generally a number followed by a dot and another number. '121.1', '13.4', '1.9'
        :param str appendix: AN APPENDIX REQUIRES A SUBTITLE, CHAPTER or PART. Multiple formats. 'A', 'III', 'App. A'
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['_date', 'title', 'subtitle', 'chapter', 'subchapter', 'part', 'subpart', 'section', 'appendix']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_versioner_v1_ancestry_date_title_title_json_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter '_date' is set
        if ('_date' not in params or
                params['_date'] is None):
            raise ValueError("Missing the required parameter `_date` when calling `api_versioner_v1_ancestry_date_title_title_json_get`")  # noqa: E501
        # verify the required parameter 'title' is set
        if ('title' not in params or
                params['title'] is None):
            raise ValueError("Missing the required parameter `title` when calling `api_versioner_v1_ancestry_date_title_title_json_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if '_date' in params:
            path_params['date'] = params['_date']  # noqa: E501
        if 'title' in params:
            path_params['title'] = params['title']  # noqa: E501

        query_params = []
        if 'subtitle' in params:
            query_params.append(('subtitle', params['subtitle']))  # noqa: E501
        if 'chapter' in params:
            query_params.append(('chapter', params['chapter']))  # noqa: E501
        if 'subchapter' in params:
            query_params.append(('subchapter', params['subchapter']))  # noqa: E501
        if 'part' in params:
            query_params.append(('part', params['part']))  # noqa: E501
        if 'subpart' in params:
            query_params.append(('subpart', params['subpart']))  # noqa: E501
        if 'section' in params:
            query_params.append(('section', params['section']))  # noqa: E501
        if 'appendix' in params:
            query_params.append(('appendix', params['appendix']))  # noqa: E501

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
            '/api/versioner/v1/ancestry/{date}/title-{title}.json', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_versioner_v1_full_date_title_title_xml_get(self, _date, title, **kwargs):  # noqa: E501
        """Source XML for a title or subset of a title. Requests can be for entire titles or part level and below.  Downloadable XML document is returned for title requests.  Processed XML is returned if part, subpart, section, or appendix is requested.  # noqa: E501

        The title source route can be used to retrieve the source xml for a complete title or subset. The subset of xml is determined by the lowest leaf node given. For example, if you request Title 1, Chapter I, Part 1, you'll receive the XML only for Part 1 and its children. If you request a section you'll receive the section XML inside its parent Part as well as relevant non-section sibling nodes (Auth, Source, etc). The largest title source xml files can be dozens of megabytes.  [GPO eCFR XML User guide](https://github.com/usgpo/bulk-data/blob/master/ECFR-XML-User-Guide.md)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_versioner_v1_full_date_title_title_xml_get(_date, title, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date _date: YYYY-MM-DD (required)
        :param str title: Title Number: '1', '2', '50', etc (required)
        :param str subtitle: Uppercase letter. 'A', 'B', 'C'
        :param str chapter: Roman Numerals and digits 0-9. 'I', 'X', '1'
        :param str subchapter: A SUBCHAPTER REQUIRES A CHAPTER. Uppercase letters with optional underscore or dash. 'A', 'B', 'I'
        :param str part: Uppercase letters with optional underscore or dash. 'A', 'B', 'I'
        :param str subpart: A SUBPART REQUIRES A PART. Generally an uppercase letter. 'A', 'B', 'C'
        :param str section: A SECTION REQUIRES A PART. Generally a number followed by a dot and another number. '121.1', '13.4', '1.9'
        :param str appendix: AN APPENDIX REQUIRES A SUBTITLE, CHAPTER or PART. Multiple formats. 'A', 'III', 'App. A'
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_versioner_v1_full_date_title_title_xml_get_with_http_info(_date, title, **kwargs)  # noqa: E501
        else:
            (data) = self.api_versioner_v1_full_date_title_title_xml_get_with_http_info(_date, title, **kwargs)  # noqa: E501
            return data

    def api_versioner_v1_full_date_title_title_xml_get_with_http_info(self, _date, title, **kwargs):  # noqa: E501
        """Source XML for a title or subset of a title. Requests can be for entire titles or part level and below.  Downloadable XML document is returned for title requests.  Processed XML is returned if part, subpart, section, or appendix is requested.  # noqa: E501

        The title source route can be used to retrieve the source xml for a complete title or subset. The subset of xml is determined by the lowest leaf node given. For example, if you request Title 1, Chapter I, Part 1, you'll receive the XML only for Part 1 and its children. If you request a section you'll receive the section XML inside its parent Part as well as relevant non-section sibling nodes (Auth, Source, etc). The largest title source xml files can be dozens of megabytes.  [GPO eCFR XML User guide](https://github.com/usgpo/bulk-data/blob/master/ECFR-XML-User-Guide.md)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_versioner_v1_full_date_title_title_xml_get_with_http_info(_date, title, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date _date: YYYY-MM-DD (required)
        :param str title: Title Number: '1', '2', '50', etc (required)
        :param str subtitle: Uppercase letter. 'A', 'B', 'C'
        :param str chapter: Roman Numerals and digits 0-9. 'I', 'X', '1'
        :param str subchapter: A SUBCHAPTER REQUIRES A CHAPTER. Uppercase letters with optional underscore or dash. 'A', 'B', 'I'
        :param str part: Uppercase letters with optional underscore or dash. 'A', 'B', 'I'
        :param str subpart: A SUBPART REQUIRES A PART. Generally an uppercase letter. 'A', 'B', 'C'
        :param str section: A SECTION REQUIRES A PART. Generally a number followed by a dot and another number. '121.1', '13.4', '1.9'
        :param str appendix: AN APPENDIX REQUIRES A SUBTITLE, CHAPTER or PART. Multiple formats. 'A', 'III', 'App. A'
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['_date', 'title', 'subtitle', 'chapter', 'subchapter', 'part', 'subpart', 'section', 'appendix']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_versioner_v1_full_date_title_title_xml_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter '_date' is set
        if ('_date' not in params or
                params['_date'] is None):
            raise ValueError("Missing the required parameter `_date` when calling `api_versioner_v1_full_date_title_title_xml_get`")  # noqa: E501
        # verify the required parameter 'title' is set
        if ('title' not in params or
                params['title'] is None):
            raise ValueError("Missing the required parameter `title` when calling `api_versioner_v1_full_date_title_title_xml_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if '_date' in params:
            path_params['date'] = params['_date']  # noqa: E501
        if 'title' in params:
            path_params['title'] = params['title']  # noqa: E501

        query_params = []
        if 'subtitle' in params:
            query_params.append(('subtitle', params['subtitle']))  # noqa: E501
        if 'chapter' in params:
            query_params.append(('chapter', params['chapter']))  # noqa: E501
        if 'subchapter' in params:
            query_params.append(('subchapter', params['subchapter']))  # noqa: E501
        if 'part' in params:
            query_params.append(('part', params['part']))  # noqa: E501
        if 'subpart' in params:
            query_params.append(('subpart', params['subpart']))  # noqa: E501
        if 'section' in params:
            query_params.append(('section', params['section']))  # noqa: E501
        if 'appendix' in params:
            query_params.append(('appendix', params['appendix']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/versioner/v1/full/{date}/title-{title}.xml', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_versioner_v1_structure_date_title_title_json_get(self, _date, title, **kwargs):  # noqa: E501
        """Structure JSON for a title  # noqa: E501

        The structure JSON endpoint returns the complete structure of a title back as json. This format does not include the content of the title but does include all structure and content nodes as well as their meta data including their type, label, description, identifier and children.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_versioner_v1_structure_date_title_title_json_get(_date, title, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date _date: YYYY-MM-DD (required)
        :param str title: Title Number: '1', '2', '50', etc (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_versioner_v1_structure_date_title_title_json_get_with_http_info(_date, title, **kwargs)  # noqa: E501
        else:
            (data) = self.api_versioner_v1_structure_date_title_title_json_get_with_http_info(_date, title, **kwargs)  # noqa: E501
            return data

    def api_versioner_v1_structure_date_title_title_json_get_with_http_info(self, _date, title, **kwargs):  # noqa: E501
        """Structure JSON for a title  # noqa: E501

        The structure JSON endpoint returns the complete structure of a title back as json. This format does not include the content of the title but does include all structure and content nodes as well as their meta data including their type, label, description, identifier and children.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_versioner_v1_structure_date_title_title_json_get_with_http_info(_date, title, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date _date: YYYY-MM-DD (required)
        :param str title: Title Number: '1', '2', '50', etc (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['_date', 'title']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_versioner_v1_structure_date_title_title_json_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter '_date' is set
        if ('_date' not in params or
                params['_date'] is None):
            raise ValueError("Missing the required parameter `_date` when calling `api_versioner_v1_structure_date_title_title_json_get`")  # noqa: E501
        # verify the required parameter 'title' is set
        if ('title' not in params or
                params['title'] is None):
            raise ValueError("Missing the required parameter `title` when calling `api_versioner_v1_structure_date_title_title_json_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if '_date' in params:
            path_params['date'] = params['_date']  # noqa: E501
        if 'title' in params:
            path_params['title'] = params['title']  # noqa: E501

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
            '/api/versioner/v1/structure/{date}/title-{title}.json', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_versioner_v1_titles_json_get(self, **kwargs):  # noqa: E501
        """Summary information about each title  # noqa: E501

        The Title service can be used to determine the status of each individual title and of the overall status of title imports and reprocessings. It returns an array of all titles containing a hash for each with the name of the title, the latest amended date, latest issue date, up-to-date date, reserved status, and if applicable, processing in progress status. The meta data returned indicates the latest issue date and whether titles are currently being reprocessed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_versioner_v1_titles_json_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_versioner_v1_titles_json_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_versioner_v1_titles_json_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_versioner_v1_titles_json_get_with_http_info(self, **kwargs):  # noqa: E501
        """Summary information about each title  # noqa: E501

        The Title service can be used to determine the status of each individual title and of the overall status of title imports and reprocessings. It returns an array of all titles containing a hash for each with the name of the title, the latest amended date, latest issue date, up-to-date date, reserved status, and if applicable, processing in progress status. The meta data returned indicates the latest issue date and whether titles are currently being reprocessed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_versioner_v1_titles_json_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
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
                    " to method api_versioner_v1_titles_json_get" % key
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/versioner/v1/titles.json', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_versioner_v1_versions_title_title_json_get(self, title, **kwargs):  # noqa: E501
        """Returns an array of all sections and appendices inside a title.  # noqa: E501

        Returns the content versions meeting the specified criteria. Each content object includes its identifier, parent hierarchy, last amendment date and issue date it was last updated. Queries return content versions `on` an issue date, or before or on a specific issue date `lte` or on or after `gte` a specific issue date. The `gte` and `lte` parameters may be combined. Use of the `on` parameter precludes use of `gte` or `lte`. In the response, the `date` field is identical to `amendment_date` and is deprecated. <br> A response of `400 Bad Request` indicates that your request could not be processed. If possible the response will include a message indicating the problem. <br> A response of `503 Service Unavailable` indicates that the title is currently unavailable, typlically because it is currently being processed. The value of the `Retry-After` header suggests a number of seconds to wait before retrying the request.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_versioner_v1_versions_title_title_json_get(title, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str title: Title Number: '1', '2', '50', etc (required)
        :param date issue_date_on: select content added on the supplied issue date
        :param date issue_date_lte: select content added on or before the supplied issue date
        :param date issue_date_gte: select content added on or after the supplied issue date
        :param str subtitle: Uppercase letter. 'A', 'B', 'C'
        :param str chapter: Roman Numerals and digits 0-9. 'I', 'X', '1'
        :param str subchapter: A SUBCHAPTER REQUIRES A CHAPTER. Uppercase letters with optional underscore or dash. 'A', 'B', 'I'
        :param str part: Uppercase letters with optional underscore or dash. 'A', 'B', 'I'
        :param str subpart: A SUBPART REQUIRES A PART. Generally an uppercase letter. 'A', 'B', 'C'
        :param str section: A SECTION REQUIRES A PART. Generally a number followed by a dot and another number. '121.1', '13.4', '1.9'
        :param str appendix: AN APPENDIX REQUIRES A SUBTITLE, CHAPTER or PART. Multiple formats. 'A', 'III', 'App. A'
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_versioner_v1_versions_title_title_json_get_with_http_info(title, **kwargs)  # noqa: E501
        else:
            (data) = self.api_versioner_v1_versions_title_title_json_get_with_http_info(title, **kwargs)  # noqa: E501
            return data

    def api_versioner_v1_versions_title_title_json_get_with_http_info(self, title, **kwargs):  # noqa: E501
        """Returns an array of all sections and appendices inside a title.  # noqa: E501

        Returns the content versions meeting the specified criteria. Each content object includes its identifier, parent hierarchy, last amendment date and issue date it was last updated. Queries return content versions `on` an issue date, or before or on a specific issue date `lte` or on or after `gte` a specific issue date. The `gte` and `lte` parameters may be combined. Use of the `on` parameter precludes use of `gte` or `lte`. In the response, the `date` field is identical to `amendment_date` and is deprecated. <br> A response of `400 Bad Request` indicates that your request could not be processed. If possible the response will include a message indicating the problem. <br> A response of `503 Service Unavailable` indicates that the title is currently unavailable, typlically because it is currently being processed. The value of the `Retry-After` header suggests a number of seconds to wait before retrying the request.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_versioner_v1_versions_title_title_json_get_with_http_info(title, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str title: Title Number: '1', '2', '50', etc (required)
        :param date issue_date_on: select content added on the supplied issue date
        :param date issue_date_lte: select content added on or before the supplied issue date
        :param date issue_date_gte: select content added on or after the supplied issue date
        :param str subtitle: Uppercase letter. 'A', 'B', 'C'
        :param str chapter: Roman Numerals and digits 0-9. 'I', 'X', '1'
        :param str subchapter: A SUBCHAPTER REQUIRES A CHAPTER. Uppercase letters with optional underscore or dash. 'A', 'B', 'I'
        :param str part: Uppercase letters with optional underscore or dash. 'A', 'B', 'I'
        :param str subpart: A SUBPART REQUIRES A PART. Generally an uppercase letter. 'A', 'B', 'C'
        :param str section: A SECTION REQUIRES A PART. Generally a number followed by a dot and another number. '121.1', '13.4', '1.9'
        :param str appendix: AN APPENDIX REQUIRES A SUBTITLE, CHAPTER or PART. Multiple formats. 'A', 'III', 'App. A'
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['title', 'issue_date_on', 'issue_date_lte', 'issue_date_gte', 'subtitle', 'chapter', 'subchapter', 'part', 'subpart', 'section', 'appendix']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_versioner_v1_versions_title_title_json_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'title' is set
        if ('title' not in params or
                params['title'] is None):
            raise ValueError("Missing the required parameter `title` when calling `api_versioner_v1_versions_title_title_json_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'title' in params:
            path_params['title'] = params['title']  # noqa: E501

        query_params = []
        if 'issue_date_on' in params:
            query_params.append(('issue_date[on]', params['issue_date_on']))  # noqa: E501
        if 'issue_date_lte' in params:
            query_params.append(('issue_date[lte]', params['issue_date_lte']))  # noqa: E501
        if 'issue_date_gte' in params:
            query_params.append(('issue_date[gte]', params['issue_date_gte']))  # noqa: E501
        if 'subtitle' in params:
            query_params.append(('subtitle', params['subtitle']))  # noqa: E501
        if 'chapter' in params:
            query_params.append(('chapter', params['chapter']))  # noqa: E501
        if 'subchapter' in params:
            query_params.append(('subchapter', params['subchapter']))  # noqa: E501
        if 'part' in params:
            query_params.append(('part', params['part']))  # noqa: E501
        if 'subpart' in params:
            query_params.append(('subpart', params['subpart']))  # noqa: E501
        if 'section' in params:
            query_params.append(('section', params['section']))  # noqa: E501
        if 'appendix' in params:
            query_params.append(('appendix', params['appendix']))  # noqa: E501

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
            '/api/versioner/v1/versions/title-{title}.json', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
