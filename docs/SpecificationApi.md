# swagger_client.SpecificationApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_specification**](SpecificationApi.md#get_specification) | **GET** /specification | Data Plane API Specification

# **get_specification**
> object get_specification()

Data Plane API Specification

Return Data Plane API OpenAPI specification

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
api_instance = dataplaneapi.SpecificationApi(dataplaneapi.ApiClient(configuration))

try:
    # Data Plane API Specification
    api_response = api_instance.get_specification()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecificationApi->get_specification: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

