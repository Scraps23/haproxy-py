# swagger_client.HTTPRequestRuleApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_http_request_rule**](HTTPRequestRuleApi.md#create_http_request_rule) | **POST** /services/haproxy/configuration/http_request_rules | Add a new HTTP Request Rule
[**delete_http_request_rule**](HTTPRequestRuleApi.md#delete_http_request_rule) | **DELETE** /services/haproxy/configuration/http_request_rules/{index} | Delete a HTTP Request Rule
[**get_http_request_rule**](HTTPRequestRuleApi.md#get_http_request_rule) | **GET** /services/haproxy/configuration/http_request_rules/{index} | Return one HTTP Request Rule
[**get_http_request_rules**](HTTPRequestRuleApi.md#get_http_request_rules) | **GET** /services/haproxy/configuration/http_request_rules | Return an array of all HTTP Request Rules
[**replace_http_request_rule**](HTTPRequestRuleApi.md#replace_http_request_rule) | **PUT** /services/haproxy/configuration/http_request_rules/{index} | Replace a HTTP Request Rule

# **create_http_request_rule**
> HttpRequestRule create_http_request_rule(body, parent_name, parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)

Add a new HTTP Request Rule

Adds a new HTTP Request Rule of the specified type in the specified parent.

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
api_instance = dataplaneapi.HTTPRequestRuleApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.HttpRequestRule() # HttpRequestRule | 
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Add a new HTTP Request Rule
    api_response = api_instance.create_http_request_rule(body, parent_name, parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HTTPRequestRuleApi->create_http_request_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HttpRequestRule**](HttpRequestRule.md)|  | 
 **parent_name** | **str**| Parent name | 
 **parent_type** | **str**| Parent type | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**HttpRequestRule**](HttpRequestRule.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_http_request_rule**
> delete_http_request_rule(index, parent_name, parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)

Delete a HTTP Request Rule

Deletes a HTTP Request Rule configuration by it's index from the specified parent.

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
api_instance = dataplaneapi.HTTPRequestRuleApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | HTTP Request Rule Index
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Delete a HTTP Request Rule
    api_instance.delete_http_request_rule(index, parent_name, parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling HTTPRequestRuleApi->delete_http_request_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| HTTP Request Rule Index | 
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

# **get_http_request_rule**
> InlineResponse20037 get_http_request_rule(index, parent_name, parent_type, transaction_id=transaction_id)

Return one HTTP Request Rule

Returns one HTTP Request Rule configuration by it's index in the specified parent.

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
api_instance = dataplaneapi.HTTPRequestRuleApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | HTTP Request Rule Index
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return one HTTP Request Rule
    api_response = api_instance.get_http_request_rule(index, parent_name, parent_type, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HTTPRequestRuleApi->get_http_request_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| HTTP Request Rule Index | 
 **parent_name** | **str**| Parent name | 
 **parent_type** | **str**| Parent type | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_http_request_rules**
> InlineResponse20036 get_http_request_rules(parent_name, parent_type, transaction_id=transaction_id)

Return an array of all HTTP Request Rules

Returns all HTTP Request Rules that are configured in specified parent.

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
api_instance = dataplaneapi.HTTPRequestRuleApi(dataplaneapi.ApiClient(configuration))
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of all HTTP Request Rules
    api_response = api_instance.get_http_request_rules(parent_name, parent_type, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HTTPRequestRuleApi->get_http_request_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_name** | **str**| Parent name | 
 **parent_type** | **str**| Parent type | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_http_request_rule**
> HttpRequestRule replace_http_request_rule(body, parent_name, parent_type, index, transaction_id=transaction_id, version=version, force_reload=force_reload)

Replace a HTTP Request Rule

Replaces a HTTP Request Rule configuration by it's index in the specified parent.

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
api_instance = dataplaneapi.HTTPRequestRuleApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.HttpRequestRule() # HttpRequestRule | 
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
index = 56 # int | HTTP Request Rule Index
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace a HTTP Request Rule
    api_response = api_instance.replace_http_request_rule(body, parent_name, parent_type, index, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HTTPRequestRuleApi->replace_http_request_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HttpRequestRule**](HttpRequestRule.md)|  | 
 **parent_name** | **str**| Parent name | 
 **parent_type** | **str**| Parent type | 
 **index** | **int**| HTTP Request Rule Index | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**HttpRequestRule**](HttpRequestRule.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

