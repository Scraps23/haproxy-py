# swagger_client.TransactionsApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commit_transaction**](TransactionsApi.md#commit_transaction) | **PUT** /services/haproxy/transactions/{id} | Commit transaction
[**delete_transaction**](TransactionsApi.md#delete_transaction) | **DELETE** /services/haproxy/transactions/{id} | Delete a transaction
[**get_transaction**](TransactionsApi.md#get_transaction) | **GET** /services/haproxy/transactions/{id} | Return one HAProxy configuration transactions
[**get_transactions**](TransactionsApi.md#get_transactions) | **GET** /services/haproxy/transactions | Return list of HAProxy configuration transactions.
[**start_transaction**](TransactionsApi.md#start_transaction) | **POST** /services/haproxy/transactions | Start a new transaction

# **commit_transaction**
> Transaction commit_transaction(id, force_reload=force_reload)

Commit transaction

Commit transaction, execute all operations in transaction and return msg

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
api_instance = dataplaneapi.TransactionsApi(dataplaneapi.ApiClient(configuration))
id = 'id_example' # str | Transaction id
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Commit transaction
    api_response = api_instance.commit_transaction(id, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->commit_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Transaction id | 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**Transaction**](Transaction.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction**
> delete_transaction(id)

Delete a transaction

Deletes a transaction.

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
api_instance = dataplaneapi.TransactionsApi(dataplaneapi.ApiClient(configuration))
id = 'id_example' # str | Transaction id

try:
    # Delete a transaction
    api_instance.delete_transaction(id)
except ApiException as e:
    print("Exception when calling TransactionsApi->delete_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Transaction id | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction**
> Transaction get_transaction(id)

Return one HAProxy configuration transactions

Returns one HAProxy configuration transactions.

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
api_instance = dataplaneapi.TransactionsApi(dataplaneapi.ApiClient(configuration))
id = 'id_example' # str | Transaction id

try:
    # Return one HAProxy configuration transactions
    api_response = api_instance.get_transaction(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Transaction id | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> Transactions get_transactions(status=status)

Return list of HAProxy configuration transactions.

Returns a list of HAProxy configuration transactions. Transactions can be filtered by their status.

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
api_instance = dataplaneapi.TransactionsApi(dataplaneapi.ApiClient(configuration))
status = 'status_example' # str | Filter by transaction status (optional)

try:
    # Return list of HAProxy configuration transactions.
    api_response = api_instance.get_transactions(status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter by transaction status | [optional] 

### Return type

[**Transactions**](Transactions.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_transaction**
> Transaction start_transaction(version)

Start a new transaction

Starts a new transaction and returns it's id

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
api_instance = dataplaneapi.TransactionsApi(dataplaneapi.ApiClient(configuration))
version = 56 # int | Configuration version on which to work on

try:
    # Start a new transaction
    api_response = api_instance.start_transaction(version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->start_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **int**| Configuration version on which to work on | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

