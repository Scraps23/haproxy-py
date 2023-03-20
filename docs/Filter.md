# Filter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** | Name of the fcgi-app section this filter will use. | [optional] 
**bandwidth_limit_name** | **str** | Filter name that will be used by &#x27;set-bandwidth-limit&#x27; actions to reference a specific bandwidth limitation filter | [optional] 
**cache_name** | **str** |  | [optional] 
**default_limit** | **int** | The max number of bytes that can be forwarded over the period. The value must be specified for per-stream and shared bandwidth limitation filters. It follows the HAProxy size format and is expressed in bytes. | [optional] 
**default_period** | **int** | The default time period used to evaluate the bandwidth limitation rate. It can be specified for per-stream bandwidth limitation filters only. It follows the HAProxy time format and is expressed in milliseconds. | [optional] 
**index** | **int** |  | 
**key** | **str** | A sample expression rule. It describes what elements will be analyzed, extracted, combined, and used to select which table entry to update the counters. It must be specified for shared bandwidth limitation filters only. | [optional] 
**limit** | **int** | The max number of bytes that can be forwarded over the period. The value must be specified for per-stream and shared bandwidth limitation filters. It follows the HAProxy size format and is expressed in bytes. | [optional] 
**min_size** | **int** | The optional minimum number of bytes forwarded at a time by a stream excluding the last packet that may be smaller. This value can be specified for per-stream and shared bandwidth limitation filters. It follows the HAProxy size format and is expressed in bytes. | [optional] 
**spoe_config** | **str** |  | [optional] 
**spoe_engine** | **str** |  | [optional] 
**table** | **str** | An optional table to be used instead of the default one, which is the stick-table declared in the current proxy. It can be specified for shared bandwidth limitation filters only. | [optional] 
**trace_hexdump** | **bool** |  | [optional] 
**trace_name** | **str** |  | [optional] 
**trace_rnd_forwarding** | **bool** |  | [optional] 
**trace_rnd_parsing** | **bool** |  | [optional] 
**type** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

