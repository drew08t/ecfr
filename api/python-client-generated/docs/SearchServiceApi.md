# swagger_client.SearchServiceApi

All URIs are relative to *www.ecfr.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_search_v1_count_get**](SearchServiceApi.md#api_search_v1_count_get) | **GET** /api/search/v1/count | Search result count
[**api_search_v1_counts_daily_get**](SearchServiceApi.md#api_search_v1_counts_daily_get) | **GET** /api/search/v1/counts/daily | Search result counts by date
[**api_search_v1_counts_hierarchy_get**](SearchServiceApi.md#api_search_v1_counts_hierarchy_get) | **GET** /api/search/v1/counts/hierarchy | Search result counts by hierarchy
[**api_search_v1_counts_titles_get**](SearchServiceApi.md#api_search_v1_counts_titles_get) | **GET** /api/search/v1/counts/titles | Search result counts by title
[**api_search_v1_results_get**](SearchServiceApi.md#api_search_v1_results_get) | **GET** /api/search/v1/results | Search results
[**api_search_v1_suggestions_get**](SearchServiceApi.md#api_search_v1_suggestions_get) | **GET** /api/search/v1/suggestions | Search suggestions
[**api_search_v1_summary_get**](SearchServiceApi.md#api_search_v1_summary_get) | **GET** /api/search/v1/summary | Search summary details

# **api_search_v1_count_get**
> object api_search_v1_count_get(query=query, agency_slugs=agency_slugs, _date=_date, last_modified_after=last_modified_after, last_modified_on_or_after=last_modified_on_or_after, last_modified_before=last_modified_before, last_modified_on_or_before=last_modified_on_or_before)

Search result count

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchServiceApi()
query = 'query_example' # str | Search term; searches the headings and the full text (optional)
agency_slugs = ['agency_slugs_example'] # list[str] | limit to content currently associated with these agencies (see AdminService agencies endpoint to retrieve a list of agency slugs) (optional)
_date = '2013-10-20' # date | limit to content present on this date (YYYY-MM-DD) (optional)
last_modified_after = '2013-10-20' # date | limit to content last modified after this date (YYYY-MM-DD) (optional)
last_modified_on_or_after = '2013-10-20' # date | limit to content last modified on or after this date (YYYY-MM-DD) (optional)
last_modified_before = '2013-10-20' # date | limit to content last modified before this date (YYYY-MM-DD) (optional)
last_modified_on_or_before = '2013-10-20' # date | limit to content last modified on or before this date (YYYY-MM-DD) (optional)

try:
    # Search result count
    api_response = api_instance.api_search_v1_count_get(query=query, agency_slugs=agency_slugs, _date=_date, last_modified_after=last_modified_after, last_modified_on_or_after=last_modified_on_or_after, last_modified_before=last_modified_before, last_modified_on_or_before=last_modified_on_or_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchServiceApi->api_search_v1_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search term; searches the headings and the full text | [optional] 
 **agency_slugs** | [**list[str]**](str.md)| limit to content currently associated with these agencies (see AdminService agencies endpoint to retrieve a list of agency slugs) | [optional] 
 **_date** | **date**| limit to content present on this date (YYYY-MM-DD) | [optional] 
 **last_modified_after** | **date**| limit to content last modified after this date (YYYY-MM-DD) | [optional] 
 **last_modified_on_or_after** | **date**| limit to content last modified on or after this date (YYYY-MM-DD) | [optional] 
 **last_modified_before** | **date**| limit to content last modified before this date (YYYY-MM-DD) | [optional] 
 **last_modified_on_or_before** | **date**| limit to content last modified on or before this date (YYYY-MM-DD) | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_search_v1_counts_daily_get**
> object api_search_v1_counts_daily_get(query=query, agency_slugs=agency_slugs, _date=_date, last_modified_after=last_modified_after, last_modified_on_or_after=last_modified_on_or_after, last_modified_before=last_modified_before, last_modified_on_or_before=last_modified_on_or_before)

Search result counts by date

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchServiceApi()
query = 'query_example' # str | Search term; searches the headings and the full text (optional)
agency_slugs = ['agency_slugs_example'] # list[str] | limit to content currently associated with these agencies (see AdminService agencies endpoint to retrieve a list of agency slugs) (optional)
_date = '2013-10-20' # date | limit to content present on this date (YYYY-MM-DD) (optional)
last_modified_after = '2013-10-20' # date | limit to content last modified after this date (YYYY-MM-DD) (optional)
last_modified_on_or_after = '2013-10-20' # date | limit to content last modified on or after this date (YYYY-MM-DD) (optional)
last_modified_before = '2013-10-20' # date | limit to content last modified before this date (YYYY-MM-DD) (optional)
last_modified_on_or_before = '2013-10-20' # date | limit to content last modified on or before this date (YYYY-MM-DD) (optional)

try:
    # Search result counts by date
    api_response = api_instance.api_search_v1_counts_daily_get(query=query, agency_slugs=agency_slugs, _date=_date, last_modified_after=last_modified_after, last_modified_on_or_after=last_modified_on_or_after, last_modified_before=last_modified_before, last_modified_on_or_before=last_modified_on_or_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchServiceApi->api_search_v1_counts_daily_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search term; searches the headings and the full text | [optional] 
 **agency_slugs** | [**list[str]**](str.md)| limit to content currently associated with these agencies (see AdminService agencies endpoint to retrieve a list of agency slugs) | [optional] 
 **_date** | **date**| limit to content present on this date (YYYY-MM-DD) | [optional] 
 **last_modified_after** | **date**| limit to content last modified after this date (YYYY-MM-DD) | [optional] 
 **last_modified_on_or_after** | **date**| limit to content last modified on or after this date (YYYY-MM-DD) | [optional] 
 **last_modified_before** | **date**| limit to content last modified before this date (YYYY-MM-DD) | [optional] 
 **last_modified_on_or_before** | **date**| limit to content last modified on or before this date (YYYY-MM-DD) | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_search_v1_counts_hierarchy_get**
> object api_search_v1_counts_hierarchy_get(query=query, agency_slugs=agency_slugs, _date=_date, last_modified_after=last_modified_after, last_modified_on_or_after=last_modified_on_or_after, last_modified_before=last_modified_before, last_modified_on_or_before=last_modified_on_or_before)

Search result counts by hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchServiceApi()
query = 'query_example' # str | Search term; searches the headings and the full text (optional)
agency_slugs = ['agency_slugs_example'] # list[str] | limit to content currently associated with these agencies (see AdminService agencies endpoint to retrieve a list of agency slugs) (optional)
_date = '2013-10-20' # date | limit to content present on this date (YYYY-MM-DD) (optional)
last_modified_after = '2013-10-20' # date | limit to content last modified after this date (YYYY-MM-DD) (optional)
last_modified_on_or_after = '2013-10-20' # date | limit to content last modified on or after this date (YYYY-MM-DD) (optional)
last_modified_before = '2013-10-20' # date | limit to content last modified before this date (YYYY-MM-DD) (optional)
last_modified_on_or_before = '2013-10-20' # date | limit to content last modified on or before this date (YYYY-MM-DD) (optional)

try:
    # Search result counts by hierarchy
    api_response = api_instance.api_search_v1_counts_hierarchy_get(query=query, agency_slugs=agency_slugs, _date=_date, last_modified_after=last_modified_after, last_modified_on_or_after=last_modified_on_or_after, last_modified_before=last_modified_before, last_modified_on_or_before=last_modified_on_or_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchServiceApi->api_search_v1_counts_hierarchy_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search term; searches the headings and the full text | [optional] 
 **agency_slugs** | [**list[str]**](str.md)| limit to content currently associated with these agencies (see AdminService agencies endpoint to retrieve a list of agency slugs) | [optional] 
 **_date** | **date**| limit to content present on this date (YYYY-MM-DD) | [optional] 
 **last_modified_after** | **date**| limit to content last modified after this date (YYYY-MM-DD) | [optional] 
 **last_modified_on_or_after** | **date**| limit to content last modified on or after this date (YYYY-MM-DD) | [optional] 
 **last_modified_before** | **date**| limit to content last modified before this date (YYYY-MM-DD) | [optional] 
 **last_modified_on_or_before** | **date**| limit to content last modified on or before this date (YYYY-MM-DD) | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_search_v1_counts_titles_get**
> object api_search_v1_counts_titles_get(query=query, agency_slugs=agency_slugs, _date=_date, last_modified_after=last_modified_after, last_modified_on_or_after=last_modified_on_or_after, last_modified_before=last_modified_before, last_modified_on_or_before=last_modified_on_or_before)

Search result counts by title

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchServiceApi()
query = 'query_example' # str | Search term; searches the headings and the full text (optional)
agency_slugs = ['agency_slugs_example'] # list[str] | limit to content currently associated with these agencies (see AdminService agencies endpoint to retrieve a list of agency slugs) (optional)
_date = '2013-10-20' # date | limit to content present on this date (YYYY-MM-DD) (optional)
last_modified_after = '2013-10-20' # date | limit to content last modified after this date (YYYY-MM-DD) (optional)
last_modified_on_or_after = '2013-10-20' # date | limit to content last modified on or after this date (YYYY-MM-DD) (optional)
last_modified_before = '2013-10-20' # date | limit to content last modified before this date (YYYY-MM-DD) (optional)
last_modified_on_or_before = '2013-10-20' # date | limit to content last modified on or before this date (YYYY-MM-DD) (optional)

try:
    # Search result counts by title
    api_response = api_instance.api_search_v1_counts_titles_get(query=query, agency_slugs=agency_slugs, _date=_date, last_modified_after=last_modified_after, last_modified_on_or_after=last_modified_on_or_after, last_modified_before=last_modified_before, last_modified_on_or_before=last_modified_on_or_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchServiceApi->api_search_v1_counts_titles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search term; searches the headings and the full text | [optional] 
 **agency_slugs** | [**list[str]**](str.md)| limit to content currently associated with these agencies (see AdminService agencies endpoint to retrieve a list of agency slugs) | [optional] 
 **_date** | **date**| limit to content present on this date (YYYY-MM-DD) | [optional] 
 **last_modified_after** | **date**| limit to content last modified after this date (YYYY-MM-DD) | [optional] 
 **last_modified_on_or_after** | **date**| limit to content last modified on or after this date (YYYY-MM-DD) | [optional] 
 **last_modified_before** | **date**| limit to content last modified before this date (YYYY-MM-DD) | [optional] 
 **last_modified_on_or_before** | **date**| limit to content last modified on or before this date (YYYY-MM-DD) | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_search_v1_results_get**
> InlineResponse200 api_search_v1_results_get(query=query, agency_slugs=agency_slugs, _date=_date, last_modified_after=last_modified_after, last_modified_on_or_after=last_modified_on_or_after, last_modified_before=last_modified_before, last_modified_on_or_before=last_modified_on_or_before, per_page=per_page, page=page, order=order, paginate_by=paginate_by)

Search results

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchServiceApi()
query = 'query_example' # str | Search term; searches the headings and the full text (optional)
agency_slugs = ['agency_slugs_example'] # list[str] | limit to content currently associated with these agencies (see AdminService agencies endpoint to retrieve a list of agency slugs) (optional)
_date = '2013-10-20' # date | limit to content present on this date (YYYY-MM-DD) (optional)
last_modified_after = '2013-10-20' # date | limit to content last modified after this date (YYYY-MM-DD) (optional)
last_modified_on_or_after = '2013-10-20' # date | limit to content last modified on or after this date (YYYY-MM-DD) (optional)
last_modified_before = '2013-10-20' # date | limit to content last modified before this date (YYYY-MM-DD) (optional)
last_modified_on_or_before = '2013-10-20' # date | limit to content last modified on or before this date (YYYY-MM-DD) (optional)
per_page = 20 # int | number of results per page; max of 1,000 (optional) (default to 20)
page = 1 # int | page of results; can't paginate beyond 10,000 total results (optional) (default to 1)
order = 'relevance' # str | order of results (optional) (default to relevance)
paginate_by = 'results' # str | how results should be paginated - 'date' will group results so that all results from a date appear on the same page of pagination. If 'date' is chosen then one of the last_modified_* options is required. (optional) (default to results)

try:
    # Search results
    api_response = api_instance.api_search_v1_results_get(query=query, agency_slugs=agency_slugs, _date=_date, last_modified_after=last_modified_after, last_modified_on_or_after=last_modified_on_or_after, last_modified_before=last_modified_before, last_modified_on_or_before=last_modified_on_or_before, per_page=per_page, page=page, order=order, paginate_by=paginate_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchServiceApi->api_search_v1_results_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search term; searches the headings and the full text | [optional] 
 **agency_slugs** | [**list[str]**](str.md)| limit to content currently associated with these agencies (see AdminService agencies endpoint to retrieve a list of agency slugs) | [optional] 
 **_date** | **date**| limit to content present on this date (YYYY-MM-DD) | [optional] 
 **last_modified_after** | **date**| limit to content last modified after this date (YYYY-MM-DD) | [optional] 
 **last_modified_on_or_after** | **date**| limit to content last modified on or after this date (YYYY-MM-DD) | [optional] 
 **last_modified_before** | **date**| limit to content last modified before this date (YYYY-MM-DD) | [optional] 
 **last_modified_on_or_before** | **date**| limit to content last modified on or before this date (YYYY-MM-DD) | [optional] 
 **per_page** | **int**| number of results per page; max of 1,000 | [optional] [default to 20]
 **page** | **int**| page of results; can&#x27;t paginate beyond 10,000 total results | [optional] [default to 1]
 **order** | **str**| order of results | [optional] [default to relevance]
 **paginate_by** | **str**| how results should be paginated - &#x27;date&#x27; will group results so that all results from a date appear on the same page of pagination. If &#x27;date&#x27; is chosen then one of the last_modified_* options is required. | [optional] [default to results]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_search_v1_suggestions_get**
> object api_search_v1_suggestions_get(query=query, agency_slugs=agency_slugs, _date=_date, last_modified_after=last_modified_after, last_modified_on_or_after=last_modified_on_or_after, last_modified_before=last_modified_before, last_modified_on_or_before=last_modified_on_or_before)

Search suggestions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchServiceApi()
query = 'query_example' # str | Search term; searches the headings and the full text (optional)
agency_slugs = ['agency_slugs_example'] # list[str] | limit to content currently associated with these agencies (see AdminService agencies endpoint to retrieve a list of agency slugs) (optional)
_date = '2013-10-20' # date | limit to content present on this date (YYYY-MM-DD) (optional)
last_modified_after = '2013-10-20' # date | limit to content last modified after this date (YYYY-MM-DD) (optional)
last_modified_on_or_after = '2013-10-20' # date | limit to content last modified on or after this date (YYYY-MM-DD) (optional)
last_modified_before = '2013-10-20' # date | limit to content last modified before this date (YYYY-MM-DD) (optional)
last_modified_on_or_before = '2013-10-20' # date | limit to content last modified on or before this date (YYYY-MM-DD) (optional)

try:
    # Search suggestions
    api_response = api_instance.api_search_v1_suggestions_get(query=query, agency_slugs=agency_slugs, _date=_date, last_modified_after=last_modified_after, last_modified_on_or_after=last_modified_on_or_after, last_modified_before=last_modified_before, last_modified_on_or_before=last_modified_on_or_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchServiceApi->api_search_v1_suggestions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search term; searches the headings and the full text | [optional] 
 **agency_slugs** | [**list[str]**](str.md)| limit to content currently associated with these agencies (see AdminService agencies endpoint to retrieve a list of agency slugs) | [optional] 
 **_date** | **date**| limit to content present on this date (YYYY-MM-DD) | [optional] 
 **last_modified_after** | **date**| limit to content last modified after this date (YYYY-MM-DD) | [optional] 
 **last_modified_on_or_after** | **date**| limit to content last modified on or after this date (YYYY-MM-DD) | [optional] 
 **last_modified_before** | **date**| limit to content last modified before this date (YYYY-MM-DD) | [optional] 
 **last_modified_on_or_before** | **date**| limit to content last modified on or before this date (YYYY-MM-DD) | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_search_v1_summary_get**
> object api_search_v1_summary_get(query=query, agency_slugs=agency_slugs, _date=_date, last_modified_after=last_modified_after, last_modified_on_or_after=last_modified_on_or_after, last_modified_before=last_modified_before, last_modified_on_or_before=last_modified_on_or_before)

Search summary details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchServiceApi()
query = 'query_example' # str | Search term; searches the headings and the full text (optional)
agency_slugs = ['agency_slugs_example'] # list[str] | limit to content currently associated with these agencies (see AdminService agencies endpoint to retrieve a list of agency slugs) (optional)
_date = '2013-10-20' # date | limit to content present on this date (YYYY-MM-DD) (optional)
last_modified_after = '2013-10-20' # date | limit to content last modified after this date (YYYY-MM-DD) (optional)
last_modified_on_or_after = '2013-10-20' # date | limit to content last modified on or after this date (YYYY-MM-DD) (optional)
last_modified_before = '2013-10-20' # date | limit to content last modified before this date (YYYY-MM-DD) (optional)
last_modified_on_or_before = '2013-10-20' # date | limit to content last modified on or before this date (YYYY-MM-DD) (optional)

try:
    # Search summary details
    api_response = api_instance.api_search_v1_summary_get(query=query, agency_slugs=agency_slugs, _date=_date, last_modified_after=last_modified_after, last_modified_on_or_after=last_modified_on_or_after, last_modified_before=last_modified_before, last_modified_on_or_before=last_modified_on_or_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchServiceApi->api_search_v1_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search term; searches the headings and the full text | [optional] 
 **agency_slugs** | [**list[str]**](str.md)| limit to content currently associated with these agencies (see AdminService agencies endpoint to retrieve a list of agency slugs) | [optional] 
 **_date** | **date**| limit to content present on this date (YYYY-MM-DD) | [optional] 
 **last_modified_after** | **date**| limit to content last modified after this date (YYYY-MM-DD) | [optional] 
 **last_modified_on_or_after** | **date**| limit to content last modified on or after this date (YYYY-MM-DD) | [optional] 
 **last_modified_before** | **date**| limit to content last modified before this date (YYYY-MM-DD) | [optional] 
 **last_modified_on_or_before** | **date**| limit to content last modified on or before this date (YYYY-MM-DD) | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

