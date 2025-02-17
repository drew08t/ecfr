# swagger_client.AdminServiceApi

All URIs are relative to *www.ecfr.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_admin_v1_agencies_json_get**](AdminServiceApi.md#api_admin_v1_agencies_json_get) | **GET** /api/admin/v1/agencies.json | Agencies
[**api_admin_v1_corrections_json_get**](AdminServiceApi.md#api_admin_v1_corrections_json_get) | **GET** /api/admin/v1/corrections.json | Corrections route returns all eCFR corrections.
[**api_admin_v1_corrections_title_title_json_get**](AdminServiceApi.md#api_admin_v1_corrections_title_title_json_get) | **GET** /api/admin/v1/corrections/title/{title}.json | Corrections title route returns all corrections for the supplied title.

# **api_admin_v1_agencies_json_get**
> object api_admin_v1_agencies_json_get()

Agencies

All top-level agencies in name order with children also in name order

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminServiceApi()

try:
    # Agencies
    api_response = api_instance.api_admin_v1_agencies_json_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminServiceApi->api_admin_v1_agencies_json_get: %s\n" % e)
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

# **api_admin_v1_corrections_json_get**
> object api_admin_v1_corrections_json_get(_date=_date, title=title, error_corrected_date=error_corrected_date)

Corrections route returns all eCFR corrections.

The Corrections service can be used to determine all corrections or can be filtered by title, effective date, or correction date. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminServiceApi()
_date = '2013-10-20' # date | Restricts results to eCFR corrections that occurred on or before the specified date and that were corrected on or after the specified date. Format: YYYY-MM-DD (optional)
title = 'title_example' # str | Restricts results to the given title number: Format: '1', '2', '50', etc (optional)
error_corrected_date = '2013-10-20' # date | Returns only corrections that were corrected on the given date. Format: YYYY-MM-DD (optional)

try:
    # Corrections route returns all eCFR corrections.
    api_response = api_instance.api_admin_v1_corrections_json_get(_date=_date, title=title, error_corrected_date=error_corrected_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminServiceApi->api_admin_v1_corrections_json_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **date**| Restricts results to eCFR corrections that occurred on or before the specified date and that were corrected on or after the specified date. Format: YYYY-MM-DD | [optional] 
 **title** | **str**| Restricts results to the given title number: Format: &#x27;1&#x27;, &#x27;2&#x27;, &#x27;50&#x27;, etc | [optional] 
 **error_corrected_date** | **date**| Returns only corrections that were corrected on the given date. Format: YYYY-MM-DD | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_admin_v1_corrections_title_title_json_get**
> object api_admin_v1_corrections_title_title_json_get(title)

Corrections title route returns all corrections for the supplied title.

The Corrections service can be used to determine all corrections for the given title.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminServiceApi()
title = 'title_example' # str | Restricts results to the given title number: Format: '1', '2', '50', etc

try:
    # Corrections title route returns all corrections for the supplied title.
    api_response = api_instance.api_admin_v1_corrections_title_title_json_get(title)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminServiceApi->api_admin_v1_corrections_title_title_json_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| Restricts results to the given title number: Format: &#x27;1&#x27;, &#x27;2&#x27;, &#x27;50&#x27;, etc | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

