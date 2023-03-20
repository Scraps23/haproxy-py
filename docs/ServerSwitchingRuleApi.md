# swagger_client.ServerSwitchingRuleApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_server_switching_rule**](ServerSwitchingRuleApi.md#create_server_switching_rule) | **POST** /services/haproxy/configuration/server_switching_rules | Add a new Server Switching Rule
[**delete_server_switching_rule**](ServerSwitchingRuleApi.md#delete_server_switching_rule) | **DELETE** /services/haproxy/configuration/server_switching_rules/{index} | Delete a Server Switching Rule
[**get_server_switching_rule**](ServerSwitchingRuleApi.md#get_server_switching_rule) | **GET** /services/haproxy/configuration/server_switching_rules/{index} | Return one Server Switching Rule
[**get_server_switching_rules**](ServerSwitchingRuleApi.md#get_server_switching_rules) | **GET** /services/haproxy/configuration/server_switching_rules | Return an array of all Server Switching Rules
[**replace_server_switching_rule**](ServerSwitchingRuleApi.md#replace_server_switching_rule) | **PUT** /services/haproxy/configuration/server_switching_rules/{index} | Replace a Server Switching Rule

# **create_server_switching_rule**
> ServerSwitchingRule create_server_switching_rule(body, backend, transaction_id=transaction_id, version=version, force_reload=force_reload)

Add a new Server Switching Rule

Adds a new Server Switching Rule of the specified type in the specified backend.

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
api_instance = dataplaneapi.ServerSwitchingRuleApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.ServerSwitchingRule() # ServerSwitchingRule | 
backend = 'backend_example' # str | Backend name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Add a new Server Switching Rule
    api_response = api_instance.create_server_switching_rule(body, backend, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSwitchingRuleApi->create_server_switching_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServerSwitchingRule**](ServerSwitchingRule.md)|  | 
 **backend** | **str**| Backend name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**ServerSwitchingRule**](ServerSwitchingRule.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_server_switching_rule**
> delete_server_switching_rule(index, backend, transaction_id=transaction_id, version=version, force_reload=force_reload)

Delete a Server Switching Rule

Deletes a Server Switching Rule configuration by it's index from the specified backend.

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
api_instance = dataplaneapi.ServerSwitchingRuleApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | Switching Rule Index
backend = 'backend_example' # str | Backend name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Delete a Server Switching Rule
    api_instance.delete_server_switching_rule(index, backend, transaction_id=transaction_id, version=version, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling ServerSwitchingRuleApi->delete_server_switching_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| Switching Rule Index | 
 **backend** | **str**| Backend name | 
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

# **get_server_switching_rule**
> InlineResponse20063 get_server_switching_rule(index, backend, transaction_id=transaction_id)

Return one Server Switching Rule

Returns one Server Switching Rule configuration by it's index in the specified backend.

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
api_instance = dataplaneapi.ServerSwitchingRuleApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | Switching Rule Index
backend = 'backend_example' # str | Backend name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return one Server Switching Rule
    api_response = api_instance.get_server_switching_rule(index, backend, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSwitchingRuleApi->get_server_switching_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| Switching Rule Index | 
 **backend** | **str**| Backend name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20063**](InlineResponse20063.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_switching_rules**
> InlineResponse20062 get_server_switching_rules(backend, transaction_id=transaction_id)

Return an array of all Server Switching Rules

Returns all Backend Switching Rules that are configured in specified backend.

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
api_instance = dataplaneapi.ServerSwitchingRuleApi(dataplaneapi.ApiClient(configuration))
backend = 'backend_example' # str | Backend name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of all Server Switching Rules
    api_response = api_instance.get_server_switching_rules(backend, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSwitchingRuleApi->get_server_switching_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backend** | **str**| Backend name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20062**](InlineResponse20062.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_server_switching_rule**
> ServerSwitchingRule replace_server_switching_rule(body, backend, index, transaction_id=transaction_id, version=version, force_reload=force_reload)

Replace a Server Switching Rule

Replaces a Server Switching Rule configuration by it's index in the specified backend.

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
api_instance = dataplaneapi.ServerSwitchingRuleApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.ServerSwitchingRule() # ServerSwitchingRule | 
backend = 'backend_example' # str | Backend name
index = 56 # int | Switching Rule Index
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace a Server Switching Rule
    api_response = api_instance.replace_server_switching_rule(body, backend, index, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSwitchingRuleApi->replace_server_switching_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServerSwitchingRule**](ServerSwitchingRule.md)|  | 
 **backend** | **str**| Backend name | 
 **index** | **int**| Switching Rule Index | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**ServerSwitchingRule**](ServerSwitchingRule.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

