# swagger_client.HTTPResponseRuleApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_http_response_rule**](HTTPResponseRuleApi.md#create_http_response_rule) | **POST** /services/haproxy/configuration/http_response_rules | Add a new HTTP Response Rule
[**delete_http_response_rule**](HTTPResponseRuleApi.md#delete_http_response_rule) | **DELETE** /services/haproxy/configuration/http_response_rules/{index} | Delete a HTTP Response Rule
[**get_http_response_rule**](HTTPResponseRuleApi.md#get_http_response_rule) | **GET** /services/haproxy/configuration/http_response_rules/{index} | Return one HTTP Response Rule
[**get_http_response_rules**](HTTPResponseRuleApi.md#get_http_response_rules) | **GET** /services/haproxy/configuration/http_response_rules | Return an array of all HTTP Response Rules
[**replace_http_response_rule**](HTTPResponseRuleApi.md#replace_http_response_rule) | **PUT** /services/haproxy/configuration/http_response_rules/{index} | Replace a HTTP Response Rule

# **create_http_response_rule**
> HttpResponseRule create_http_response_rule(body, parent_name, parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)

Add a new HTTP Response Rule

Adds a new HTTP Response Rule of the specified type in the specified parent.

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
api_instance = dataplaneapi.HTTPResponseRuleApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.HttpResponseRule() # HttpResponseRule | 
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Add a new HTTP Response Rule
    api_response = api_instance.create_http_response_rule(body, parent_name, parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HTTPResponseRuleApi->create_http_response_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HttpResponseRule**](HttpResponseRule.md)|  | 
 **parent_name** | **str**| Parent name | 
 **parent_type** | **str**| Parent type | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**HttpResponseRule**](HttpResponseRule.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_http_response_rule**
> delete_http_response_rule(index, parent_name, parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)

Delete a HTTP Response Rule

Deletes a HTTP Response Rule configuration by it's index from the specified parent.

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
api_instance = dataplaneapi.HTTPResponseRuleApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | HTTP Response Rule Index
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Delete a HTTP Response Rule
    api_instance.delete_http_response_rule(index, parent_name, parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling HTTPResponseRuleApi->delete_http_response_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| HTTP Response Rule Index | 
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

# **get_http_response_rule**
> InlineResponse20039 get_http_response_rule(index, parent_name, parent_type, transaction_id=transaction_id)

Return one HTTP Response Rule

Returns one HTTP Response Rule configuration by it's index in the specified parent.

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
api_instance = dataplaneapi.HTTPResponseRuleApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | HTTP Response Rule Index
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return one HTTP Response Rule
    api_response = api_instance.get_http_response_rule(index, parent_name, parent_type, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HTTPResponseRuleApi->get_http_response_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| HTTP Response Rule Index | 
 **parent_name** | **str**| Parent name | 
 **parent_type** | **str**| Parent type | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_http_response_rules**
> InlineResponse20038 get_http_response_rules(parent_name, parent_type, transaction_id=transaction_id)

Return an array of all HTTP Response Rules

Returns all HTTP Response Rules that are configured in specified parent.

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
api_instance = dataplaneapi.HTTPResponseRuleApi(dataplaneapi.ApiClient(configuration))
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of all HTTP Response Rules
    api_response = api_instance.get_http_response_rules(parent_name, parent_type, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HTTPResponseRuleApi->get_http_response_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_name** | **str**| Parent name | 
 **parent_type** | **str**| Parent type | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_http_response_rule**
> HttpResponseRule replace_http_response_rule(body, parent_name, parent_type, index, transaction_id=transaction_id, version=version, force_reload=force_reload)

Replace a HTTP Response Rule

Replaces a HTTP Response Rule configuration by it's index in the specified parent.

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
api_instance = dataplaneapi.HTTPResponseRuleApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.HttpResponseRule() # HttpResponseRule | 
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
index = 56 # int | HTTP Response Rule Index
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace a HTTP Response Rule
    api_response = api_instance.replace_http_response_rule(body, parent_name, parent_type, index, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HTTPResponseRuleApi->replace_http_response_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HttpResponseRule**](HttpResponseRule.md)|  | 
 **parent_name** | **str**| Parent name | 
 **parent_type** | **str**| Parent type | 
 **index** | **int**| HTTP Response Rule Index | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**HttpResponseRule**](HttpResponseRule.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

