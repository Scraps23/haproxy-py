# swagger_client.HTTPCheckApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_http_check**](HTTPCheckApi.md#create_http_check) | **POST** /services/haproxy/configuration/http_checks | Add a new HTTP check
[**delete_http_check**](HTTPCheckApi.md#delete_http_check) | **DELETE** /services/haproxy/configuration/http_checks/{index} | Delete a HTTP check
[**get_http_check**](HTTPCheckApi.md#get_http_check) | **GET** /services/haproxy/configuration/http_checks/{index} | Return one HTTP check
[**get_http_checks**](HTTPCheckApi.md#get_http_checks) | **GET** /services/haproxy/configuration/http_checks | Return an array of HTTP checks
[**replace_http_check**](HTTPCheckApi.md#replace_http_check) | **PUT** /services/haproxy/configuration/http_checks/{index} | Replace a HTTP check

# **create_http_check**
> HttpCheck create_http_check(body, parent_type, parent_name=parent_name, transaction_id=transaction_id, version=version, force_reload=force_reload)

Add a new HTTP check

Adds a new HTTP check of the specified type in the specified parent.

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
api_instance = dataplaneapi.HTTPCheckApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.HttpCheck() # HttpCheck | 
parent_type = 'parent_type_example' # str | Parent type
parent_name = 'parent_name_example' # str | Parent name (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Add a new HTTP check
    api_response = api_instance.create_http_check(body, parent_type, parent_name=parent_name, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HTTPCheckApi->create_http_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HttpCheck**](HttpCheck.md)|  | 
 **parent_type** | **str**| Parent type | 
 **parent_name** | **str**| Parent name | [optional] 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**HttpCheck**](HttpCheck.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_http_check**
> delete_http_check(index, parent_type, parent_name=parent_name, transaction_id=transaction_id, version=version, force_reload=force_reload)

Delete a HTTP check

Deletes a HTTP check configuration by it's index from the specified parent.

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
api_instance = dataplaneapi.HTTPCheckApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | HTTP check Index
parent_type = 'parent_type_example' # str | Parent type
parent_name = 'parent_name_example' # str | Parent name (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Delete a HTTP check
    api_instance.delete_http_check(index, parent_type, parent_name=parent_name, transaction_id=transaction_id, version=version, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling HTTPCheckApi->delete_http_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| HTTP check Index | 
 **parent_type** | **str**| Parent type | 
 **parent_name** | **str**| Parent name | [optional] 
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

# **get_http_check**
> InlineResponse20031 get_http_check(index, parent_type, parent_name=parent_name, transaction_id=transaction_id)

Return one HTTP check

Returns one HTTP check configuration by it's index in the specified parent.

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
api_instance = dataplaneapi.HTTPCheckApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | HTTP Check Index
parent_type = 'parent_type_example' # str | Parent type
parent_name = 'parent_name_example' # str | Parent name (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return one HTTP check
    api_response = api_instance.get_http_check(index, parent_type, parent_name=parent_name, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HTTPCheckApi->get_http_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| HTTP Check Index | 
 **parent_type** | **str**| Parent type | 
 **parent_name** | **str**| Parent name | [optional] 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_http_checks**
> InlineResponse20030 get_http_checks(parent_type, parent_name=parent_name, transaction_id=transaction_id)

Return an array of HTTP checks

Returns all HTTP checks that are configured in specified parent.

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
api_instance = dataplaneapi.HTTPCheckApi(dataplaneapi.ApiClient(configuration))
parent_type = 'parent_type_example' # str | Parent type
parent_name = 'parent_name_example' # str | Parent name (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of HTTP checks
    api_response = api_instance.get_http_checks(parent_type, parent_name=parent_name, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HTTPCheckApi->get_http_checks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_type** | **str**| Parent type | 
 **parent_name** | **str**| Parent name | [optional] 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_http_check**
> HttpCheck replace_http_check(body, parent_type, index, parent_name=parent_name, transaction_id=transaction_id, version=version, force_reload=force_reload)

Replace a HTTP check

Replaces a HTTP Check configuration by it's index in the specified parent.

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
api_instance = dataplaneapi.HTTPCheckApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.HttpCheck() # HttpCheck | 
parent_type = 'parent_type_example' # str | Parent type
index = 56 # int | HTTP Check Index
parent_name = 'parent_name_example' # str | Parent name (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace a HTTP check
    api_response = api_instance.replace_http_check(body, parent_type, index, parent_name=parent_name, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HTTPCheckApi->replace_http_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HttpCheck**](HttpCheck.md)|  | 
 **parent_type** | **str**| Parent type | 
 **index** | **int**| HTTP Check Index | 
 **parent_name** | **str**| Parent name | [optional] 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**HttpCheck**](HttpCheck.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

