# swagger_client.ServerApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_runtime_server**](ServerApi.md#add_runtime_server) | **POST** /services/haproxy/runtime/servers | Adds a new server to a backend
[**create_server**](ServerApi.md#create_server) | **POST** /services/haproxy/configuration/servers | Add a new server
[**delete_runtime_server**](ServerApi.md#delete_runtime_server) | **DELETE** /services/haproxy/runtime/servers/{name} | Deletes a server from a backend
[**delete_server**](ServerApi.md#delete_server) | **DELETE** /services/haproxy/configuration/servers/{name} | Delete a server
[**get_runtime_server**](ServerApi.md#get_runtime_server) | **GET** /services/haproxy/runtime/servers/{name} | Return one server runtime settings
[**get_runtime_servers**](ServerApi.md#get_runtime_servers) | **GET** /services/haproxy/runtime/servers | Return an array of runtime servers&#x27; settings
[**get_server**](ServerApi.md#get_server) | **GET** /services/haproxy/configuration/servers/{name} | Return one server
[**get_servers**](ServerApi.md#get_servers) | **GET** /services/haproxy/configuration/servers | Return an array of servers
[**replace_runtime_server**](ServerApi.md#replace_runtime_server) | **PUT** /services/haproxy/runtime/servers/{name} | Replace server transient settings
[**replace_server**](ServerApi.md#replace_server) | **PUT** /services/haproxy/configuration/servers/{name} | Replace a server

# **add_runtime_server**
> RuntimeAddServer add_runtime_server(body, backend)

Adds a new server to a backend

Adds a new server to the specified backend

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
api_instance = dataplaneapi.ServerApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.RuntimeAddServer() # RuntimeAddServer | 
backend = 'backend_example' # str | Parent backend name

try:
    # Adds a new server to a backend
    api_response = api_instance.add_runtime_server(body, backend)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->add_runtime_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RuntimeAddServer**](RuntimeAddServer.md)|  | 
 **backend** | **str**| Parent backend name | 

### Return type

[**RuntimeAddServer**](RuntimeAddServer.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_server**
> Server create_server(body, backend=backend, parent_name=parent_name, parent_type=parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)

Add a new server

Adds a new server in the specified backend in the configuration file.

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
api_instance = dataplaneapi.ServerApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.Server() # Server | 
backend = 'backend_example' # str | Parent backend name (optional)
parent_name = 'parent_name_example' # str | Parent name (optional)
parent_type = 'parent_type_example' # str | Parent type (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Add a new server
    api_response = api_instance.create_server(body, backend=backend, parent_name=parent_name, parent_type=parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->create_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Server**](Server.md)|  | 
 **backend** | **str**| Parent backend name | [optional] 
 **parent_name** | **str**| Parent name | [optional] 
 **parent_type** | **str**| Parent type | [optional] 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**Server**](Server.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_runtime_server**
> delete_runtime_server(name, backend)

Deletes a server from a backend

Deletes a server from the specified backend

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
api_instance = dataplaneapi.ServerApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | Server name
backend = 'backend_example' # str | Parent backend name

try:
    # Deletes a server from a backend
    api_instance.delete_runtime_server(name, backend)
except ApiException as e:
    print("Exception when calling ServerApi->delete_runtime_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Server name | 
 **backend** | **str**| Parent backend name | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_server**
> delete_server(name, backend=backend, parent_name=parent_name, parent_type=parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)

Delete a server

Deletes a server configuration by it's name in the specified backend.

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
api_instance = dataplaneapi.ServerApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | Server name
backend = 'backend_example' # str | Parent backend name (optional)
parent_name = 'parent_name_example' # str | Parent name (optional)
parent_type = 'parent_type_example' # str | Parent type (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Delete a server
    api_instance.delete_server(name, backend=backend, parent_name=parent_name, parent_type=parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling ServerApi->delete_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Server name | 
 **backend** | **str**| Parent backend name | [optional] 
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

# **get_runtime_server**
> RuntimeServer get_runtime_server(name, backend)

Return one server runtime settings

Returns one server runtime settings by it's name in the specified backend.

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
api_instance = dataplaneapi.ServerApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | Server name
backend = 'backend_example' # str | Parent backend name

try:
    # Return one server runtime settings
    api_response = api_instance.get_runtime_server(name, backend)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->get_runtime_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Server name | 
 **backend** | **str**| Parent backend name | 

### Return type

[**RuntimeServer**](RuntimeServer.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runtime_servers**
> RuntimeServers get_runtime_servers(backend)

Return an array of runtime servers' settings

Returns an array of all servers' runtime settings.

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
api_instance = dataplaneapi.ServerApi(dataplaneapi.ApiClient(configuration))
backend = 'backend_example' # str | Parent backend name

try:
    # Return an array of runtime servers' settings
    api_response = api_instance.get_runtime_servers(backend)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->get_runtime_servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backend** | **str**| Parent backend name | 

### Return type

[**RuntimeServers**](RuntimeServers.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server**
> InlineResponse20067 get_server(name, backend=backend, parent_name=parent_name, parent_type=parent_type, transaction_id=transaction_id)

Return one server

Returns one server configuration by it's name in the specified backend.

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
api_instance = dataplaneapi.ServerApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | Server name
backend = 'backend_example' # str | Parent backend name (optional)
parent_name = 'parent_name_example' # str | Parent name (optional)
parent_type = 'parent_type_example' # str | Parent type (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return one server
    api_response = api_instance.get_server(name, backend=backend, parent_name=parent_name, parent_type=parent_type, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->get_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Server name | 
 **backend** | **str**| Parent backend name | [optional] 
 **parent_name** | **str**| Parent name | [optional] 
 **parent_type** | **str**| Parent type | [optional] 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20067**](InlineResponse20067.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_servers**
> InlineResponse20066 get_servers(backend=backend, parent_name=parent_name, parent_type=parent_type, transaction_id=transaction_id)

Return an array of servers

Returns an array of all servers that are configured in specified backend.

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
api_instance = dataplaneapi.ServerApi(dataplaneapi.ApiClient(configuration))
backend = 'backend_example' # str | Parent backend name (optional)
parent_name = 'parent_name_example' # str | Parent name (optional)
parent_type = 'parent_type_example' # str | Parent type (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of servers
    api_response = api_instance.get_servers(backend=backend, parent_name=parent_name, parent_type=parent_type, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->get_servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backend** | **str**| Parent backend name | [optional] 
 **parent_name** | **str**| Parent name | [optional] 
 **parent_type** | **str**| Parent type | [optional] 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20066**](InlineResponse20066.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_runtime_server**
> RuntimeServer replace_runtime_server(body, backend, name)

Replace server transient settings

Replaces a server transient settings by it's name in the specified backend.

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
api_instance = dataplaneapi.ServerApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.RuntimeServer() # RuntimeServer | 
backend = 'backend_example' # str | Parent backend name
name = 'name_example' # str | Server name

try:
    # Replace server transient settings
    api_response = api_instance.replace_runtime_server(body, backend, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->replace_runtime_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RuntimeServer**](RuntimeServer.md)|  | 
 **backend** | **str**| Parent backend name | 
 **name** | **str**| Server name | 

### Return type

[**RuntimeServer**](RuntimeServer.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_server**
> Server replace_server(body, name, backend=backend, parent_name=parent_name, parent_type=parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)

Replace a server

Replaces a server configuration by it's name in the specified backend.

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
api_instance = dataplaneapi.ServerApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.Server() # Server | 
name = 'name_example' # str | Server name
backend = 'backend_example' # str | Parent backend name (optional)
parent_name = 'parent_name_example' # str | Parent name (optional)
parent_type = 'parent_type_example' # str | Parent type (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace a server
    api_response = api_instance.replace_server(body, name, backend=backend, parent_name=parent_name, parent_type=parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->replace_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Server**](Server.md)|  | 
 **name** | **str**| Server name | 
 **backend** | **str**| Parent backend name | [optional] 
 **parent_name** | **str**| Parent name | [optional] 
 **parent_type** | **str**| Parent type | [optional] 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**Server**](Server.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

