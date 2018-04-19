# HTTP Methods for creating heat-stack: Edge router

Checking heat-stack of "edge_router" via heatclient.
```
$ heat stack-show edge_router_b7e6d8ad-5377-4380-bbb4-1a62566cbd6d
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                     |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                        |
| creation_time         | 2018-04-16T00:03:46Z                                                                                                                                                                      |
| description           | Physical port template                                                                                                                                                                    |
| disable_rollback      | True                                                                                                                                                                                      |
| id                    | 0d503769-c7ea-4a39-af3d-ed1e2a5c4798                                                                                                                                                      |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/b3e3095c0a5b4383805efe9cf2a6b5ef/stacks/edge_router_b7e6d8ad-5377-4380-bbb4-1a62566cbd6d/0d503769-c7ea-4a39-af3d-ed1e2a5c4798 |
| notification_topics   | []                                                                                                                                                                                        |
| outputs               | [                                                                                                                                                                                         |
|                       |   {                                                                                                                                                                                       |
|                       |     "output_value": "1e628441-c77a-4ebe-b5fe-6bd69816456d",                                                                                                                               |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                  |
|                       |   },                                                                                                                                                                                      |
|                       |   {                                                                                                                                                                                       |
|                       |     "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/1e628441-c77a-4ebe-b5fe-6bd69816456d",                                                      |
|                       |     "description": "Monitoring Process Link",                                                                                                                                             |
|                       |     "output_key": "monitoring_link"                                                                                                                                                       |
|                       |   }                                                                                                                                                                                       |
|                       | ]                                                                                                                                                                                         |
| parameters            | {                                                                                                                                                                                         |
|                       |   "OS::stack_id": "0d503769-c7ea-4a39-af3d-ed1e2a5c4798",                                                                                                                                 |
|                       |   "OS::stack_name": "edge_router_b7e6d8ad-5377-4380-bbb4-1a62566cbd6d",                                                                                                                   |
|                       |   "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",                                                                                                                                        |
|                       |   "device_ip": "10.79.5.184",                                                                                                                                                             |
|                       |   "version": "1",                                                                                                                                                                         |
|                       |   "gohan_id": "b7e6d8ad-5377-4380-bbb4-1a62566cbd6d"                                                                                                                                      |
|                       | }                                                                                                                                                                                         |
| parent                | None                                                                                                                                                                                      |
| stack_name            | edge_router_b7e6d8ad-5377-4380-bbb4-1a62566cbd6d                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                     |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                           |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                       |
| stack_user_project_id | b3e3095c0a5b4383805efe9cf2a6b5ef                                                                                                                                                          |
| template_description  | Physical port template                                                                                                                                                                    |
| timeout_mins          | 3                                                                                                                                                                                         |
| updated_time          | None                                                                                                                                                                                      |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "edge_router" via heatclient.
```
$ heat template-show edge_router_b7e6d8ad-5377-4380-bbb4-1a62566cbd6d
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
