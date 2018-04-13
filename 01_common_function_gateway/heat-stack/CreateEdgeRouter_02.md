# HTTP Methods for creating heat-stack: Edge router

Checking heat-stack of "edge_router" via heatclient.
```
$ heat stack-show edge_router_2d056865-47a9-45cf-a890-ed10e3b5912a
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                     |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                        |
| creation_time         | 2018-04-09T04:45:39Z                                                                                                                                                                      |
| description           | Physical port template                                                                                                                                                                    |
| disable_rollback      | True                                                                                                                                                                                      |
| id                    | 36e9b437-d8f6-412d-85c5-f8c913379c2c                                                                                                                                                      |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/c583ce78843344adbe5fd20f13620274/stacks/edge_router_2d056865-47a9-45cf-a890-ed10e3b5912a/36e9b437-d8f6-412d-85c5-f8c913379c2c |
| notification_topics   | []                                                                                                                                                                                        |
| outputs               | [                                                                                                                                                                                         |
|                       |   {                                                                                                                                                                                       |
|                       |     "output_value": "ad464fbb-0810-447e-b10d-31715221cb95",                                                                                                                               |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                  |
|                       |   },                                                                                                                                                                                      |
|                       |   {                                                                                                                                                                                       |
|                       |     "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/ad464fbb-0810-447e-b10d-31715221cb95",                                                      |
|                       |     "description": "Monitoring Process Link",                                                                                                                                             |
|                       |     "output_key": "monitoring_link"                                                                                                                                                       |
|                       |   }                                                                                                                                                                                       |
|                       | ]                                                                                                                                                                                         |
| parameters            | {                                                                                                                                                                                         |
|                       |   "OS::stack_id": "36e9b437-d8f6-412d-85c5-f8c913379c2c",                                                                                                                                 |
|                       |   "OS::stack_name": "edge_router_2d056865-47a9-45cf-a890-ed10e3b5912a",                                                                                                                   |
|                       |   "tenant_id": "c583ce78843344adbe5fd20f13620274",                                                                                                                                        |
|                       |   "device_ip": "10.79.5.184",                                                                                                                                                             |
|                       |   "version": "1",                                                                                                                                                                         |
|                       |   "gohan_id": "2d056865-47a9-45cf-a890-ed10e3b5912a"                                                                                                                                      |
|                       | }                                                                                                                                                                                         |
| parent                | None                                                                                                                                                                                      |
| stack_name            | edge_router_2d056865-47a9-45cf-a890-ed10e3b5912a                                                                                                                                          |
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
$ heat template-show edge_router_2d056865-47a9-45cf-a890-ed10e3b5912a
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
