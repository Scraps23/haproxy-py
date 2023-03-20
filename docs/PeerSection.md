# PeerSection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_bind** | [**DefaultBind**](DefaultBind.md) |  | [optional] 
**default_server** | [**DefaultServer**](DefaultServer.md) |  | [optional] 
**disabled** | **bool** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**name** | **str** |  | 
**shards** | **int** | In some configurations, one would like to distribute the stick-table contents to some peers in place of sending all the stick-table contents to each peer declared in the \&quot;peers\&quot; section. In such cases, \&quot;shards\&quot; specifies the number of peer involved in this stick-table contents distribution. | [optional] 
**stick_table** | [**ConfigStickTable**](ConfigStickTable.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

