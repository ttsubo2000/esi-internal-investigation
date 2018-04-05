# HTTP Methods for creating heat-stack: Edge router

Checking heat-stack of "edge_router" via heatclient.
```
$ heat stack-show edge_router_cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                     |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                        |
| creation_time         | 2018-04-04T04:55:44Z                                                                                                                                                                      |
| description           | Physical port template                                                                                                                                                                    |
| disable_rollback      | True                                                                                                                                                                                      |
| id                    | 21d3a7cd-246e-4dfc-9922-795d8dbaf969                                                                                                                                                      |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/06d6b792b31c40daa546fb0f4e35980d/stacks/edge_router_cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78/21d3a7cd-246e-4dfc-9922-795d8dbaf969 |
| notification_topics   | []                                                                                                                                                                                        |
| outputs               | [                                                                                                                                                                                         |
|                       |   {                                                                                                                                                                                       |
|                       |     "output_value": "9363d0ec-e347-482c-8d0d-da1d8e11ad73",                                                                                                                               |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                  |
|                       |   },                                                                                                                                                                                      |
|                       |   {                                                                                                                                                                                       |
|                       |     "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/9363d0ec-e347-482c-8d0d-da1d8e11ad73",                                                      |
|                       |     "description": "Monitoring Process Link",                                                                                                                                             |
|                       |     "output_key": "monitoring_link"                                                                                                                                                       |
|                       |   }                                                                                                                                                                                       |
|                       | ]                                                                                                                                                                                         |
| parameters            | {                                                                                                                                                                                         |
|                       |   "OS::stack_id": "21d3a7cd-246e-4dfc-9922-795d8dbaf969",                                                                                                                                 |
|                       |   "OS::stack_name": "edge_router_cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78",                                                                                                                   |
|                       |   "tenant_id": "06d6b792b31c40daa546fb0f4e35980d",                                                                                                                                        |
|                       |   "device_ip": "10.79.5.185",                                                                                                                                                             |
|                       |   "version": "1",                                                                                                                                                                         |
|                       |   "gohan_id": "cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78"                                                                                                                                      |
|                       | }                                                                                                                                                                                         |
| parent                | None                                                                                                                                                                                      |
| stack_name            | edge_router_cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                     |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                           |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                       |
| stack_user_project_id | 06d6b792b31c40daa546fb0f4e35980d                                                                                                                                                          |
| template_description  | Physical port template                                                                                                                                                                    |
| timeout_mins          | 3                                                                                                                                                                                         |
| updated_time          | None                                                                                                                                                                                      |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "edge_router" via heatclient.
```
$ heat template-show edge_router_cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78
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
