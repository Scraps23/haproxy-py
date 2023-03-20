# swagger_client.HealthApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health**](HealthApi.md#get_health) | **GET** /health | Return managed services health

# **get_health**
> Health get_health()

Return managed services health

Return managed services health

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
api_instance = dataplaneapi.HealthApi(dataplaneapi.ApiClient(configuration))

try:
    # Return managed services health
    api_response = api_instance.get_health()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->get_health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Health**](Health.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

