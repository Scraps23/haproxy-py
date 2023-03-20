# swagger_client.GlobalApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_global**](GlobalApi.md#get_global) | **GET** /services/haproxy/configuration/global | Return a global part of configuration
[**replace_global**](GlobalApi.md#replace_global) | **PUT** /services/haproxy/configuration/global | Replace global

# **get_global**
> InlineResponse20025 get_global(transaction_id=transaction_id)

Return a global part of configuration

Returns global part of configuration.

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
api_instance = dataplaneapi.GlobalApi(dataplaneapi.ApiClient(configuration))
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return a global part of configuration
    api_response = api_instance.get_global(transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlobalApi->get_global: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_global**
> ModelGlobal replace_global(body, transaction_id=transaction_id, version=version, force_reload=force_reload)

Replace global

Replace global part of config

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
api_instance = dataplaneapi.GlobalApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.ModelGlobal() # ModelGlobal | 
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace global
    api_response = api_instance.replace_global(body, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlobalApi->replace_global: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelGlobal**](ModelGlobal.md)|  | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**ModelGlobal**](ModelGlobal.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

