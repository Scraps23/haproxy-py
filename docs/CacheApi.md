# swagger_client.CacheApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cache**](CacheApi.md#create_cache) | **POST** /services/haproxy/configuration/caches | Add a cache
[**delete_cache**](CacheApi.md#delete_cache) | **DELETE** /services/haproxy/configuration/caches/{name} | Delete a cache
[**get_cache**](CacheApi.md#get_cache) | **GET** /services/haproxy/configuration/caches/{name} | Return a cache
[**get_caches**](CacheApi.md#get_caches) | **GET** /services/haproxy/configuration/caches | Return an array of caches
[**replace_cache**](CacheApi.md#replace_cache) | **PUT** /services/haproxy/configuration/caches/{name} | Replace a cache

# **create_cache**
> Cache create_cache(body, transaction_id=transaction_id, version=version, force_reload=force_reload)

Add a cache

Adds a new cache section to the configuration file.

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
api_instance = dataplaneapi.CacheApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.Cache() # Cache | 
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Add a cache
    api_response = api_instance.create_cache(body, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CacheApi->create_cache: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Cache**](Cache.md)|  | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**Cache**](Cache.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cache**
> delete_cache(name, transaction_id=transaction_id, version=version, force_reload=force_reload)

Delete a cache

Deletes a cache from the configuration by it's name.

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
api_instance = dataplaneapi.CacheApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | Cache name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Delete a cache
    api_instance.delete_cache(name, transaction_id=transaction_id, version=version, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling CacheApi->delete_cache: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Cache name | 
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

# **get_cache**
> InlineResponse20013 get_cache(name, transaction_id=transaction_id)

Return a cache

Returns one cache section configuration by it's name.

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
api_instance = dataplaneapi.CacheApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | Cache name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return a cache
    api_response = api_instance.get_cache(name, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CacheApi->get_cache: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Cache name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_caches**
> InlineResponse20012 get_caches(transaction_id=transaction_id)

Return an array of caches

Returns an array of all configured caches.

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
api_instance = dataplaneapi.CacheApi(dataplaneapi.ApiClient(configuration))
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of caches
    api_response = api_instance.get_caches(transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CacheApi->get_caches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_cache**
> Cache replace_cache(body, name, transaction_id=transaction_id, version=version, force_reload=force_reload)

Replace a cache

Replaces a cache configuration by it's name.

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
api_instance = dataplaneapi.CacheApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.Cache() # Cache | 
name = 'name_example' # str | Cache name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace a cache
    api_response = api_instance.replace_cache(body, name, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CacheApi->replace_cache: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Cache**](Cache.md)|  | 
 **name** | **str**| Cache name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**Cache**](Cache.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

