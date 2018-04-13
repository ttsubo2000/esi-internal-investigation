# HTTP Methods for creating heat-stack: Er physical interface

Checking heat-stack of "er_physical_interface" via heatclient.
```
$ heat stack-show er_physical_interface_b9c7c1f4-1b90-4a7a-8161-34276bb2ed10
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                               |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                                  |
| creation_time         | 2018-04-09T04:47:49Z                                                                                                                                                                                |
| description           | Physical port template                                                                                                                                                                              |
| disable_rollback      | True                                                                                                                                                                                                |
| id                    | 6aa1108c-bb2d-4a0f-a7e0-835e3581ed20                                                                                                                                                                |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/c583ce78843344adbe5fd20f13620274/stacks/er_physical_interface_b9c7c1f4-1b90-4a7a-8161-34276bb2ed10/6aa1108c-bb2d-4a0f-a7e0-835e3581ed20 |
| notification_topics   | []                                                                                                                                                                                                  |
| outputs               | [                                                                                                                                                                                                   |
|                       |   {                                                                                                                                                                                                 |
|                       |     "output_value": "17d442df-0ac4-4c5e-bbef-34fc7e4c4b06",                                                                                                                                         |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                          |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                            |
|                       |   },                                                                                                                                                                                                |
|                       |   {                                                                                                                                                                                                 |
|                       |     "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/17d442df-0ac4-4c5e-bbef-34fc7e4c4b06",                                                                |
|                       |     "description": "Monitoring Process Link",                                                                                                                                                       |
|                       |     "output_key": "monitoring_link"                                                                                                                                                                 |
|                       |   }                                                                                                                                                                                                 |
|                       | ]                                                                                                                                                                                                   |
| parameters            | {                                                                                                                                                                                                   |
|                       |   "OS::stack_id": "6aa1108c-bb2d-4a0f-a7e0-835e3581ed20",                                                                                                                                           |
|                       |   "OS::stack_name": "er_physical_interface_b9c7c1f4-1b90-4a7a-8161-34276bb2ed10",                                                                                                                   |
|                       |   "tenant_id": "c583ce78843344adbe5fd20f13620274",                                                                                                                                                  |
|                       |   "device_ip": "10.79.5.184",                                                                                                                                                                       |
|                       |   "if_name": "ae0",                                                                                                                                                                                 |
|                       |   "version": "1",                                                                                                                                                                                   |
|                       |   "gohan_id": "b9c7c1f4-1b90-4a7a-8161-34276bb2ed10"                                                                                                                                                |
|                       | }                                                                                                                                                                                                   |
| parent                | None                                                                                                                                                                                                |
| stack_name            | er_physical_interface_b9c7c1f4-1b90-4a7a-8161-34276bb2ed10                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                               |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                                     |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                                 |
| stack_user_project_id | c583ce78843344adbe5fd20f13620274                                                                                                                                                                    |
| template_description  | Physical port template                                                                                                                                                                              |
| timeout_mins          | 3                                                                                                                                                                                                   |
| updated_time          | None                                                                                                                                                                                                |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "er_physical_interface" via heatclient.
```
$ heat template-show er_physical_interface_b9c7c1f4-1b90-4a7a-8161-34276bb2ed10
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
