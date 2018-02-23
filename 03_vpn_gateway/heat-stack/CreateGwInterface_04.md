# HTTP Methods for creating heat-stack: Logical port

Checking heat-stack of "ese_logical_port" via heatclient.
```
$ heat stack-show ese_logical_port_ecb4c4ac-3ebc-4045-a27c-52fecc93bac5
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                             |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                |
| creation_time         | 2017-05-11T05:02:43Z                                                                                                                                              |
| description           | Logical port template                                                                                                                                             |
| disable_rollback      | True                                                                                                                                                              |
| id                    | 356486d9-72dd-4d6e-80c8-e252926c957d                                                                                                                              |
| links                 | http://heat-api:8004/v1/0b576f6f4cbf414f829cd12f008bf08f/stacks/ese_logical_port_ecb4c4ac-3ebc-4045-a27c-52fecc93bac5/356486d9-72dd-4d6e-80c8-e252926c957d (self) |
| notification_topics   | []                                                                                                                                                                |
| outputs               | [                                                                                                                                                                 |
|                       |   {                                                                                                                                                               |
|                       |     "output_value": "cccccccc-cccc-cccc-cccc-cccccccccccc",                                                                                                       |
|                       |     "description": "A unique id for the logical interface",                                                                                                       |
|                       |     "output_key": "id"                                                                                                                                            |
|                       |   },                                                                                                                                                              |
|                       |   {                                                                                                                                                               |
|                       |     "output_value": null,                                                                                                                                         |
|                       |     "output_error": "'ContrailLogicalInterface' object has no attribute 'li_uuid'",                                                                               |
|                       |     "description": "The name of the logical interface.",                                                                                                          |
|                       |     "output_key": "name"                                                                                                                                          |
|                       |   }                                                                                                                                                               |
|                       | ]                                                                                                                                                                 |
| parameters            | {                                                                                                                                                                 |
|                       |   "logical_port_type": "L2",                                                                                                                                      |
|                       |   "physical_port_id": "dddddddd-dddd-dddd-dddd-dddddddddddd",                                                                                                     |
|                       |   "OS::stack_id": "356486d9-72dd-4d6e-80c8-e252926c957d",                                                                                                         |
|                       |   "OS::stack_name": "ese_logical_port_ecb4c4ac-3ebc-4045-a27c-52fecc93bac5",                                                                                      |
|                       |   "virtual_machine_interface_ids": "67d9f139-b5be-4082-a090-3a1a9cbf1df8",                                                                                        |
|                       |   "logical_port_name": "xe-0/0/4.1025",                                                                                                                           |
|                       |   "logical_port_vlan_id": "1025"                                                                                                                                  |
|                       | }                                                                                                                                                                 |
| parent                | None                                                                                                                                                              |
| stack_name            | ese_logical_port_ecb4c4ac-3ebc-4045-a27c-52fecc93bac5                                                                                                             |
| stack_owner           | admin                                                                                                                                                             |
| stack_status          | CREATE_COMPLETE                                                                                                                                                   |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                               |
| stack_user_project_id | 0b576f6f4cbf414f829cd12f008bf08f                                                                                                                                  |
| template_description  | Logical port template                                                                                                                                             |
| timeout_mins          | 10                                                                                                                                                                |
| updated_time          | None                                                                                                                                                              |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "ese_logical_port" via heatclient.
```
$ heat template-show ese_logical_port_ecb4c4ac-3ebc-4045-a27c-52fecc93bac5
description: 'Logical port template

  '
heat_template_version: '2013-05-23'
outputs:
  id:
    description: A unique id for the logical interface
    value: {get_resource: logical_interface}
  name:
    description: The name of the logical interface.
    value:
      get_attr: [logical_interface, name]
parameters:
  logical_port_name: {description: Name of the logical port., label: Logical Port
      Name, type: string}
  logical_port_type: {description: Type of the logical port., label: Logical Port
      Type, type: string}
  logical_port_vlan_id: {default: 0, description: VLAN id to use for logical port
      creation., label: VLAN id for Logical Port, type: number}
  physical_port_id: {description: A unique id for the Physical Interface., label: Physical
      Interface ID, type: string}
  virtual_machine_interface_ids: {description: Virtual Machine Interface ID., label: Virtual
      Machine Interface ID, type: comma_delimited_list}
resources:
  logical_interface:
    properties:
      name: {get_param: logical_port_name}
      physical_interface: {get_param: physical_port_id}
      type: {get_param: logical_port_type}
      virtual_machine_interfaces: {get_param: virtual_machine_interface_ids}
      vlan: {get_param: logical_port_vlan_id}
    type: OS::Contrail::LogicalInterface
```
