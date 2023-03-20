# swagger_client.DgramBindApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dgram_bind**](DgramBindApi.md#create_dgram_bind) | **POST** /services/haproxy/configuration/dgram_binds | Add a new dgram bind
[**delete_dgram_bind**](DgramBindApi.md#delete_dgram_bind) | **DELETE** /services/haproxy/configuration/dgram_binds/{name} | Delete a dgram bind
[**get_dgram_bind**](DgramBindApi.md#get_dgram_bind) | **GET** /services/haproxy/configuration/dgram_binds/{name} | Return one dgram bind
[**get_dgram_binds**](DgramBindApi.md#get_dgram_binds) | **GET** /services/haproxy/configuration/dgram_binds | Return an array of dgram binds
[**replace_dgram_bind**](DgramBindApi.md#replace_dgram_bind) | **PUT** /services/haproxy/configuration/dgram_binds/{name} | Replace a dgram bind

# **create_dgram_bind**
> DgramBind create_dgram_bind(body, log_forward, transaction_id=transaction_id, version=version, force_reload=force_reload)

Add a new dgram bind

Adds a new dgram bind in the specified log forward in the configuration file.

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
api_instance = dataplaneapi.DgramBindApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.DgramBind() # DgramBind | 
log_forward = 'log_forward_example' # str | Parent log forward name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Add a new dgram bind
    api_response = api_instance.create_dgram_bind(body, log_forward, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DgramBindApi->create_dgram_bind: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DgramBind**](DgramBind.md)|  | 
 **log_forward** | **str**| Parent log forward name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**DgramBind**](DgramBind.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dgram_bind**
> delete_dgram_bind(name, log_forward, transaction_id=transaction_id, version=version, force_reload=force_reload)

Delete a dgram bind

Deletes a dgram bind configuration by it's name in the specified log forward.

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
api_instance = dataplaneapi.DgramBindApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | Bind name
log_forward = 'log_forward_example' # str | Parent log forward name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Delete a dgram bind
    api_instance.delete_dgram_bind(name, log_forward, transaction_id=transaction_id, version=version, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling DgramBindApi->delete_dgram_bind: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Bind name | 
 **log_forward** | **str**| Parent log forward name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dgram_bind**
> InlineResponse20018 get_dgram_bind(name, log_forward, transaction_id=transaction_id)

Return one dgram bind

Returns one dgram bind configuration by it's name in the specified log forward.

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
api_instance = dataplaneapi.DgramBindApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | Bind name
log_forward = 'log_forward_example' # str | Parent log forward name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return one dgram bind
    api_response = api_instance.get_dgram_bind(name, log_forward, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DgramBindApi->get_dgram_bind: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Bind name | 
 **log_forward** | **str**| Parent log forward name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dgram_binds**
> InlineResponse20017 get_dgram_binds(log_forward, transaction_id=transaction_id)

Return an array of dgram binds

Returns an array of all dgram binds that are configured in specified log forward.

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
api_instance = dataplaneapi.DgramBindApi(dataplaneapi.ApiClient(configuration))
log_forward = 'log_forward_example' # str | Parent log forward name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of dgram binds
    api_response = api_instance.get_dgram_binds(log_forward, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DgramBindApi->get_dgram_binds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_forward** | **str**| Parent log forward name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_dgram_bind**
> DgramBind replace_dgram_bind(body, log_forward, name, transaction_id=transaction_id, version=version, force_reload=force_reload)

Replace a dgram bind

Replaces a dgram bind configuration by it's name in the specified log forward.

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
api_instance = dataplaneapi.DgramBindApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.DgramBind() # DgramBind | 
log_forward = 'log_forward_example' # str | Parent log forward name
name = 'name_example' # str | Bind name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace a dgram bind
    api_response = api_instance.replace_dgram_bind(body, log_forward, name, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DgramBindApi->replace_dgram_bind: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DgramBind**](DgramBind.md)|  | 
 **log_forward** | **str**| Parent log forward name | 
 **name** | **str**| Bind name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**DgramBind**](DgramBind.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

