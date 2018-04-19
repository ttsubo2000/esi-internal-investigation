# HTTP Methods for creating heat-stack: Er physical interface

Checking heat-stack of "er_physical_interface" via heatclient.
```
$ heat stack-show er_physical_interface_2bc8e40d-ab01-4738-a4aa-e69d8fd30688
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                               |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                                  |
| creation_time         | 2018-04-16T00:08:02Z                                                                                                                                                                                |
| description           | Physical port template                                                                                                                                                                              |
| disable_rollback      | True                                                                                                                                                                                                |
| id                    | 868bb9da-99b7-4030-91bc-1fc94821b0f5                                                                                                                                                                |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/b3e3095c0a5b4383805efe9cf2a6b5ef/stacks/er_physical_interface_2bc8e40d-ab01-4738-a4aa-e69d8fd30688/868bb9da-99b7-4030-91bc-1fc94821b0f5 |
| notification_topics   | []                                                                                                                                                                                                  |
| outputs               | [                                                                                                                                                                                                   |
|                       |   {                                                                                                                                                                                                 |
|                       |     "output_value": "d80c91c1-a82c-4742-b571-03c17cbeff1c",                                                                                                                                         |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                          |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                            |
|                       |   },                                                                                                                                                                                                |
|                       |   {                                                                                                                                                                                                 |
|                       |     "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/d80c91c1-a82c-4742-b571-03c17cbeff1c",                                                                |
|                       |     "description": "Monitoring Process Link",                                                                                                                                                       |
|                       |     "output_key": "monitoring_link"                                                                                                                                                                 |
|                       |   }                                                                                                                                                                                                 |
|                       | ]                                                                                                                                                                                                   |
| parameters            | {                                                                                                                                                                                                   |
|                       |   "OS::stack_id": "868bb9da-99b7-4030-91bc-1fc94821b0f5",                                                                                                                                           |
|                       |   "OS::stack_name": "er_physical_interface_2bc8e40d-ab01-4738-a4aa-e69d8fd30688",                                                                                                                   |
|                       |   "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",                                                                                                                                                  |
|                       |   "device_ip": "10.79.5.184",                                                                                                                                                                       |
|                       |   "if_name": "ge-0/0/1",                                                                                                                                                                            |
|                       |   "version": "1",                                                                                                                                                                                   |
|                       |   "gohan_id": "2bc8e40d-ab01-4738-a4aa-e69d8fd30688"                                                                                                                                                |
|                       | }                                                                                                                                                                                                   |
| parent                | None                                                                                                                                                                                                |
| stack_name            | er_physical_interface_2bc8e40d-ab01-4738-a4aa-e69d8fd30688                                                                                                                                          |
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
$ heat template-show er_physical_interface_2bc8e40d-ab01-4738-a4aa-e69d8fd30688
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
