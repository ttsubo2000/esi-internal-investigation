# HTTP Methods for updating heat-stack: Virtual Machine Interface

Checking heat-stack of "port" via heatclient.
```
$ heat stack-show port_327f59b7-df38-4d8f-97db-d320defcab76
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                 |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                    |
| creation_time         | 2017-05-11T03:05:37Z                                                                                                                                  |
| description           | Virtual Machine Interface Template                                                                                                                    |
| disable_rollback      | True                                                                                                                                                  |
| id                    | 67472096-f3b3-48d1-962c-23ea4912b1d3                                                                                                                  |
| links                 | http://heat-api:8004/v1/0b576f6f4cbf414f829cd12f008bf08f/stacks/port_327f59b7-df38-4d8f-97db-d320defcab76/67472096-f3b3-48d1-962c-23ea4912b1d3 (self) |
| notification_topics   | []                                                                                                                                                    |
| outputs               | [                                                                                                                                                     |
|                       |   {                                                                                                                                                   |
|                       |     "output_value": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb",                                                                                           |
|                       |     "description": "Virtual network.",                                                                                                                |
|                       |     "output_key": "virtual_network"                                                                                                                   |
|                       |   },                                                                                                                                                  |
|                       |   {                                                                                                                                                   |
|                       |     "output_value": "default-domain:admin:327f59b7-df38-4d8f-97db-d320defcab76",                                                                      |
|                       |     "description": "Fully Qualified Name of the VMI",                                                                                                 |
|                       |     "output_key": "fq_name"                                                                                                                           |
|                       |   },                                                                                                                                                  |
|                       |   {                                                                                                                                                   |
|                       |     "output_value": "327f59b7-df38-4d8f-97db-d320defcab76",                                                                                           |
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
|                       |   "virtual_machine": "5c241c51-2003-407a-a239-689fabd19022",                                                                                          |
|                       |   "name": "327f59b7-df38-4d8f-97db-d320defcab76",                                                                                                     |
|                       |   "OS::stack_name": "port_327f59b7-df38-4d8f-97db-d320defcab76",                                                                                      |
|                       |   "admin_state_up": "True",                                                                                                                           |
|                       |   "virtual_machine_interface_allowed_address_pairs": "null",                                                                                          |
|                       |   "virtual_machine_interface_mac_address": "fa:16:3e:e5:f6:39",                                                                                       |
|                       |   "OS::stack_id": "67472096-f3b3-48d1-962c-23ea4912b1d3",                                                                                             |
|                       |   "device_owner": "network:common_function_gateway",                                                                                                  |
|                       |   "virtual_network": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57",                                                                                          |
|                       |   "uuid": "327f59b7-df38-4d8f-97db-d320defcab76"                                                                                                      |
|                       | }                                                                                                                                                     |
| parent                | None                                                                                                                                                  |
| stack_name            | port_327f59b7-df38-4d8f-97db-d320defcab76                                                                                                             |
| stack_owner           | admin                                                                                                                                                 |
| stack_status          | UPDATE_COMPLETE                                                                                                                                       |
| stack_status_reason   | Stack successfully updated                                                                                                                            |
| stack_user_project_id | 0b576f6f4cbf414f829cd12f008bf08f                                                                                                                      |
| template_description  | Virtual Machine Interface Template                                                                                                                    |
| timeout_mins          | 10                                                                                                                                                    |
| updated_time          | 2017-05-11T03:05:57Z                                                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "port" via heatclient.
```
$ heat template-show port_327f59b7-df38-4d8f-97db-d320defcab76
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
      ip_address: 169.254.0.3
      name:
        str_replace:
          params:
            '%ip%': 169.254.0.3
            '%name%': {get_param: name}
            '%zone%': e1353d56-b05a-43a9-b924-383ab0d64d7b
          template: '%name%_%zone%_%ip%'
      network_id: {get_param: virtual_network}
      subnet_id: 9e61b626-a866-4ba5-b1c7-01935fdac3f4
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