# swagger_client.InformationApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_haproxy_process_info**](InformationApi.md#get_haproxy_process_info) | **GET** /services/haproxy/runtime/info | Return HAProxy process information
[**get_info**](InformationApi.md#get_info) | **GET** /info | Return API, hardware and OS information

# **get_haproxy_process_info**
> ProcessInfos get_haproxy_process_info()

Return HAProxy process information

Return HAProxy process information

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
api_instance = dataplaneapi.InformationApi(dataplaneapi.ApiClient(configuration))

try:
    # Return HAProxy process information
    api_response = api_instance.get_haproxy_process_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InformationApi->get_haproxy_process_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProcessInfos**](ProcessInfos.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_info**
> Info get_info()

Return API, hardware and OS information

Return API, hardware and OS information

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
api_instance = dataplaneapi.InformationApi(dataplaneapi.ApiClient(configuration))

try:
    # Return API, hardware and OS information
    api_response = api_instance.get_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InformationApi->get_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Info**](Info.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

