# swagger_client.PeerEntryApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_peer_entry**](PeerEntryApi.md#create_peer_entry) | **POST** /services/haproxy/configuration/peer_entries | Add a new peer_entry
[**delete_peer_entry**](PeerEntryApi.md#delete_peer_entry) | **DELETE** /services/haproxy/configuration/peer_entries/{name} | Delete a peer_entry
[**get_peer_entries**](PeerEntryApi.md#get_peer_entries) | **GET** /services/haproxy/configuration/peer_entries | Return an array of peer_entries
[**get_peer_entry**](PeerEntryApi.md#get_peer_entry) | **GET** /services/haproxy/configuration/peer_entries/{name} | Return one peer_entry
[**replace_peer_entry**](PeerEntryApi.md#replace_peer_entry) | **PUT** /services/haproxy/configuration/peer_entries/{name} | Replace a peer_entry

# **create_peer_entry**
> PeerEntry create_peer_entry(body, peer_section, transaction_id=transaction_id, version=version, force_reload=force_reload)

Add a new peer_entry

Adds a new peer entry in the specified peer section in the configuration file.

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
api_instance = dataplaneapi.PeerEntryApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.PeerEntry() # PeerEntry | 
peer_section = 'peer_section_example' # str | Parent peer section name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Add a new peer_entry
    api_response = api_instance.create_peer_entry(body, peer_section, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerEntryApi->create_peer_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PeerEntry**](PeerEntry.md)|  | 
 **peer_section** | **str**| Parent peer section name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**PeerEntry**](PeerEntry.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_peer_entry**
> delete_peer_entry(name, peer_section, transaction_id=transaction_id, version=version, force_reload=force_reload)

Delete a peer_entry

Deletes a peer entry configuration by it's name in the specified peer section.

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
api_instance = dataplaneapi.PeerEntryApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | PeerEntry name
peer_section = 'peer_section_example' # str | Parent peers name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Delete a peer_entry
    api_instance.delete_peer_entry(name, peer_section, transaction_id=transaction_id, version=version, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling PeerEntryApi->delete_peer_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| PeerEntry name | 
 **peer_section** | **str**| Parent peers name | 
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

# **get_peer_entries**
> InlineResponse20051 get_peer_entries(peer_section, transaction_id=transaction_id)

Return an array of peer_entries

Returns an array of all peer_entries that are configured in specified peer section.

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
api_instance = dataplaneapi.PeerEntryApi(dataplaneapi.ApiClient(configuration))
peer_section = 'peer_section_example' # str | Parent peer section name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of peer_entries
    api_response = api_instance.get_peer_entries(peer_section, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerEntryApi->get_peer_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **peer_section** | **str**| Parent peer section name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_peer_entry**
> InlineResponse20052 get_peer_entry(name, peer_section, transaction_id=transaction_id)

Return one peer_entry

Returns one peer_entry configuration by it's name in the specified peer section.

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
api_instance = dataplaneapi.PeerEntryApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | PeerEntry name
peer_section = 'peer_section_example' # str | Parent peers name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return one peer_entry
    api_response = api_instance.get_peer_entry(name, peer_section, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerEntryApi->get_peer_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| PeerEntry name | 
 **peer_section** | **str**| Parent peers name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_peer_entry**
> PeerEntry replace_peer_entry(body, peer_section, name, transaction_id=transaction_id, version=version, force_reload=force_reload)

Replace a peer_entry

Replaces a peer entry configuration by it's name in the specified peer section.

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
api_instance = dataplaneapi.PeerEntryApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.PeerEntry() # PeerEntry | 
peer_section = 'peer_section_example' # str | Parent peers name
name = 'name_example' # str | PeerEntry name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace a peer_entry
    api_response = api_instance.replace_peer_entry(body, peer_section, name, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerEntryApi->replace_peer_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PeerEntry**](PeerEntry.md)|  | 
 **peer_section** | **str**| Parent peers name | 
 **name** | **str**| PeerEntry name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**PeerEntry**](PeerEntry.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

