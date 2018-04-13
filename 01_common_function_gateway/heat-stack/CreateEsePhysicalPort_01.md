# HTTP Methods for creating heat-stack: Physical port

Checking heat-stack of "ese_physical_port" via heatclient.
```
$ heat stack-show ese_physical_port_9451c9ca-289d-42ba-846d-359c448e910c
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                           |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                              |
| creation_time         | 2018-04-09T04:42:29Z                                                                                                                                                                            |
| description           | Physical port template                                                                                                                                                                          |
| disable_rollback      | True                                                                                                                                                                                            |
| id                    | 90f0d5d9-e55d-4f3f-9fcf-f94d5aceadbe                                                                                                                                                            |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/c583ce78843344adbe5fd20f13620274/stacks/ese_physical_port_9451c9ca-289d-42ba-846d-359c448e910c/90f0d5d9-e55d-4f3f-9fcf-f94d5aceadbe |
| notification_topics   | []                                                                                                                                                                                              |
| outputs               | [                                                                                                                                                                                               |
|                       |   {                                                                                                                                                                                             |
|                       |     "output_value": "78d717f0-66d9-4f82-afe6-833c5e8f38f5",                                                                                                                                     |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                      |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                        |
|                       |   },                                                                                                                                                                                            |
|                       |   {                                                                                                                                                                                             |
|                       |     "output_value": "06bfe521-07f0-4931-9f8c-318c3ad8114e",                                                                                                                                     |
|                       |     "description": "A unique id for the physical interface",                                                                                                                                    |
|                       |     "output_key": "id"                                                                                                                                                                          |
|                       |   },                                                                                                                                                                                            |
|                       |   {                                                                                                                                                                                             |
|                       |     "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/78d717f0-66d9-4f82-afe6-833c5e8f38f5",                                                            |
|                       |     "description": "Monitoring Process Link",                                                                                                                                                   |
|                       |     "output_key": "monitoring_link"                                                                                                                                                             |
|                       |   },                                                                                                                                                                                            |
|                       |   {                                                                                                                                                                                             |
|                       |     "output_value": "xe-0/0/38",                                                                                                                                                                |
|                       |     "description": "The name of the physical interface.",                                                                                                                                       |
|                       |     "output_key": "name"                                                                                                                                                                        |
|                       |   }                                                                                                                                                                                             |
|                       | ]                                                                                                                                                                                               |
| parameters            | {                                                                                                                                                                                               |
|                       |   "physical_port_name": "xe-0/0/3",                                                                                                                                                             |
|                       |   "OS::stack_id": "90f0d5d9-e55d-4f3f-9fcf-f94d5aceadbe",                                                                                                                                       |
|                       |   "OS::stack_name": "ese_physical_port_9451c9ca-289d-42ba-846d-359c448e910c",                                                                                                                   |
|                       |   "tenant_id": "c583ce78843344adbe5fd20f13620274",                                                                                                                                              |
|                       |   "device_ip": "10.161.0.34",                                                                                                                                                                   |
|                       |   "physical_device": "7e5c78fa-71c0-427e-947f-586b1fc3c470",                                                                                                                                    |
|                       |   "version": "1",                                                                                                                                                                               |
|                       |   "gohan_id": "9451c9ca-289d-42ba-846d-359c448e910c"                                                                                                                                            |
|                       | }                                                                                                                                                                                               |
| parent                | None                                                                                                                                                                                            |
| stack_name            | ese_physical_port_9451c9ca-289d-42ba-846d-359c448e910c                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                           |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                                 |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                             |
| stack_user_project_id | c583ce78843344adbe5fd20f13620274                                                                                                                                                                |
| template_description  | Physical port template                                                                                                                                                                          |
| timeout_mins          | 6                                                                                                                                                                                               |
| updated_time          | None                                                                                                                                                                                            |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "ese_physical_port" via heatclient.
```
$ heat template-show ese_physical_port_9451c9ca-289d-42ba-846d-359c448e910c
description: 'Physical port template

  '
heat_template_version: '2013-05-23'
outputs:
  id:
    description: A unique id for the physical interface
    value: {get_resource: physical_interface}
  monitoring_link:
    description: Monitoring Process Link
    value:
      get_attr: [interface_monitor, link]
  monitoring_target_id:
    description: Monitoring Target ID
    value: {get_resource: interface_monitor}
  name:
    description: The name of the physical interface.
    value:
      get_attr: [physical_interface, name]
parameters:
  device_ip: {description: Device IP Address., label: Device IP Address, type: string}
  gohan_id: {description: UUID of the ESE Physical Port, label: Gohan resource ID,
    type: string}
  physical_device: {description: Id of the physical device on which physical port
      will be created., label: Physical Device Id, type: string}
  physical_port_name: {description: Name of the physical port., label: Physical Interface
      Name, type: string}
  tenant_id: {label: Tenant ID, type: string}
  version: {label: Config version, type: number}
resources:
  interface_monitor:
    depends_on: physical_interface
    properties:
      field_name: port
      properties:
        community_name: ESE_NODE_COMMUNITY
        device_ip: {get_param: device_ip}
        if_name: {get_param: physical_port_name}
      resource_id: {get_param: gohan_id}
      resource_type: ese_physical_ports
      syncer_properties:
        etcd:
          status: {key: port}
      tenant_id: {get_param: tenant_id}
      type: snmp_ports_status
      version: {get_param: version}
    type: ESI::Monitoring::MonitoringTarget
  physical_interface:
    properties:
      name: {get_param: physical_port_name}
      physical_router: {get_param: physical_device}
    type: OS::Contrail::PhysicalInterface
```
