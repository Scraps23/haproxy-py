# swagger_client.StickTableApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stick_table**](StickTableApi.md#get_stick_table) | **GET** /services/haproxy/runtime/stick_tables/{name} | Return Stick Table
[**get_stick_table_entries**](StickTableApi.md#get_stick_table_entries) | **GET** /services/haproxy/runtime/stick_table_entries | Return Stick Table Entries
[**get_stick_tables**](StickTableApi.md#get_stick_tables) | **GET** /services/haproxy/runtime/stick_tables | Return Stick Tables
[**set_stick_table_entries**](StickTableApi.md#set_stick_table_entries) | **POST** /services/haproxy/runtime/stick_table_entries | Set Entry to Stick Table

# **get_stick_table**
> StickTable get_stick_table(name, process)

Return Stick Table

Returns one stick table from runtime.

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
api_instance = dataplaneapi.StickTableApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | Stick table name
process = 56 # int | Process number if master-worker mode, if not only first process is returned

try:
    # Return Stick Table
    api_response = api_instance.get_stick_table(name, process)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StickTableApi->get_stick_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Stick table name | 
 **process** | **int**| Process number if master-worker mode, if not only first process is returned | 

### Return type

[**StickTable**](StickTable.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stick_table_entries**
> StickTableEntries get_stick_table_entries(stick_table, process, filter=filter, key=key, count=count, offset=offset)

Return Stick Table Entries

Returns an array of all entries in a given stick tables.

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
api_instance = dataplaneapi.StickTableApi(dataplaneapi.ApiClient(configuration))
stick_table = 'stick_table_example' # str | Stick table name
process = 56 # int | Process number if master-worker mode, if not only first process is returned
filter = 'filter_example' # str | A list of filters in format data.<type> <operator> <value> separated by comma (optional)
key = 'key_example' # str | Key which we want the entries for (optional)
count = 56 # int | Max number of entries to be returned for pagination (optional)
offset = 56 # int | Offset which indicates how many items we skip in pagination (optional)

try:
    # Return Stick Table Entries
    api_response = api_instance.get_stick_table_entries(stick_table, process, filter=filter, key=key, count=count, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StickTableApi->get_stick_table_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stick_table** | **str**| Stick table name | 
 **process** | **int**| Process number if master-worker mode, if not only first process is returned | 
 **filter** | **str**| A list of filters in format data.&lt;type&gt; &lt;operator&gt; &lt;value&gt; separated by comma | [optional] 
 **key** | **str**| Key which we want the entries for | [optional] 
 **count** | **int**| Max number of entries to be returned for pagination | [optional] 
 **offset** | **int**| Offset which indicates how many items we skip in pagination | [optional] 

### Return type

[**StickTableEntries**](StickTableEntries.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stick_tables**
> StickTables get_stick_tables(process=process)

Return Stick Tables

Returns an array of all stick tables.

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
api_instance = dataplaneapi.StickTableApi(dataplaneapi.ApiClient(configuration))
process = 56 # int | Process number if master-worker mode, if not all processes are returned (optional)

try:
    # Return Stick Tables
    api_response = api_instance.get_stick_tables(process=process)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StickTableApi->get_stick_tables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process** | **int**| Process number if master-worker mode, if not all processes are returned | [optional] 

### Return type

[**StickTables**](StickTables.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_stick_table_entries**
> set_stick_table_entries(stick_table, process, body=body)

Set Entry to Stick Table

Create or update a stick-table entry in the table.

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
api_instance = dataplaneapi.StickTableApi(dataplaneapi.ApiClient(configuration))
stick_table = 'stick_table_example' # str | Stick table name
process = 56 # int | Process number if master-worker mode, if not only first process is returned
body = dataplaneapi.RuntimeStickTableEntriesBody() # RuntimeStickTableEntriesBody | Stick table entry (optional)

try:
    # Set Entry to Stick Table
    api_instance.set_stick_table_entries(stick_table, process, body=body)
except ApiException as e:
    print("Exception when calling StickTableApi->set_stick_table_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stick_table** | **str**| Stick table name | 
 **process** | **int**| Process number if master-worker mode, if not only first process is returned | 
 **body** | [**RuntimeStickTableEntriesBody**](RuntimeStickTableEntriesBody.md)| Stick table entry | [optional] 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

