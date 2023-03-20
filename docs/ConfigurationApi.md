# swagger_client.ConfigurationApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_configuration_version**](ConfigurationApi.md#get_configuration_version) | **GET** /services/haproxy/configuration/version | Return a configuration version
[**get_ha_proxy_configuration**](ConfigurationApi.md#get_ha_proxy_configuration) | **GET** /services/haproxy/configuration/raw | Return HAProxy configuration
[**post_ha_proxy_configuration**](ConfigurationApi.md#post_ha_proxy_configuration) | **POST** /services/haproxy/configuration/raw | Push new haproxy configuration

# **get_configuration_version**
> int get_configuration_version(transaction_id=transaction_id)

Return a configuration version

Returns configuration version.

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
api_instance = dataplaneapi.ConfigurationApi(dataplaneapi.ApiClient(configuration))
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return a configuration version
    api_response = api_instance.get_configuration_version(transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_configuration_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

**int**

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ha_proxy_configuration**
> InlineResponse20057 get_ha_proxy_configuration(transaction_id=transaction_id, version=version)

Return HAProxy configuration

Returns HAProxy configuration file in plain text

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
api_instance = dataplaneapi.ConfigurationApi(dataplaneapi.ApiClient(configuration))
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)

try:
    # Return HAProxy configuration
    api_response = api_instance.get_ha_proxy_configuration(transaction_id=transaction_id, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_ha_proxy_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ha_proxy_configuration**
> str post_ha_proxy_configuration(body, x_runtime_actions=x_runtime_actions, skip_version=skip_version, skip_reload=skip_reload, only_validate=only_validate, version=version, force_reload=force_reload)

Push new haproxy configuration

Push a new haproxy configuration file in plain text

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
api_instance = dataplaneapi.ConfigurationApi(dataplaneapi.ApiClient(configuration))
body = 'body_example' # str | 
x_runtime_actions = 'x_runtime_actions_example' # str | List of Runtime API commands with parameters separated by ';' (optional)
skip_version = false # bool | If set, no version check will be done and the pushed config will be enforced (optional) (default to false)
skip_reload = false # bool | If set, no reload will be initiated and runtime actions from X-Runtime-Actions will be applied (optional) (default to false)
only_validate = false # bool | If set, only validates configuration, without applying it (optional) (default to false)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Push new haproxy configuration
    api_response = api_instance.post_ha_proxy_configuration(body, x_runtime_actions=x_runtime_actions, skip_version=skip_version, skip_reload=skip_reload, only_validate=only_validate, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->post_ha_proxy_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **x_runtime_actions** | **str**| List of Runtime API commands with parameters separated by &#x27;;&#x27; | [optional] 
 **skip_version** | **bool**| If set, no version check will be done and the pushed config will be enforced | [optional] [default to false]
 **skip_reload** | **bool**| If set, no reload will be initiated and runtime actions from X-Runtime-Actions will be applied | [optional] [default to false]
 **only_validate** | **bool**| If set, only validates configuration, without applying it | [optional] [default to false]
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

**str**

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

