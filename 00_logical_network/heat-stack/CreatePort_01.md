# HTTP Methods for creating heat-stack: Logical port

Checking heat-stack of "ese_logical_port" via heatclient.
```
$ heat stack-show ese_logical_port_ced1435d-6dfa-4dab-bb7c-19da4d8e48b7
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                          |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                             |
| creation_time         | 2018-02-15T06:55:21Z                                                                                                                                                                           |
| description           | Logical port template                                                                                                                                                                          |
| disable_rollback      | True                                                                                                                                                                                           |
| id                    | d3aa6aec-08f6-47ab-91ab-0512a1955f7e                                                                                                                                                           |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/ae69b52f46ba480bb9636f62736436f4/stacks/ese_logical_port_ced1435d-6dfa-4dab-bb7c-19da4d8e48b7/d3aa6aec-08f6-47ab-91ab-0512a1955f7e |
| notification_topics   | []                                                                                                                                                                                             |
| outputs               | [                                                                                                                                                                                              |
|                       |   {                                                                                                                                                                                            |
|                       |     "output_value": "9dcbbbbc-e9ea-4276-ba65-68ce8737e568",                                                                                                                                    |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                     |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                       |
|                       |   },                                                                                                                                                                                           |
|                       |   {                                                                                                                                                                                            |
|                       |     "output_value": "46b0cd68-d0fb-4d72-9def-830164f9e215",                                                                                                                                    |
|                       |     "description": "A unique id for the logical interface",                                                                                                                                    |
|                       |     "output_key": "id"                                                                                                                                                                         |
|                       |   },                                                                                                                                                                                           |
|                       |   {                                                                                                                                                                                            |
|                       |     "output_value": "http://collector-agents-se:7070/targets/9dcbbbbc-e9ea-4276-ba65-68ce8737e568",                                                                                            |
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
|                       |   "logical_port_vlan_id": "1003",                                                                                                                                                              |
|                       |   "OS::stack_name": "ese_logical_port_ced1435d-6dfa-4dab-bb7c-19da4d8e48b7",                                                                                                                   |
|                       |   "virtual_machine_interface_ids": "f68d0924-ef20-4c1b-ac45-0e6b879af5e7",                                                                                                                     |
|                       |   "device_ip": "10.161.0.33",                                                                                                                                                                  |
|                       |   "OS::stack_id": "d3aa6aec-08f6-47ab-91ab-0512a1955f7e",                                                                                                                                      |
|                       |   "version": "1",                                                                                                                                                                              |
|                       |   "tenant_id": "ae69b52f46ba480bb9636f62736436f4",                                                                                                                                             |
|                       |   "logical_port_name": "xe-0/0/1.1003",                                                                                                                                                        |
|                       |   "gohan_id": "ced1435d-6dfa-4dab-bb7c-19da4d8e48b7",                                                                                                                                          |
|                       |   "physical_port_id": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457"                                                                                                                                   |
|                       | }                                                                                                                                                                                              |
| parent                | None                                                                                                                                                                                           |
| stack_name            | ese_logical_port_ced1435d-6dfa-4dab-bb7c-19da4d8e48b7                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                          |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                                |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                            |
| stack_user_project_id | ae69b52f46ba480bb9636f62736436f4                                                                                                                                                               |
| template_description  | Logical port template                                                                                                                                                                          |
| timeout_mins          | 6                                                                                                                                                                                              |
| updated_time          | None                                                                                                                                                                                           |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "ese_logical_port" via heatclient.
```
$ heat template-show ese_logical_port_ced1435d-6dfa-4dab-bb7c-19da4d8e48b7
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
              port_id: fde61b02-9615-4e75-aac0-30a333657c1b
              resource_id: {get_param: gohan_id}
          traffic.out:
            metric: traffic.bytes
            tags:
            - direction: out
              port_id: fde61b02-9615-4e75-aac0-30a333657c1b
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
