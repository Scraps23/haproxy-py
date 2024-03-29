All URIs are relative to *http://0.0.0.0/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ACLApi* | [**create_acl**](../docs/ACLApi.md#create_acl) | **POST** /services/haproxy/configuration/acls | Add a new ACL line
*ACLApi* | [**delete_acl**](../docs/ACLApi.md#delete_acl) | **DELETE** /services/haproxy/configuration/acls/{index} | Delete a ACL line
*ACLApi* | [**get_acl**](../docs/ACLApi.md#get_acl) | **GET** /services/haproxy/configuration/acls/{index} | Return one ACL line
*ACLApi* | [**get_acls**](../docs/ACLApi.md#get_acls) | **GET** /services/haproxy/configuration/acls | Return an array of all ACL lines
*ACLApi* | [**replace_acl**](../docs/ACLApi.md#replace_acl) | **PUT** /services/haproxy/configuration/acls/{index} | Replace a ACL line
*ACLRuntimeApi* | [**add_payload_runtime_acl**](../docs/ACLRuntimeApi.md#add_payload_runtime_acl) | **PUT** /services/haproxy/runtime/acl_file_entries | Add a new ACL payload
*ACLRuntimeApi* | [**services_haproxy_runtime_acl_file_entries_get**](../docs/ACLRuntimeApi.md#services_haproxy_runtime_acl_file_entries_get) | **GET** /services/haproxy/runtime/acl_file_entries | Return an ACL entries
*ACLRuntimeApi* | [**services_haproxy_runtime_acl_file_entries_id_delete**](../docs/ACLRuntimeApi.md#services_haproxy_runtime_acl_file_entries_id_delete) | **DELETE** /services/haproxy/runtime/acl_file_entries/{id} | Delete an ACL entry
*ACLRuntimeApi* | [**services_haproxy_runtime_acl_file_entries_id_get**](../docs/ACLRuntimeApi.md#services_haproxy_runtime_acl_file_entries_id_get) | **GET** /services/haproxy/runtime/acl_file_entries/{id} | Return an ACL entry
*ACLRuntimeApi* | [**services_haproxy_runtime_acl_file_entries_post**](../docs/ACLRuntimeApi.md#services_haproxy_runtime_acl_file_entries_post) | **POST** /services/haproxy/runtime/acl_file_entries | Add entry to an ACL file
*ACLRuntimeApi* | [**services_haproxy_runtime_acls_get**](../docs/ACLRuntimeApi.md#services_haproxy_runtime_acls_get) | **GET** /services/haproxy/runtime/acls | Return an array of all ACL files
*ACLRuntimeApi* | [**services_haproxy_runtime_acls_id_get**](../docs/ACLRuntimeApi.md#services_haproxy_runtime_acls_id_get) | **GET** /services/haproxy/runtime/acls/{id} | Return an ACL file
*BackendApi* | [**create_backend**](../docs/BackendApi.md#create_backend) | **POST** /services/haproxy/configuration/backends | Add a backend
*BackendApi* | [**delete_backend**](../docs/BackendApi.md#delete_backend) | **DELETE** /services/haproxy/configuration/backends/{name} | Delete a backend
*BackendApi* | [**get_backend**](../docs/BackendApi.md#get_backend) | **GET** /services/haproxy/configuration/backends/{name} | Return a backend
*BackendApi* | [**get_backends**](../docs/BackendApi.md#get_backends) | **GET** /services/haproxy/configuration/backends | Return an array of backends
*BackendApi* | [**replace_backend**](../docs/BackendApi.md#replace_backend) | **PUT** /services/haproxy/configuration/backends/{name} | Replace a backend
*BackendSwitchingRuleApi* | [**create_backend_switching_rule**](../docs/BackendSwitchingRuleApi.md#create_backend_switching_rule) | **POST** /services/haproxy/configuration/backend_switching_rules | Add a new Backend Switching Rule
*BackendSwitchingRuleApi* | [**delete_backend_switching_rule**](../docs/BackendSwitchingRuleApi.md#delete_backend_switching_rule) | **DELETE** /services/haproxy/configuration/backend_switching_rules/{index} | Delete a Backend Switching Rule
*BackendSwitchingRuleApi* | [**get_backend_switching_rule**](../docs/BackendSwitchingRuleApi.md#get_backend_switching_rule) | **GET** /services/haproxy/configuration/backend_switching_rules/{index} | Return one Backend Switching Rule
*BackendSwitchingRuleApi* | [**get_backend_switching_rules**](../docs/BackendSwitchingRuleApi.md#get_backend_switching_rules) | **GET** /services/haproxy/configuration/backend_switching_rules | Return an array of all Backend Switching Rules
*BackendSwitchingRuleApi* | [**replace_backend_switching_rule**](../docs/BackendSwitchingRuleApi.md#replace_backend_switching_rule) | **PUT** /services/haproxy/configuration/backend_switching_rules/{index} | Replace a Backend Switching Rule
*BindApi* | [**create_bind**](../docs/BindApi.md#create_bind) | **POST** /services/haproxy/configuration/binds | Add a new bind
*BindApi* | [**delete_bind**](../docs/BindApi.md#delete_bind) | **DELETE** /services/haproxy/configuration/binds/{name} | Delete a bind
*BindApi* | [**get_bind**](../docs/BindApi.md#get_bind) | **GET** /services/haproxy/configuration/binds/{name} | Return one bind
*BindApi* | [**get_binds**](../docs/BindApi.md#get_binds) | **GET** /services/haproxy/configuration/binds | Return an array of binds
*BindApi* | [**replace_bind**](../docs/BindApi.md#replace_bind) | **PUT** /services/haproxy/configuration/binds/{name} | Replace a bind
*CacheApi* | [**create_cache**](../docs/CacheApi.md#create_cache) | **POST** /services/haproxy/configuration/caches | Add a cache
*CacheApi* | [**delete_cache**](../docs/CacheApi.md#delete_cache) | **DELETE** /services/haproxy/configuration/caches/{name} | Delete a cache
*CacheApi* | [**get_cache**](../docs/CacheApi.md#get_cache) | **GET** /services/haproxy/configuration/caches/{name} | Return a cache
*CacheApi* | [**get_caches**](../docs/CacheApi.md#get_caches) | **GET** /services/haproxy/configuration/caches | Return an array of caches
*CacheApi* | [**replace_cache**](../docs/CacheApi.md#replace_cache) | **PUT** /services/haproxy/configuration/caches/{name} | Replace a cache
*ClusterApi* | [**delete_cluster**](../docs/ClusterApi.md#delete_cluster) | **DELETE** /cluster | Delete cluster settings
*ClusterApi* | [**edit_cluster**](../docs/ClusterApi.md#edit_cluster) | **PUT** /cluster | Edit cluster settings
*ClusterApi* | [**get_cluster**](../docs/ClusterApi.md#get_cluster) | **GET** /cluster | Return cluster data
*ClusterApi* | [**initiate_certificate_refresh**](../docs/ClusterApi.md#initiate_certificate_refresh) | **POST** /cluster/certificate | Initiates a certificate refresh
*ClusterApi* | [**post_cluster**](../docs/ClusterApi.md#post_cluster) | **POST** /cluster | Post cluster settings
*ConfigurationApi* | [**get_configuration_version**](../docs/ConfigurationApi.md#get_configuration_version) | **GET** /services/haproxy/configuration/version | Return a configuration version
*ConfigurationApi* | [**get_ha_proxy_configuration**](../docs/ConfigurationApi.md#get_ha_proxy_configuration) | **GET** /services/haproxy/configuration/raw | Return HAProxy configuration
*ConfigurationApi* | [**post_ha_proxy_configuration**](../docs/ConfigurationApi.md#post_ha_proxy_configuration) | **POST** /services/haproxy/configuration/raw | Push new haproxy configuration
*DeclareCaptureApi* | [**create_declare_capture**](../docs/DeclareCaptureApi.md#create_declare_capture) | **POST** /services/haproxy/configuration/captures | Add a new declare capture
*DeclareCaptureApi* | [**delete_declare_capture**](../docs/DeclareCaptureApi.md#delete_declare_capture) | **DELETE** /services/haproxy/configuration/captures/{index} | Delete a declare capture
*DeclareCaptureApi* | [**get_declare_capture**](../docs/DeclareCaptureApi.md#get_declare_capture) | **GET** /services/haproxy/configuration/captures/{index} | Return one declare capture
*DeclareCaptureApi* | [**get_declare_captures**](../docs/DeclareCaptureApi.md#get_declare_captures) | **GET** /services/haproxy/configuration/captures | Return an array of declare captures
*DeclareCaptureApi* | [**replace_declare_capture**](../docs/DeclareCaptureApi.md#replace_declare_capture) | **PUT** /services/haproxy/configuration/captures/{index} | Replace a declare capture
*DefaultsApi* | [**create_defaults_section**](../docs/DefaultsApi.md#create_defaults_section) | **POST** /services/haproxy/configuration/named_defaults | Add a defaults section
*DefaultsApi* | [**delete_defaults_section**](../docs/DefaultsApi.md#delete_defaults_section) | **DELETE** /services/haproxy/configuration/named_defaults/{name} | Delete a defaults section
*DefaultsApi* | [**get_defaults**](../docs/DefaultsApi.md#get_defaults) | **GET** /services/haproxy/configuration/defaults | Return defaults part of configuration
*DefaultsApi* | [**get_defaults_section**](../docs/DefaultsApi.md#get_defaults_section) | **GET** /services/haproxy/configuration/named_defaults/{name} | Return a defautls section
*DefaultsApi* | [**get_defaults_sections**](../docs/DefaultsApi.md#get_defaults_sections) | **GET** /services/haproxy/configuration/named_defaults | Return an array of defaults
*DefaultsApi* | [**replace_defaults**](../docs/DefaultsApi.md#replace_defaults) | **PUT** /services/haproxy/configuration/defaults | Replace defaults
*DefaultsApi* | [**replace_defaults_section**](../docs/DefaultsApi.md#replace_defaults_section) | **PUT** /services/haproxy/configuration/named_defaults/{name} | Replace a defatults section
*DgramBindApi* | [**create_dgram_bind**](../docs/DgramBindApi.md#create_dgram_bind) | **POST** /services/haproxy/configuration/dgram_binds | Add a new dgram bind
*DgramBindApi* | [**delete_dgram_bind**](../docs/DgramBindApi.md#delete_dgram_bind) | **DELETE** /services/haproxy/configuration/dgram_binds/{name} | Delete a dgram bind
*DgramBindApi* | [**get_dgram_bind**](../docs/DgramBindApi.md#get_dgram_bind) | **GET** /services/haproxy/configuration/dgram_binds/{name} | Return one dgram bind
*DgramBindApi* | [**get_dgram_binds**](../docs/DgramBindApi.md#get_dgram_binds) | **GET** /services/haproxy/configuration/dgram_binds | Return an array of dgram binds
*DgramBindApi* | [**replace_dgram_bind**](../docs/DgramBindApi.md#replace_dgram_bind) | **PUT** /services/haproxy/configuration/dgram_binds/{name} | Replace a dgram bind
*DiscoveryApi* | [**get_api_endpoints**](../docs/DiscoveryApi.md#get_api_endpoints) | **GET** / | Return list of root endpoints
*DiscoveryApi* | [**get_configuration_endpoints**](../docs/DiscoveryApi.md#get_configuration_endpoints) | **GET** /services/haproxy/configuration | Return list of HAProxy advanced configuration endpoints
*DiscoveryApi* | [**get_haproxy_endpoints**](../docs/DiscoveryApi.md#get_haproxy_endpoints) | **GET** /services/haproxy | Return list of HAProxy related endpoints
*DiscoveryApi* | [**get_runtime_endpoints**](../docs/DiscoveryApi.md#get_runtime_endpoints) | **GET** /services/haproxy/runtime | Return list of HAProxy advanced runtime endpoints
*DiscoveryApi* | [**get_services_endpoints**](../docs/DiscoveryApi.md#get_services_endpoints) | **GET** /services | Return list of service endpoints
*DiscoveryApi* | [**get_spoe_endpoints**](../docs/DiscoveryApi.md#get_spoe_endpoints) | **GET** /services/haproxy/spoe | Return list of HAProxy SPOE endpoints
*DiscoveryApi* | [**get_stats_endpoints**](../docs/DiscoveryApi.md#get_stats_endpoints) | **GET** /services/haproxy/stats | Return list of HAProxy stats endpoints
*DiscoveryApi* | [**get_storage_endpoints**](../docs/DiscoveryApi.md#get_storage_endpoints) | **GET** /services/haproxy/storage | Return list of HAProxy storage endpoints
*FCGIAppApi* | [**create_fcgi_app**](../docs/FCGIAppApi.md#create_fcgi_app) | **POST** /services/haproxy/configuration/fcgi_apps | Add an FCGI app
*FCGIAppApi* | [**delete_fcgi_app**](../docs/FCGIAppApi.md#delete_fcgi_app) | **DELETE** /services/haproxy/configuration/fcgi_apps/{name} | Delete an FCGI app
*FCGIAppApi* | [**get_fcgi_app**](../docs/FCGIAppApi.md#get_fcgi_app) | **GET** /services/haproxy/configuration/fcgi_apps/{name} | Return a FCGI app
*FCGIAppApi* | [**get_fcgi_apps**](../docs/FCGIAppApi.md#get_fcgi_apps) | **GET** /services/haproxy/configuration/fcgi_apps | Return an array of FCGI apps
*FCGIAppApi* | [**replace_fcgi_app**](../docs/FCGIAppApi.md#replace_fcgi_app) | **PUT** /services/haproxy/configuration/fcgi_apps/{name} | Replace a FCGI app
*FilterApi* | [**create_filter**](../docs/FilterApi.md#create_filter) | **POST** /services/haproxy/configuration/filters | Add a new Filter
*FilterApi* | [**delete_filter**](../docs/FilterApi.md#delete_filter) | **DELETE** /services/haproxy/configuration/filters/{index} | Delete a Filter
*FilterApi* | [**get_filter**](../docs/FilterApi.md#get_filter) | **GET** /services/haproxy/configuration/filters/{index} | Return one Filter
*FilterApi* | [**get_filters**](../docs/FilterApi.md#get_filters) | **GET** /services/haproxy/configuration/filters | Return an array of all Filters
*FilterApi* | [**replace_filter**](../docs/FilterApi.md#replace_filter) | **PUT** /services/haproxy/configuration/filters/{index} | Replace a Filter
*FrontendApi* | [**create_frontend**](../docs/FrontendApi.md#create_frontend) | **POST** /services/haproxy/configuration/frontends | Add a frontend
*FrontendApi* | [**delete_frontend**](../docs/FrontendApi.md#delete_frontend) | **DELETE** /services/haproxy/configuration/frontends/{name} | Delete a frontend
*FrontendApi* | [**get_frontend**](../docs/FrontendApi.md#get_frontend) | **GET** /services/haproxy/configuration/frontends/{name} | Return a frontend
*FrontendApi* | [**get_frontends**](../docs/FrontendApi.md#get_frontends) | **GET** /services/haproxy/configuration/frontends | Return an array of frontends
*FrontendApi* | [**replace_frontend**](../docs/FrontendApi.md#replace_frontend) | **PUT** /services/haproxy/configuration/frontends/{name} | Replace a frontend
*GlobalApi* | [**get_global**](../docs/GlobalApi.md#get_global) | **GET** /services/haproxy/configuration/global | Return a global part of configuration
*GlobalApi* | [**replace_global**](../docs/GlobalApi.md#replace_global) | **PUT** /services/haproxy/configuration/global | Replace global
*GroupApi* | [**create_group**](../docs/GroupApi.md#create_group) | **POST** /services/haproxy/configuration/groups | Add a new userlist group
*GroupApi* | [**delete_group**](../docs/GroupApi.md#delete_group) | **DELETE** /services/haproxy/configuration/groups/{name} | Delete a group
*GroupApi* | [**get_group**](../docs/GroupApi.md#get_group) | **GET** /services/haproxy/configuration/groups/{name} | Return one userlist group
*GroupApi* | [**get_groups**](../docs/GroupApi.md#get_groups) | **GET** /services/haproxy/configuration/groups | Return an array of userlist groups
*GroupApi* | [**replace_group**](../docs/GroupApi.md#replace_group) | **PUT** /services/haproxy/configuration/groups/{name} | Replace a group
*HTTPAfterResponseRuleApi* | [**create_http_after_response_rule**](../docs/HTTPAfterResponseRuleApi.md#create_http_after_response_rule) | **POST** /services/haproxy/configuration/http_after_response_rules | Add a new HTTP After Response Rule
*HTTPAfterResponseRuleApi* | [**delete_http_after_response_rule**](../docs/HTTPAfterResponseRuleApi.md#delete_http_after_response_rule) | **DELETE** /services/haproxy/configuration/http_after_response_rules/{index} | Delete a HTTP After Response Rule
*HTTPAfterResponseRuleApi* | [**get_http_after_response_rule**](../docs/HTTPAfterResponseRuleApi.md#get_http_after_response_rule) | **GET** /services/haproxy/configuration/http_after_response_rules/{index} | Return one HTTP After Response Rule
*HTTPAfterResponseRuleApi* | [**get_http_after_response_rules**](../docs/HTTPAfterResponseRuleApi.md#get_http_after_response_rules) | **GET** /services/haproxy/configuration/http_after_response_rules | Return an array of all HTTP After Response Rules
*HTTPAfterResponseRuleApi* | [**replace_http_after_response_rule**](../docs/HTTPAfterResponseRuleApi.md#replace_http_after_response_rule) | **PUT** /services/haproxy/configuration/http_after_response_rules/{index} | Replace a HTTP After Response Rule
*HTTPCheckApi* | [**create_http_check**](../docs/HTTPCheckApi.md#create_http_check) | **POST** /services/haproxy/configuration/http_checks | Add a new HTTP check
*HTTPCheckApi* | [**delete_http_check**](../docs/HTTPCheckApi.md#delete_http_check) | **DELETE** /services/haproxy/configuration/http_checks/{index} | Delete a HTTP check
*HTTPCheckApi* | [**get_http_check**](../docs/HTTPCheckApi.md#get_http_check) | **GET** /services/haproxy/configuration/http_checks/{index} | Return one HTTP check
*HTTPCheckApi* | [**get_http_checks**](../docs/HTTPCheckApi.md#get_http_checks) | **GET** /services/haproxy/configuration/http_checks | Return an array of HTTP checks
*HTTPCheckApi* | [**replace_http_check**](../docs/HTTPCheckApi.md#replace_http_check) | **PUT** /services/haproxy/configuration/http_checks/{index} | Replace a HTTP check
*HTTPErrorRuleApi* | [**create_http_error_rule**](../docs/HTTPErrorRuleApi.md#create_http_error_rule) | **POST** /services/haproxy/configuration/http_error_rules | Add a new HTTP Error Rule
*HTTPErrorRuleApi* | [**delete_http_error_rule**](../docs/HTTPErrorRuleApi.md#delete_http_error_rule) | **DELETE** /services/haproxy/configuration/http_error_rules/{index} | Delete a HTTP Error Rule
*HTTPErrorRuleApi* | [**get_http_error_rule**](../docs/HTTPErrorRuleApi.md#get_http_error_rule) | **GET** /services/haproxy/configuration/http_error_rules/{index} | Return one HTTP Error Rule
*HTTPErrorRuleApi* | [**get_http_error_rules**](../docs/HTTPErrorRuleApi.md#get_http_error_rules) | **GET** /services/haproxy/configuration/http_error_rules | Return an array of all HTTP Error Rules
*HTTPErrorRuleApi* | [**replace_http_error_rule**](../docs/HTTPErrorRuleApi.md#replace_http_error_rule) | **PUT** /services/haproxy/configuration/http_error_rules/{index} | Replace a HTTP Error Rule
*HTTPErrorsApi* | [**create_http_errors_section**](../docs/HTTPErrorsApi.md#create_http_errors_section) | **POST** /services/haproxy/configuration/http_errors_sections | Add a new http-error section
*HTTPErrorsApi* | [**delete_http_errors_section**](../docs/HTTPErrorsApi.md#delete_http_errors_section) | **DELETE** /services/haproxy/configuration/http_errors_sections/{name} | Delete a http-error section
*HTTPErrorsApi* | [**get_http_errors_section**](../docs/HTTPErrorsApi.md#get_http_errors_section) | **GET** /services/haproxy/configuration/http_errors_sections/{name} | Return a http-error section
*HTTPErrorsApi* | [**get_http_errors_sections**](../docs/HTTPErrorsApi.md#get_http_errors_sections) | **GET** /services/haproxy/configuration/http_errors_sections | Return an array of http-error sections
*HTTPErrorsApi* | [**replace_http_errors_section**](../docs/HTTPErrorsApi.md#replace_http_errors_section) | **PUT** /services/haproxy/configuration/http_errors_sections/{name} | Replace a http-error section
*HTTPRequestRuleApi* | [**create_http_request_rule**](../docs/HTTPRequestRuleApi.md#create_http_request_rule) | **POST** /services/haproxy/configuration/http_request_rules | Add a new HTTP Request Rule
*HTTPRequestRuleApi* | [**delete_http_request_rule**](../docs/HTTPRequestRuleApi.md#delete_http_request_rule) | **DELETE** /services/haproxy/configuration/http_request_rules/{index} | Delete a HTTP Request Rule
*HTTPRequestRuleApi* | [**get_http_request_rule**](../docs/HTTPRequestRuleApi.md#get_http_request_rule) | **GET** /services/haproxy/configuration/http_request_rules/{index} | Return one HTTP Request Rule
*HTTPRequestRuleApi* | [**get_http_request_rules**](../docs/HTTPRequestRuleApi.md#get_http_request_rules) | **GET** /services/haproxy/configuration/http_request_rules | Return an array of all HTTP Request Rules
*HTTPRequestRuleApi* | [**replace_http_request_rule**](../docs/HTTPRequestRuleApi.md#replace_http_request_rule) | **PUT** /services/haproxy/configuration/http_request_rules/{index} | Replace a HTTP Request Rule
*HTTPResponseRuleApi* | [**create_http_response_rule**](../docs/HTTPResponseRuleApi.md#create_http_response_rule) | **POST** /services/haproxy/configuration/http_response_rules | Add a new HTTP Response Rule
*HTTPResponseRuleApi* | [**delete_http_response_rule**](../docs/HTTPResponseRuleApi.md#delete_http_response_rule) | **DELETE** /services/haproxy/configuration/http_response_rules/{index} | Delete a HTTP Response Rule
*HTTPResponseRuleApi* | [**get_http_response_rule**](../docs/HTTPResponseRuleApi.md#get_http_response_rule) | **GET** /services/haproxy/configuration/http_response_rules/{index} | Return one HTTP Response Rule
*HTTPResponseRuleApi* | [**get_http_response_rules**](../docs/HTTPResponseRuleApi.md#get_http_response_rules) | **GET** /services/haproxy/configuration/http_response_rules | Return an array of all HTTP Response Rules
*HTTPResponseRuleApi* | [**replace_http_response_rule**](../docs/HTTPResponseRuleApi.md#replace_http_response_rule) | **PUT** /services/haproxy/configuration/http_response_rules/{index} | Replace a HTTP Response Rule
*HealthApi* | [**get_health**](../docs/HealthApi.md#get_health) | **GET** /health | Return managed services health
*InformationApi* | [**get_haproxy_process_info**](../docs/InformationApi.md#get_haproxy_process_info) | **GET** /services/haproxy/runtime/info | Return HAProxy process information
*InformationApi* | [**get_info**](../docs/InformationApi.md#get_info) | **GET** /info | Return API, hardware and OS information
*LogForwardApi* | [**create_log_forward**](../docs/LogForwardApi.md#create_log_forward) | **POST** /services/haproxy/configuration/log_forwards | Add a log forward
*LogForwardApi* | [**delete_log_forward**](../docs/LogForwardApi.md#delete_log_forward) | **DELETE** /services/haproxy/configuration/log_forwards/{name} | Delete a log forward
*LogForwardApi* | [**get_log_forward**](../docs/LogForwardApi.md#get_log_forward) | **GET** /services/haproxy/configuration/log_forwards/{name} | Return a log forward
*LogForwardApi* | [**get_log_forwards**](../docs/LogForwardApi.md#get_log_forwards) | **GET** /services/haproxy/configuration/log_forwards | Return an array of log forwards
*LogForwardApi* | [**replace_log_forward**](../docs/LogForwardApi.md#replace_log_forward) | **PUT** /services/haproxy/configuration/log_forwards/{name} | Replace a log forward
*LogTargetApi* | [**create_log_target**](../docs/LogTargetApi.md#create_log_target) | **POST** /services/haproxy/configuration/log_targets | Add a new Log Target
*LogTargetApi* | [**delete_log_target**](../docs/LogTargetApi.md#delete_log_target) | **DELETE** /services/haproxy/configuration/log_targets/{index} | Delete a Log Target
*LogTargetApi* | [**get_log_target**](../docs/LogTargetApi.md#get_log_target) | **GET** /services/haproxy/configuration/log_targets/{index} | Return one Log Target
*LogTargetApi* | [**get_log_targets**](../docs/LogTargetApi.md#get_log_targets) | **GET** /services/haproxy/configuration/log_targets | Return an array of all Log Targets
*LogTargetApi* | [**replace_log_target**](../docs/LogTargetApi.md#replace_log_target) | **PUT** /services/haproxy/configuration/log_targets/{index} | Replace a Log Target
*MailerEntryApi* | [**create_mailer_entry**](../docs/MailerEntryApi.md#create_mailer_entry) | **POST** /services/haproxy/configuration/mailer_entries | Add a new mailer_entry
*MailerEntryApi* | [**delete_mailer_entry**](../docs/MailerEntryApi.md#delete_mailer_entry) | **DELETE** /services/haproxy/configuration/mailer_entries/{name} | Delete a mailer_entry
*MailerEntryApi* | [**get_mailer_entries**](../docs/MailerEntryApi.md#get_mailer_entries) | **GET** /services/haproxy/configuration/mailer_entries | Return an array of mailer_entries
*MailerEntryApi* | [**get_mailer_entry**](../docs/MailerEntryApi.md#get_mailer_entry) | **GET** /services/haproxy/configuration/mailer_entries/{name} | Return one mailer_entry
*MailerEntryApi* | [**replace_mailer_entry**](../docs/MailerEntryApi.md#replace_mailer_entry) | **PUT** /services/haproxy/configuration/mailer_entries/{name} | Replace a mailer_entry
*MailersApi* | [**create_mailers_section**](../docs/MailersApi.md#create_mailers_section) | **POST** /services/haproxy/configuration/mailers_section | Add a new Mailers section
*MailersApi* | [**delete_mailers_section**](../docs/MailersApi.md#delete_mailers_section) | **DELETE** /services/haproxy/configuration/mailers_section/{name} | Delete a Mailers section
*MailersApi* | [**edit_mailers_section**](../docs/MailersApi.md#edit_mailers_section) | **PUT** /services/haproxy/configuration/mailers_section/{name} | Modify a Mailers section
*MailersApi* | [**get_mailers_section**](../docs/MailersApi.md#get_mailers_section) | **GET** /services/haproxy/configuration/mailers_section/{name} | Return a Mailers section
*MailersApi* | [**get_mailers_sections**](../docs/MailersApi.md#get_mailers_sections) | **GET** /services/haproxy/configuration/mailers_section | Return an array of mailers sections
*MapsApi* | [**add_map_entry**](../docs/MapsApi.md#add_map_entry) | **POST** /services/haproxy/runtime/maps_entries | Adds an entry into the map file
*MapsApi* | [**add_payload_runtime_map**](../docs/MapsApi.md#add_payload_runtime_map) | **PUT** /services/haproxy/runtime/maps/{name} | Add a new map payload
*MapsApi* | [**clear_runtime_map**](../docs/MapsApi.md#clear_runtime_map) | **DELETE** /services/haproxy/runtime/maps/{name} | Remove all map entries from the map file
*MapsApi* | [**delete_runtime_map_entry**](../docs/MapsApi.md#delete_runtime_map_entry) | **DELETE** /services/haproxy/runtime/maps_entries/{id} | Deletes all the map entries from the map by its id
*MapsApi* | [**get_all_runtime_map_files**](../docs/MapsApi.md#get_all_runtime_map_files) | **GET** /services/haproxy/runtime/maps | Return runtime map files
*MapsApi* | [**get_one_runtime_map**](../docs/MapsApi.md#get_one_runtime_map) | **GET** /services/haproxy/runtime/maps/{name} | Return one runtime map file
*MapsApi* | [**get_runtime_map_entry**](../docs/MapsApi.md#get_runtime_map_entry) | **GET** /services/haproxy/runtime/maps_entries/{id} | Return one map runtime setting
*MapsApi* | [**replace_runtime_map_entry**](../docs/MapsApi.md#replace_runtime_map_entry) | **PUT** /services/haproxy/runtime/maps_entries/{id} | Replace the value corresponding to each id in a map
*MapsApi* | [**show_runtime_map**](../docs/MapsApi.md#show_runtime_map) | **GET** /services/haproxy/runtime/maps_entries | Return one map runtime entries
*NameserverApi* | [**create_nameserver**](../docs/NameserverApi.md#create_nameserver) | **POST** /services/haproxy/configuration/nameservers | Add a nameserver
*NameserverApi* | [**delete_nameserver**](../docs/NameserverApi.md#delete_nameserver) | **DELETE** /services/haproxy/configuration/nameservers/{name} | Delete a nameserver
*NameserverApi* | [**get_nameserver**](../docs/NameserverApi.md#get_nameserver) | **GET** /services/haproxy/configuration/nameservers/{name} | Return a nameserver
*NameserverApi* | [**get_nameservers**](../docs/NameserverApi.md#get_nameservers) | **GET** /services/haproxy/configuration/nameservers | Return an array of nameservers
*NameserverApi* | [**replace_nameserver**](../docs/NameserverApi.md#replace_nameserver) | **PUT** /services/haproxy/configuration/nameservers/{name} | Replace a nameserver
*PeerApi* | [**create_peer**](../docs/PeerApi.md#create_peer) | **POST** /services/haproxy/configuration/peer_section | Add a peer
*PeerApi* | [**delete_peer**](../docs/PeerApi.md#delete_peer) | **DELETE** /services/haproxy/configuration/peer_section/{name} | Delete a peer
*PeerApi* | [**get_peer_section**](../docs/PeerApi.md#get_peer_section) | **GET** /services/haproxy/configuration/peer_section/{name} | Return a peer
*PeerApi* | [**get_peer_sections**](../docs/PeerApi.md#get_peer_sections) | **GET** /services/haproxy/configuration/peer_section | Return an array of peer_section
*PeerEntryApi* | [**create_peer_entry**](../docs/PeerEntryApi.md#create_peer_entry) | **POST** /services/haproxy/configuration/peer_entries | Add a new peer_entry
*PeerEntryApi* | [**delete_peer_entry**](../docs/PeerEntryApi.md#delete_peer_entry) | **DELETE** /services/haproxy/configuration/peer_entries/{name} | Delete a peer_entry
*PeerEntryApi* | [**get_peer_entries**](../docs/PeerEntryApi.md#get_peer_entries) | **GET** /services/haproxy/configuration/peer_entries | Return an array of peer_entries
*PeerEntryApi* | [**get_peer_entry**](../docs/PeerEntryApi.md#get_peer_entry) | **GET** /services/haproxy/configuration/peer_entries/{name} | Return one peer_entry
*PeerEntryApi* | [**replace_peer_entry**](../docs/PeerEntryApi.md#replace_peer_entry) | **PUT** /services/haproxy/configuration/peer_entries/{name} | Replace a peer_entry
*ProcessManagerApi* | [**create_program**](../docs/ProcessManagerApi.md#create_program) | **POST** /services/haproxy/configuration/programs | Add a program
*ProcessManagerApi* | [**delete_program**](../docs/ProcessManagerApi.md#delete_program) | **DELETE** /services/haproxy/configuration/programs/{name} | Delete a program
*ProcessManagerApi* | [**get_program**](../docs/ProcessManagerApi.md#get_program) | **GET** /services/haproxy/configuration/programs/{name} | Return a program
*ProcessManagerApi* | [**get_programs**](../docs/ProcessManagerApi.md#get_programs) | **GET** /services/haproxy/configuration/programs | Return an array of programs
*ProcessManagerApi* | [**replace_program**](../docs/ProcessManagerApi.md#replace_program) | **PUT** /services/haproxy/configuration/programs/{name} | Replace a program
*ReloadsApi* | [**get_reload**](../docs/ReloadsApi.md#get_reload) | **GET** /services/haproxy/reloads/{id} | Return one HAProxy reload status
*ReloadsApi* | [**get_reloads**](../docs/ReloadsApi.md#get_reloads) | **GET** /services/haproxy/reloads | Return list of HAProxy Reloads.
*ResolverApi* | [**create_resolver**](../docs/ResolverApi.md#create_resolver) | **POST** /services/haproxy/configuration/resolvers | Add a resolver
*ResolverApi* | [**delete_resolver**](../docs/ResolverApi.md#delete_resolver) | **DELETE** /services/haproxy/configuration/resolvers/{name} | Delete a resolver
*ResolverApi* | [**get_resolver**](../docs/ResolverApi.md#get_resolver) | **GET** /services/haproxy/configuration/resolvers/{name} | Return a resolver
*ResolverApi* | [**get_resolvers**](../docs/ResolverApi.md#get_resolvers) | **GET** /services/haproxy/configuration/resolvers | Return an array of resolvers
*ResolverApi* | [**replace_resolver**](../docs/ResolverApi.md#replace_resolver) | **PUT** /services/haproxy/configuration/resolvers/{name} | Replace a resolver
*RingApi* | [**create_ring**](../docs/RingApi.md#create_ring) | **POST** /services/haproxy/configuration/rings | Add a ring
*RingApi* | [**delete_ring**](../docs/RingApi.md#delete_ring) | **DELETE** /services/haproxy/configuration/rings/{name} | Delete a ring
*RingApi* | [**get_ring**](../docs/RingApi.md#get_ring) | **GET** /services/haproxy/configuration/rings/{name} | Return a ring
*RingApi* | [**get_rings**](../docs/RingApi.md#get_rings) | **GET** /services/haproxy/configuration/rings | Return an array of rings
*RingApi* | [**replace_ring**](../docs/RingApi.md#replace_ring) | **PUT** /services/haproxy/configuration/rings/{name} | Replace a ring
*ServerApi* | [**add_runtime_server**](../docs/ServerApi.md#add_runtime_server) | **POST** /services/haproxy/runtime/servers | Adds a new server to a backend
*ServerApi* | [**create_server**](../docs/ServerApi.md#create_server) | **POST** /services/haproxy/configuration/servers | Add a new server
*ServerApi* | [**delete_runtime_server**](../docs/ServerApi.md#delete_runtime_server) | **DELETE** /services/haproxy/runtime/servers/{name} | Deletes a server from a backend
*ServerApi* | [**delete_server**](../docs/ServerApi.md#delete_server) | **DELETE** /services/haproxy/configuration/servers/{name} | Delete a server
*ServerApi* | [**get_runtime_server**](../docs/ServerApi.md#get_runtime_server) | **GET** /services/haproxy/runtime/servers/{name} | Return one server runtime settings
*ServerApi* | [**get_runtime_servers**](../docs/ServerApi.md#get_runtime_servers) | **GET** /services/haproxy/runtime/servers | Return an array of runtime servers&#x27; settings
*ServerApi* | [**get_server**](../docs/ServerApi.md#get_server) | **GET** /services/haproxy/configuration/servers/{name} | Return one server
*ServerApi* | [**get_servers**](../docs/ServerApi.md#get_servers) | **GET** /services/haproxy/configuration/servers | Return an array of servers
*ServerApi* | [**replace_runtime_server**](../docs/ServerApi.md#replace_runtime_server) | **PUT** /services/haproxy/runtime/servers/{name} | Replace server transient settings
*ServerApi* | [**replace_server**](../docs/ServerApi.md#replace_server) | **PUT** /services/haproxy/configuration/servers/{name} | Replace a server
*ServerSwitchingRuleApi* | [**create_server_switching_rule**](../docs/ServerSwitchingRuleApi.md#create_server_switching_rule) | **POST** /services/haproxy/configuration/server_switching_rules | Add a new Server Switching Rule
*ServerSwitchingRuleApi* | [**delete_server_switching_rule**](../docs/ServerSwitchingRuleApi.md#delete_server_switching_rule) | **DELETE** /services/haproxy/configuration/server_switching_rules/{index} | Delete a Server Switching Rule
*ServerSwitchingRuleApi* | [**get_server_switching_rule**](../docs/ServerSwitchingRuleApi.md#get_server_switching_rule) | **GET** /services/haproxy/configuration/server_switching_rules/{index} | Return one Server Switching Rule
*ServerSwitchingRuleApi* | [**get_server_switching_rules**](../docs/ServerSwitchingRuleApi.md#get_server_switching_rules) | **GET** /services/haproxy/configuration/server_switching_rules | Return an array of all Server Switching Rules
*ServerSwitchingRuleApi* | [**replace_server_switching_rule**](../docs/ServerSwitchingRuleApi.md#replace_server_switching_rule) | **PUT** /services/haproxy/configuration/server_switching_rules/{index} | Replace a Server Switching Rule
*ServerTemplateApi* | [**create_server_template**](../docs/ServerTemplateApi.md#create_server_template) | **POST** /services/haproxy/configuration/server_templates | Add a new server template
*ServerTemplateApi* | [**delete_server_template**](../docs/ServerTemplateApi.md#delete_server_template) | **DELETE** /services/haproxy/configuration/server_templates/{prefix} | Delete a server template
*ServerTemplateApi* | [**get_server_template**](../docs/ServerTemplateApi.md#get_server_template) | **GET** /services/haproxy/configuration/server_templates/{prefix} | Return one server template
*ServerTemplateApi* | [**get_server_templates**](../docs/ServerTemplateApi.md#get_server_templates) | **GET** /services/haproxy/configuration/server_templates | Return an array of server templates
*ServerTemplateApi* | [**replace_server_template**](../docs/ServerTemplateApi.md#replace_server_template) | **PUT** /services/haproxy/configuration/server_templates/{prefix} | Replace a server template
*ServiceDiscoveryApi* | [**create_aws_region**](../docs/ServiceDiscoveryApi.md#create_aws_region) | **POST** /service_discovery/aws | Add a new AWS region
*ServiceDiscoveryApi* | [**create_consul**](../docs/ServiceDiscoveryApi.md#create_consul) | **POST** /service_discovery/consul | Add a new Consul server
*ServiceDiscoveryApi* | [**delete_aws_region**](../docs/ServiceDiscoveryApi.md#delete_aws_region) | **DELETE** /service_discovery/aws/{id} | Delete an AWS region
*ServiceDiscoveryApi* | [**delete_consul**](../docs/ServiceDiscoveryApi.md#delete_consul) | **DELETE** /service_discovery/consul/{id} | Delete a Consul server
*ServiceDiscoveryApi* | [**get_aws_region**](../docs/ServiceDiscoveryApi.md#get_aws_region) | **GET** /service_discovery/aws/{id} | Return an AWS region
*ServiceDiscoveryApi* | [**get_aws_regions**](../docs/ServiceDiscoveryApi.md#get_aws_regions) | **GET** /service_discovery/aws | Return an array of all configured AWS regions
*ServiceDiscoveryApi* | [**get_consul**](../docs/ServiceDiscoveryApi.md#get_consul) | **GET** /service_discovery/consul/{id} | Return one Consul server
*ServiceDiscoveryApi* | [**get_consuls**](../docs/ServiceDiscoveryApi.md#get_consuls) | **GET** /service_discovery/consul | Return an array of all configured Consul servers
*ServiceDiscoveryApi* | [**replace_aws_region**](../docs/ServiceDiscoveryApi.md#replace_aws_region) | **PUT** /service_discovery/aws/{id} | Replace an AWS region
*ServiceDiscoveryApi* | [**replace_consul**](../docs/ServiceDiscoveryApi.md#replace_consul) | **PUT** /service_discovery/consul/{id} | Replace a Consul server
*SitesApi* | [**create_site**](../docs/SitesApi.md#create_site) | **POST** /services/haproxy/sites | Add a site
*SitesApi* | [**delete_site**](../docs/SitesApi.md#delete_site) | **DELETE** /services/haproxy/sites/{name} | Delete a site
*SitesApi* | [**get_site**](../docs/SitesApi.md#get_site) | **GET** /services/haproxy/sites/{name} | Return a site
*SitesApi* | [**get_sites**](../docs/SitesApi.md#get_sites) | **GET** /services/haproxy/sites | Return an array of sites
*SitesApi* | [**replace_site**](../docs/SitesApi.md#replace_site) | **PUT** /services/haproxy/sites/{name} | Replace a site
*SpecificationApi* | [**get_specification**](../docs/SpecificationApi.md#get_specification) | **GET** /specification | Data Plane API Specification
*SpecificationOpenapiv3Api* | [**get_openapiv3_specification**](../docs/SpecificationOpenapiv3Api.md#get_openapiv3_specification) | **GET** /specification_openapiv3 | Data Plane API v3 Specification
*SpoeApi* | [**create_spoe**](../docs/SpoeApi.md#create_spoe) | **POST** /services/haproxy/spoe/spoe_files | Creates SPOE file with its entries
*SpoeApi* | [**create_spoe_agent**](../docs/SpoeApi.md#create_spoe_agent) | **POST** /services/haproxy/spoe/spoe_agents | Add a new spoe agent to scope
*SpoeApi* | [**create_spoe_group**](../docs/SpoeApi.md#create_spoe_group) | **POST** /services/haproxy/spoe/spoe_groups | Add a new SPOE groups
*SpoeApi* | [**create_spoe_message**](../docs/SpoeApi.md#create_spoe_message) | **POST** /services/haproxy/spoe/spoe_messages | Add a new spoe message to scope
*SpoeApi* | [**create_spoe_scope**](../docs/SpoeApi.md#create_spoe_scope) | **POST** /services/haproxy/spoe/spoe_scopes | Add a new spoe scope
*SpoeApi* | [**delete_spoe_agent**](../docs/SpoeApi.md#delete_spoe_agent) | **DELETE** /services/haproxy/spoe/spoe_agents/{name} | Delete a SPOE agent
*SpoeApi* | [**delete_spoe_file**](../docs/SpoeApi.md#delete_spoe_file) | **DELETE** /services/haproxy/spoe/spoe_files/{name} | Delete SPOE file
*SpoeApi* | [**delete_spoe_group**](../docs/SpoeApi.md#delete_spoe_group) | **DELETE** /services/haproxy/spoe/spoe_groups/{name} | Delete a SPOE groups
*SpoeApi* | [**delete_spoe_message**](../docs/SpoeApi.md#delete_spoe_message) | **DELETE** /services/haproxy/spoe/spoe_messages/{name} | Delete a spoe message
*SpoeApi* | [**delete_spoe_scope**](../docs/SpoeApi.md#delete_spoe_scope) | **DELETE** /services/haproxy/spoe/spoe_scopes/{name} | Delete a SPOE scope
*SpoeApi* | [**get_all_spoe_files**](../docs/SpoeApi.md#get_all_spoe_files) | **GET** /services/haproxy/spoe/spoe_files | Return all available SPOE files
*SpoeApi* | [**get_one_spoe_file**](../docs/SpoeApi.md#get_one_spoe_file) | **GET** /services/haproxy/spoe/spoe_files/{name} | Return one SPOE file
*SpoeApi* | [**get_spoe_agent**](../docs/SpoeApi.md#get_spoe_agent) | **GET** /services/haproxy/spoe/spoe_agents/{name} | Return a spoe agent
*SpoeApi* | [**get_spoe_agents**](../docs/SpoeApi.md#get_spoe_agents) | **GET** /services/haproxy/spoe/spoe_agents | Return an array of spoe agents in one scope
*SpoeApi* | [**get_spoe_configuration_version**](../docs/SpoeApi.md#get_spoe_configuration_version) | **GET** /services/haproxy/spoe/version | Return a SPOE configuration version
*SpoeApi* | [**get_spoe_group**](../docs/SpoeApi.md#get_spoe_group) | **GET** /services/haproxy/spoe/spoe_groups/{name} | Return a SPOE groups
*SpoeApi* | [**get_spoe_groups**](../docs/SpoeApi.md#get_spoe_groups) | **GET** /services/haproxy/spoe/spoe_groups | Return an array of SPOE groups
*SpoeApi* | [**get_spoe_message**](../docs/SpoeApi.md#get_spoe_message) | **GET** /services/haproxy/spoe/spoe_messages/{name} | Return a spoe message
*SpoeApi* | [**get_spoe_messages**](../docs/SpoeApi.md#get_spoe_messages) | **GET** /services/haproxy/spoe/spoe_messages | Return an array of spoe messages in one scope
*SpoeApi* | [**get_spoe_scope**](../docs/SpoeApi.md#get_spoe_scope) | **GET** /services/haproxy/spoe/spoe_scopes/{name} | Return one SPOE scope
*SpoeApi* | [**get_spoe_scopes**](../docs/SpoeApi.md#get_spoe_scopes) | **GET** /services/haproxy/spoe/spoe_scopes | Return an array of spoe scopes
*SpoeApi* | [**replace_spoe_agent**](../docs/SpoeApi.md#replace_spoe_agent) | **PUT** /services/haproxy/spoe/spoe_agents/{name} | Replace a SPOE agent
*SpoeApi* | [**replace_spoe_group**](../docs/SpoeApi.md#replace_spoe_group) | **PUT** /services/haproxy/spoe/spoe_groups/{name} | Replace a SPOE groups
*SpoeApi* | [**replace_spoe_message**](../docs/SpoeApi.md#replace_spoe_message) | **PUT** /services/haproxy/spoe/spoe_messages/{name} | Replace a spoe message
*SpoeTransactionsApi* | [**commit_spoe_transaction**](../docs/SpoeTransactionsApi.md#commit_spoe_transaction) | **PUT** /services/haproxy/spoe_transactions/{id} | Commit transaction
*SpoeTransactionsApi* | [**delete_spoe_transaction**](../docs/SpoeTransactionsApi.md#delete_spoe_transaction) | **DELETE** /services/haproxy/spoe_transactions/{id} | Delete a transaction
*SpoeTransactionsApi* | [**get_spoe_transaction**](../docs/SpoeTransactionsApi.md#get_spoe_transaction) | **GET** /services/haproxy/spoe_transactions/{id} | Return one SPOE configuration transactions
*SpoeTransactionsApi* | [**get_spoe_transactions**](../docs/SpoeTransactionsApi.md#get_spoe_transactions) | **GET** /services/haproxy/spoe_transactions | Return list of SPOE configuration transactions.
*SpoeTransactionsApi* | [**start_spoe_transaction**](../docs/SpoeTransactionsApi.md#start_spoe_transaction) | **POST** /services/haproxy/spoe_transactions | Start a new transaction
*StatsApi* | [**get_stats**](../docs/StatsApi.md#get_stats) | **GET** /services/haproxy/stats/native | Gets stats
*StickRuleApi* | [**create_stick_rule**](../docs/StickRuleApi.md#create_stick_rule) | **POST** /services/haproxy/configuration/stick_rules | Add a new Stick Rule
*StickRuleApi* | [**delete_stick_rule**](../docs/StickRuleApi.md#delete_stick_rule) | **DELETE** /services/haproxy/configuration/stick_rules/{index} | Delete a Stick Rule
*StickRuleApi* | [**get_stick_rule**](../docs/StickRuleApi.md#get_stick_rule) | **GET** /services/haproxy/configuration/stick_rules/{index} | Return one Stick Rule
*StickRuleApi* | [**get_stick_rules**](../docs/StickRuleApi.md#get_stick_rules) | **GET** /services/haproxy/configuration/stick_rules | Return an array of all Stick Rules
*StickRuleApi* | [**replace_stick_rule**](../docs/StickRuleApi.md#replace_stick_rule) | **PUT** /services/haproxy/configuration/stick_rules/{index} | Replace a Stick Rule
*StickTableApi* | [**get_stick_table**](../docs/StickTableApi.md#get_stick_table) | **GET** /services/haproxy/runtime/stick_tables/{name} | Return Stick Table
*StickTableApi* | [**get_stick_table_entries**](../docs/StickTableApi.md#get_stick_table_entries) | **GET** /services/haproxy/runtime/stick_table_entries | Return Stick Table Entries
*StickTableApi* | [**get_stick_tables**](../docs/StickTableApi.md#get_stick_tables) | **GET** /services/haproxy/runtime/stick_tables | Return Stick Tables
*StickTableApi* | [**set_stick_table_entries**](../docs/StickTableApi.md#set_stick_table_entries) | **POST** /services/haproxy/runtime/stick_table_entries | Set Entry to Stick Table
*StorageApi* | [**create_storage_general_file**](../docs/StorageApi.md#create_storage_general_file) | **POST** /services/haproxy/storage/general | Creates a managed storage general use file with contents
*StorageApi* | [**create_storage_map_file**](../docs/StorageApi.md#create_storage_map_file) | **POST** /services/haproxy/storage/maps | Creates a managed storage map file with its entries
*StorageApi* | [**create_storage_ssl_certificate**](../docs/StorageApi.md#create_storage_ssl_certificate) | **POST** /services/haproxy/storage/ssl_certificates | Create SSL certificate
*StorageApi* | [**delete_storage_general_file**](../docs/StorageApi.md#delete_storage_general_file) | **DELETE** /services/haproxy/storage/general/{name} | Deletes a managed general use file from disk
*StorageApi* | [**delete_storage_map**](../docs/StorageApi.md#delete_storage_map) | **DELETE** /services/haproxy/storage/maps/{name} | Deletes a managed map file from disk
*StorageApi* | [**delete_storage_ssl_certificate**](../docs/StorageApi.md#delete_storage_ssl_certificate) | **DELETE** /services/haproxy/storage/ssl_certificates/{name} | Delete SSL certificate from disk
*StorageApi* | [**get_all_storage_general_files**](../docs/StorageApi.md#get_all_storage_general_files) | **GET** /services/haproxy/storage/general | Return a list of all managed general use files
*StorageApi* | [**get_all_storage_map_files**](../docs/StorageApi.md#get_all_storage_map_files) | **GET** /services/haproxy/storage/maps | Return a list of all managed map files
*StorageApi* | [**get_all_storage_ssl_certificates**](../docs/StorageApi.md#get_all_storage_ssl_certificates) | **GET** /services/haproxy/storage/ssl_certificates | Return all available SSL certificates on disk
*StorageApi* | [**get_one_storage_general_file**](../docs/StorageApi.md#get_one_storage_general_file) | **GET** /services/haproxy/storage/general/{name} | Return the contents of one managed general use file from disk
*StorageApi* | [**get_one_storage_map**](../docs/StorageApi.md#get_one_storage_map) | **GET** /services/haproxy/storage/maps/{name} | Return the contents of one managed map file from disk
*StorageApi* | [**get_one_storage_ssl_certificate**](../docs/StorageApi.md#get_one_storage_ssl_certificate) | **GET** /services/haproxy/storage/ssl_certificates/{name} | Return one SSL certificate from disk
*StorageApi* | [**replace_storage_general_file**](../docs/StorageApi.md#replace_storage_general_file) | **PUT** /services/haproxy/storage/general/{name} | Replace contents of a managed general use file on disk
*StorageApi* | [**replace_storage_map_file**](../docs/StorageApi.md#replace_storage_map_file) | **PUT** /services/haproxy/storage/maps/{name} | Replace contents of a managed map file on disk
*StorageApi* | [**replace_storage_ssl_certificate**](../docs/StorageApi.md#replace_storage_ssl_certificate) | **PUT** /services/haproxy/storage/ssl_certificates/{name} | Replace SSL certificates on disk
*TCPCheckApi* | [**create_tcp_check**](../docs/TCPCheckApi.md#create_tcp_check) | **POST** /services/haproxy/configuration/tcp_checks | Add a new TCP check
*TCPCheckApi* | [**delete_tcp_check**](../docs/TCPCheckApi.md#delete_tcp_check) | **DELETE** /services/haproxy/configuration/tcp_checks/{index} | Delete a TCP check
*TCPCheckApi* | [**get_tcp_check**](../docs/TCPCheckApi.md#get_tcp_check) | **GET** /services/haproxy/configuration/tcp_checks/{index} | Return one TCP check
*TCPCheckApi* | [**get_tcp_checks**](../docs/TCPCheckApi.md#get_tcp_checks) | **GET** /services/haproxy/configuration/tcp_checks | Return an array of TCP checks
*TCPCheckApi* | [**replace_tcp_check**](../docs/TCPCheckApi.md#replace_tcp_check) | **PUT** /services/haproxy/configuration/tcp_checks/{index} | Replace a TCP check
*TCPRequestRuleApi* | [**create_tcp_request_rule**](../docs/TCPRequestRuleApi.md#create_tcp_request_rule) | **POST** /services/haproxy/configuration/tcp_request_rules | Add a new TCP Request Rule
*TCPRequestRuleApi* | [**delete_tcp_request_rule**](../docs/TCPRequestRuleApi.md#delete_tcp_request_rule) | **DELETE** /services/haproxy/configuration/tcp_request_rules/{index} | Delete a TCP Request Rule
*TCPRequestRuleApi* | [**get_tcp_request_rule**](../docs/TCPRequestRuleApi.md#get_tcp_request_rule) | **GET** /services/haproxy/configuration/tcp_request_rules/{index} | Return one TCP Request Rule
*TCPRequestRuleApi* | [**get_tcp_request_rules**](../docs/TCPRequestRuleApi.md#get_tcp_request_rules) | **GET** /services/haproxy/configuration/tcp_request_rules | Return an array of all TCP Request Rules
*TCPRequestRuleApi* | [**replace_tcp_request_rule**](../docs/TCPRequestRuleApi.md#replace_tcp_request_rule) | **PUT** /services/haproxy/configuration/tcp_request_rules/{index} | Replace a TCP Request Rule
*TCPResponseRuleApi* | [**create_tcp_response_rule**](../docs/TCPResponseRuleApi.md#create_tcp_response_rule) | **POST** /services/haproxy/configuration/tcp_response_rules | Add a new TCP Response Rule
*TCPResponseRuleApi* | [**delete_tcp_response_rule**](../docs/TCPResponseRuleApi.md#delete_tcp_response_rule) | **DELETE** /services/haproxy/configuration/tcp_response_rules/{index} | Delete a TCP Response Rule
*TCPResponseRuleApi* | [**get_tcp_response_rule**](../docs/TCPResponseRuleApi.md#get_tcp_response_rule) | **GET** /services/haproxy/configuration/tcp_response_rules/{index} | Return one TCP Response Rule
*TCPResponseRuleApi* | [**get_tcp_response_rules**](../docs/TCPResponseRuleApi.md#get_tcp_response_rules) | **GET** /services/haproxy/configuration/tcp_response_rules | Return an array of all TCP Response Rules
*TCPResponseRuleApi* | [**replace_tcp_response_rule**](../docs/TCPResponseRuleApi.md#replace_tcp_response_rule) | **PUT** /services/haproxy/configuration/tcp_response_rules/{index} | Replace a TCP Response Rule
*TransactionsApi* | [**commit_transaction**](../docs/TransactionsApi.md#commit_transaction) | **PUT** /services/haproxy/transactions/{id} | Commit transaction
*TransactionsApi* | [**delete_transaction**](../docs/TransactionsApi.md#delete_transaction) | **DELETE** /services/haproxy/transactions/{id} | Delete a transaction
*TransactionsApi* | [**get_transaction**](../docs/TransactionsApi.md#get_transaction) | **GET** /services/haproxy/transactions/{id} | Return one HAProxy configuration transactions
*TransactionsApi* | [**get_transactions**](../docs/TransactionsApi.md#get_transactions) | **GET** /services/haproxy/transactions | Return list of HAProxy configuration transactions.
*TransactionsApi* | [**start_transaction**](../docs/TransactionsApi.md#start_transaction) | **POST** /services/haproxy/transactions | Start a new transaction
*UserApi* | [**create_user**](../docs/UserApi.md#create_user) | **POST** /services/haproxy/configuration/users | Add a new userlist user
*UserApi* | [**delete_user**](../docs/UserApi.md#delete_user) | **DELETE** /services/haproxy/configuration/users/{username} | Delete a user
*UserApi* | [**get_user**](../docs/UserApi.md#get_user) | **GET** /services/haproxy/configuration/users/{username} | Return one userlist user
*UserApi* | [**get_users**](../docs/UserApi.md#get_users) | **GET** /services/haproxy/configuration/users | Return an array of userlist users
*UserApi* | [**replace_user**](../docs/UserApi.md#replace_user) | **PUT** /services/haproxy/configuration/users/{username} | Replace a user
*UserlistApi* | [**create_userlist**](../docs/UserlistApi.md#create_userlist) | **POST** /services/haproxy/configuration/userlists | Add a new userlist
*UserlistApi* | [**delete_userlist**](../docs/UserlistApi.md#delete_userlist) | **DELETE** /services/haproxy/configuration/userlists/{name} | Delete a userlist
*UserlistApi* | [**get_userlist**](../docs/UserlistApi.md#get_userlist) | **GET** /services/haproxy/configuration/userlists/{name} | Return one userlist
*UserlistApi* | [**get_userlists**](../docs/UserlistApi.md#get_userlists) | **GET** /services/haproxy/configuration/userlists | Return an array of userlists

## Documentation For Models

 - [Acl](../docs/Acl.md)
 - [AclFile](../docs/AclFile.md)
 - [AclFileEntry](../docs/AclFileEntry.md)
 - [AclFiles](../docs/AclFiles.md)
 - [AclFilesEntries](../docs/AclFilesEntries.md)
 - [Acls](../docs/Acls.md)
 - [AwsFilters](../docs/AwsFilters.md)
 - [AwsRegion](../docs/AwsRegion.md)
 - [AwsRegions](../docs/AwsRegions.md)
 - [Backend](../docs/Backend.md)
 - [BackendForcePersist](../docs/BackendForcePersist.md)
 - [BackendSwitchingRule](../docs/BackendSwitchingRule.md)
 - [BackendSwitchingRules](../docs/BackendSwitchingRules.md)
 - [Backends](../docs/Backends.md)
 - [Balance](../docs/Balance.md)
 - [Bind](../docs/Bind.md)
 - [BindParams](../docs/BindParams.md)
 - [Binds](../docs/Binds.md)
 - [Cache](../docs/Cache.md)
 - [Caches](../docs/Caches.md)
 - [Capture](../docs/Capture.md)
 - [Captures](../docs/Captures.md)
 - [ClusterControllerInformation](../docs/ClusterControllerInformation.md)
 - [ClusterControllerInformationLogTargets](../docs/ClusterControllerInformationLogTargets.md)
 - [ClusterSettings](../docs/ClusterSettings.md)
 - [Compression](../docs/Compression.md)
 - [ConfigStickTable](../docs/ConfigStickTable.md)
 - [Consul](../docs/Consul.md)
 - [Consuls](../docs/Consuls.md)
 - [Cookie](../docs/Cookie.md)
 - [CookieAttr](../docs/CookieAttr.md)
 - [DefaultBind](../docs/DefaultBind.md)
 - [DefaultServer](../docs/DefaultServer.md)
 - [Defaults](../docs/Defaults.md)
 - [DefaultsSections](../docs/DefaultsSections.md)
 - [DgramBind](../docs/DgramBind.md)
 - [DgramBinds](../docs/DgramBinds.md)
 - [EmailAlert](../docs/EmailAlert.md)
 - [Endpoint](../docs/Endpoint.md)
 - [Endpoints](../docs/Endpoints.md)
 - [Error](../docs/Error.md)
 - [Errorfile](../docs/Errorfile.md)
 - [Errorfiles](../docs/Errorfiles.md)
 - [Errorloc](../docs/Errorloc.md)
 - [FcgiApp](../docs/FcgiApp.md)
 - [FcgiApps](../docs/FcgiApps.md)
 - [FcgiLogStderr](../docs/FcgiLogStderr.md)
 - [FcgiPassHeader](../docs/FcgiPassHeader.md)
 - [FcgiSetParam](../docs/FcgiSetParam.md)
 - [Filter](../docs/Filter.md)
 - [Filters](../docs/Filters.md)
 - [Forwardfor](../docs/Forwardfor.md)
 - [Frontend](../docs/Frontend.md)
 - [Frontends](../docs/Frontends.md)
 - [GeneralFile](../docs/GeneralFile.md)
 - [GeneralFiles](../docs/GeneralFiles.md)
 - [GlobalCpuMaps](../docs/GlobalCpuMaps.md)
 - [GlobalDefaultPath](../docs/GlobalDefaultPath.md)
 - [GlobalDeviceAtlasOptions](../docs/GlobalDeviceAtlasOptions.md)
 - [GlobalFiftyOneDegreesOptions](../docs/GlobalFiftyOneDegreesOptions.md)
 - [GlobalH1CaseAdjust](../docs/GlobalH1CaseAdjust.md)
 - [GlobalLogSendHostname](../docs/GlobalLogSendHostname.md)
 - [GlobalLuaLoads](../docs/GlobalLuaLoads.md)
 - [GlobalLuaPrependPath](../docs/GlobalLuaPrependPath.md)
 - [GlobalPresetenv](../docs/GlobalPresetenv.md)
 - [GlobalRuntimeApis](../docs/GlobalRuntimeApis.md)
 - [GlobalSetVar](../docs/GlobalSetVar.md)
 - [GlobalSetVarFmt](../docs/GlobalSetVarFmt.md)
 - [GlobalSslEngines](../docs/GlobalSslEngines.md)
 - [GlobalThreadGroupLines](../docs/GlobalThreadGroupLines.md)
 - [GlobalTuneOptions](../docs/GlobalTuneOptions.md)
 - [GlobalWurflOptions](../docs/GlobalWurflOptions.md)
 - [Group](../docs/Group.md)
 - [Groups](../docs/Groups.md)
 - [HashType](../docs/HashType.md)
 - [Health](../docs/Health.md)
 - [HttpAfterResponseRule](../docs/HttpAfterResponseRule.md)
 - [HttpAfterResponseRules](../docs/HttpAfterResponseRules.md)
 - [HttpCheck](../docs/HttpCheck.md)
 - [HttpChecks](../docs/HttpChecks.md)
 - [HttpErrorRule](../docs/HttpErrorRule.md)
 - [HttpErrorRules](../docs/HttpErrorRules.md)
 - [HttpErrorsSection](../docs/HttpErrorsSection.md)
 - [HttpErrorsSections](../docs/HttpErrorsSections.md)
 - [HttpRequestRule](../docs/HttpRequestRule.md)
 - [HttpRequestRules](../docs/HttpRequestRules.md)
 - [HttpResponseRule](../docs/HttpResponseRule.md)
 - [HttpResponseRules](../docs/HttpResponseRules.md)
 - [HttpchkParams](../docs/HttpchkParams.md)
 - [Info](../docs/Info.md)
 - [InfoApi](../docs/InfoApi.md)
 - [InfoSystem](../docs/InfoSystem.md)
 - [InfoSystemCpuInfo](../docs/InfoSystemCpuInfo.md)
 - [InfoSystemMemInfo](../docs/InfoSystemMemInfo.md)
 - [InlineResponse200](../docs/InlineResponse200.md)
 - [InlineResponse2001](../docs/InlineResponse2001.md)
 - [InlineResponse20010](../docs/InlineResponse20010.md)
 - [InlineResponse20011](../docs/InlineResponse20011.md)
 - [InlineResponse20012](../docs/InlineResponse20012.md)
 - [InlineResponse20013](../docs/InlineResponse20013.md)
 - [InlineResponse20014](../docs/InlineResponse20014.md)
 - [InlineResponse20015](../docs/InlineResponse20015.md)
 - [InlineResponse20016](../docs/InlineResponse20016.md)
 - [InlineResponse20017](../docs/InlineResponse20017.md)
 - [InlineResponse20018](../docs/InlineResponse20018.md)
 - [InlineResponse20019](../docs/InlineResponse20019.md)
 - [InlineResponse2002](../docs/InlineResponse2002.md)
 - [InlineResponse20020](../docs/InlineResponse20020.md)
 - [InlineResponse20021](../docs/InlineResponse20021.md)
 - [InlineResponse20022](../docs/InlineResponse20022.md)
 - [InlineResponse20023](../docs/InlineResponse20023.md)
 - [InlineResponse20024](../docs/InlineResponse20024.md)
 - [InlineResponse20025](../docs/InlineResponse20025.md)
 - [InlineResponse20026](../docs/InlineResponse20026.md)
 - [InlineResponse20027](../docs/InlineResponse20027.md)
 - [InlineResponse20028](../docs/InlineResponse20028.md)
 - [InlineResponse20029](../docs/InlineResponse20029.md)
 - [InlineResponse2003](../docs/InlineResponse2003.md)
 - [InlineResponse20030](../docs/InlineResponse20030.md)
 - [InlineResponse20031](../docs/InlineResponse20031.md)
 - [InlineResponse20032](../docs/InlineResponse20032.md)
 - [InlineResponse20033](../docs/InlineResponse20033.md)
 - [InlineResponse20034](../docs/InlineResponse20034.md)
 - [InlineResponse20035](../docs/InlineResponse20035.md)
 - [InlineResponse20036](../docs/InlineResponse20036.md)
 - [InlineResponse20037](../docs/InlineResponse20037.md)
 - [InlineResponse20038](../docs/InlineResponse20038.md)
 - [InlineResponse20039](../docs/InlineResponse20039.md)
 - [InlineResponse2004](../docs/InlineResponse2004.md)
 - [InlineResponse20040](../docs/InlineResponse20040.md)
 - [InlineResponse20041](../docs/InlineResponse20041.md)
 - [InlineResponse20042](../docs/InlineResponse20042.md)
 - [InlineResponse20043](../docs/InlineResponse20043.md)
 - [InlineResponse20044](../docs/InlineResponse20044.md)
 - [InlineResponse20045](../docs/InlineResponse20045.md)
 - [InlineResponse20046](../docs/InlineResponse20046.md)
 - [InlineResponse20047](../docs/InlineResponse20047.md)
 - [InlineResponse20048](../docs/InlineResponse20048.md)
 - [InlineResponse20049](../docs/InlineResponse20049.md)
 - [InlineResponse2005](../docs/InlineResponse2005.md)
 - [InlineResponse20050](../docs/InlineResponse20050.md)
 - [InlineResponse20051](../docs/InlineResponse20051.md)
 - [InlineResponse20052](../docs/InlineResponse20052.md)
 - [InlineResponse20053](../docs/InlineResponse20053.md)
 - [InlineResponse20054](../docs/InlineResponse20054.md)
 - [InlineResponse20055](../docs/InlineResponse20055.md)
 - [InlineResponse20056](../docs/InlineResponse20056.md)
 - [InlineResponse20057](../docs/InlineResponse20057.md)
 - [InlineResponse20058](../docs/InlineResponse20058.md)
 - [InlineResponse20059](../docs/InlineResponse20059.md)
 - [InlineResponse2006](../docs/InlineResponse2006.md)
 - [InlineResponse20060](../docs/InlineResponse20060.md)
 - [InlineResponse20061](../docs/InlineResponse20061.md)
 - [InlineResponse20062](../docs/InlineResponse20062.md)
 - [InlineResponse20063](../docs/InlineResponse20063.md)
 - [InlineResponse20064](../docs/InlineResponse20064.md)
 - [InlineResponse20065](../docs/InlineResponse20065.md)
 - [InlineResponse20066](../docs/InlineResponse20066.md)
 - [InlineResponse20067](../docs/InlineResponse20067.md)
 - [InlineResponse20068](../docs/InlineResponse20068.md)
 - [InlineResponse20069](../docs/InlineResponse20069.md)
 - [InlineResponse2007](../docs/InlineResponse2007.md)
 - [InlineResponse20070](../docs/InlineResponse20070.md)
 - [InlineResponse20071](../docs/InlineResponse20071.md)
 - [InlineResponse20072](../docs/InlineResponse20072.md)
 - [InlineResponse20073](../docs/InlineResponse20073.md)
 - [InlineResponse20074](../docs/InlineResponse20074.md)
 - [InlineResponse20075](../docs/InlineResponse20075.md)
 - [InlineResponse20076](../docs/InlineResponse20076.md)
 - [InlineResponse20077](../docs/InlineResponse20077.md)
 - [InlineResponse20078](../docs/InlineResponse20078.md)
 - [InlineResponse20079](../docs/InlineResponse20079.md)
 - [InlineResponse2008](../docs/InlineResponse2008.md)
 - [InlineResponse20080](../docs/InlineResponse20080.md)
 - [InlineResponse20081](../docs/InlineResponse20081.md)
 - [InlineResponse20082](../docs/InlineResponse20082.md)
 - [InlineResponse20083](../docs/InlineResponse20083.md)
 - [InlineResponse20084](../docs/InlineResponse20084.md)
 - [InlineResponse20085](../docs/InlineResponse20085.md)
 - [InlineResponse20086](../docs/InlineResponse20086.md)
 - [InlineResponse20087](../docs/InlineResponse20087.md)
 - [InlineResponse20088](../docs/InlineResponse20088.md)
 - [InlineResponse20089](../docs/InlineResponse20089.md)
 - [InlineResponse2009](../docs/InlineResponse2009.md)
 - [InlineResponse20090](../docs/InlineResponse20090.md)
 - [InlineResponse429](../docs/InlineResponse429.md)
 - [LogForward](../docs/LogForward.md)
 - [LogForwards](../docs/LogForwards.md)
 - [LogTarget](../docs/LogTarget.md)
 - [LogTargets](../docs/LogTargets.md)
 - [MailerEntries](../docs/MailerEntries.md)
 - [MailerEntry](../docs/MailerEntry.md)
 - [MailersSection](../docs/MailersSection.md)
 - [MailersSections](../docs/MailersSections.md)
 - [Map](../docs/Map.md)
 - [MapEntries](../docs/MapEntries.md)
 - [MapEntry](../docs/MapEntry.md)
 - [Maps](../docs/Maps.md)
 - [MapsEntriesIdBody](../docs/MapsEntriesIdBody.md)
 - [ModelGlobal](../docs/ModelGlobal.md)
 - [MonitorFail](../docs/MonitorFail.md)
 - [MonitorUri](../docs/MonitorUri.md)
 - [MysqlCheckParams](../docs/MysqlCheckParams.md)
 - [Nameserver](../docs/Nameserver.md)
 - [Nameservers](../docs/Nameservers.md)
 - [NativeStat](../docs/NativeStat.md)
 - [NativeStatStats](../docs/NativeStatStats.md)
 - [NativeStats](../docs/NativeStats.md)
 - [NativeStatsCollection](../docs/NativeStatsCollection.md)
 - [Originalto](../docs/Originalto.md)
 - [PeerEntries](../docs/PeerEntries.md)
 - [PeerEntry](../docs/PeerEntry.md)
 - [PeerSection](../docs/PeerSection.md)
 - [PeerSections](../docs/PeerSections.md)
 - [PersistRule](../docs/PersistRule.md)
 - [PgsqlCheckParams](../docs/PgsqlCheckParams.md)
 - [ProcessInfo](../docs/ProcessInfo.md)
 - [ProcessInfoItem](../docs/ProcessInfoItem.md)
 - [ProcessInfos](../docs/ProcessInfos.md)
 - [Program](../docs/Program.md)
 - [Programs](../docs/Programs.md)
 - [Redispatch](../docs/Redispatch.md)
 - [Reload](../docs/Reload.md)
 - [Reloads](../docs/Reloads.md)
 - [Resolver](../docs/Resolver.md)
 - [Resolvers](../docs/Resolvers.md)
 - [ReturnHeader](../docs/ReturnHeader.md)
 - [Ring](../docs/Ring.md)
 - [Rings](../docs/Rings.md)
 - [RuntimeAddServer](../docs/RuntimeAddServer.md)
 - [RuntimeServer](../docs/RuntimeServer.md)
 - [RuntimeServers](../docs/RuntimeServers.md)
 - [RuntimeStickTableEntriesBody](../docs/RuntimeStickTableEntriesBody.md)
 - [Sample](../docs/Sample.md)
 - [Server](../docs/Server.md)
 - [ServerParams](../docs/ServerParams.md)
 - [ServerSwitchingRule](../docs/ServerSwitchingRule.md)
 - [ServerSwitchingRules](../docs/ServerSwitchingRules.md)
 - [ServerTemplate](../docs/ServerTemplate.md)
 - [ServerTemplates](../docs/ServerTemplates.md)
 - [Servers](../docs/Servers.md)
 - [Site](../docs/Site.md)
 - [SiteFarms](../docs/SiteFarms.md)
 - [SiteService](../docs/SiteService.md)
 - [Sites](../docs/Sites.md)
 - [SmtpchkParams](../docs/SmtpchkParams.md)
 - [Source](../docs/Source.md)
 - [SpoeAgent](../docs/SpoeAgent.md)
 - [SpoeAgents](../docs/SpoeAgents.md)
 - [SpoeFiles](../docs/SpoeFiles.md)
 - [SpoeGroup](../docs/SpoeGroup.md)
 - [SpoeGroups](../docs/SpoeGroups.md)
 - [SpoeMessage](../docs/SpoeMessage.md)
 - [SpoeMessageEvent](../docs/SpoeMessageEvent.md)
 - [SpoeMessages](../docs/SpoeMessages.md)
 - [SpoeScope](../docs/SpoeScope.md)
 - [SpoeScopes](../docs/SpoeScopes.md)
 - [SpoeSpoeFilesBody](../docs/SpoeSpoeFilesBody.md)
 - [SpoeTransaction](../docs/SpoeTransaction.md)
 - [SpoeTransactions](../docs/SpoeTransactions.md)
 - [SslCertEntry](../docs/SslCertEntry.md)
 - [SslCertificate](../docs/SslCertificate.md)
 - [SslCertificates](../docs/SslCertificates.md)
 - [StatsAuth](../docs/StatsAuth.md)
 - [StatsHttpRequest](../docs/StatsHttpRequest.md)
 - [StatsOptions](../docs/StatsOptions.md)
 - [StickRule](../docs/StickRule.md)
 - [StickRules](../docs/StickRules.md)
 - [StickTable](../docs/StickTable.md)
 - [StickTableEntries](../docs/StickTableEntries.md)
 - [StickTableEntry](../docs/StickTableEntry.md)
 - [StickTableFields](../docs/StickTableFields.md)
 - [StickTables](../docs/StickTables.md)
 - [StorageGeneralBody](../docs/StorageGeneralBody.md)
 - [StorageMapsBody](../docs/StorageMapsBody.md)
 - [StorageSslCertificatesBody](../docs/StorageSslCertificatesBody.md)
 - [TcpCheck](../docs/TcpCheck.md)
 - [TcpChecks](../docs/TcpChecks.md)
 - [TcpRequestRule](../docs/TcpRequestRule.md)
 - [TcpRequestRules](../docs/TcpRequestRules.md)
 - [TcpResponseRule](../docs/TcpResponseRule.md)
 - [TcpResponseRules](../docs/TcpResponseRules.md)
 - [Transaction](../docs/Transaction.md)
 - [Transactions](../docs/Transactions.md)
 - [User](../docs/User.md)
 - [Userlist](../docs/Userlist.md)
 - [Userlists](../docs/Userlists.md)
 - [Users](../docs/Users.md)

## Documentation For Authorization


## basic_auth

- **Type**: HTTP basic authentication


## Author

bennassif@gmail.com
