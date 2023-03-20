# swagger_client.DeclareCaptureApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_declare_capture**](DeclareCaptureApi.md#create_declare_capture) | **POST** /services/haproxy/configuration/captures | Add a new declare capture
[**delete_declare_capture**](DeclareCaptureApi.md#delete_declare_capture) | **DELETE** /services/haproxy/configuration/captures/{index} | Delete a declare capture
[**get_declare_capture**](DeclareCaptureApi.md#get_declare_capture) | **GET** /services/haproxy/configuration/captures/{index} | Return one declare capture
[**get_declare_captures**](DeclareCaptureApi.md#get_declare_captures) | **GET** /services/haproxy/configuration/captures | Return an array of declare captures
[**replace_declare_capture**](DeclareCaptureApi.md#replace_declare_capture) | **PUT** /services/haproxy/configuration/captures/{index} | Replace a declare capture

# **create_declare_capture**
> Capture create_declare_capture(body, frontend, transaction_id=transaction_id, version=version, force_reload=force_reload)

Add a new declare capture

Adds a new declare capture in the specified frontend in the configuration file.

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
api_instance = dataplaneapi.DeclareCaptureApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.Capture() # Capture | 
frontend = 'frontend_example' # str | Parent frontend name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Add a new declare capture
    api_response = api_instance.create_declare_capture(body, frontend, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeclareCaptureApi->create_declare_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Capture**](Capture.md)|  | 
 **frontend** | **str**| Parent frontend name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**Capture**](Capture.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_declare_capture**
> delete_declare_capture(index, frontend, transaction_id=transaction_id, version=version, force_reload=force_reload)

Delete a declare capture

Deletes a declare capture configuration by it's index in the specified frontend.

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
api_instance = dataplaneapi.DeclareCaptureApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | Declare Capture Index
frontend = 'frontend_example' # str | Parent frontend name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Delete a declare capture
    api_instance.delete_declare_capture(index, frontend, transaction_id=transaction_id, version=version, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling DeclareCaptureApi->delete_declare_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| Declare Capture Index | 
 **frontend** | **str**| Parent frontend name | 
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

# **get_declare_capture**
> InlineResponse20015 get_declare_capture(index, frontend, transaction_id=transaction_id)

Return one declare capture

Returns one declare capture configuration by it's index in the specified frontend.

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
api_instance = dataplaneapi.DeclareCaptureApi(dataplaneapi.ApiClient(configuration))
index = 56 # int | Declare Capture Index
frontend = 'frontend_example' # str | Parent frontend name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return one declare capture
    api_response = api_instance.get_declare_capture(index, frontend, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeclareCaptureApi->get_declare_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| Declare Capture Index | 
 **frontend** | **str**| Parent frontend name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_declare_captures**
> InlineResponse20014 get_declare_captures(frontend, transaction_id=transaction_id)

Return an array of declare captures

Returns an array of all declare capture records that are configured in specified frontend.

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
api_instance = dataplaneapi.DeclareCaptureApi(dataplaneapi.ApiClient(configuration))
frontend = 'frontend_example' # str | Parent frontend name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of declare captures
    api_response = api_instance.get_declare_captures(frontend, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeclareCaptureApi->get_declare_captures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **frontend** | **str**| Parent frontend name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_declare_capture**
> Capture replace_declare_capture(body, frontend, index, transaction_id=transaction_id, version=version, force_reload=force_reload)

Replace a declare capture

Replaces a declare capture configuration by it's index in the specified frontend.

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
api_instance = dataplaneapi.DeclareCaptureApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.Capture() # Capture | 
frontend = 'frontend_example' # str | Parent frontend name
index = 56 # int | Declare Capture Index
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace a declare capture
    api_response = api_instance.replace_declare_capture(body, frontend, index, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeclareCaptureApi->replace_declare_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Capture**](Capture.md)|  | 
 **frontend** | **str**| Parent frontend name | 
 **index** | **int**| Declare Capture Index | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**Capture**](Capture.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

