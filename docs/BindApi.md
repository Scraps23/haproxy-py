# swagger_client.BindApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bind**](BindApi.md#create_bind) | **POST** /services/haproxy/configuration/binds | Add a new bind
[**delete_bind**](BindApi.md#delete_bind) | **DELETE** /services/haproxy/configuration/binds/{name} | Delete a bind
[**get_bind**](BindApi.md#get_bind) | **GET** /services/haproxy/configuration/binds/{name} | Return one bind
[**get_binds**](BindApi.md#get_binds) | **GET** /services/haproxy/configuration/binds | Return an array of binds
[**replace_bind**](BindApi.md#replace_bind) | **PUT** /services/haproxy/configuration/binds/{name} | Replace a bind

# **create_bind**
> Bind create_bind(body, frontend=frontend, parent_name=parent_name, parent_type=parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)

Add a new bind

Adds a new bind in the specified frontend in the configuration file.

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
api_instance = dataplaneapi.BindApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.Bind() # Bind | 
frontend = 'frontend_example' # str | Parent frontend name (optional)
parent_name = 'parent_name_example' # str | Parent name (optional)
parent_type = 'parent_type_example' # str | Parent type (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Add a new bind
    api_response = api_instance.create_bind(body, frontend=frontend, parent_name=parent_name, parent_type=parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BindApi->create_bind: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Bind**](Bind.md)|  | 
 **frontend** | **str**| Parent frontend name | [optional] 
 **parent_name** | **str**| Parent name | [optional] 
 **parent_type** | **str**| Parent type | [optional] 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**Bind**](Bind.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bind**
> delete_bind(name, frontend=frontend, parent_name=parent_name, parent_type=parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)

Delete a bind

Deletes a bind configuration by it's name in the specified frontend.

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
api_instance = dataplaneapi.BindApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | Bind name
frontend = 'frontend_example' # str | Parent frontend name (optional)
parent_name = 'parent_name_example' # str | Parent name (optional)
parent_type = 'parent_type_example' # str | Parent type (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Delete a bind
    api_instance.delete_bind(name, frontend=frontend, parent_name=parent_name, parent_type=parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling BindApi->delete_bind: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Bind name | 
 **frontend** | **str**| Parent frontend name | [optional] 
 **parent_name** | **str**| Parent name | [optional] 
 **parent_type** | **str**| Parent type | [optional] 
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

# **get_bind**
> InlineResponse20011 get_bind(name, frontend=frontend, parent_name=parent_name, parent_type=parent_type, transaction_id=transaction_id)

Return one bind

Returns one bind configuration by it's name in the specified frontend.

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
api_instance = dataplaneapi.BindApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | Bind name
frontend = 'frontend_example' # str | Parent frontend name (optional)
parent_name = 'parent_name_example' # str | Parent name (optional)
parent_type = 'parent_type_example' # str | Parent type (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return one bind
    api_response = api_instance.get_bind(name, frontend=frontend, parent_name=parent_name, parent_type=parent_type, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BindApi->get_bind: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Bind name | 
 **frontend** | **str**| Parent frontend name | [optional] 
 **parent_name** | **str**| Parent name | [optional] 
 **parent_type** | **str**| Parent type | [optional] 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_binds**
> InlineResponse20010 get_binds(frontend=frontend, parent_name=parent_name, parent_type=parent_type, transaction_id=transaction_id)

Return an array of binds

Returns an array of all binds that are configured in specified frontend.

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
api_instance = dataplaneapi.BindApi(dataplaneapi.ApiClient(configuration))
frontend = 'frontend_example' # str | Parent frontend name (optional)
parent_name = 'parent_name_example' # str | Parent name (optional)
parent_type = 'parent_type_example' # str | Parent type (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of binds
    api_response = api_instance.get_binds(frontend=frontend, parent_name=parent_name, parent_type=parent_type, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BindApi->get_binds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **frontend** | **str**| Parent frontend name | [optional] 
 **parent_name** | **str**| Parent name | [optional] 
 **parent_type** | **str**| Parent type | [optional] 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_bind**
> Bind replace_bind(body, name, frontend=frontend, parent_name=parent_name, parent_type=parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)

Replace a bind

Replaces a bind configuration by it's name in the specified frontend.

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
api_instance = dataplaneapi.BindApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.Bind() # Bind | 
name = 'name_example' # str | Bind name
frontend = 'frontend_example' # str | Parent frontend name (optional)
parent_name = 'parent_name_example' # str | Parent name (optional)
parent_type = 'parent_type_example' # str | Parent type (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace a bind
    api_response = api_instance.replace_bind(body, name, frontend=frontend, parent_name=parent_name, parent_type=parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BindApi->replace_bind: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Bind**](Bind.md)|  | 
 **name** | **str**| Bind name | 
 **frontend** | **str**| Parent frontend name | [optional] 
 **parent_name** | **str**| Parent name | [optional] 
 **parent_type** | **str**| Parent type | [optional] 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**Bind**](Bind.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

