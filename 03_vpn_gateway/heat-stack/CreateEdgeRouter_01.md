# HTTP Methods for creating heat-stack: Edge router

Checking heat-stack of "edge_router" via heatclient.
```
$ heat stack-show edge_router_7a35974a-a19f-49e2-b907-ad7fd8692975
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                     |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                        |
| creation_time         | 2018-04-16T00:02:42Z                                                                                                                                                                      |
| description           | Physical port template                                                                                                                                                                    |
| disable_rollback      | True                                                                                                                                                                                      |
| id                    | d1412d29-2acb-4105-95e4-9b55346b58ec                                                                                                                                                      |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/b3e3095c0a5b4383805efe9cf2a6b5ef/stacks/edge_router_7a35974a-a19f-49e2-b907-ad7fd8692975/d1412d29-2acb-4105-95e4-9b55346b58ec |
| notification_topics   | []                                                                                                                                                                                        |
| outputs               | [                                                                                                                                                                                         |
|                       |   {                                                                                                                                                                                       |
|                       |     "output_value": "cc896303-29e2-47d6-a409-a84c23b5722b",                                                                                                                               |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                  |
|                       |   },                                                                                                                                                                                      |
|                       |   {                                                                                                                                                                                       |
|                       |     "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/cc896303-29e2-47d6-a409-a84c23b5722b",                                                      |
|                       |     "description": "Monitoring Process Link",                                                                                                                                             |
|                       |     "output_key": "monitoring_link"                                                                                                                                                       |
|                       |   }                                                                                                                                                                                       |
|                       | ]                                                                                                                                                                                         |
| parameters            | {                                                                                                                                                                                         |
|                       |   "OS::stack_id": "d1412d29-2acb-4105-95e4-9b55346b58ec",                                                                                                                                 |
|                       |   "OS::stack_name": "edge_router_7a35974a-a19f-49e2-b907-ad7fd8692975",                                                                                                                   |
|                       |   "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",                                                                                                                                        |
|                       |   "device_ip": "10.79.5.185",                                                                                                                                                             |
|                       |   "version": "1",                                                                                                                                                                         |
|                       |   "gohan_id": "7a35974a-a19f-49e2-b907-ad7fd8692975"                                                                                                                                      |
|                       | }                                                                                                                                                                                         |
| parent                | None                                                                                                                                                                                      |
| stack_name            | edge_router_7a35974a-a19f-49e2-b907-ad7fd8692975                                                                                                                                          |
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
$ heat template-show edge_router_7a35974a-a19f-49e2-b907-ad7fd8692975
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
