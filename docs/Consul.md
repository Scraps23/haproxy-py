# Consul

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | 
**id** | **str** | Auto generated ID. | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**port** | **int** |  | 
**retry_timeout** | **int** | Duration in seconds in-between data pulling requests to the consul server | 
**server_slots_base** | **int** |  | [optional] [default to 10]
**server_slots_growth_increment** | **int** |  | [optional] 
**server_slots_growth_type** | **str** |  | [optional] [default to 'exponential']
**service_blacklist** | **list[str]** | deprecated, use service_denylist | [optional] 
**service_whitelist** | **list[str]** | deprecated, use service_allowlist | [optional] 
**service_allowlist** | **list[str]** |  | [optional] 
**service_denylist** | **list[str]** |  | [optional] 
**token** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

