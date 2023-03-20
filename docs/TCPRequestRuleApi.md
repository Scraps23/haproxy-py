# swagger_client.TCPRequestRuleApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tcp_request_rule**](TCPRequestRuleApi.md#create_tcp_request_rule) | **POST** /services/haproxy/configuration/tcp_request_rules | Add a new TCP Request Rule
[**delete_tcp_request_rule**](TCPRequestRuleApi.md#delete_tcp_request_rule) | **DELETE** /services/haproxy/configuration/tcp_request_rules/{index} | Delete a TCP Request Rule
[**get_tcp_request_rule**](TCPRequestRuleApi.md#get_tcp_request_rule) | **GET** /services/haproxy/configuration/tcp_request_rules/{index} | Return one TCP Request Rule
[**get_tcp_request_rules**](TCPRequestRuleApi.md#get_tcp_request_rules) | **GET** /services/haproxy/configuration/tcp_request_rules | Return an array of all TCP Request Rules
[**replace_tcp_request_rule**](TCPRequestRuleApi.md#replace_tcp_request_rule) | **PUT** /services/haproxy/configuration/tcp_request_rules/{index} | Replace a TCP Request Rule

# **create_tcp_request_rule**
> TcpRequestRule create_tcp_request_rule(body, parent_name, parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)

Add a new TCP Request Rule

Adds a new TCP Request Rule of the specified type in the specified parent.

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
api_instance = dataplaneapi.TCPRequestRuleApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.TcpRequestRule() # TcpRequestRule | 
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Add a new TCP Request Rule
    api_response = api_instance.create_tcp_request_rule(body, parent_name, parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TCPRequestRuleApi->create_tcp_request_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TcpRequestRule**](TcpRequestRule.md)|  | 
 **parent_name** | **str**| Parent name | 
 **parent_type** | **str**| Parent type | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**TcpRequestRule**](TcpRequestRule.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tcp_request_rule**
> delete_tcp_request_rule(index, parent_name, parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)

Delete a TCP Request Rule

Deletes a TCP Request Rule configuration by it's index from the specified parent.

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
api_instance = dataplaneapi.TCPRequestRuleApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | TCP Request Rule Index
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Delete a TCP Request Rule
    api_instance.delete_tcp_request_rule(index, parent_name, parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling TCPRequestRuleApi->delete_tcp_request_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| TCP Request Rule Index | 
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

# **get_tcp_request_rule**
> InlineResponse20073 get_tcp_request_rule(index, parent_name, parent_type, transaction_id=transaction_id)

Return one TCP Request Rule

Returns one TCP Request Rule configuration by it's index in the specified parent.

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
api_instance = dataplaneapi.TCPRequestRuleApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | TCP Request Rule Index
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return one TCP Request Rule
    api_response = api_instance.get_tcp_request_rule(index, parent_name, parent_type, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TCPRequestRuleApi->get_tcp_request_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| TCP Request Rule Index | 
 **parent_name** | **str**| Parent name | 
 **parent_type** | **str**| Parent type | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20073**](InlineResponse20073.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tcp_request_rules**
> InlineResponse20072 get_tcp_request_rules(parent_name, parent_type, transaction_id=transaction_id)

Return an array of all TCP Request Rules

Returns all TCP Request Rules that are configured in specified parent and parent type.

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
api_instance = dataplaneapi.TCPRequestRuleApi(dataplaneapi.ApiClient(configuration))
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of all TCP Request Rules
    api_response = api_instance.get_tcp_request_rules(parent_name, parent_type, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TCPRequestRuleApi->get_tcp_request_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_name** | **str**| Parent name | 
 **parent_type** | **str**| Parent type | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20072**](InlineResponse20072.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_tcp_request_rule**
> TcpRequestRule replace_tcp_request_rule(body, parent_name, parent_type, index, transaction_id=transaction_id, version=version, force_reload=force_reload)

Replace a TCP Request Rule

Replaces a TCP Request Rule configuration by it's index in the specified parent.

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
api_instance = dataplaneapi.TCPRequestRuleApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.TcpRequestRule() # TcpRequestRule | 
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
index = 56 # int | TCP Request Rule Index
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace a TCP Request Rule
    api_response = api_instance.replace_tcp_request_rule(body, parent_name, parent_type, index, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TCPRequestRuleApi->replace_tcp_request_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TcpRequestRule**](TcpRequestRule.md)|  | 
 **parent_name** | **str**| Parent name | 
 **parent_type** | **str**| Parent type | 
 **index** | **int**| TCP Request Rule Index | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**TcpRequestRule**](TcpRequestRule.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

