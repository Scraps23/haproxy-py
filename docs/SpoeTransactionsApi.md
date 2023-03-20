# swagger_client.SpoeTransactionsApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commit_spoe_transaction**](SpoeTransactionsApi.md#commit_spoe_transaction) | **PUT** /services/haproxy/spoe_transactions/{id} | Commit transaction
[**delete_spoe_transaction**](SpoeTransactionsApi.md#delete_spoe_transaction) | **DELETE** /services/haproxy/spoe_transactions/{id} | Delete a transaction
[**get_spoe_transaction**](SpoeTransactionsApi.md#get_spoe_transaction) | **GET** /services/haproxy/spoe_transactions/{id} | Return one SPOE configuration transactions
[**get_spoe_transactions**](SpoeTransactionsApi.md#get_spoe_transactions) | **GET** /services/haproxy/spoe_transactions | Return list of SPOE configuration transactions.
[**start_spoe_transaction**](SpoeTransactionsApi.md#start_spoe_transaction) | **POST** /services/haproxy/spoe_transactions | Start a new transaction

# **commit_spoe_transaction**
> SpoeTransaction commit_spoe_transaction(spoe, id, force_reload=force_reload)

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
api_instance = dataplaneapi.SpoeTransactionsApi(dataplaneapi.ApiClient(configuration))
spoe = 'spoe_example' # str | Spoe file name
id = 'id_example' # str | Transaction id
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Commit transaction
    api_response = api_instance.commit_spoe_transaction(spoe, id, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeTransactionsApi->commit_spoe_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spoe** | **str**| Spoe file name | 
 **id** | **str**| Transaction id | 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**SpoeTransaction**](SpoeTransaction.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_spoe_transaction**
> delete_spoe_transaction(spoe, id)

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
api_instance = dataplaneapi.SpoeTransactionsApi(dataplaneapi.ApiClient(configuration))
spoe = 'spoe_example' # str | Spoe file name
id = 'id_example' # str | Transaction id

try:
    # Delete a transaction
    api_instance.delete_spoe_transaction(spoe, id)
except ApiException as e:
    print("Exception when calling SpoeTransactionsApi->delete_spoe_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spoe** | **str**| Spoe file name | 
 **id** | **str**| Transaction id | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spoe_transaction**
> SpoeTransaction get_spoe_transaction(spoe, id)

Return one SPOE configuration transactions

Returns one SPOE configuration transactions.

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
api_instance = dataplaneapi.SpoeTransactionsApi(dataplaneapi.ApiClient(configuration))
spoe = 'spoe_example' # str | Spoe file name
id = 'id_example' # str | Transaction id

try:
    # Return one SPOE configuration transactions
    api_response = api_instance.get_spoe_transaction(spoe, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeTransactionsApi->get_spoe_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spoe** | **str**| Spoe file name | 
 **id** | **str**| Transaction id | 

### Return type

[**SpoeTransaction**](SpoeTransaction.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spoe_transactions**
> SpoeTransactions get_spoe_transactions(spoe, status=status)

Return list of SPOE configuration transactions.

Returns a list of SPOE configuration transactions. Transactions can be filtered by their status.

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
api_instance = dataplaneapi.SpoeTransactionsApi(dataplaneapi.ApiClient(configuration))
spoe = 'spoe_example' # str | Spoe file name
status = 'status_example' # str | Filter by transaction status (optional)

try:
    # Return list of SPOE configuration transactions.
    api_response = api_instance.get_spoe_transactions(spoe, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeTransactionsApi->get_spoe_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spoe** | **str**| Spoe file name | 
 **status** | **str**| Filter by transaction status | [optional] 

### Return type

[**SpoeTransactions**](SpoeTransactions.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_spoe_transaction**
> SpoeTransaction start_spoe_transaction(spoe, version)

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
api_instance = dataplaneapi.SpoeTransactionsApi(dataplaneapi.ApiClient(configuration))
spoe = 'spoe_example' # str | Spoe file name
version = 56 # int | Configuration version on which to work on

try:
    # Start a new transaction
    api_response = api_instance.start_spoe_transaction(spoe, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpoeTransactionsApi->start_spoe_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spoe** | **str**| Spoe file name | 
 **version** | **int**| Configuration version on which to work on | 

### Return type

[**SpoeTransaction**](SpoeTransaction.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

