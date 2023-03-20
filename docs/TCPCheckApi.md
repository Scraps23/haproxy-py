# swagger_client.TCPCheckApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tcp_check**](TCPCheckApi.md#create_tcp_check) | **POST** /services/haproxy/configuration/tcp_checks | Add a new TCP check
[**delete_tcp_check**](TCPCheckApi.md#delete_tcp_check) | **DELETE** /services/haproxy/configuration/tcp_checks/{index} | Delete a TCP check
[**get_tcp_check**](TCPCheckApi.md#get_tcp_check) | **GET** /services/haproxy/configuration/tcp_checks/{index} | Return one TCP check
[**get_tcp_checks**](TCPCheckApi.md#get_tcp_checks) | **GET** /services/haproxy/configuration/tcp_checks | Return an array of TCP checks
[**replace_tcp_check**](TCPCheckApi.md#replace_tcp_check) | **PUT** /services/haproxy/configuration/tcp_checks/{index} | Replace a TCP check

# **create_tcp_check**
> TcpCheck create_tcp_check(body, parent_type, parent_name=parent_name, transaction_id=transaction_id, version=version, force_reload=force_reload)

Add a new TCP check

Adds a new TCP check of the specified type in the specified parent.

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
api_instance = dataplaneapi.TCPCheckApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.TcpCheck() # TcpCheck | 
parent_type = 'parent_type_example' # str | Parent type
parent_name = 'parent_name_example' # str | Parent name (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Add a new TCP check
    api_response = api_instance.create_tcp_check(body, parent_type, parent_name=parent_name, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TCPCheckApi->create_tcp_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TcpCheck**](TcpCheck.md)|  | 
 **parent_type** | **str**| Parent type | 
 **parent_name** | **str**| Parent name | [optional] 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**TcpCheck**](TcpCheck.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tcp_check**
> delete_tcp_check(index, parent_type, parent_name=parent_name, transaction_id=transaction_id, version=version, force_reload=force_reload)

Delete a TCP check

Deletes a TCP check configuration by it's index from the specified parent.

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
api_instance = dataplaneapi.TCPCheckApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | TCP check Index
parent_type = 'parent_type_example' # str | Parent type
parent_name = 'parent_name_example' # str | Parent name (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Delete a TCP check
    api_instance.delete_tcp_check(index, parent_type, parent_name=parent_name, transaction_id=transaction_id, version=version, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling TCPCheckApi->delete_tcp_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| TCP check Index | 
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

# **get_tcp_check**
> InlineResponse20071 get_tcp_check(index, parent_type, parent_name=parent_name, transaction_id=transaction_id)

Return one TCP check

Returns one TCP check configuration by it's index in the specified parent.

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
api_instance = dataplaneapi.TCPCheckApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | TCP Check Index
parent_type = 'parent_type_example' # str | Parent type
parent_name = 'parent_name_example' # str | Parent name (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return one TCP check
    api_response = api_instance.get_tcp_check(index, parent_type, parent_name=parent_name, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TCPCheckApi->get_tcp_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| TCP Check Index | 
 **parent_type** | **str**| Parent type | 
 **parent_name** | **str**| Parent name | [optional] 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20071**](InlineResponse20071.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tcp_checks**
> InlineResponse20070 get_tcp_checks(parent_type, parent_name=parent_name, transaction_id=transaction_id)

Return an array of TCP checks

Returns all TCP checks that are configured in specified parent.

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
api_instance = dataplaneapi.TCPCheckApi(dataplaneapi.ApiClient(configuration))
parent_type = 'parent_type_example' # str | Parent type
parent_name = 'parent_name_example' # str | Parent name (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of TCP checks
    api_response = api_instance.get_tcp_checks(parent_type, parent_name=parent_name, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TCPCheckApi->get_tcp_checks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_type** | **str**| Parent type | 
 **parent_name** | **str**| Parent name | [optional] 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20070**](InlineResponse20070.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_tcp_check**
> TcpCheck replace_tcp_check(body, parent_type, index, parent_name=parent_name, transaction_id=transaction_id, version=version, force_reload=force_reload)

Replace a TCP check

Replaces a TCP Check configuration by it's index in the specified parent.

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
api_instance = dataplaneapi.TCPCheckApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.TcpCheck() # TcpCheck | 
parent_type = 'parent_type_example' # str | Parent type
index = 56 # int | TCP Check Index
parent_name = 'parent_name_example' # str | Parent name (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace a TCP check
    api_response = api_instance.replace_tcp_check(body, parent_type, index, parent_name=parent_name, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TCPCheckApi->replace_tcp_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TcpCheck**](TcpCheck.md)|  | 
 **parent_type** | **str**| Parent type | 
 **index** | **int**| TCP Check Index | 
 **parent_name** | **str**| Parent name | [optional] 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**TcpCheck**](TcpCheck.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

