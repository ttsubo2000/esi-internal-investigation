# HTTP Methods for creating heat-stack: Er physical interface

Checking heat-stack of "er_physical_interface" via heatclient.
```
$ heat stack-show er_physical_interface_53712736-354c-4374-be82-6f07bea9d1bd
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                               |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                                  |
| creation_time         | 2018-04-04T04:57:55Z                                                                                                                                                                                |
| description           | Physical port template                                                                                                                                                                              |
| disable_rollback      | True                                                                                                                                                                                                |
| id                    | e0413e79-cb55-484a-822d-f360397a320d                                                                                                                                                                |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/06d6b792b31c40daa546fb0f4e35980d/stacks/er_physical_interface_53712736-354c-4374-be82-6f07bea9d1bd/e0413e79-cb55-484a-822d-f360397a320d |
| notification_topics   | []                                                                                                                                                                                                  |
| outputs               | [                                                                                                                                                                                                   |
|                       |   {                                                                                                                                                                                                 |
|                       |     "output_value": "c38b03bf-0c61-44ff-9dec-599c9951df58",                                                                                                                                         |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                          |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                            |
|                       |   },                                                                                                                                                                                                |
|                       |   {                                                                                                                                                                                                 |
|                       |     "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/c38b03bf-0c61-44ff-9dec-599c9951df58",                                                                |
|                       |     "description": "Monitoring Process Link",                                                                                                                                                       |
|                       |     "output_key": "monitoring_link"                                                                                                                                                                 |
|                       |   }                                                                                                                                                                                                 |
|                       | ]                                                                                                                                                                                                   |
| parameters            | {                                                                                                                                                                                                   |
|                       |   "OS::stack_id": "e0413e79-cb55-484a-822d-f360397a320d",                                                                                                                                           |
|                       |   "OS::stack_name": "er_physical_interface_53712736-354c-4374-be82-6f07bea9d1bd",                                                                                                                   |
|                       |   "tenant_id": "06d6b792b31c40daa546fb0f4e35980d",                                                                                                                                                  |
|                       |   "device_ip": "10.79.5.185",                                                                                                                                                                       |
|                       |   "if_name": "ae0",                                                                                                                                                                                 |
|                       |   "version": "1",                                                                                                                                                                                   |
|                       |   "gohan_id": "53712736-354c-4374-be82-6f07bea9d1bd"                                                                                                                                                |
|                       | }                                                                                                                                                                                                   |
| parent                | None                                                                                                                                                                                                |
| stack_name            | er_physical_interface_53712736-354c-4374-be82-6f07bea9d1bd                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                               |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                                     |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                                 |
| stack_user_project_id | 06d6b792b31c40daa546fb0f4e35980d                                                                                                                                                                    |
| template_description  | Physical port template                                                                                                                                                                              |
| timeout_mins          | 3                                                                                                                                                                                                   |
| updated_time          | None                                                                                                                                                                                                |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "er_physical_interface" via heatclient.
```
$ heat template-show er_physical_interface_53712736-354c-4374-be82-6f07bea9d1bd
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
