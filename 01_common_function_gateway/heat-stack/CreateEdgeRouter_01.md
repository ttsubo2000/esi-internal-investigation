# HTTP Methods for creating heat-stack: Edge router

Checking heat-stack of "edge_router" via heatclient.
```
$ heat stack-show edge_router_f4f54175-93fe-406b-ae66-dbca4df99e03
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                     |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                        |
| creation_time         | 2018-04-09T04:44:35Z                                                                                                                                                                      |
| description           | Physical port template                                                                                                                                                                    |
| disable_rollback      | True                                                                                                                                                                                      |
| id                    | 521c324d-4685-43c7-9e51-a7153e188aae                                                                                                                                                      |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/c583ce78843344adbe5fd20f13620274/stacks/edge_router_f4f54175-93fe-406b-ae66-dbca4df99e03/521c324d-4685-43c7-9e51-a7153e188aae |
| notification_topics   | []                                                                                                                                                                                        |
| outputs               | [                                                                                                                                                                                         |
|                       |   {                                                                                                                                                                                       |
|                       |     "output_value": "b88cbb53-f850-44f2-9960-95ade457e46c",                                                                                                                               |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                  |
|                       |   },                                                                                                                                                                                      |
|                       |   {                                                                                                                                                                                       |
|                       |     "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/b88cbb53-f850-44f2-9960-95ade457e46c",                                                      |
|                       |     "description": "Monitoring Process Link",                                                                                                                                             |
|                       |     "output_key": "monitoring_link"                                                                                                                                                       |
|                       |   }                                                                                                                                                                                       |
|                       | ]                                                                                                                                                                                         |
| parameters            | {                                                                                                                                                                                         |
|                       |   "OS::stack_id": "521c324d-4685-43c7-9e51-a7153e188aae",                                                                                                                                 |
|                       |   "OS::stack_name": "edge_router_f4f54175-93fe-406b-ae66-dbca4df99e03",                                                                                                                   |
|                       |   "tenant_id": "c583ce78843344adbe5fd20f13620274",                                                                                                                                        |
|                       |   "device_ip": "10.79.5.185",                                                                                                                                                             |
|                       |   "version": "1",                                                                                                                                                                         |
|                       |   "gohan_id": "f4f54175-93fe-406b-ae66-dbca4df99e03"                                                                                                                                      |
|                       | }                                                                                                                                                                                         |
| parent                | None                                                                                                                                                                                      |
| stack_name            | edge_router_f4f54175-93fe-406b-ae66-dbca4df99e03                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                     |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                           |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                       |
| stack_user_project_id | c583ce78843344adbe5fd20f13620274                                                                                                                                                          |
| template_description  | Physical port template                                                                                                                                                                    |
| timeout_mins          | 3                                                                                                                                                                                         |
| updated_time          | None                                                                                                                                                                                      |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "edge_router" via heatclient.
```
$ heat template-show edge_router_f4f54175-93fe-406b-ae66-dbca4df99e03
description: 'Physical port template

  '
heat_template_version: '2013-05-23'
outputs:
  monitoring_link:
    description: Monitoring Process Link
    value:
      get_attr: [device_monitor, link]
  monitoring_target_id:
    description: Monitoring Target ID
    value: {get_resource: device_monitor}
parameters:
  device_ip: {description: Device IP Address, label: Device IP Address, type: string}
  gohan_id: {description: UUID of the Edge Router, label: Gohan resource ID, type: string}
  tenant_id: {label: Tenant ID, type: string}
  version: {label: Config version, type: number}
resources:
  device_monitor:
    properties:
      field_name: router
      properties:
        community_name: EDGE_ROUTER_COMMUNITY
        device_ip: {get_param: device_ip}
      resource_id: {get_param: gohan_id}
      resource_type: edge_routers
      syncer_properties:
        etcd:
          status: {key: router}
      tenant_id: {get_param: tenant_id}
      type: snmp_device
      version: {get_param: version}
    type: ESI::Monitoring::MonitoringTarget
```
