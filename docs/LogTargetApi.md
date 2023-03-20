# swagger_client.LogTargetApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_log_target**](LogTargetApi.md#create_log_target) | **POST** /services/haproxy/configuration/log_targets | Add a new Log Target
[**delete_log_target**](LogTargetApi.md#delete_log_target) | **DELETE** /services/haproxy/configuration/log_targets/{index} | Delete a Log Target
[**get_log_target**](LogTargetApi.md#get_log_target) | **GET** /services/haproxy/configuration/log_targets/{index} | Return one Log Target
[**get_log_targets**](LogTargetApi.md#get_log_targets) | **GET** /services/haproxy/configuration/log_targets | Return an array of all Log Targets
[**replace_log_target**](LogTargetApi.md#replace_log_target) | **PUT** /services/haproxy/configuration/log_targets/{index} | Replace a Log Target

# **create_log_target**
> LogTarget create_log_target(body, parent_type, parent_name=parent_name, transaction_id=transaction_id, version=version, force_reload=force_reload)

Add a new Log Target

Adds a new Log Target of the specified type in the specified parent.

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
api_instance = dataplaneapi.LogTargetApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.LogTarget() # LogTarget | 
parent_type = 'parent_type_example' # str | Parent type
parent_name = 'parent_name_example' # str | Parent name (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Add a new Log Target
    api_response = api_instance.create_log_target(body, parent_type, parent_name=parent_name, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogTargetApi->create_log_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogTarget**](LogTarget.md)|  | 
 **parent_type** | **str**| Parent type | 
 **parent_name** | **str**| Parent name | [optional] 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**LogTarget**](LogTarget.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_log_target**
> delete_log_target(index, parent_type, parent_name=parent_name, transaction_id=transaction_id, version=version, force_reload=force_reload)

Delete a Log Target

Deletes a Log Target configuration by it's index from the specified parent.

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
api_instance = dataplaneapi.LogTargetApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | Log Target Index
parent_type = 'parent_type_example' # str | Parent type
parent_name = 'parent_name_example' # str | Parent name (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Delete a Log Target
    api_instance.delete_log_target(index, parent_type, parent_name=parent_name, transaction_id=transaction_id, version=version, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling LogTargetApi->delete_log_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| Log Target Index | 
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

# **get_log_target**
> InlineResponse20043 get_log_target(index, parent_type, parent_name=parent_name, transaction_id=transaction_id)

Return one Log Target

Returns one Log Target configuration by it's index in the specified parent.

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
api_instance = dataplaneapi.LogTargetApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | Log Target Index
parent_type = 'parent_type_example' # str | Parent type
parent_name = 'parent_name_example' # str | Parent name (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return one Log Target
    api_response = api_instance.get_log_target(index, parent_type, parent_name=parent_name, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogTargetApi->get_log_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| Log Target Index | 
 **parent_type** | **str**| Parent type | 
 **parent_name** | **str**| Parent name | [optional] 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_targets**
> InlineResponse20042 get_log_targets(parent_type, parent_name=parent_name, transaction_id=transaction_id)

Return an array of all Log Targets

Returns all Log Targets that are configured in specified parent.

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
api_instance = dataplaneapi.LogTargetApi(dataplaneapi.ApiClient(configuration))
parent_type = 'parent_type_example' # str | Parent type
parent_name = 'parent_name_example' # str | Parent name (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of all Log Targets
    api_response = api_instance.get_log_targets(parent_type, parent_name=parent_name, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogTargetApi->get_log_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_type** | **str**| Parent type | 
 **parent_name** | **str**| Parent name | [optional] 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_log_target**
> LogTarget replace_log_target(body, parent_type, index, parent_name=parent_name, transaction_id=transaction_id, version=version, force_reload=force_reload)

Replace a Log Target

Replaces a Log Target configuration by it's index in the specified parent.

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
api_instance = dataplaneapi.LogTargetApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.LogTarget() # LogTarget | 
parent_type = 'parent_type_example' # str | Parent type
index = 56 # int | Log Target Index
parent_name = 'parent_name_example' # str | Parent name (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace a Log Target
    api_response = api_instance.replace_log_target(body, parent_type, index, parent_name=parent_name, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogTargetApi->replace_log_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogTarget**](LogTarget.md)|  | 
 **parent_type** | **str**| Parent type | 
 **index** | **int**| Log Target Index | 
 **parent_name** | **str**| Parent name | [optional] 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**LogTarget**](LogTarget.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

