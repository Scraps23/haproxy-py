# swagger_client.ACLApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_acl**](ACLApi.md#create_acl) | **POST** /services/haproxy/configuration/acls | Add a new ACL line
[**delete_acl**](ACLApi.md#delete_acl) | **DELETE** /services/haproxy/configuration/acls/{index} | Delete a ACL line
[**get_acl**](ACLApi.md#get_acl) | **GET** /services/haproxy/configuration/acls/{index} | Return one ACL line
[**get_acls**](ACLApi.md#get_acls) | **GET** /services/haproxy/configuration/acls | Return an array of all ACL lines
[**replace_acl**](ACLApi.md#replace_acl) | **PUT** /services/haproxy/configuration/acls/{index} | Replace a ACL line

# **create_acl**
> Acl create_acl(body, parent_name, parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)

Add a new ACL line

Adds a new ACL line of the specified type in the specified parent.

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
api_instance = dataplaneapi.ACLApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.Acl() # Acl | 
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Add a new ACL line
    api_response = api_instance.create_acl(body, parent_name, parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ACLApi->create_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Acl**](Acl.md)|  | 
 **parent_name** | **str**| Parent name | 
 **parent_type** | **str**| Parent type | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**Acl**](Acl.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_acl**
> delete_acl(index, parent_name, parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)

Delete a ACL line

Deletes a ACL line configuration by it's index from the specified parent.

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
api_instance = dataplaneapi.ACLApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | ACL line Index
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Delete a ACL line
    api_instance.delete_acl(index, parent_name, parent_type, transaction_id=transaction_id, version=version, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling ACLApi->delete_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| ACL line Index | 
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

# **get_acl**
> InlineResponse2005 get_acl(index, parent_name, parent_type, transaction_id=transaction_id)

Return one ACL line

Returns one ACL line configuration by it's index in the specified parent.

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
api_instance = dataplaneapi.ACLApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | ACL line Index
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return one ACL line
    api_response = api_instance.get_acl(index, parent_name, parent_type, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ACLApi->get_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| ACL line Index | 
 **parent_name** | **str**| Parent name | 
 **parent_type** | **str**| Parent type | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_acls**
> InlineResponse2004 get_acls(parent_name, parent_type, acl_name=acl_name, transaction_id=transaction_id)

Return an array of all ACL lines

Returns all ACL lines that are configured in specified parent.

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
api_instance = dataplaneapi.ACLApi(dataplaneapi.ApiClient(configuration))
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
acl_name = 'acl_name_example' # str | ACL name (optional)
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of all ACL lines
    api_response = api_instance.get_acls(parent_name, parent_type, acl_name=acl_name, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ACLApi->get_acls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_name** | **str**| Parent name | 
 **parent_type** | **str**| Parent type | 
 **acl_name** | **str**| ACL name | [optional] 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_acl**
> Acl replace_acl(body, parent_name, parent_type, index, transaction_id=transaction_id, version=version, force_reload=force_reload)

Replace a ACL line

Replaces a ACL line configuration by it's index in the specified parent.

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
api_instance = dataplaneapi.ACLApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.Acl() # Acl | 
parent_name = 'parent_name_example' # str | Parent name
parent_type = 'parent_type_example' # str | Parent type
index = 56 # int | ACL line Index
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace a ACL line
    api_response = api_instance.replace_acl(body, parent_name, parent_type, index, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ACLApi->replace_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Acl**](Acl.md)|  | 
 **parent_name** | **str**| Parent name | 
 **parent_type** | **str**| Parent type | 
 **index** | **int**| ACL line Index | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**Acl**](Acl.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

