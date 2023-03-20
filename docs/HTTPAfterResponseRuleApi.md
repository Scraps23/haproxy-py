# swagger_client.HTTPAfterResponseRuleApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_http_after_response_rule**](HTTPAfterResponseRuleApi.md#create_http_after_response_rule) | **POST** /services/haproxy/configuration/http_after_response_rules | Add a new HTTP After Response Rule
[**delete_http_after_response_rule**](HTTPAfterResponseRuleApi.md#delete_http_after_response_rule) | **DELETE** /services/haproxy/configuration/http_after_response_rules/{index} | Delete a HTTP After Response Rule
[**get_http_after_response_rule**](HTTPAfterResponseRuleApi.md#get_http_after_response_rule) | **GET** /services/haproxy/configuration/http_after_response_rules/{index} | Return one HTTP After Response Rule
[**get_http_after_response_rules**](HTTPAfterResponseRuleApi.md#get_http_after_response_rules) | **GET** /services/haproxy/configuration/http_after_response_rules | Return an array of all HTTP After Response Rules
[**replace_http_after_response_rule**](HTTPAfterResponseRuleApi.md#replace_http_after_response_rule) | **PUT** /services/haproxy/configuration/http_after_response_rules/{index} | Replace a HTTP After Response Rule

# **create_http_after_response_rule**
> HttpAfterResponseRule create_http_after_response_rule(body, parent_name, parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)

Add a new HTTP After Response Rule

Adds a new HTTP After Response Rule of the specified type in the specified parent.

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
api_instance = dataplaneapi.HTTPAfterResponseRuleApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.HttpAfterResponseRule() # HttpAfterResponseRule | 
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Add a new HTTP After Response Rule
    api_response = api_instance.create_http_after_response_rule(body, parent_name, parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HTTPAfterResponseRuleApi->create_http_after_response_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HttpAfterResponseRule**](HttpAfterResponseRule.md)|  | 
 **parent_name** | **str**| Parent name | 
 **parent_type** | **str**| Parent type | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**HttpAfterResponseRule**](HttpAfterResponseRule.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_http_after_response_rule**
> delete_http_after_response_rule(index, parent_name, parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)

Delete a HTTP After Response Rule

Deletes a HTTP After Response Rule configuration by it's index from the specified parent.

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
api_instance = dataplaneapi.HTTPAfterResponseRuleApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | HTTP After Response Rule Index
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Delete a HTTP After Response Rule
    api_instance.delete_http_after_response_rule(index, parent_name, parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling HTTPAfterResponseRuleApi->delete_http_after_response_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| HTTP After Response Rule Index | 
 **parent_name** | **str**| Parent name | 
 **parent_type** | **str**| Parent type | 
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

# **get_http_after_response_rule**
> InlineResponse20029 get_http_after_response_rule(index, parent_name, parent_type, transaction_id=transaction_id)

Return one HTTP After Response Rule

Returns one HTTP After Response Rule configuration by it's index in the specified parent.

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
api_instance = dataplaneapi.HTTPAfterResponseRuleApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | HTTP After Response Rule Index
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return one HTTP After Response Rule
    api_response = api_instance.get_http_after_response_rule(index, parent_name, parent_type, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HTTPAfterResponseRuleApi->get_http_after_response_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| HTTP After Response Rule Index | 
 **parent_name** | **str**| Parent name | 
 **parent_type** | **str**| Parent type | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_http_after_response_rules**
> InlineResponse20028 get_http_after_response_rules(parent_name, parent_type, transaction_id=transaction_id)

Return an array of all HTTP After Response Rules

Returns all HTTP After Response Rules that are configured in specified parent.

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
api_instance = dataplaneapi.HTTPAfterResponseRuleApi(dataplaneapi.ApiClient(configuration))
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of all HTTP After Response Rules
    api_response = api_instance.get_http_after_response_rules(parent_name, parent_type, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HTTPAfterResponseRuleApi->get_http_after_response_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_name** | **str**| Parent name | 
 **parent_type** | **str**| Parent type | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_http_after_response_rule**
> HttpAfterResponseRule replace_http_after_response_rule(body, parent_name, parent_type, index, transaction_id=transaction_id, version=version, force_reload=force_reload)

Replace a HTTP After Response Rule

Replaces a HTTP After Response Rule configuration by it's index in the specified parent.

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
api_instance = dataplaneapi.HTTPAfterResponseRuleApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.HttpAfterResponseRule() # HttpAfterResponseRule | 
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
index = 56 # int | HTTP After Response Rule Index
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace a HTTP After Response Rule
    api_response = api_instance.replace_http_after_response_rule(body, parent_name, parent_type, index, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HTTPAfterResponseRuleApi->replace_http_after_response_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HttpAfterResponseRule**](HttpAfterResponseRule.md)|  | 
 **parent_name** | **str**| Parent name | 
 **parent_type** | **str**| Parent type | 
 **index** | **int**| HTTP After Response Rule Index | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**HttpAfterResponseRule**](HttpAfterResponseRule.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

