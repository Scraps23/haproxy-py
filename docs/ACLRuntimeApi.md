# swagger_client.ACLRuntimeApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_payload_runtime_acl**](ACLRuntimeApi.md#add_payload_runtime_acl) | **PUT** /services/haproxy/runtime/acl_file_entries | Add a new ACL payload
[**services_haproxy_runtime_acl_file_entries_get**](ACLRuntimeApi.md#services_haproxy_runtime_acl_file_entries_get) | **GET** /services/haproxy/runtime/acl_file_entries | Return an ACL entries
[**services_haproxy_runtime_acl_file_entries_id_delete**](ACLRuntimeApi.md#services_haproxy_runtime_acl_file_entries_id_delete) | **DELETE** /services/haproxy/runtime/acl_file_entries/{id} | Delete an ACL entry
[**services_haproxy_runtime_acl_file_entries_id_get**](ACLRuntimeApi.md#services_haproxy_runtime_acl_file_entries_id_get) | **GET** /services/haproxy/runtime/acl_file_entries/{id} | Return an ACL entry
[**services_haproxy_runtime_acl_file_entries_post**](ACLRuntimeApi.md#services_haproxy_runtime_acl_file_entries_post) | **POST** /services/haproxy/runtime/acl_file_entries | Add entry to an ACL file
[**services_haproxy_runtime_acls_get**](ACLRuntimeApi.md#services_haproxy_runtime_acls_get) | **GET** /services/haproxy/runtime/acls | Return an array of all ACL files
[**services_haproxy_runtime_acls_id_get**](ACLRuntimeApi.md#services_haproxy_runtime_acls_id_get) | **GET** /services/haproxy/runtime/acls/{id} | Return an ACL file

# **add_payload_runtime_acl**
> AclFilesEntries add_payload_runtime_acl(body, acl_id)

Add a new ACL payload

Adds a new ACL payload.

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
api_instance = dataplaneapi.ACLRuntimeApi(dataplaneapi.ApiClient(configuration))
body = [dataplaneapi.AclFileEntry()] # list[AclFileEntry] | 
acl_id = 'acl_id_example' # str | ACL ID

try:
    # Add a new ACL payload
    api_response = api_instance.add_payload_runtime_acl(body, acl_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ACLRuntimeApi->add_payload_runtime_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AclFileEntry]**](AclFileEntry.md)|  | 
 **acl_id** | **str**| ACL ID | 

### Return type

[**AclFilesEntries**](AclFilesEntries.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **services_haproxy_runtime_acl_file_entries_get**
> AclFilesEntries services_haproxy_runtime_acl_file_entries_get(acl_id)

Return an ACL entries

Returns an ACL runtime setting using the runtime socket.

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
api_instance = dataplaneapi.ACLRuntimeApi(dataplaneapi.ApiClient(configuration))
acl_id = 'acl_id_example' # str | ACL ID

try:
    # Return an ACL entries
    api_response = api_instance.services_haproxy_runtime_acl_file_entries_get(acl_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ACLRuntimeApi->services_haproxy_runtime_acl_file_entries_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acl_id** | **str**| ACL ID | 

### Return type

[**AclFilesEntries**](AclFilesEntries.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **services_haproxy_runtime_acl_file_entries_id_delete**
> services_haproxy_runtime_acl_file_entries_id_delete(acl_id, id)

Delete an ACL entry

Deletes the entry from the ACL by its value using the runtime socket.

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
api_instance = dataplaneapi.ACLRuntimeApi(dataplaneapi.ApiClient(configuration))
acl_id = 'acl_id_example' # str | ACL ID
id = 'id_example' # str | File entry ID

try:
    # Delete an ACL entry
    api_instance.services_haproxy_runtime_acl_file_entries_id_delete(acl_id, id)
except ApiException as e:
    print("Exception when calling ACLRuntimeApi->services_haproxy_runtime_acl_file_entries_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acl_id** | **str**| ACL ID | 
 **id** | **str**| File entry ID | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **services_haproxy_runtime_acl_file_entries_id_get**
> AclFileEntry services_haproxy_runtime_acl_file_entries_id_get(acl_id, id)

Return an ACL entry

Returns the ACL entry by its ID using the runtime socket.

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
api_instance = dataplaneapi.ACLRuntimeApi(dataplaneapi.ApiClient(configuration))
acl_id = 'acl_id_example' # str | ACL ID
id = 'id_example' # str | File entry ID

try:
    # Return an ACL entry
    api_response = api_instance.services_haproxy_runtime_acl_file_entries_id_get(acl_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ACLRuntimeApi->services_haproxy_runtime_acl_file_entries_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acl_id** | **str**| ACL ID | 
 **id** | **str**| File entry ID | 

### Return type

[**AclFileEntry**](AclFileEntry.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **services_haproxy_runtime_acl_file_entries_post**
> AclFileEntry services_haproxy_runtime_acl_file_entries_post(body, acl_id)

Add entry to an ACL file

Adds an entry into the ACL file using the runtime socket.

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
api_instance = dataplaneapi.ACLRuntimeApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.AclFileEntry() # AclFileEntry | 
acl_id = 'acl_id_example' # str | ACL ID

try:
    # Add entry to an ACL file
    api_response = api_instance.services_haproxy_runtime_acl_file_entries_post(body, acl_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ACLRuntimeApi->services_haproxy_runtime_acl_file_entries_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AclFileEntry**](AclFileEntry.md)|  | 
 **acl_id** | **str**| ACL ID | 

### Return type

[**AclFileEntry**](AclFileEntry.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **services_haproxy_runtime_acls_get**
> AclFiles services_haproxy_runtime_acls_get()

Return an array of all ACL files

Returns all ACL files using the runtime socket.

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
api_instance = dataplaneapi.ACLRuntimeApi(dataplaneapi.ApiClient(configuration))

try:
    # Return an array of all ACL files
    api_response = api_instance.services_haproxy_runtime_acls_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ACLRuntimeApi->services_haproxy_runtime_acls_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AclFiles**](AclFiles.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **services_haproxy_runtime_acls_id_get**
> AclFile services_haproxy_runtime_acls_id_get(id)

Return an ACL file

Returns an ACL file by id using the runtime socket.

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
api_instance = dataplaneapi.ACLRuntimeApi(dataplaneapi.ApiClient(configuration))
id = 'id_example' # str | ACL file entry ID

try:
    # Return an ACL file
    api_response = api_instance.services_haproxy_runtime_acls_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ACLRuntimeApi->services_haproxy_runtime_acls_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ACL file entry ID | 

### Return type

[**AclFile**](AclFile.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

