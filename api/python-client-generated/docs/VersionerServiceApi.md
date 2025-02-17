# swagger_client.VersionerServiceApi

All URIs are relative to *www.ecfr.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_versioner_v1_ancestry_date_title_title_json_get**](VersionerServiceApi.md#api_versioner_v1_ancestry_date_title_title_json_get) | **GET** /api/versioner/v1/ancestry/{date}/title-{title}.json | Ancestors route returns all ancestors (including self) from a given level through the top title node.
[**api_versioner_v1_full_date_title_title_xml_get**](VersionerServiceApi.md#api_versioner_v1_full_date_title_title_xml_get) | **GET** /api/versioner/v1/full/{date}/title-{title}.xml | Source XML for a title or subset of a title. Requests can be for entire titles or part level and below.  Downloadable XML document is returned for title requests.  Processed XML is returned if part, subpart, section, or appendix is requested.
[**api_versioner_v1_structure_date_title_title_json_get**](VersionerServiceApi.md#api_versioner_v1_structure_date_title_title_json_get) | **GET** /api/versioner/v1/structure/{date}/title-{title}.json | Structure JSON for a title
[**api_versioner_v1_titles_json_get**](VersionerServiceApi.md#api_versioner_v1_titles_json_get) | **GET** /api/versioner/v1/titles.json | Summary information about each title
[**api_versioner_v1_versions_title_title_json_get**](VersionerServiceApi.md#api_versioner_v1_versions_title_title_json_get) | **GET** /api/versioner/v1/versions/title-{title}.json | Returns an array of all sections and appendices inside a title.

# **api_versioner_v1_ancestry_date_title_title_json_get**
> object api_versioner_v1_ancestry_date_title_title_json_get(_date, title, subtitle=subtitle, chapter=chapter, subchapter=subchapter, part=part, subpart=subpart, section=section, appendix=appendix)

Ancestors route returns all ancestors (including self) from a given level through the top title node.

The Ancestry service can be used to determine the complete ancestry to a leaf node at a specific point in time. ### Example The complete hierarchy for **2 CFR 1532.137** is ``` Title 2   Subtitle B     Chapter XV       Part 1532         Subpart A           Section 1532.137 ``` To retrieve this complete hierarchy you can use the ancestry endpoint and provide a Title, Part and Section (you can provide additional layers of the hierarchy) to retrieve a full ancestry. See sample json responses below. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionerServiceApi()
_date = '2013-10-20' # date | YYYY-MM-DD
title = 'title_example' # str | Title Number: '1', '2', '50', etc
subtitle = 'subtitle_example' # str | Uppercase letter. 'A', 'B', 'C' (optional)
chapter = 'chapter_example' # str | Roman Numerals and digits 0-9. 'I', 'X', '1' (optional)
subchapter = 'subchapter_example' # str | A SUBCHAPTER REQUIRES A CHAPTER. Uppercase letters with optional underscore or dash. 'A', 'B', 'I' (optional)
part = 'part_example' # str | Uppercase letters with optional underscore or dash. 'A', 'B', 'I' (optional)
subpart = 'subpart_example' # str | A SUBPART REQUIRES A PART. Generally an uppercase letter. 'A', 'B', 'C' (optional)
section = 'section_example' # str | A SECTION REQUIRES A PART. Generally a number followed by a dot and another number. '121.1', '13.4', '1.9' (optional)
appendix = 'appendix_example' # str | AN APPENDIX REQUIRES A SUBTITLE, CHAPTER or PART. Multiple formats. 'A', 'III', 'App. A' (optional)

try:
    # Ancestors route returns all ancestors (including self) from a given level through the top title node.
    api_response = api_instance.api_versioner_v1_ancestry_date_title_title_json_get(_date, title, subtitle=subtitle, chapter=chapter, subchapter=subchapter, part=part, subpart=subpart, section=section, appendix=appendix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionerServiceApi->api_versioner_v1_ancestry_date_title_title_json_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **date**| YYYY-MM-DD | 
 **title** | **str**| Title Number: &#x27;1&#x27;, &#x27;2&#x27;, &#x27;50&#x27;, etc | 
 **subtitle** | **str**| Uppercase letter. &#x27;A&#x27;, &#x27;B&#x27;, &#x27;C&#x27; | [optional] 
 **chapter** | **str**| Roman Numerals and digits 0-9. &#x27;I&#x27;, &#x27;X&#x27;, &#x27;1&#x27; | [optional] 
 **subchapter** | **str**| A SUBCHAPTER REQUIRES A CHAPTER. Uppercase letters with optional underscore or dash. &#x27;A&#x27;, &#x27;B&#x27;, &#x27;I&#x27; | [optional] 
 **part** | **str**| Uppercase letters with optional underscore or dash. &#x27;A&#x27;, &#x27;B&#x27;, &#x27;I&#x27; | [optional] 
 **subpart** | **str**| A SUBPART REQUIRES A PART. Generally an uppercase letter. &#x27;A&#x27;, &#x27;B&#x27;, &#x27;C&#x27; | [optional] 
 **section** | **str**| A SECTION REQUIRES A PART. Generally a number followed by a dot and another number. &#x27;121.1&#x27;, &#x27;13.4&#x27;, &#x27;1.9&#x27; | [optional] 
 **appendix** | **str**| AN APPENDIX REQUIRES A SUBTITLE, CHAPTER or PART. Multiple formats. &#x27;A&#x27;, &#x27;III&#x27;, &#x27;App. A&#x27; | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_versioner_v1_full_date_title_title_xml_get**
> object api_versioner_v1_full_date_title_title_xml_get(_date, title, subtitle=subtitle, chapter=chapter, subchapter=subchapter, part=part, subpart=subpart, section=section, appendix=appendix)

Source XML for a title or subset of a title. Requests can be for entire titles or part level and below.  Downloadable XML document is returned for title requests.  Processed XML is returned if part, subpart, section, or appendix is requested.

The title source route can be used to retrieve the source xml for a complete title or subset. The subset of xml is determined by the lowest leaf node given. For example, if you request Title 1, Chapter I, Part 1, you'll receive the XML only for Part 1 and its children. If you request a section you'll receive the section XML inside its parent Part as well as relevant non-section sibling nodes (Auth, Source, etc). The largest title source xml files can be dozens of megabytes.  [GPO eCFR XML User guide](https://github.com/usgpo/bulk-data/blob/master/ECFR-XML-User-Guide.md) 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionerServiceApi()
_date = '2013-10-20' # date | YYYY-MM-DD
title = 'title_example' # str | Title Number: '1', '2', '50', etc
subtitle = 'subtitle_example' # str | Uppercase letter. 'A', 'B', 'C' (optional)
chapter = 'chapter_example' # str | Roman Numerals and digits 0-9. 'I', 'X', '1' (optional)
subchapter = 'subchapter_example' # str | A SUBCHAPTER REQUIRES A CHAPTER. Uppercase letters with optional underscore or dash. 'A', 'B', 'I' (optional)
part = 'part_example' # str | Uppercase letters with optional underscore or dash. 'A', 'B', 'I' (optional)
subpart = 'subpart_example' # str | A SUBPART REQUIRES A PART. Generally an uppercase letter. 'A', 'B', 'C' (optional)
section = 'section_example' # str | A SECTION REQUIRES A PART. Generally a number followed by a dot and another number. '121.1', '13.4', '1.9' (optional)
appendix = 'appendix_example' # str | AN APPENDIX REQUIRES A SUBTITLE, CHAPTER or PART. Multiple formats. 'A', 'III', 'App. A' (optional)

try:
    # Source XML for a title or subset of a title. Requests can be for entire titles or part level and below.  Downloadable XML document is returned for title requests.  Processed XML is returned if part, subpart, section, or appendix is requested.
    api_response = api_instance.api_versioner_v1_full_date_title_title_xml_get(_date, title, subtitle=subtitle, chapter=chapter, subchapter=subchapter, part=part, subpart=subpart, section=section, appendix=appendix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionerServiceApi->api_versioner_v1_full_date_title_title_xml_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **date**| YYYY-MM-DD | 
 **title** | **str**| Title Number: &#x27;1&#x27;, &#x27;2&#x27;, &#x27;50&#x27;, etc | 
 **subtitle** | **str**| Uppercase letter. &#x27;A&#x27;, &#x27;B&#x27;, &#x27;C&#x27; | [optional] 
 **chapter** | **str**| Roman Numerals and digits 0-9. &#x27;I&#x27;, &#x27;X&#x27;, &#x27;1&#x27; | [optional] 
 **subchapter** | **str**| A SUBCHAPTER REQUIRES A CHAPTER. Uppercase letters with optional underscore or dash. &#x27;A&#x27;, &#x27;B&#x27;, &#x27;I&#x27; | [optional] 
 **part** | **str**| Uppercase letters with optional underscore or dash. &#x27;A&#x27;, &#x27;B&#x27;, &#x27;I&#x27; | [optional] 
 **subpart** | **str**| A SUBPART REQUIRES A PART. Generally an uppercase letter. &#x27;A&#x27;, &#x27;B&#x27;, &#x27;C&#x27; | [optional] 
 **section** | **str**| A SECTION REQUIRES A PART. Generally a number followed by a dot and another number. &#x27;121.1&#x27;, &#x27;13.4&#x27;, &#x27;1.9&#x27; | [optional] 
 **appendix** | **str**| AN APPENDIX REQUIRES A SUBTITLE, CHAPTER or PART. Multiple formats. &#x27;A&#x27;, &#x27;III&#x27;, &#x27;App. A&#x27; | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_versioner_v1_structure_date_title_title_json_get**
> object api_versioner_v1_structure_date_title_title_json_get(_date, title)

Structure JSON for a title

The structure JSON endpoint returns the complete structure of a title back as json. This format does not include the content of the title but does include all structure and content nodes as well as their meta data including their type, label, description, identifier and children.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionerServiceApi()
_date = '2013-10-20' # date | YYYY-MM-DD
title = 'title_example' # str | Title Number: '1', '2', '50', etc

try:
    # Structure JSON for a title
    api_response = api_instance.api_versioner_v1_structure_date_title_title_json_get(_date, title)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionerServiceApi->api_versioner_v1_structure_date_title_title_json_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **date**| YYYY-MM-DD | 
 **title** | **str**| Title Number: &#x27;1&#x27;, &#x27;2&#x27;, &#x27;50&#x27;, etc | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_versioner_v1_titles_json_get**
> object api_versioner_v1_titles_json_get()

Summary information about each title

The Title service can be used to determine the status of each individual title and of the overall status of title imports and reprocessings. It returns an array of all titles containing a hash for each with the name of the title, the latest amended date, latest issue date, up-to-date date, reserved status, and if applicable, processing in progress status. The meta data returned indicates the latest issue date and whether titles are currently being reprocessed.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionerServiceApi()

try:
    # Summary information about each title
    api_response = api_instance.api_versioner_v1_titles_json_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionerServiceApi->api_versioner_v1_titles_json_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_versioner_v1_versions_title_title_json_get**
> object api_versioner_v1_versions_title_title_json_get(title, issue_date_on=issue_date_on, issue_date_lte=issue_date_lte, issue_date_gte=issue_date_gte, subtitle=subtitle, chapter=chapter, subchapter=subchapter, part=part, subpart=subpart, section=section, appendix=appendix)

Returns an array of all sections and appendices inside a title.

Returns the content versions meeting the specified criteria. Each content object includes its identifier, parent hierarchy, last amendment date and issue date it was last updated. Queries return content versions `on` an issue date, or before or on a specific issue date `lte` or on or after `gte` a specific issue date. The `gte` and `lte` parameters may be combined. Use of the `on` parameter precludes use of `gte` or `lte`. In the response, the `date` field is identical to `amendment_date` and is deprecated. <br> A response of `400 Bad Request` indicates that your request could not be processed. If possible the response will include a message indicating the problem. <br> A response of `503 Service Unavailable` indicates that the title is currently unavailable, typlically because it is currently being processed. The value of the `Retry-After` header suggests a number of seconds to wait before retrying the request. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionerServiceApi()
title = 'title_example' # str | Title Number: '1', '2', '50', etc
issue_date_on = '2013-10-20' # date | select content added on the supplied issue date (optional)
issue_date_lte = '2013-10-20' # date | select content added on or before the supplied issue date (optional)
issue_date_gte = '2013-10-20' # date | select content added on or after the supplied issue date (optional)
subtitle = 'subtitle_example' # str | Uppercase letter. 'A', 'B', 'C' (optional)
chapter = 'chapter_example' # str | Roman Numerals and digits 0-9. 'I', 'X', '1' (optional)
subchapter = 'subchapter_example' # str | A SUBCHAPTER REQUIRES A CHAPTER. Uppercase letters with optional underscore or dash. 'A', 'B', 'I' (optional)
part = 'part_example' # str | Uppercase letters with optional underscore or dash. 'A', 'B', 'I' (optional)
subpart = 'subpart_example' # str | A SUBPART REQUIRES A PART. Generally an uppercase letter. 'A', 'B', 'C' (optional)
section = 'section_example' # str | A SECTION REQUIRES A PART. Generally a number followed by a dot and another number. '121.1', '13.4', '1.9' (optional)
appendix = 'appendix_example' # str | AN APPENDIX REQUIRES A SUBTITLE, CHAPTER or PART. Multiple formats. 'A', 'III', 'App. A' (optional)

try:
    # Returns an array of all sections and appendices inside a title.
    api_response = api_instance.api_versioner_v1_versions_title_title_json_get(title, issue_date_on=issue_date_on, issue_date_lte=issue_date_lte, issue_date_gte=issue_date_gte, subtitle=subtitle, chapter=chapter, subchapter=subchapter, part=part, subpart=subpart, section=section, appendix=appendix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionerServiceApi->api_versioner_v1_versions_title_title_json_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| Title Number: &#x27;1&#x27;, &#x27;2&#x27;, &#x27;50&#x27;, etc | 
 **issue_date_on** | **date**| select content added on the supplied issue date | [optional] 
 **issue_date_lte** | **date**| select content added on or before the supplied issue date | [optional] 
 **issue_date_gte** | **date**| select content added on or after the supplied issue date | [optional] 
 **subtitle** | **str**| Uppercase letter. &#x27;A&#x27;, &#x27;B&#x27;, &#x27;C&#x27; | [optional] 
 **chapter** | **str**| Roman Numerals and digits 0-9. &#x27;I&#x27;, &#x27;X&#x27;, &#x27;1&#x27; | [optional] 
 **subchapter** | **str**| A SUBCHAPTER REQUIRES A CHAPTER. Uppercase letters with optional underscore or dash. &#x27;A&#x27;, &#x27;B&#x27;, &#x27;I&#x27; | [optional] 
 **part** | **str**| Uppercase letters with optional underscore or dash. &#x27;A&#x27;, &#x27;B&#x27;, &#x27;I&#x27; | [optional] 
 **subpart** | **str**| A SUBPART REQUIRES A PART. Generally an uppercase letter. &#x27;A&#x27;, &#x27;B&#x27;, &#x27;C&#x27; | [optional] 
 **section** | **str**| A SECTION REQUIRES A PART. Generally a number followed by a dot and another number. &#x27;121.1&#x27;, &#x27;13.4&#x27;, &#x27;1.9&#x27; | [optional] 
 **appendix** | **str**| AN APPENDIX REQUIRES A SUBTITLE, CHAPTER or PART. Multiple formats. &#x27;A&#x27;, &#x27;III&#x27;, &#x27;App. A&#x27; | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

