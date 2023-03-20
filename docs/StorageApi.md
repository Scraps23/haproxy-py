# swagger_client.StorageApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_storage_general_file**](StorageApi.md#create_storage_general_file) | **POST** /services/haproxy/storage/general | Creates a managed storage general use file with contents
[**create_storage_map_file**](StorageApi.md#create_storage_map_file) | **POST** /services/haproxy/storage/maps | Creates a managed storage map file with its entries
[**create_storage_ssl_certificate**](StorageApi.md#create_storage_ssl_certificate) | **POST** /services/haproxy/storage/ssl_certificates | Create SSL certificate
[**delete_storage_general_file**](StorageApi.md#delete_storage_general_file) | **DELETE** /services/haproxy/storage/general/{name} | Deletes a managed general use file from disk
[**delete_storage_map**](StorageApi.md#delete_storage_map) | **DELETE** /services/haproxy/storage/maps/{name} | Deletes a managed map file from disk
[**delete_storage_ssl_certificate**](StorageApi.md#delete_storage_ssl_certificate) | **DELETE** /services/haproxy/storage/ssl_certificates/{name} | Delete SSL certificate from disk
[**get_all_storage_general_files**](StorageApi.md#get_all_storage_general_files) | **GET** /services/haproxy/storage/general | Return a list of all managed general use files
[**get_all_storage_map_files**](StorageApi.md#get_all_storage_map_files) | **GET** /services/haproxy/storage/maps | Return a list of all managed map files
[**get_all_storage_ssl_certificates**](StorageApi.md#get_all_storage_ssl_certificates) | **GET** /services/haproxy/storage/ssl_certificates | Return all available SSL certificates on disk
[**get_one_storage_general_file**](StorageApi.md#get_one_storage_general_file) | **GET** /services/haproxy/storage/general/{name} | Return the contents of one managed general use file from disk
[**get_one_storage_map**](StorageApi.md#get_one_storage_map) | **GET** /services/haproxy/storage/maps/{name} | Return the contents of one managed map file from disk
[**get_one_storage_ssl_certificate**](StorageApi.md#get_one_storage_ssl_certificate) | **GET** /services/haproxy/storage/ssl_certificates/{name} | Return one SSL certificate from disk
[**replace_storage_general_file**](StorageApi.md#replace_storage_general_file) | **PUT** /services/haproxy/storage/general/{name} | Replace contents of a managed general use file on disk
[**replace_storage_map_file**](StorageApi.md#replace_storage_map_file) | **PUT** /services/haproxy/storage/maps/{name} | Replace contents of a managed map file on disk
[**replace_storage_ssl_certificate**](StorageApi.md#replace_storage_ssl_certificate) | **PUT** /services/haproxy/storage/ssl_certificates/{name} | Replace SSL certificates on disk

# **create_storage_general_file**
> GeneralFile create_storage_general_file(file_upload=file_upload)

Creates a managed storage general use file with contents

Creates a managed storage general use file with contents.

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
api_instance = dataplaneapi.StorageApi(dataplaneapi.ApiClient(configuration))
file_upload = 'file_upload_example' # str |  (optional)

try:
    # Creates a managed storage general use file with contents
    api_response = api_instance.create_storage_general_file(file_upload=file_upload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->create_storage_general_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_upload** | **str**|  | [optional] 

### Return type

[**GeneralFile**](GeneralFile.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_storage_map_file**
> dict create_storage_map_file(file_upload=file_upload)

Creates a managed storage map file with its entries

Creates a managed storage map file with its entries.

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
api_instance = dataplaneapi.StorageApi(dataplaneapi.ApiClient(configuration))
file_upload = 'file_upload_example' # str |  (optional)

try:
    # Creates a managed storage map file with its entries
    api_response = api_instance.create_storage_map_file(file_upload=file_upload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->create_storage_map_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_upload** | **str**|  | [optional] 

### Return type

**dict**

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_storage_ssl_certificate**
> SslCertificate create_storage_ssl_certificate(file_upload=file_upload, force_reload=force_reload)

Create SSL certificate

Creates SSL certificate.

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
api_instance = dataplaneapi.StorageApi(dataplaneapi.ApiClient(configuration))
file_upload = 'file_upload_example' # str |  (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Create SSL certificate
    api_response = api_instance.create_storage_ssl_certificate(file_upload=file_upload, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->create_storage_ssl_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_upload** | **str**|  | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**SslCertificate**](SslCertificate.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_storage_general_file**
> delete_storage_general_file(name)

Deletes a managed general use file from disk

Deletes a managed general use file from disk.

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
api_instance = dataplaneapi.StorageApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | General use file storage_name

try:
    # Deletes a managed general use file from disk
    api_instance.delete_storage_general_file(name)
except ApiException as e:
    print("Exception when calling StorageApi->delete_storage_general_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| General use file storage_name | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_storage_map**
> delete_storage_map(name)

Deletes a managed map file from disk

Deletes a managed map file from disk.

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
api_instance = dataplaneapi.StorageApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | Map file storage_name

try:
    # Deletes a managed map file from disk
    api_instance.delete_storage_map(name)
except ApiException as e:
    print("Exception when calling StorageApi->delete_storage_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Map file storage_name | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_storage_ssl_certificate**
> delete_storage_ssl_certificate(name, skip_reload=skip_reload, force_reload=force_reload)

Delete SSL certificate from disk

Deletes SSL certificate from disk.

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
api_instance = dataplaneapi.StorageApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | SSL certificate name
skip_reload = false # bool | If set, no reload will be initiated after update (optional) (default to false)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Delete SSL certificate from disk
    api_instance.delete_storage_ssl_certificate(name, skip_reload=skip_reload, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling StorageApi->delete_storage_ssl_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| SSL certificate name | 
 **skip_reload** | **bool**| If set, no reload will be initiated after update | [optional] [default to false]
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_storage_general_files**
> GeneralFiles get_all_storage_general_files()

Return a list of all managed general use files

Returns a list of all managed general use files

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
api_instance = dataplaneapi.StorageApi(dataplaneapi.ApiClient(configuration))

try:
    # Return a list of all managed general use files
    api_response = api_instance.get_all_storage_general_files()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->get_all_storage_general_files: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GeneralFiles**](GeneralFiles.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_storage_map_files**
> Maps get_all_storage_map_files()

Return a list of all managed map files

Returns a list of all managed map files

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
api_instance = dataplaneapi.StorageApi(dataplaneapi.ApiClient(configuration))

try:
    # Return a list of all managed map files
    api_response = api_instance.get_all_storage_map_files()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->get_all_storage_map_files: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Maps**](Maps.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_storage_ssl_certificates**
> SslCertificates get_all_storage_ssl_certificates()

Return all available SSL certificates on disk

Returns all available SSL certificates on disk.

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
api_instance = dataplaneapi.StorageApi(dataplaneapi.ApiClient(configuration))

try:
    # Return all available SSL certificates on disk
    api_response = api_instance.get_all_storage_ssl_certificates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->get_all_storage_ssl_certificates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SslCertificates**](SslCertificates.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_storage_general_file**
> str get_one_storage_general_file(name)

Return the contents of one managed general use file from disk

Returns the contents of one managed general use file from disk

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
api_instance = dataplaneapi.StorageApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | General use file storage_name

try:
    # Return the contents of one managed general use file from disk
    api_response = api_instance.get_one_storage_general_file(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->get_one_storage_general_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| General use file storage_name | 

### Return type

**str**

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_storage_map**
> str get_one_storage_map(name)

Return the contents of one managed map file from disk

Returns the contents of one managed map file from disk

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
api_instance = dataplaneapi.StorageApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | Map file storage_name

try:
    # Return the contents of one managed map file from disk
    api_response = api_instance.get_one_storage_map(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->get_one_storage_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Map file storage_name | 

### Return type

**str**

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_storage_ssl_certificate**
> SslCertificate get_one_storage_ssl_certificate(name)

Return one SSL certificate from disk

Returns one SSL certificate from disk.

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
api_instance = dataplaneapi.StorageApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | SSL certificate name

try:
    # Return one SSL certificate from disk
    api_response = api_instance.get_one_storage_ssl_certificate(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->get_one_storage_ssl_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| SSL certificate name | 

### Return type

[**SslCertificate**](SslCertificate.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_storage_general_file**
> replace_storage_general_file(body, name, skip_reload=skip_reload, force_reload=force_reload)

Replace contents of a managed general use file on disk

Replaces the contents of a managed general use file on disk

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
api_instance = dataplaneapi.StorageApi(dataplaneapi.ApiClient(configuration))
body = 'body_example' # str | 
name = 'name_example' # str | General use file storage_name
skip_reload = false # bool | If set, no reload will be initiated after update (optional) (default to false)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace contents of a managed general use file on disk
    api_instance.replace_storage_general_file(body, name, skip_reload=skip_reload, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling StorageApi->replace_storage_general_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **name** | **str**| General use file storage_name | 
 **skip_reload** | **bool**| If set, no reload will be initiated after update | [optional] [default to false]
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_storage_map_file**
> replace_storage_map_file(body, name, skip_reload=skip_reload, force_reload=force_reload)

Replace contents of a managed map file on disk

Replaces the contents of a managed map file on disk

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
api_instance = dataplaneapi.StorageApi(dataplaneapi.ApiClient(configuration))
body = 'body_example' # str | 
name = 'name_example' # str | Map file storage_name
skip_reload = false # bool | If set, no reload will be initiated after update (optional) (default to false)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace contents of a managed map file on disk
    api_instance.replace_storage_map_file(body, name, skip_reload=skip_reload, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling StorageApi->replace_storage_map_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **name** | **str**| Map file storage_name | 
 **skip_reload** | **bool**| If set, no reload will be initiated after update | [optional] [default to false]
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_storage_ssl_certificate**
> SslCertificate replace_storage_ssl_certificate(body, name, skip_reload=skip_reload, force_reload=force_reload)

Replace SSL certificates on disk

Replaces SSL certificate on disk.

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
api_instance = dataplaneapi.StorageApi(dataplaneapi.ApiClient(configuration))
body = 'body_example' # str | 
name = 'name_example' # str | SSL certificate name
skip_reload = false # bool | If set, no reload will be initiated after update (optional) (default to false)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace SSL certificates on disk
    api_response = api_instance.replace_storage_ssl_certificate(body, name, skip_reload=skip_reload, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->replace_storage_ssl_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **name** | **str**| SSL certificate name | 
 **skip_reload** | **bool**| If set, no reload will be initiated after update | [optional] [default to false]
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**SslCertificate**](SslCertificate.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

