# swagger_client.SpecificationOpenapiv3Api

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_openapiv3_specification**](SpecificationOpenapiv3Api.md#get_openapiv3_specification) | **GET** /specification_openapiv3 | Data Plane API v3 Specification

# **get_openapiv3_specification**
> object get_openapiv3_specification()

Data Plane API v3 Specification

Return Data Plane API OpenAPI v3 specification

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
api_instance = dataplaneapi.SpecificationOpenapiv3Api(dataplaneapi.ApiClient(configuration))

try:
    # Data Plane API v3 Specification
    api_response = api_instance.get_openapiv3_specification()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecificationOpenapiv3Api->get_openapiv3_specification: %s\n" % e)
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

