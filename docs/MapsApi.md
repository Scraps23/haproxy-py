# swagger_client.MapsApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_map_entry**](MapsApi.md#add_map_entry) | **POST** /services/haproxy/runtime/maps_entries | Adds an entry into the map file
[**add_payload_runtime_map**](MapsApi.md#add_payload_runtime_map) | **PUT** /services/haproxy/runtime/maps/{name} | Add a new map payload
[**clear_runtime_map**](MapsApi.md#clear_runtime_map) | **DELETE** /services/haproxy/runtime/maps/{name} | Remove all map entries from the map file
[**delete_runtime_map_entry**](MapsApi.md#delete_runtime_map_entry) | **DELETE** /services/haproxy/runtime/maps_entries/{id} | Deletes all the map entries from the map by its id
[**get_all_runtime_map_files**](MapsApi.md#get_all_runtime_map_files) | **GET** /services/haproxy/runtime/maps | Return runtime map files
[**get_one_runtime_map**](MapsApi.md#get_one_runtime_map) | **GET** /services/haproxy/runtime/maps/{name} | Return one runtime map file
[**get_runtime_map_entry**](MapsApi.md#get_runtime_map_entry) | **GET** /services/haproxy/runtime/maps_entries/{id} | Return one map runtime setting
[**replace_runtime_map_entry**](MapsApi.md#replace_runtime_map_entry) | **PUT** /services/haproxy/runtime/maps_entries/{id} | Replace the value corresponding to each id in a map
[**show_runtime_map**](MapsApi.md#show_runtime_map) | **GET** /services/haproxy/runtime/maps_entries | Return one map runtime entries

# **add_map_entry**
> MapEntry add_map_entry(body, map, force_sync=force_sync)

Adds an entry into the map file

Adds an entry into the map file.

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
api_instance = dataplaneapi.MapsApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.MapEntry() # MapEntry | 
map = 'map_example' # str | Mapfile attribute storage_name
force_sync = false # bool | If true, immediately syncs changes to disk (optional) (default to false)

try:
    # Adds an entry into the map file
    api_response = api_instance.add_map_entry(body, map, force_sync=force_sync)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->add_map_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MapEntry**](MapEntry.md)|  | 
 **map** | **str**| Mapfile attribute storage_name | 
 **force_sync** | **bool**| If true, immediately syncs changes to disk | [optional] [default to false]

### Return type

[**MapEntry**](MapEntry.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_payload_runtime_map**
> MapEntries add_payload_runtime_map(body, name, force_sync=force_sync)

Add a new map payload

Adds a new map payload.

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
api_instance = dataplaneapi.MapsApi(dataplaneapi.ApiClient(configuration))
body = [dataplaneapi.MapEntry()] # list[MapEntry] | 
name = 'name_example' # str | Map file name
force_sync = false # bool | If true, immediately syncs changes to disk (optional) (default to false)

try:
    # Add a new map payload
    api_response = api_instance.add_payload_runtime_map(body, name, force_sync=force_sync)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->add_payload_runtime_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MapEntry]**](MapEntry.md)|  | 
 **name** | **str**| Map file name | 
 **force_sync** | **bool**| If true, immediately syncs changes to disk | [optional] [default to false]

### Return type

[**MapEntries**](MapEntries.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_runtime_map**
> clear_runtime_map(name, force_delete=force_delete, force_sync=force_sync)

Remove all map entries from the map file

Remove all map entries from the map file.

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
api_instance = dataplaneapi.MapsApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | Map file name
force_delete = true # bool | If true, deletes file from disk (optional)
force_sync = false # bool | If true, immediately syncs changes to disk (optional) (default to false)

try:
    # Remove all map entries from the map file
    api_instance.clear_runtime_map(name, force_delete=force_delete, force_sync=force_sync)
except ApiException as e:
    print("Exception when calling MapsApi->clear_runtime_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Map file name | 
 **force_delete** | **bool**| If true, deletes file from disk | [optional] 
 **force_sync** | **bool**| If true, immediately syncs changes to disk | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_runtime_map_entry**
> delete_runtime_map_entry(id, map, force_sync=force_sync)

Deletes all the map entries from the map by its id

Delete all the map entries from the map by its id.

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
api_instance = dataplaneapi.MapsApi(dataplaneapi.ApiClient(configuration))
id = 'id_example' # str | Map id
map = 'map_example' # str | Mapfile attribute storage_name
force_sync = false # bool | If true, immediately syncs changes to disk (optional) (default to false)

try:
    # Deletes all the map entries from the map by its id
    api_instance.delete_runtime_map_entry(id, map, force_sync=force_sync)
except ApiException as e:
    print("Exception when calling MapsApi->delete_runtime_map_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Map id | 
 **map** | **str**| Mapfile attribute storage_name | 
 **force_sync** | **bool**| If true, immediately syncs changes to disk | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_runtime_map_files**
> Maps get_all_runtime_map_files(include_unmanaged=include_unmanaged)

Return runtime map files

Returns runtime map files.

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
api_instance = dataplaneapi.MapsApi(dataplaneapi.ApiClient(configuration))
include_unmanaged = false # bool | If true, also show unmanaged map files loaded in haproxy (optional) (default to false)

try:
    # Return runtime map files
    api_response = api_instance.get_all_runtime_map_files(include_unmanaged=include_unmanaged)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->get_all_runtime_map_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_unmanaged** | **bool**| If true, also show unmanaged map files loaded in haproxy | [optional] [default to false]

### Return type

[**Maps**](Maps.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_runtime_map**
> dict get_one_runtime_map(name)

Return one runtime map file

Returns one runtime map file.

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
api_instance = dataplaneapi.MapsApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | Map file name

try:
    # Return one runtime map file
    api_response = api_instance.get_one_runtime_map(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->get_one_runtime_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Map file name | 

### Return type

**dict**

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runtime_map_entry**
> MapEntry get_runtime_map_entry(id, map)

Return one map runtime setting

Returns one map runtime setting by it's id.

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
api_instance = dataplaneapi.MapsApi(dataplaneapi.ApiClient(configuration))
id = 'id_example' # str | Map id
map = 'map_example' # str | Mapfile attribute storage_name

try:
    # Return one map runtime setting
    api_response = api_instance.get_runtime_map_entry(id, map)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->get_runtime_map_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Map id | 
 **map** | **str**| Mapfile attribute storage_name | 

### Return type

[**MapEntry**](MapEntry.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_runtime_map_entry**
> MapEntry replace_runtime_map_entry(body, map, id, force_sync=force_sync)

Replace the value corresponding to each id in a map

Replaces the value corresponding to each id in a map.

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
api_instance = dataplaneapi.MapsApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.MapsEntriesIdBody() # MapsEntriesIdBody | 
map = 'map_example' # str | Mapfile attribute storage_name
id = 'id_example' # str | Map id
force_sync = false # bool | If true, immediately syncs changes to disk (optional) (default to false)

try:
    # Replace the value corresponding to each id in a map
    api_response = api_instance.replace_runtime_map_entry(body, map, id, force_sync=force_sync)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->replace_runtime_map_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MapsEntriesIdBody**](MapsEntriesIdBody.md)|  | 
 **map** | **str**| Mapfile attribute storage_name | 
 **id** | **str**| Map id | 
 **force_sync** | **bool**| If true, immediately syncs changes to disk | [optional] [default to false]

### Return type

[**MapEntry**](MapEntry.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_runtime_map**
> MapEntries show_runtime_map(map)

Return one map runtime entries

Returns an array of all entries in a given runtime map file.

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
api_instance = dataplaneapi.MapsApi(dataplaneapi.ApiClient(configuration))
map = 'map_example' # str | Mapfile attribute storage_name

try:
    # Return one map runtime entries
    api_response = api_instance.show_runtime_map(map)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->show_runtime_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map** | **str**| Mapfile attribute storage_name | 

### Return type

[**MapEntries**](MapEntries.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

