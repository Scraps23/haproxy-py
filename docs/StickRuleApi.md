# swagger_client.StickRuleApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stick_rule**](StickRuleApi.md#create_stick_rule) | **POST** /services/haproxy/configuration/stick_rules | Add a new Stick Rule
[**delete_stick_rule**](StickRuleApi.md#delete_stick_rule) | **DELETE** /services/haproxy/configuration/stick_rules/{index} | Delete a Stick Rule
[**get_stick_rule**](StickRuleApi.md#get_stick_rule) | **GET** /services/haproxy/configuration/stick_rules/{index} | Return one Stick Rule
[**get_stick_rules**](StickRuleApi.md#get_stick_rules) | **GET** /services/haproxy/configuration/stick_rules | Return an array of all Stick Rules
[**replace_stick_rule**](StickRuleApi.md#replace_stick_rule) | **PUT** /services/haproxy/configuration/stick_rules/{index} | Replace a Stick Rule

# **create_stick_rule**
> StickRule create_stick_rule(body, backend, transaction_id=transaction_id, version=version, force_reload=force_reload)

Add a new Stick Rule

Adds a new Stick Rule of the specified type in the specified backend.

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
api_instance = dataplaneapi.StickRuleApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.StickRule() # StickRule | 
backend = 'backend_example' # str | Backend name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Add a new Stick Rule
    api_response = api_instance.create_stick_rule(body, backend, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StickRuleApi->create_stick_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StickRule**](StickRule.md)|  | 
 **backend** | **str**| Backend name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**StickRule**](StickRule.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stick_rule**
> delete_stick_rule(index, backend, transaction_id=transaction_id, version=version, force_reload=force_reload)

Delete a Stick Rule

Deletes a Stick Rule configuration by it's index from the specified backend.

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
api_instance = dataplaneapi.StickRuleApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | Stick Rule Index
backend = 'backend_example' # str | Backend name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Delete a Stick Rule
    api_instance.delete_stick_rule(index, backend, transaction_id=transaction_id, version=version, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling StickRuleApi->delete_stick_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| Stick Rule Index | 
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

# **get_stick_rule**
> InlineResponse20069 get_stick_rule(index, backend, transaction_id=transaction_id)

Return one Stick Rule

Returns one Stick Rule configuration by it's index in the specified backend.

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
api_instance = dataplaneapi.StickRuleApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | Stick Rule Index
backend = 'backend_example' # str | Backend name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return one Stick Rule
    api_response = api_instance.get_stick_rule(index, backend, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StickRuleApi->get_stick_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| Stick Rule Index | 
 **backend** | **str**| Backend name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20069**](InlineResponse20069.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stick_rules**
> InlineResponse20068 get_stick_rules(backend, transaction_id=transaction_id)

Return an array of all Stick Rules

Returns all Stick Rules that are configured in specified backend.

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
api_instance = dataplaneapi.StickRuleApi(dataplaneapi.ApiClient(configuration))
backend = 'backend_example' # str | Backend name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of all Stick Rules
    api_response = api_instance.get_stick_rules(backend, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StickRuleApi->get_stick_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backend** | **str**| Backend name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20068**](InlineResponse20068.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_stick_rule**
> StickRule replace_stick_rule(body, backend, index, transaction_id=transaction_id, version=version, force_reload=force_reload)

Replace a Stick Rule

Replaces a Stick Rule configuration by it's index in the specified backend.

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
api_instance = dataplaneapi.StickRuleApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.StickRule() # StickRule | 
backend = 'backend_example' # str | Backend name
index = 56 # int | Stick Rule Index
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace a Stick Rule
    api_response = api_instance.replace_stick_rule(body, backend, index, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StickRuleApi->replace_stick_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StickRule**](StickRule.md)|  | 
 **backend** | **str**| Backend name | 
 **index** | **int**| Stick Rule Index | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**StickRule**](StickRule.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

