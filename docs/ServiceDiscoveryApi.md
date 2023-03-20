# swagger_client.ServiceDiscoveryApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_aws_region**](ServiceDiscoveryApi.md#create_aws_region) | **POST** /service_discovery/aws | Add a new AWS region
[**create_consul**](ServiceDiscoveryApi.md#create_consul) | **POST** /service_discovery/consul | Add a new Consul server
[**delete_aws_region**](ServiceDiscoveryApi.md#delete_aws_region) | **DELETE** /service_discovery/aws/{id} | Delete an AWS region
[**delete_consul**](ServiceDiscoveryApi.md#delete_consul) | **DELETE** /service_discovery/consul/{id} | Delete a Consul server
[**get_aws_region**](ServiceDiscoveryApi.md#get_aws_region) | **GET** /service_discovery/aws/{id} | Return an AWS region
[**get_aws_regions**](ServiceDiscoveryApi.md#get_aws_regions) | **GET** /service_discovery/aws | Return an array of all configured AWS regions
[**get_consul**](ServiceDiscoveryApi.md#get_consul) | **GET** /service_discovery/consul/{id} | Return one Consul server
[**get_consuls**](ServiceDiscoveryApi.md#get_consuls) | **GET** /service_discovery/consul | Return an array of all configured Consul servers
[**replace_aws_region**](ServiceDiscoveryApi.md#replace_aws_region) | **PUT** /service_discovery/aws/{id} | Replace an AWS region
[**replace_consul**](ServiceDiscoveryApi.md#replace_consul) | **PUT** /service_discovery/consul/{id} | Replace a Consul server

# **create_aws_region**
> AwsRegion create_aws_region(body)

Add a new AWS region

Add a new AWS region. Credentials are not required in case Dataplane API is running in an EC2 instance with proper IAM role attached.

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
api_instance = dataplaneapi.ServiceDiscoveryApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.AwsRegion() # AwsRegion | 

try:
    # Add a new AWS region
    api_response = api_instance.create_aws_region(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceDiscoveryApi->create_aws_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AwsRegion**](AwsRegion.md)|  | 

### Return type

[**AwsRegion**](AwsRegion.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_consul**
> Consul create_consul(body)

Add a new Consul server

Adds a new Consul server.

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
api_instance = dataplaneapi.ServiceDiscoveryApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.Consul() # Consul | 

try:
    # Add a new Consul server
    api_response = api_instance.create_consul(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceDiscoveryApi->create_consul: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Consul**](Consul.md)|  | 

### Return type

[**Consul**](Consul.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_aws_region**
> delete_aws_region(id)

Delete an AWS region

Delete an AWS region configuration by it's id.

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
api_instance = dataplaneapi.ServiceDiscoveryApi(dataplaneapi.ApiClient(configuration))
id = 'id_example' # str | AWS region ID

try:
    # Delete an AWS region
    api_instance.delete_aws_region(id)
except ApiException as e:
    print("Exception when calling ServiceDiscoveryApi->delete_aws_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| AWS region ID | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_consul**
> delete_consul(id)

Delete a Consul server

Deletes a Consul server configuration by it's id.

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
api_instance = dataplaneapi.ServiceDiscoveryApi(dataplaneapi.ApiClient(configuration))
id = 'id_example' # str | Consul server Index

try:
    # Delete a Consul server
    api_instance.delete_consul(id)
except ApiException as e:
    print("Exception when calling ServiceDiscoveryApi->delete_consul: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Consul server Index | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_region**
> InlineResponse2001 get_aws_region(id)

Return an AWS region

Return one AWS Region configuration by it's id.

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
api_instance = dataplaneapi.ServiceDiscoveryApi(dataplaneapi.ApiClient(configuration))
id = 'id_example' # str | AWS region id

try:
    # Return an AWS region
    api_response = api_instance.get_aws_region(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceDiscoveryApi->get_aws_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| AWS region id | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_regions**
> InlineResponse200 get_aws_regions()

Return an array of all configured AWS regions

Return all configured AWS regions.

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
api_instance = dataplaneapi.ServiceDiscoveryApi(dataplaneapi.ApiClient(configuration))

try:
    # Return an array of all configured AWS regions
    api_response = api_instance.get_aws_regions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceDiscoveryApi->get_aws_regions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consul**
> InlineResponse2003 get_consul(id)

Return one Consul server

Returns one Consul server configuration by it's id.

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
api_instance = dataplaneapi.ServiceDiscoveryApi(dataplaneapi.ApiClient(configuration))
id = 'id_example' # str | Consul server id

try:
    # Return one Consul server
    api_response = api_instance.get_consul(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceDiscoveryApi->get_consul: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Consul server id | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consuls**
> InlineResponse2002 get_consuls()

Return an array of all configured Consul servers

Returns all configured Consul servers.

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
api_instance = dataplaneapi.ServiceDiscoveryApi(dataplaneapi.ApiClient(configuration))

try:
    # Return an array of all configured Consul servers
    api_response = api_instance.get_consuls()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceDiscoveryApi->get_consuls: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_aws_region**
> AwsRegion replace_aws_region(body, id)

Replace an AWS region

Replace an AWS region configuration by its id.

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
api_instance = dataplaneapi.ServiceDiscoveryApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.AwsRegion() # AwsRegion | 
id = 'id_example' # str | AWS Region ID

try:
    # Replace an AWS region
    api_response = api_instance.replace_aws_region(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceDiscoveryApi->replace_aws_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AwsRegion**](AwsRegion.md)|  | 
 **id** | **str**| AWS Region ID | 

### Return type

[**AwsRegion**](AwsRegion.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_consul**
> Consul replace_consul(body, id)

Replace a Consul server

Replaces a Consul server configuration by it's id.

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
api_instance = dataplaneapi.ServiceDiscoveryApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.Consul() # Consul | 
id = 'id_example' # str | Consul Index

try:
    # Replace a Consul server
    api_response = api_instance.replace_consul(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceDiscoveryApi->replace_consul: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Consul**](Consul.md)|  | 
 **id** | **str**| Consul Index | 

### Return type

[**Consul**](Consul.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

