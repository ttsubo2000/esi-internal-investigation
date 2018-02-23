# HTTP Methods for creating heat-stack: Virtual Machine Interface

Checking heat-stack of "port" via heatclient.
```
$ heat stack-show port_33907bcb-8689-425d-a700-fe8acfd94aed
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                 |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                    |
| creation_time         | 2017-05-11T05:02:39Z                                                                                                                                  |
| description           | Virtual Machine Interface Template                                                                                                                    |
| disable_rollback      | True                                                                                                                                                  |
| id                    | 5bf72e78-0650-4f7f-a7c8-d668e838ac93                                                                                                                  |
| links                 | http://heat-api:8004/v1/0b576f6f4cbf414f829cd12f008bf08f/stacks/port_33907bcb-8689-425d-a700-fe8acfd94aed/5bf72e78-0650-4f7f-a7c8-d668e838ac93 (self) |
| notification_topics   | []                                                                                                                                                    |
| outputs               | [                                                                                                                                                     |
|                       |   {                                                                                                                                                   |
|                       |     "output_value": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb",                                                                                           |
|                       |     "description": "Virtual network.",                                                                                                                |
|                       |     "output_key": "virtual_network"                                                                                                                   |
|                       |   },                                                                                                                                                  |
|                       |   {                                                                                                                                                   |
|                       |     "output_value": "default-domain:admin:33907bcb-8689-425d-a700-fe8acfd94aed",                                                                      |
|                       |     "description": "Fully Qualified Name of the VMI",                                                                                                 |
|                       |     "output_key": "fq_name"                                                                                                                           |
|                       |   },                                                                                                                                                  |
|                       |   {                                                                                                                                                   |
|                       |     "output_value": "33907bcb-8689-425d-a700-fe8acfd94aed",                                                                                           |
|                       |     "description": "A unique id for the virtual machine interface.",                                                                                  |
|                       |     "output_key": "id"                                                                                                                                |
|                       |   },                                                                                                                                                  |
|                       |   {                                                                                                                                                   |
|                       |     "output_value": "null",                                                                                                                           |
|                       |     "description": "Virtual machine allowed address pairs.",                                                                                          |
|                       |     "output_key": "allowed_address_pairs"                                                                                                             |
|                       |   },                                                                                                                                                  |
|                       |   {                                                                                                                                                   |
|                       |     "output_value": "xx:xx:xx:xx:xx:xx",                                                                                                              |
|                       |     "description": "Virtual machine interface mac address.",                                                                                          |
|                       |     "output_key": "mac_address"                                                                                                                       |
|                       |   }                                                                                                                                                   |
|                       | ]                                                                                                                                                     |
| parameters            | {                                                                                                                                                     |
|                       |   "virtual_machine": "fbd7d07e-9e84-4ad7-ab85-36d46adb9435",                                                                                          |
|                       |   "name": "33907bcb-8689-425d-a700-fe8acfd94aed",                                                                                                     |
|                       |   "OS::stack_name": "port_33907bcb-8689-425d-a700-fe8acfd94aed",                                                                                      |
|                       |   "admin_state_up": "True",                                                                                                                           |
|                       |   "virtual_machine_interface_allowed_address_pairs": "null",                                                                                          |
|                       |   "virtual_machine_interface_mac_address": "fa:16:3e:ef:15:a2",                                                                                       |
|                       |   "OS::stack_id": "5bf72e78-0650-4f7f-a7c8-d668e838ac93",                                                                                             |
|                       |   "device_owner": "network:gw_interface",                                                                                                             |
|                       |   "virtual_network": "bb69041d-c654-4e9f-a763-afd4333275bc",                                                                                          |
|                       |   "uuid": "33907bcb-8689-425d-a700-fe8acfd94aed"                                                                                                      |
|                       | }                                                                                                                                                     |
| parent                | None                                                                                                                                                  |
| stack_name            | port_33907bcb-8689-425d-a700-fe8acfd94aed                                                                                                             |
| stack_owner           | admin                                                                                                                                                 |
| stack_status          | CREATE_COMPLETE                                                                                                                                       |
| stack_status_reason   | Stack successfully updated                                                                                                                            |
| stack_user_project_id | 0b576f6f4cbf414f829cd12f008bf08f                                                                                                                      |
| template_description  | Virtual Machine Interface Template                                                                                                                    |
| timeout_mins          | 10                                                                                                                                                    |
| updated_time          | None                                                                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "port" via heatclient.
```
$ heat template-show port_33907bcb-8689-425d-a700-fe8acfd94aed
description: 'Virtual Machine Interface Template

  '
heat_template_version: '2013-05-23'
outputs:
  allowed_address_pairs:
    description: Virtual machine allowed address pairs.
    value:
      get_attr: [virtual_machine_interface, virtual_machine_interface_allowed_address_pairs]
  fq_name:
    description: Fully Qualified Name of the VMI
    value:
      get_attr: [virtual_machine_interface, fq_name]
  id:
    description: A unique id for the virtual machine interface.
    value: {get_resource: virtual_machine_interface}
  mac_address:
    description: Virtual machine interface mac address.
    value:
      get_attr: [virtual_machine_interface, virtual_machine_interface_mac_addresses]
  virtual_network:
    description: Virtual network.
    value:
      get_attr: [virtual_machine_interface, virtual_networks]
parameters:
  admin_state_up: {default: true, label: Admin state up, type: boolean}
  device_owner: {default: '', label: Device Owner, type: string}
  name: {description: A unique id for the Physical Interface., label: Physical Interface
      ID, type: string}
  uuid: {description: A unique id for the Virtual Machine Interface., label: Backend
      Virtual Machine Interface UUID, type: string}
  virtual_machine: {default: '', label: Virtual Machine., type: string}
  virtual_machine_interface_allowed_address_pairs: {label: Virtual machine interface
      allowed address pairs., type: json}
  virtual_machine_interface_mac_address: {default: 'fe:ff:ff:ff:ff:ff', label: Virtual
      machine interface mac address., type: string}
  virtual_network: {label: Virtual Network., type: string}
resources:
  instance_ip_0:
    properties:
      ip_address: 172.16.101.151
      name:
        str_replace:
          params:
            '%ip%': 172.16.101.151
            '%name%': {get_param: name}
            '%zone%': b4f0c956-2fe0-4634-b7c8-22bfd8095aaf
          template: '%name%_%zone%_%ip%'
      network_id: {get_param: virtual_network}
      subnet_id: 8f9e2ede-c3b4-438e-888d-55e326ec29a9
      virtual_machine_interfaces:
      - {get_resource: virtual_machine_interface}
    type: OS::Contrail::InstanceIp
  instance_ip_1:
    properties:
      ip_address: 172.16.101.152
      name:
        str_replace:
          params:
            '%ip%': 172.16.101.152
            '%name%': {get_param: name}
            '%zone%': b4f0c956-2fe0-4634-b7c8-22bfd8095aaf
          template: '%name%_%zone%_%ip%'
      network_id: {get_param: virtual_network}
      subnet_id: 8f9e2ede-c3b4-438e-888d-55e326ec29a9
      virtual_machine_interfaces:
      - {get_resource: virtual_machine_interface}
    type: OS::Contrail::InstanceIp
  virtual_machine_interface:
    properties:
      admin_state_up: {get_param: admin_state_up}
      device_owner: {get_param: device_owner}
      name: {get_param: name}
      uuid: {get_param: uuid}
      virtual_machine: {get_param: virtual_machine}
      virtual_machine_interface_allowed_address_pairs: {get_param: virtual_machine_interface_allowed_address_pairs}
      virtual_machine_interface_mac_addresses:
      - {get_param: virtual_machine_interface_mac_address}
      virtual_networks:
      - {get_param: virtual_network}
    type: OS::Contrail::VirtualMachineInterface
```
