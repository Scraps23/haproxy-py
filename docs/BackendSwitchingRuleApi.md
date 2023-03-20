# swagger_client.BackendSwitchingRuleApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_backend_switching_rule**](BackendSwitchingRuleApi.md#create_backend_switching_rule) | **POST** /services/haproxy/configuration/backend_switching_rules | Add a new Backend Switching Rule
[**delete_backend_switching_rule**](BackendSwitchingRuleApi.md#delete_backend_switching_rule) | **DELETE** /services/haproxy/configuration/backend_switching_rules/{index} | Delete a Backend Switching Rule
[**get_backend_switching_rule**](BackendSwitchingRuleApi.md#get_backend_switching_rule) | **GET** /services/haproxy/configuration/backend_switching_rules/{index} | Return one Backend Switching Rule
[**get_backend_switching_rules**](BackendSwitchingRuleApi.md#get_backend_switching_rules) | **GET** /services/haproxy/configuration/backend_switching_rules | Return an array of all Backend Switching Rules
[**replace_backend_switching_rule**](BackendSwitchingRuleApi.md#replace_backend_switching_rule) | **PUT** /services/haproxy/configuration/backend_switching_rules/{index} | Replace a Backend Switching Rule

# **create_backend_switching_rule**
> BackendSwitchingRule create_backend_switching_rule(body, frontend, transaction_id=transaction_id, version=version, force_reload=force_reload)

Add a new Backend Switching Rule

Adds a new Backend Switching Rule of the specified type in the specified frontend.

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
api_instance = dataplaneapi.BackendSwitchingRuleApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.BackendSwitchingRule() # BackendSwitchingRule | 
frontend = 'frontend_example' # str | Frontend name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Add a new Backend Switching Rule
    api_response = api_instance.create_backend_switching_rule(body, frontend, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackendSwitchingRuleApi->create_backend_switching_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BackendSwitchingRule**](BackendSwitchingRule.md)|  | 
 **frontend** | **str**| Frontend name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**BackendSwitchingRule**](BackendSwitchingRule.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_backend_switching_rule**
> delete_backend_switching_rule(index, frontend, transaction_id=transaction_id, version=version, force_reload=force_reload)

Delete a Backend Switching Rule

Deletes a Backend Switching Rule configuration by it's index from the specified frontend.

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
api_instance = dataplaneapi.BackendSwitchingRuleApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | Switching Rule Index
frontend = 'frontend_example' # str | Frontend name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Delete a Backend Switching Rule
    api_instance.delete_backend_switching_rule(index, frontend, transaction_id=transaction_id, version=version, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling BackendSwitchingRuleApi->delete_backend_switching_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| Switching Rule Index | 
 **frontend** | **str**| Frontend name | 
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

# **get_backend_switching_rule**
> InlineResponse2007 get_backend_switching_rule(index, frontend, transaction_id=transaction_id)

Return one Backend Switching Rule

Returns one Backend Switching Rule configuration by it's index in the specified frontend.

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
api_instance = dataplaneapi.BackendSwitchingRuleApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | Switching Rule Index
frontend = 'frontend_example' # str | Frontend name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return one Backend Switching Rule
    api_response = api_instance.get_backend_switching_rule(index, frontend, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackendSwitchingRuleApi->get_backend_switching_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| Switching Rule Index | 
 **frontend** | **str**| Frontend name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backend_switching_rules**
> InlineResponse2006 get_backend_switching_rules(frontend, transaction_id=transaction_id)

Return an array of all Backend Switching Rules

Returns all Backend Switching Rules that are configured in specified frontend.

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
api_instance = dataplaneapi.BackendSwitchingRuleApi(dataplaneapi.ApiClient(configuration))
frontend = 'frontend_example' # str | Frontend name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of all Backend Switching Rules
    api_response = api_instance.get_backend_switching_rules(frontend, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackendSwitchingRuleApi->get_backend_switching_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **frontend** | **str**| Frontend name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_backend_switching_rule**
> BackendSwitchingRule replace_backend_switching_rule(body, frontend, index, transaction_id=transaction_id, version=version, force_reload=force_reload)

Replace a Backend Switching Rule

Replaces a Backend Switching Rule configuration by it's index in the specified frontend.

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
api_instance = dataplaneapi.BackendSwitchingRuleApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.BackendSwitchingRule() # BackendSwitchingRule | 
frontend = 'frontend_example' # str | Frontend name
index = 56 # int | Switching Rule Index
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace a Backend Switching Rule
    api_response = api_instance.replace_backend_switching_rule(body, frontend, index, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackendSwitchingRuleApi->replace_backend_switching_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BackendSwitchingRule**](BackendSwitchingRule.md)|  | 
 **frontend** | **str**| Frontend name | 
 **index** | **int**| Switching Rule Index | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**BackendSwitchingRule**](BackendSwitchingRule.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

