# swagger_client.StatsApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stats**](StatsApi.md#get_stats) | **GET** /services/haproxy/stats/native | Gets stats

# **get_stats**
> NativeStats get_stats(type=type, name=name, parent=parent)

Gets stats

Getting stats from the HAProxy.

### Example

```python
from __future__ import print_function
import time
import dataplaneapi
from dataplaneapi.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic_auth
configuration = dataplaneapi.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = dataplaneapi.StatsApi(dataplaneapi.ApiClient(configuration))
type = 'type_example' # str | Object type to get stats for (one of frontend, backend, server) (optional)
name = 'name_example' # str | Object name to get stats for (optional)
parent = 'parent_example' # str | Object parent name to get stats for, in case the object is a server (optional)

try:
    # Gets stats
    api_response = api_instance.get_stats(type=type, name=name, parent=parent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Object type to get stats for (one of frontend, backend, server) | [optional] 
 **name** | **str**| Object name to get stats for | [optional] 
 **parent** | **str**| Object parent name to get stats for, in case the object is a server | [optional] 

### Return type

[**NativeStats**](NativeStats.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

