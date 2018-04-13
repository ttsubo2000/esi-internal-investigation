# HTTP Methods for creating heat-stack: Logical port

Checking heat-stack of "ese_logical_port" via heatclient.
```
$ heat stack-show ese_logical_port_e8555ee6-529c-42d9-8bb1-bfbe217133b1
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                          |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                             |
| creation_time         | 2018-04-09T04:50:06Z                                                                                                                                                                           |
| description           | Logical port template                                                                                                                                                                          |
| disable_rollback      | True                                                                                                                                                                                           |
| id                    | 93209400-c90d-499f-a9db-b20cc38265be                                                                                                                                                           |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/c583ce78843344adbe5fd20f13620274/stacks/ese_logical_port_e8555ee6-529c-42d9-8bb1-bfbe217133b1/93209400-c90d-499f-a9db-b20cc38265be |
| notification_topics   | []                                                                                                                                                                                             |
| outputs               | [                                                                                                                                                                                              |
|                       |   {                                                                                                                                                                                            |
|                       |     "output_value": "7f066c44-1dc2-44b2-95f7-d59d70bd77fb",                                                                                                                                    |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                     |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                       |
|                       |   },                                                                                                                                                                                           |
|                       |   {                                                                                                                                                                                            |
|                       |     "output_value": "46b0cd68-d0fb-4d72-9def-830164f9e215",                                                                                                                                    |
|                       |     "description": "A unique id for the logical interface",                                                                                                                                    |
|                       |     "output_key": "id"                                                                                                                                                                         |
|                       |   },                                                                                                                                                                                           |
|                       |   {                                                                                                                                                                                            |
|                       |     "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/7f066c44-1dc2-44b2-95f7-d59d70bd77fb",                                                           |
|                       |     "description": "Monitoring Process Link",                                                                                                                                                  |
|                       |     "output_key": "monitoring_link"                                                                                                                                                            |
|                       |   },                                                                                                                                                                                           |
|                       |   {                                                                                                                                                                                            |
|                       |     "output_value": "xe-0/0/38.0",                                                                                                                                                             |
|                       |     "description": "The name of the logical interface.",                                                                                                                                       |
|                       |     "output_key": "name"                                                                                                                                                                       |
|                       |   }                                                                                                                                                                                            |
|                       | ]                                                                                                                                                                                              |
| parameters            | {                                                                                                                                                                                              |
|                       |   "logical_port_type": "L2",                                                                                                                                                                   |
|                       |   "logical_port_vlan_id": "1025",                                                                                                                                                              |
|                       |   "OS::stack_name": "ese_logical_port_e8555ee6-529c-42d9-8bb1-bfbe217133b1",                                                                                                                   |
|                       |   "virtual_machine_interface_ids": "f68d0924-ef20-4c1b-ac45-0e6b879af5e7",                                                                                                                     |
|                       |   "device_ip": "10.161.0.34",                                                                                                                                                                  |
|                       |   "OS::stack_id": "93209400-c90d-499f-a9db-b20cc38265be",                                                                                                                                      |
|                       |   "version": "1",                                                                                                                                                                              |
|                       |   "tenant_id": "c583ce78843344adbe5fd20f13620274",                                                                                                                                             |
|                       |   "logical_port_name": "xe-0/0/4.1025",                                                                                                                                                        |
|                       |   "gohan_id": "e8555ee6-529c-42d9-8bb1-bfbe217133b1",                                                                                                                                          |
|                       |   "physical_port_id": "06bfe521-07f0-4931-9f8c-318c3ad8114e"                                                                                                                                   |
|                       | }                                                                                                                                                                                              |
| parent                | None                                                                                                                                                                                           |
| stack_name            | ese_logical_port_e8555ee6-529c-42d9-8bb1-bfbe217133b1                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                          |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                                |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                            |
| stack_user_project_id | c583ce78843344adbe5fd20f13620274                                                                                                                                                               |
| template_description  | Logical port template                                                                                                                                                                          |
| timeout_mins          | 6                                                                                                                                                                                              |
| updated_time          | None                                                                                                                                                                                           |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "ese_logical_port" via heatclient.
```
$ heat template-show ese_logical_port_e8555ee6-529c-42d9-8bb1-bfbe217133b1
description: 'Logical port template

  '
heat_template_version: '2013-05-23'
outputs:
  id:
    description: A unique id for the logical interface
    value: {get_resource: logical_interface}
  monitoring_link:
    description: Monitoring Process Link
    value:
      get_attr: [interface_monitor, link]
  monitoring_target_id:
    description: Monitoring Target ID
    value: {get_resource: interface_monitor}
  name:
    description: The name of the logical interface.
    value:
      get_attr: [logical_interface, name]
parameters:
  device_ip: {description: Device IP Address., label: Device IP Address, type: string}
  gohan_id: {description: UUID of the ESE Physical Port, label: Gohan resource ID,
    type: string}
  logical_port_name: {description: Name of the logical port., label: Logical Port
      Name, type: string}
  logical_port_type: {description: Type of the logical port., label: Logical Port
      Type, type: string}
  logical_port_vlan_id: {default: 0, description: VLAN id to use for logical port
      creation., label: VLAN id for Logical Port, type: number}
  physical_port_id: {description: A unique id for the Physical Interface., label: Physical
      Interface ID, type: string}
  tenant_id: {label: Tenant ID, type: string}
  version: {label: Config version, type: number}
  virtual_machine_interface_ids: {description: Virtual Machine Interface ID., label: Virtual
      Machine Interface ID, type: comma_delimited_list}
resources:
  interface_monitor:
    depends_on: logical_interface
    properties:
      field_name: logical_port
      properties:
        community_name: ESE_NODE_COMMUNITY
        device_ip: {get_param: device_ip}
        if_name: {get_param: logical_port_name}
      resource_id: {get_param: gohan_id}
      resource_type: ese_logical_ports
      syncer_properties:
        etcd:
          status: {key: logical_port}
        tsdb:
          traffic.in:
            metric: traffic.bytes
            tags:
            - direction: in
              port_id: 343b0257-512e-40e3-b063-8cc13a4b61f4
              resource_id: {get_param: gohan_id}
          traffic.out:
            metric: traffic.bytes
            tags:
            - direction: out
              port_id: 343b0257-512e-40e3-b063-8cc13a4b61f4
              resource_id: {get_param: gohan_id}
      tenant_id: {get_param: tenant_id}
      type: snmp_ports
      version: {get_param: version}
    type: ESI::Monitoring::MonitoringTarget
  logical_interface:
    properties:
      name: {get_param: logical_port_name}
      physical_interface: {get_param: physical_port_id}
      type: {get_param: logical_port_type}
      virtual_machine_interfaces: {get_param: virtual_machine_interface_ids}
      vlan: {get_param: logical_port_vlan_id}
    type: OS::Contrail::LogicalInterface
```
