# HTTP Methods for creating heat-stack: Er physical interface

Checking heat-stack of "er_physical_interface" via heatclient.
```
$ heat stack-show er_physical_interface_3118d6be-b1cb-472a-805f-7e1ec46aa5e7
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                               |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                                  |
| creation_time         | 2018-04-16T00:05:57Z                                                                                                                                                                                |
| description           | Physical port template                                                                                                                                                                              |
| disable_rollback      | True                                                                                                                                                                                                |
| id                    | 241287b8-c304-460c-9568-ac6ea69bf333                                                                                                                                                                |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/b3e3095c0a5b4383805efe9cf2a6b5ef/stacks/er_physical_interface_3118d6be-b1cb-472a-805f-7e1ec46aa5e7/241287b8-c304-460c-9568-ac6ea69bf333 |
| notification_topics   | []                                                                                                                                                                                                  |
| outputs               | [                                                                                                                                                                                                   |
|                       |   {                                                                                                                                                                                                 |
|                       |     "output_value": "e848bb97-1643-4167-9865-9a8b3b30b66f",                                                                                                                                         |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                          |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                            |
|                       |   },                                                                                                                                                                                                |
|                       |   {                                                                                                                                                                                                 |
|                       |     "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/e848bb97-1643-4167-9865-9a8b3b30b66f",                                                                |
|                       |     "description": "Monitoring Process Link",                                                                                                                                                       |
|                       |     "output_key": "monitoring_link"                                                                                                                                                                 |
|                       |   }                                                                                                                                                                                                 |
|                       | ]                                                                                                                                                                                                   |
| parameters            | {                                                                                                                                                                                                   |
|                       |   "OS::stack_id": "241287b8-c304-460c-9568-ac6ea69bf333",                                                                                                                                           |
|                       |   "OS::stack_name": "er_physical_interface_3118d6be-b1cb-472a-805f-7e1ec46aa5e7",                                                                                                                   |
|                       |   "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",                                                                                                                                                  |
|                       |   "device_ip": "10.79.5.185",                                                                                                                                                                       |
|                       |   "if_name": "ae0",                                                                                                                                                                                 |
|                       |   "version": "1",                                                                                                                                                                                   |
|                       |   "gohan_id": "3118d6be-b1cb-472a-805f-7e1ec46aa5e7"                                                                                                                                                |
|                       | }                                                                                                                                                                                                   |
| parent                | None                                                                                                                                                                                                |
| stack_name            | er_physical_interface_3118d6be-b1cb-472a-805f-7e1ec46aa5e7                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                               |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                                     |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                                 |
| stack_user_project_id | b3e3095c0a5b4383805efe9cf2a6b5ef                                                                                                                                                                    |
| template_description  | Physical port template                                                                                                                                                                              |
| timeout_mins          | 3                                                                                                                                                                                                   |
| updated_time          | None                                                                                                                                                                                                |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "er_physical_interface" via heatclient.
```
$ heat template-show er_physical_interface_3118d6be-b1cb-472a-805f-7e1ec46aa5e7
description: 'Physical port template

  '
heat_template_version: '2013-05-23'
outputs:
  monitoring_link:
    description: Monitoring Process Link
    value:
      get_attr: [interface_monitor, link]
  monitoring_target_id:
    description: Monitoring Target ID
    value: {get_resource: interface_monitor}
parameters:
  device_ip: {description: Device IP Address, label: Device IP Address, type: string}
  gohan_id: {description: UUID of the ER Physical Interface, label: Gohan resource
      ID, type: string}
  if_name: {description: Name of the ER Physical Interface, label: Interface Name,
    type: string}
  tenant_id: {label: Tenant ID, type: string}
  version: {label: Config version, type: number}
resources:
  interface_monitor:
    properties:
      field_name: interface
      properties:
        community_name: EDGE_ROUTER_COMMUNITY
        device_ip: {get_param: device_ip}
        if_name: {get_param: if_name}
      resource_id: {get_param: gohan_id}
      resource_type: er_physical_interfaces
      syncer_properties:
        etcd:
          status: {key: interface}
      tenant_id: {get_param: tenant_id}
      type: snmp_ports_status
      version: {get_param: version}
    type: ESI::Monitoring::MonitoringTarget
```
