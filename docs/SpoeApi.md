# swagger_client.SpoeApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_spoe**](SpoeApi.md#create_spoe) | **POST** /services/haproxy/spoe/spoe_files | Creates SPOE file with its entries
[**create_spoe_agent**](SpoeApi.md#create_spoe_agent) | **POST** /services/haproxy/spoe/spoe_agents | Add a new spoe agent to scope
[**create_spoe_group**](SpoeApi.md#create_spoe_group) | **POST** /services/haproxy/spoe/spoe_groups | Add a new SPOE groups
[**create_spoe_message**](SpoeApi.md#create_spoe_message) | **POST** /services/haproxy/spoe/spoe_messages | Add a new spoe message to scope
[**create_spoe_scope**](SpoeApi.md#create_spoe_scope) | **POST** /services/haproxy/spoe/spoe_scopes | Add a new spoe scope
[**delete_spoe_agent**](SpoeApi.md#delete_spoe_agent) | **DELETE** /services/haproxy/spoe/spoe_agents/{name} | Delete a SPOE agent
[**delete_spoe_file**](SpoeApi.md#delete_spoe_file) | **DELETE** /services/haproxy/spoe/spoe_files/{name} | Delete SPOE file
[**delete_spoe_group**](SpoeApi.md#delete_spoe_group) | **DELETE** /services/haproxy/spoe/spoe_groups/{name} | Delete a SPOE groups
[**delete_spoe_message**](SpoeApi.md#delete_spoe_message) | **DELETE** /services/haproxy/spoe/spoe_messages/{name} | Delete a spoe message
[**delete_spoe_scope**](SpoeApi.md#delete_spoe_scope) | **DELETE** /services/haproxy/spoe/spoe_scopes/{name} | Delete a SPOE scope
[**get_all_spoe_files**](SpoeApi.md#get_all_spoe_files) | **GET** /services/haproxy/spoe/spoe_files | Return all available SPOE files
[**get_one_spoe_file**](SpoeApi.md#get_one_spoe_file) | **GET** /services/haproxy/spoe/spoe_files/{name} | Return one SPOE file
[**get_spoe_agent**](SpoeApi.md#get_spoe_agent) | **GET** /services/haproxy/spoe/spoe_agents/{name} | Return a spoe agent
[**get_spoe_agents**](SpoeApi.md#get_spoe_agents) | **GET** /services/haproxy/spoe/spoe_agents | Return an array of spoe agents in one scope
[**get_spoe_configuration_version**](SpoeApi.md#get_spoe_configuration_version) | **GET** /services/haproxy/spoe/version | Return a SPOE configuration version
[**get_spoe_group**](SpoeApi.md#get_spoe_group) | **GET** /services/haproxy/spoe/spoe_groups/{name} | Return a SPOE groups
[**get_spoe_groups**](SpoeApi.md#get_spoe_groups) | **GET** /services/haproxy/spoe/spoe_groups | Return an array of SPOE groups
[**get_spoe_message**](SpoeApi.md#get_spoe_message) | **GET** /services/haproxy/spoe/spoe_messages/{name} | Return a spoe message
[**get_spoe_messages**](SpoeApi.md#get_spoe_messages) | **GET** /services/haproxy/spoe/spoe_messages | Return an array of spoe messages in one scope
[**get_spoe_scope**](SpoeApi.md#get_spoe_scope) | **GET** /services/haproxy/spoe/spoe_scopes/{name} | Return one SPOE scope
[**get_spoe_scopes**](SpoeApi.md#get_spoe_scopes) | **GET** /services/haproxy/spoe/spoe_scopes | Return an array of spoe scopes
[**replace_spoe_agent**](SpoeApi.md#replace_spoe_agent) | **PUT** /services/haproxy/spoe/spoe_agents/{name} | Replace a SPOE agent
[**replace_spoe_group**](SpoeApi.md#replace_spoe_group) | **PUT** /services/haproxy/spoe/spoe_groups/{name} | Replace a SPOE groups
[**replace_spoe_message**](SpoeApi.md#replace_spoe_message) | **PUT** /services/haproxy/spoe/spoe_messages/{name} | Replace a spoe message

# **create_spoe**
> str create_spoe(file_upload=file_upload)

Creates SPOE file with its entries

Creates SPOE file with its entries.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
file_upload = 'file_upload_example' # str |  (optional)

try:
    # Creates SPOE file with its entries
    api_response = api_instance.create_spoe(file_upload=file_upload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeApi->create_spoe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_upload** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_spoe_agent**
> SpoeAgent create_spoe_agent(body, spoe, scope, transaction_id=transaction_id, version=version)

Add a new spoe agent to scope

Adds a new spoe agent to the spoe scope.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.SpoeAgent() # SpoeAgent | 
spoe = 'spoe_example' # str | Spoe file name
scope = 'scope_example' # str | Spoe scope
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)

try:
    # Add a new spoe agent to scope
    api_response = api_instance.create_spoe_agent(body, spoe, scope, transaction_id=transaction_id, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeApi->create_spoe_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpoeAgent**](SpoeAgent.md)|  | 
 **spoe** | **str**| Spoe file name | 
 **scope** | **str**| Spoe scope | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 

### Return type

[**SpoeAgent**](SpoeAgent.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_spoe_group**
> SpoeGroup create_spoe_group(body, spoe, scope, transaction_id=transaction_id, version=version)

Add a new SPOE groups

Adds a new SPOE groups to the SPOE scope.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.SpoeGroup() # SpoeGroup | 
spoe = 'spoe_example' # str | Spoe file name
scope = 'scope_example' # str | Spoe scope
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)

try:
    # Add a new SPOE groups
    api_response = api_instance.create_spoe_group(body, spoe, scope, transaction_id=transaction_id, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeApi->create_spoe_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpoeGroup**](SpoeGroup.md)|  | 
 **spoe** | **str**| Spoe file name | 
 **scope** | **str**| Spoe scope | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 

### Return type

[**SpoeGroup**](SpoeGroup.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_spoe_message**
> SpoeMessage create_spoe_message(body, spoe, scope, transaction_id=transaction_id, version=version)

Add a new spoe message to scope

Adds a new spoe message to the spoe scope.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.SpoeMessage() # SpoeMessage | 
spoe = 'spoe_example' # str | Spoe file name
scope = 'scope_example' # str | Spoe scope
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)

try:
    # Add a new spoe message to scope
    api_response = api_instance.create_spoe_message(body, spoe, scope, transaction_id=transaction_id, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeApi->create_spoe_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpoeMessage**](SpoeMessage.md)|  | 
 **spoe** | **str**| Spoe file name | 
 **scope** | **str**| Spoe scope | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 

### Return type

[**SpoeMessage**](SpoeMessage.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_spoe_scope**
> SpoeScope create_spoe_scope(body, spoe, transaction_id=transaction_id, version=version)

Add a new spoe scope

Adds a new spoe scope.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
body = 'body_example' # str | 
spoe = 'spoe_example' # str | Spoe file name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)

try:
    # Add a new spoe scope
    api_response = api_instance.create_spoe_scope(body, spoe, transaction_id=transaction_id, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeApi->create_spoe_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **spoe** | **str**| Spoe file name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 

### Return type

[**SpoeScope**](SpoeScope.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_spoe_agent**
> delete_spoe_agent(spoe, scope, name, transaction_id=transaction_id, version=version)

Delete a SPOE agent

Deletes a SPOE agent from the configuration in one SPOE scope.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
spoe = 'spoe_example' # str | Spoe file name
scope = 'scope_example' # str | Spoe scope
name = 'name_example' # str | Spoe agent name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)

try:
    # Delete a SPOE agent
    api_instance.delete_spoe_agent(spoe, scope, name, transaction_id=transaction_id, version=version)
except ApiException as e:
    print("Exception when calling SpoeApi->delete_spoe_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spoe** | **str**| Spoe file name | 
 **scope** | **str**| Spoe scope | 
 **name** | **str**| Spoe agent name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_spoe_file**
> delete_spoe_file(name)

Delete SPOE file

Deletes SPOE file.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | SPOE file name

try:
    # Delete SPOE file
    api_instance.delete_spoe_file(name)
except ApiException as e:
    print("Exception when calling SpoeApi->delete_spoe_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| SPOE file name | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_spoe_group**
> delete_spoe_group(spoe, scope, name, transaction_id=transaction_id, version=version)

Delete a SPOE groups

Deletes a SPOE groups from the one SPOE scope.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
spoe = 'spoe_example' # str | Spoe file name
scope = 'scope_example' # str | Spoe scope
name = 'name_example' # str | Spoe group name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)

try:
    # Delete a SPOE groups
    api_instance.delete_spoe_group(spoe, scope, name, transaction_id=transaction_id, version=version)
except ApiException as e:
    print("Exception when calling SpoeApi->delete_spoe_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spoe** | **str**| Spoe file name | 
 **scope** | **str**| Spoe scope | 
 **name** | **str**| Spoe group name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_spoe_message**
> delete_spoe_message(spoe, scope, name, transaction_id=transaction_id, version=version)

Delete a spoe message

Deletes a spoe message from the SPOE scope.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
spoe = 'spoe_example' # str | Spoe file name
scope = 'scope_example' # str | Spoe scope
name = 'name_example' # str | Spoe message name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)

try:
    # Delete a spoe message
    api_instance.delete_spoe_message(spoe, scope, name, transaction_id=transaction_id, version=version)
except ApiException as e:
    print("Exception when calling SpoeApi->delete_spoe_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spoe** | **str**| Spoe file name | 
 **scope** | **str**| Spoe scope | 
 **name** | **str**| Spoe message name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_spoe_scope**
> delete_spoe_scope(spoe, name, transaction_id=transaction_id, version=version)

Delete a SPOE scope

Deletes a SPOE scope from the configuration file.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
spoe = 'spoe_example' # str | Spoe file name
name = 'name_example' # str | Spoe scope name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)

try:
    # Delete a SPOE scope
    api_instance.delete_spoe_scope(spoe, name, transaction_id=transaction_id, version=version)
except ApiException as e:
    print("Exception when calling SpoeApi->delete_spoe_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spoe** | **str**| Spoe file name | 
 **name** | **str**| Spoe scope name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_spoe_files**
> SpoeFiles get_all_spoe_files()

Return all available SPOE files

Returns all available SPOE files.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))

try:
    # Return all available SPOE files
    api_response = api_instance.get_all_spoe_files()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeApi->get_all_spoe_files: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SpoeFiles**](SpoeFiles.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_spoe_file**
> InlineResponse20084 get_one_spoe_file(name)

Return one SPOE file

Returns one SPOE file.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | SPOE file name

try:
    # Return one SPOE file
    api_response = api_instance.get_one_spoe_file(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeApi->get_one_spoe_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| SPOE file name | 

### Return type

[**InlineResponse20084**](InlineResponse20084.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spoe_agent**
> InlineResponse20083 get_spoe_agent(spoe, scope, name, transaction_id=transaction_id)

Return a spoe agent

Returns one spoe agent configuration in one SPOE scope.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
spoe = 'spoe_example' # str | Spoe file name
scope = 'scope_example' # str | Spoe scope
name = 'name_example' # str | Spoe agent name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return a spoe agent
    api_response = api_instance.get_spoe_agent(spoe, scope, name, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeApi->get_spoe_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spoe** | **str**| Spoe file name | 
 **scope** | **str**| Spoe scope | 
 **name** | **str**| Spoe agent name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20083**](InlineResponse20083.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spoe_agents**
> InlineResponse20082 get_spoe_agents(spoe, scope, transaction_id=transaction_id)

Return an array of spoe agents in one scope

Returns an array of all configured spoe agents in one scope.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
spoe = 'spoe_example' # str | Spoe file name
scope = 'scope_example' # str | Spoe scope
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of spoe agents in one scope
    api_response = api_instance.get_spoe_agents(spoe, scope, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeApi->get_spoe_agents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spoe** | **str**| Spoe file name | 
 **scope** | **str**| Spoe scope | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20082**](InlineResponse20082.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spoe_configuration_version**
> int get_spoe_configuration_version(spoe, transaction_id=transaction_id)

Return a SPOE configuration version

Returns SPOE configuration version.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
spoe = 'spoe_example' # str | Spoe file name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return a SPOE configuration version
    api_response = api_instance.get_spoe_configuration_version(spoe, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeApi->get_spoe_configuration_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spoe** | **str**| Spoe file name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

**int**

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spoe_group**
> InlineResponse20086 get_spoe_group(spoe, scope, name, transaction_id=transaction_id)

Return a SPOE groups

Returns one SPOE groups configuration in one SPOE scope.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
spoe = 'spoe_example' # str | Spoe file name
scope = 'scope_example' # str | Spoe scope
name = 'name_example' # str | Spoe group name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return a SPOE groups
    api_response = api_instance.get_spoe_group(spoe, scope, name, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeApi->get_spoe_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spoe** | **str**| Spoe file name | 
 **scope** | **str**| Spoe scope | 
 **name** | **str**| Spoe group name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20086**](InlineResponse20086.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spoe_groups**
> InlineResponse20085 get_spoe_groups(spoe, scope, transaction_id=transaction_id)

Return an array of SPOE groups

Returns an array of all configured SPOE groups in one SPOE scope.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
spoe = 'spoe_example' # str | Spoe file name
scope = 'scope_example' # str | Spoe scope
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of SPOE groups
    api_response = api_instance.get_spoe_groups(spoe, scope, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeApi->get_spoe_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spoe** | **str**| Spoe file name | 
 **scope** | **str**| Spoe scope | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20085**](InlineResponse20085.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spoe_message**
> InlineResponse20088 get_spoe_message(spoe, scope, name, transaction_id=transaction_id)

Return a spoe message

Returns one spoe message configuration in SPOE scope.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
spoe = 'spoe_example' # str | Spoe file name
scope = 'scope_example' # str | Spoe scope
name = 'name_example' # str | Spoe message name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return a spoe message
    api_response = api_instance.get_spoe_message(spoe, scope, name, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeApi->get_spoe_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spoe** | **str**| Spoe file name | 
 **scope** | **str**| Spoe scope | 
 **name** | **str**| Spoe message name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20088**](InlineResponse20088.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spoe_messages**
> InlineResponse20087 get_spoe_messages(spoe, scope, transaction_id=transaction_id)

Return an array of spoe messages in one scope

Returns an array of all configured spoe messages in one scope.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
spoe = 'spoe_example' # str | Spoe file name
scope = 'scope_example' # str | Spoe scope
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of spoe messages in one scope
    api_response = api_instance.get_spoe_messages(spoe, scope, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeApi->get_spoe_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spoe** | **str**| Spoe file name | 
 **scope** | **str**| Spoe scope | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20087**](InlineResponse20087.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spoe_scope**
> InlineResponse20090 get_spoe_scope(spoe, name, transaction_id=transaction_id)

Return one SPOE scope

Returns one SPOE scope in one SPOE file.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
spoe = 'spoe_example' # str | Spoe file name
name = 'name_example' # str | Spoe scope
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return one SPOE scope
    api_response = api_instance.get_spoe_scope(spoe, name, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeApi->get_spoe_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spoe** | **str**| Spoe file name | 
 **name** | **str**| Spoe scope | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20090**](InlineResponse20090.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spoe_scopes**
> InlineResponse20089 get_spoe_scopes(spoe, transaction_id=transaction_id)

Return an array of spoe scopes

Returns an array of all configured spoe scopes.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
spoe = 'spoe_example' # str | Spoe file name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of spoe scopes
    api_response = api_instance.get_spoe_scopes(spoe, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeApi->get_spoe_scopes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spoe** | **str**| Spoe file name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20089**](InlineResponse20089.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_spoe_agent**
> SpoeAgent replace_spoe_agent(body, spoe, scope, name, transaction_id=transaction_id, version=version)

Replace a SPOE agent

Replaces a SPOE agent configuration in one SPOE scope.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.SpoeAgent() # SpoeAgent | 
spoe = 'spoe_example' # str | Spoe file name
scope = 'scope_example' # str | Spoe scope
name = 'name_example' # str | Spoe agent name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)

try:
    # Replace a SPOE agent
    api_response = api_instance.replace_spoe_agent(body, spoe, scope, name, transaction_id=transaction_id, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeApi->replace_spoe_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpoeAgent**](SpoeAgent.md)|  | 
 **spoe** | **str**| Spoe file name | 
 **scope** | **str**| Spoe scope | 
 **name** | **str**| Spoe agent name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 

### Return type

[**SpoeAgent**](SpoeAgent.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_spoe_group**
> SpoeGroup replace_spoe_group(body, spoe, scope, name, transaction_id=transaction_id, version=version)

Replace a SPOE groups

Replaces a SPOE groups configuration in one SPOE scope.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.SpoeGroup() # SpoeGroup | 
spoe = 'spoe_example' # str | Spoe file name
scope = 'scope_example' # str | Spoe scope
name = 'name_example' # str | Spoe group name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)

try:
    # Replace a SPOE groups
    api_response = api_instance.replace_spoe_group(body, spoe, scope, name, transaction_id=transaction_id, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeApi->replace_spoe_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpoeGroup**](SpoeGroup.md)|  | 
 **spoe** | **str**| Spoe file name | 
 **scope** | **str**| Spoe scope | 
 **name** | **str**| Spoe group name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 

### Return type

[**SpoeGroup**](SpoeGroup.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_spoe_message**
> SpoeMessage replace_spoe_message(body, spoe, scope, name, transaction_id=transaction_id, version=version)

Replace a spoe message

Replaces a spoe message configuration in one SPOE scope.

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
api_instance = dataplaneapi.SpoeApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.SpoeMessage() # SpoeMessage | 
spoe = 'spoe_example' # str | Spoe file name
scope = 'scope_example' # str | Spoe scope
name = 'name_example' # str | Spoe message name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)

try:
    # Replace a spoe message
    api_response = api_instance.replace_spoe_message(body, spoe, scope, name, transaction_id=transaction_id, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeApi->replace_spoe_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpoeMessage**](SpoeMessage.md)|  | 
 **spoe** | **str**| Spoe file name | 
 **scope** | **str**| Spoe scope | 
 **name** | **str**| Spoe message name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 

### Return type

[**SpoeMessage**](SpoeMessage.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

