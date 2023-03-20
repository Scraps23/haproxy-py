# swagger_client.DiscoveryApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_endpoints**](DiscoveryApi.md#get_api_endpoints) | **GET** / | Return list of root endpoints
[**get_configuration_endpoints**](DiscoveryApi.md#get_configuration_endpoints) | **GET** /services/haproxy/configuration | Return list of HAProxy advanced configuration endpoints
[**get_haproxy_endpoints**](DiscoveryApi.md#get_haproxy_endpoints) | **GET** /services/haproxy | Return list of HAProxy related endpoints
[**get_runtime_endpoints**](DiscoveryApi.md#get_runtime_endpoints) | **GET** /services/haproxy/runtime | Return list of HAProxy advanced runtime endpoints
[**get_services_endpoints**](DiscoveryApi.md#get_services_endpoints) | **GET** /services | Return list of service endpoints
[**get_spoe_endpoints**](DiscoveryApi.md#get_spoe_endpoints) | **GET** /services/haproxy/spoe | Return list of HAProxy SPOE endpoints
[**get_stats_endpoints**](DiscoveryApi.md#get_stats_endpoints) | **GET** /services/haproxy/stats | Return list of HAProxy stats endpoints
[**get_storage_endpoints**](DiscoveryApi.md#get_storage_endpoints) | **GET** /services/haproxy/storage | Return list of HAProxy storage endpoints

# **get_api_endpoints**
> Endpoints get_api_endpoints()

Return list of root endpoints

Returns a list of root endpoints.

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
api_instance = dataplaneapi.DiscoveryApi(dataplaneapi.ApiClient(configuration))

try:
    # Return list of root endpoints
    api_response = api_instance.get_api_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->get_api_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Endpoints**](Endpoints.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration_endpoints**
> Endpoints get_configuration_endpoints()

Return list of HAProxy advanced configuration endpoints

Returns a list of endpoints to be used for advanced configuration of HAProxy objects.

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
api_instance = dataplaneapi.DiscoveryApi(dataplaneapi.ApiClient(configuration))

try:
    # Return list of HAProxy advanced configuration endpoints
    api_response = api_instance.get_configuration_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->get_configuration_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Endpoints**](Endpoints.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_haproxy_endpoints**
> Endpoints get_haproxy_endpoints()

Return list of HAProxy related endpoints

Returns a list of HAProxy related endpoints.

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
api_instance = dataplaneapi.DiscoveryApi(dataplaneapi.ApiClient(configuration))

try:
    # Return list of HAProxy related endpoints
    api_response = api_instance.get_haproxy_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->get_haproxy_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Endpoints**](Endpoints.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runtime_endpoints**
> Endpoints get_runtime_endpoints()

Return list of HAProxy advanced runtime endpoints

Returns a list of endpoints to be used for advanced runtime settings of HAProxy objects.

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
api_instance = dataplaneapi.DiscoveryApi(dataplaneapi.ApiClient(configuration))

try:
    # Return list of HAProxy advanced runtime endpoints
    api_response = api_instance.get_runtime_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->get_runtime_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Endpoints**](Endpoints.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services_endpoints**
> Endpoints get_services_endpoints()

Return list of service endpoints

Returns a list of API managed services endpoints.

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
api_instance = dataplaneapi.DiscoveryApi(dataplaneapi.ApiClient(configuration))

try:
    # Return list of service endpoints
    api_response = api_instance.get_services_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->get_services_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Endpoints**](Endpoints.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spoe_endpoints**
> Endpoints get_spoe_endpoints()

Return list of HAProxy SPOE endpoints

Returns a list of endpoints to be used for SPOE settings of HAProxy.

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
api_instance = dataplaneapi.DiscoveryApi(dataplaneapi.ApiClient(configuration))

try:
    # Return list of HAProxy SPOE endpoints
    api_response = api_instance.get_spoe_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->get_spoe_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Endpoints**](Endpoints.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats_endpoints**
> Endpoints get_stats_endpoints()

Return list of HAProxy stats endpoints

Returns a list of HAProxy stats endpoints.

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
api_instance = dataplaneapi.DiscoveryApi(dataplaneapi.ApiClient(configuration))

try:
    # Return list of HAProxy stats endpoints
    api_response = api_instance.get_stats_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->get_stats_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Endpoints**](Endpoints.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_endpoints**
> Endpoints get_storage_endpoints()

Return list of HAProxy storage endpoints

Returns a list of endpoints that use HAProxy storage for persistency, e.g. maps, ssl certificates...

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
api_instance = dataplaneapi.DiscoveryApi(dataplaneapi.ApiClient(configuration))

try:
    # Return list of HAProxy storage endpoints
    api_response = api_instance.get_storage_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->get_storage_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Endpoints**](Endpoints.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

