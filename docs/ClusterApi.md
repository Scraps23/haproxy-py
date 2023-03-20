# swagger_client.ClusterApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cluster**](ClusterApi.md#delete_cluster) | **DELETE** /cluster | Delete cluster settings
[**edit_cluster**](ClusterApi.md#edit_cluster) | **PUT** /cluster | Edit cluster settings
[**get_cluster**](ClusterApi.md#get_cluster) | **GET** /cluster | Return cluster data
[**initiate_certificate_refresh**](ClusterApi.md#initiate_certificate_refresh) | **POST** /cluster/certificate | Initiates a certificate refresh
[**post_cluster**](ClusterApi.md#post_cluster) | **POST** /cluster | Post cluster settings

# **delete_cluster**
> delete_cluster(configuration=configuration, version=version)

Delete cluster settings

Delete cluster settings and move the node back to single mode

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
api_instance = dataplaneapi.ClusterApi(dataplaneapi.ApiClient(configuration))
configuration = 'configuration_example' # str | In case of moving to single mode do we keep or clean configuration (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)

try:
    # Delete cluster settings
    api_instance.delete_cluster(configuration=configuration, version=version)
except ApiException as e:
    print("Exception when calling ClusterApi->delete_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration** | **str**| In case of moving to single mode do we keep or clean configuration | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_cluster**
> ClusterSettings edit_cluster(body, version=version)

Edit cluster settings

Edit cluster settings

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
api_instance = dataplaneapi.ClusterApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.ClusterSettings() # ClusterSettings | 
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)

try:
    # Edit cluster settings
    api_response = api_instance.edit_cluster(body, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->edit_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterSettings**](ClusterSettings.md)|  | 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 

### Return type

[**ClusterSettings**](ClusterSettings.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster**
> ClusterSettings get_cluster()

Return cluster data

Returns cluster data

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
api_instance = dataplaneapi.ClusterApi(dataplaneapi.ApiClient(configuration))

try:
    # Return cluster data
    api_response = api_instance.get_cluster()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterSettings**](ClusterSettings.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_certificate_refresh**
> initiate_certificate_refresh()

Initiates a certificate refresh

Initiates a certificate refresh

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
api_instance = dataplaneapi.ClusterApi(dataplaneapi.ApiClient(configuration))

try:
    # Initiates a certificate refresh
    api_instance.initiate_certificate_refresh()
except ApiException as e:
    print("Exception when calling ClusterApi->initiate_certificate_refresh: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cluster**
> ClusterSettings post_cluster(body, configuration=configuration, advertised_address=advertised_address, advertised_port=advertised_port, version=version)

Post cluster settings

Post cluster settings

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
api_instance = dataplaneapi.ClusterApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.ClusterSettings() # ClusterSettings | 
configuration = 'configuration_example' # str | In case of moving to single mode do we keep or clean configuration (optional)
advertised_address = 'advertised_address_example' # str | Force the advertised address when joining a cluster (optional)
advertised_port = 56 # int | Force the advertised port when joining a cluster (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)

try:
    # Post cluster settings
    api_response = api_instance.post_cluster(body, configuration=configuration, advertised_address=advertised_address, advertised_port=advertised_port, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->post_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterSettings**](ClusterSettings.md)|  | 
 **configuration** | **str**| In case of moving to single mode do we keep or clean configuration | [optional] 
 **advertised_address** | **str**| Force the advertised address when joining a cluster | [optional] 
 **advertised_port** | **int**| Force the advertised port when joining a cluster | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 

### Return type

[**ClusterSettings**](ClusterSettings.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

