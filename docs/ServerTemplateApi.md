# swagger_client.ServerTemplateApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_server_template**](ServerTemplateApi.md#create_server_template) | **POST** /services/haproxy/configuration/server_templates | Add a new server template
[**delete_server_template**](ServerTemplateApi.md#delete_server_template) | **DELETE** /services/haproxy/configuration/server_templates/{prefix} | Delete a server template
[**get_server_template**](ServerTemplateApi.md#get_server_template) | **GET** /services/haproxy/configuration/server_templates/{prefix} | Return one server template
[**get_server_templates**](ServerTemplateApi.md#get_server_templates) | **GET** /services/haproxy/configuration/server_templates | Return an array of server templates
[**replace_server_template**](ServerTemplateApi.md#replace_server_template) | **PUT** /services/haproxy/configuration/server_templates/{prefix} | Replace a server template

# **create_server_template**
> ServerTemplate create_server_template(body, backend, transaction_id=transaction_id, version=version, force_reload=force_reload)

Add a new server template

Adds a new server template in the specified backend in the configuration file.

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
api_instance = dataplaneapi.ServerTemplateApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.ServerTemplate() # ServerTemplate | 
backend = 'backend_example' # str | Parent backend name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Add a new server template
    api_response = api_instance.create_server_template(body, backend, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerTemplateApi->create_server_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServerTemplate**](ServerTemplate.md)|  | 
 **backend** | **str**| Parent backend name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**ServerTemplate**](ServerTemplate.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_server_template**
> delete_server_template(prefix, backend, transaction_id=transaction_id, version=version, force_reload=force_reload)

Delete a server template

Deletes a server template configuration by it's prefix in the specified backend.

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
api_instance = dataplaneapi.ServerTemplateApi(dataplaneapi.ApiClient(configuration))
prefix = 'prefix_example' # str | Server template prefix
backend = 'backend_example' # str | Parent backend name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Delete a server template
    api_instance.delete_server_template(prefix, backend, transaction_id=transaction_id, version=version, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling ServerTemplateApi->delete_server_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| Server template prefix | 
 **backend** | **str**| Parent backend name | 
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

# **get_server_template**
> InlineResponse20065 get_server_template(prefix, backend, transaction_id=transaction_id)

Return one server template

Returns one server template configuration by it's prefix in the specified backend.

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
api_instance = dataplaneapi.ServerTemplateApi(dataplaneapi.ApiClient(configuration))
prefix = 'prefix_example' # str | Server template prefix
backend = 'backend_example' # str | Parent backend name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return one server template
    api_response = api_instance.get_server_template(prefix, backend, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerTemplateApi->get_server_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| Server template prefix | 
 **backend** | **str**| Parent backend name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20065**](InlineResponse20065.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_templates**
> InlineResponse20064 get_server_templates(backend, transaction_id=transaction_id)

Return an array of server templates

Returns an array of all server templates that are configured in specified backend.

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
api_instance = dataplaneapi.ServerTemplateApi(dataplaneapi.ApiClient(configuration))
backend = 'backend_example' # str | Parent backend name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of server templates
    api_response = api_instance.get_server_templates(backend, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerTemplateApi->get_server_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backend** | **str**| Parent backend name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20064**](InlineResponse20064.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_server_template**
> ServerTemplate replace_server_template(body, backend, prefix, transaction_id=transaction_id, version=version, force_reload=force_reload)

Replace a server template

Replaces a server template configuration by it's prefix in the specified backend.

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
api_instance = dataplaneapi.ServerTemplateApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.ServerTemplate() # ServerTemplate | 
backend = 'backend_example' # str | Parent backend name
prefix = 'prefix_example' # str | Server template prefix
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace a server template
    api_response = api_instance.replace_server_template(body, backend, prefix, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerTemplateApi->replace_server_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServerTemplate**](ServerTemplate.md)|  | 
 **backend** | **str**| Parent backend name | 
 **prefix** | **str**| Server template prefix | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**ServerTemplate**](ServerTemplate.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

