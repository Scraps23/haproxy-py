# swagger_client.ReloadsApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reload**](ReloadsApi.md#get_reload) | **GET** /services/haproxy/reloads/{id} | Return one HAProxy reload status
[**get_reloads**](ReloadsApi.md#get_reloads) | **GET** /services/haproxy/reloads | Return list of HAProxy Reloads.

# **get_reload**
> Reload get_reload(id)

Return one HAProxy reload status

Returns one HAProxy reload status.

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
api_instance = dataplaneapi.ReloadsApi(dataplaneapi.ApiClient(configuration))
id = 'id_example' # str | Reload id

try:
    # Return one HAProxy reload status
    api_response = api_instance.get_reload(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReloadsApi->get_reload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Reload id | 

### Return type

[**Reload**](Reload.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reloads**
> Reloads get_reloads()

Return list of HAProxy Reloads.

Returns a list of HAProxy reloads.

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
api_instance = dataplaneapi.ReloadsApi(dataplaneapi.ApiClient(configuration))

try:
    # Return list of HAProxy Reloads.
    api_response = api_instance.get_reloads()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReloadsApi->get_reloads: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Reloads**](Reloads.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

