# swagger_client.MailerEntryApi

All URIs are relative to *http://0.0.0.0/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mailer_entry**](MailerEntryApi.md#create_mailer_entry) | **POST** /services/haproxy/configuration/mailer_entries | Add a new mailer_entry
[**delete_mailer_entry**](MailerEntryApi.md#delete_mailer_entry) | **DELETE** /services/haproxy/configuration/mailer_entries/{name} | Delete a mailer_entry
[**get_mailer_entries**](MailerEntryApi.md#get_mailer_entries) | **GET** /services/haproxy/configuration/mailer_entries | Return an array of mailer_entries
[**get_mailer_entry**](MailerEntryApi.md#get_mailer_entry) | **GET** /services/haproxy/configuration/mailer_entries/{name} | Return one mailer_entry
[**replace_mailer_entry**](MailerEntryApi.md#replace_mailer_entry) | **PUT** /services/haproxy/configuration/mailer_entries/{name} | Replace a mailer_entry

# **create_mailer_entry**
> MailerEntry create_mailer_entry(body, mailers_section, transaction_id=transaction_id, version=version, force_reload=force_reload)

Add a new mailer_entry

Adds a new mailer entry to the specified mailers section in the configuration file.

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
api_instance = dataplaneapi.MailerEntryApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.MailerEntry() # MailerEntry | 
mailers_section = 'mailers_section_example' # str | Parent mailers section name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Add a new mailer_entry
    api_response = api_instance.create_mailer_entry(body, mailers_section, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailerEntryApi->create_mailer_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MailerEntry**](MailerEntry.md)|  | 
 **mailers_section** | **str**| Parent mailers section name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**MailerEntry**](MailerEntry.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mailer_entry**
> delete_mailer_entry(name, mailers_section, transaction_id=transaction_id, version=version, force_reload=force_reload)

Delete a mailer_entry

Deletes a mailer entry configuration by it's name in the specified mailers section.

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
api_instance = dataplaneapi.MailerEntryApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | MailerEntry name
mailers_section = 'mailers_section_example' # str | Parent mailers section name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Delete a mailer_entry
    api_instance.delete_mailer_entry(name, mailers_section, transaction_id=transaction_id, version=version, force_reload=force_reload)
except ApiException as e:
    print("Exception when calling MailerEntryApi->delete_mailer_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| MailerEntry name | 
 **mailers_section** | **str**| Parent mailers section name | 
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

# **get_mailer_entries**
> InlineResponse20044 get_mailer_entries(mailers_section, transaction_id=transaction_id)

Return an array of mailer_entries

Returns an array of all the mailer_entries configured in the specified mailers section.

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
api_instance = dataplaneapi.MailerEntryApi(dataplaneapi.ApiClient(configuration))
mailers_section = 'mailers_section_example' # str | Parent mailers section name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return an array of mailer_entries
    api_response = api_instance.get_mailer_entries(mailers_section, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailerEntryApi->get_mailer_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailers_section** | **str**| Parent mailers section name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mailer_entry**
> InlineResponse20045 get_mailer_entry(name, mailers_section, transaction_id=transaction_id)

Return one mailer_entry

Returns one mailer_entry configuration by it's name in the specified mailers section.

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
api_instance = dataplaneapi.MailerEntryApi(dataplaneapi.ApiClient(configuration))
name = 'name_example' # str | MailerEntry name
mailers_section = 'mailers_section_example' # str | Parent mailers name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)

try:
    # Return one mailer_entry
    api_response = api_instance.get_mailer_entry(name, mailers_section, transaction_id=transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailerEntryApi->get_mailer_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| MailerEntry name | 
 **mailers_section** | **str**| Parent mailers name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_mailer_entry**
> MailerEntry replace_mailer_entry(body, mailers_section, name, transaction_id=transaction_id, version=version, force_reload=force_reload)

Replace a mailer_entry

Replaces a mailer entry configuration by it's name in the specified mailers section.

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
api_instance = dataplaneapi.MailerEntryApi(dataplaneapi.ApiClient(configuration))
body = dataplaneapi.MailerEntry() # MailerEntry | 
mailers_section = 'mailers_section_example' # str | Parent mailers section name
name = 'name_example' # str | MailerEntry name
transaction_id = 'transaction_id_example' # str | ID of the transaction where we want to add the operation. Cannot be used when version is specified. (optional)
version = 56 # int | Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it's own version. (optional)
force_reload = false # bool | If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. (optional) (default to false)

try:
    # Replace a mailer_entry
    api_response = api_instance.replace_mailer_entry(body, mailers_section, name, transaction_id=transaction_id, version=version, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailerEntryApi->replace_mailer_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MailerEntry**](MailerEntry.md)|  | 
 **mailers_section** | **str**| Parent mailers section name | 
 **name** | **str**| MailerEntry name | 
 **transaction_id** | **str**| ID of the transaction where we want to add the operation. Cannot be used when version is specified. | [optional] 
 **version** | **int**| Version used for checking configuration version. Cannot be used when transaction is specified, transaction has it&#x27;s own version. | [optional] 
 **force_reload** | **bool**| If set, do a force reload, do not wait for the configured reload-delay. Cannot be used when transaction is specified, as changes in transaction are not applied directly to configuration. | [optional] [default to false]

### Return type

[**MailerEntry**](MailerEntry.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

