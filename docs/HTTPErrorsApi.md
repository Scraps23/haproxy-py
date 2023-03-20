# swagger_client.HTTPErrorsApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_http_errors_section**](HTTPErrorsApi.md#create_http_errors_section) | **POST** /services/haproxy/configuration/http_errors_sections | Add a new http-error section
[**delete_http_errors_section**](HTTPErrorsApi.md#delete_http_errors_section) | **DELETE** /services/haproxy/configuration/http_errors_sections/{name} | Delete a http-error section
[**get_http_errors_section**](HTTPErrorsApi.md#get_http_errors_section) | **GET** /services/haproxy/configuration/http_errors_sections/{name} | Return a http-error section
[**get_http_errors_sections**](HTTPErrorsApi.md#get_http_errors_sections) | **GET** /services/haproxy/configuration/http_errors_sections | Return an array of http-error sections
[**replace_http_errors_section**](HTTPErrorsApi.md#replace_http_errors_section) | **PUT** /services/haproxy/configuration/http_errors_sections/{name} | Replace a http-error section

# **create_http_errors_section**
> HttpErrorsSection create_http_errors_section(body, transaction_id=transaction_id, version=version, force_reload=force_reload)

Add a new http-error section

Adds a new http-error section to the configuration.

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
api_instance = dataplaneapi.HTTPErrorsApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.HttpErrorsSection() # HttpErrorsSection | 
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Add a new http-error section
    api_response = api_instance.create_http_errors_section(body, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HTTPErrorsApi->create_http_errors_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HttpErrorsSection**](HttpErrorsSection.md)|  | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**HttpErrorsSection**](HttpErrorsSection.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_http_errors_section**
> delete_http_errors_section(name, transaction_id=transaction_id, version=version, force_reload=force_reload)

Delete a http-error section

Deletes a http-error section with a given name from the configuration.

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
api_instance = dataplaneapi.HTTPErrorsApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | http-error section name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Delete a http-error section
    api_instance.delete_http_errors_section(name, transaction_id=transaction_id, version=version, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling HTTPErrorsApi->delete_http_errors_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| http-error section name | 
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

# **get_http_errors_section**
> InlineResponse20035 get_http_errors_section(name, transaction_id=transaction_id)

Return a http-error section

Returns one http-error section with a given name from the configuration.

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
api_instance = dataplaneapi.HTTPErrorsApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | http-error section name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return a http-error section
    api_response = api_instance.get_http_errors_section(name, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HTTPErrorsApi->get_http_errors_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| http-error section name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_http_errors_sections**
> InlineResponse20034 get_http_errors_sections(transaction_id=transaction_id)

Return an array of http-error sections

Returns an array of all configured http-error sections.

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
api_instance = dataplaneapi.HTTPErrorsApi(dataplaneapi.ApiClient(configuration))
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of http-error sections
    api_response = api_instance.get_http_errors_sections(transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HTTPErrorsApi->get_http_errors_sections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_http_errors_section**
> HttpErrorsSection replace_http_errors_section(body, name, transaction_id=transaction_id, version=version, force_reload=force_reload)

Replace a http-error section

Replaces a http-error section with a given name in the configuration.

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
api_instance = dataplaneapi.HTTPErrorsApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.HttpErrorsSection() # HttpErrorsSection | 
name = 'name_example' # str | http-error section name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace a http-error section
    api_response = api_instance.replace_http_errors_section(body, name, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HTTPErrorsApi->replace_http_errors_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HttpErrorsSection**](HttpErrorsSection.md)|  | 
 **name** | **str**| http-error section name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**HttpErrorsSection**](HttpErrorsSection.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

