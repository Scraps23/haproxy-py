# AwsRegion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | AWS Access Key ID. | [optional] 
**allowlist** | [**list[AwsFilters]**](AwsFilters.md) | Specify the AWS filters used to filter the EC2 instances to add | [optional] 
**denylist** | [**list[AwsFilters]**](AwsFilters.md) | Specify the AWS filters used to filter the EC2 instances to ignore | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | 
**id** | **str** | Auto generated ID. | [optional] 
**ipv4_address** | **str** | Select which IPv4 address the Service Discovery has to use for the backend server entry | 
**name** | **str** |  | 
**region** | **str** |  | 
**retry_timeout** | **int** | Duration in seconds in-between data pulling requests to the AWS region | 
**secret_access_key** | **str** | AWS Secret Access Key. | [optional] 
**server_slots_base** | **int** |  | [optional] [default to 10]
**server_slots_growth_increment** | **int** |  | [optional] 
**server_slots_growth_type** | **str** |  | [optional] [default to 'exponential']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

