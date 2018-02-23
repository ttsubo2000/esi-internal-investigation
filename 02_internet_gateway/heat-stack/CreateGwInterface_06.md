# HTTP Methods for updating heat-stack: Virtual Machine Interface

Checking heat-stack of "port" via heatclient.
```
$ heat stack-show port_7abe783f-4837-417d-b76f-771ec4d38b97
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                 |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                    |
| creation_time         | 2017-05-11T04:25:58Z                                                                                                                                  |
| description           | Virtual Machine Interface Template                                                                                                                    |
| disable_rollback      | True                                                                                                                                                  |
| id                    | a992265b-5295-4df3-9ec0-3a205a76765f                                                                                                                  |
| links                 | http://heat-api:8004/v1/0b576f6f4cbf414f829cd12f008bf08f/stacks/port_7abe783f-4837-417d-b76f-771ec4d38b97/a992265b-5295-4df3-9ec0-3a205a76765f (self) |
| notification_topics   | []                                                                                                                                                    |
| outputs               | [                                                                                                                                                     |
|                       |   {                                                                                                                                                   |
|                       |     "output_value": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb",                                                                                           |
|                       |     "description": "Virtual network.",                                                                                                                |
|                       |     "output_key": "virtual_network"                                                                                                                   |
|                       |   },                                                                                                                                                  |
|                       |   {                                                                                                                                                   |
|                       |     "output_value": "default-domain:admin:7abe783f-4837-417d-b76f-771ec4d38b97",                                                                      |
|                       |     "description": "Fully Qualified Name of the VMI",                                                                                                 |
|                       |     "output_key": "fq_name"                                                                                                                           |
|                       |   },                                                                                                                                                  |
|                       |   {                                                                                                                                                   |
|                       |     "output_value": "7abe783f-4837-417d-b76f-771ec4d38b97",                                                                                           |
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
|                       |   "virtual_machine": "b9618566-14ea-4505-8eae-8fdb4b6a0ec1",                                                                                          |
|                       |   "name": "7abe783f-4837-417d-b76f-771ec4d38b97",                                                                                                     |
|                       |   "OS::stack_name": "port_7abe783f-4837-417d-b76f-771ec4d38b97",                                                                                      |
|                       |   "admin_state_up": "True",                                                                                                                           |
|                       |   "virtual_machine_interface_allowed_address_pairs": "null",                                                                                          |
|                       |   "virtual_machine_interface_mac_address": "fa:16:3e:f8:45:26",                                                                                       |
|                       |   "OS::stack_id": "a992265b-5295-4df3-9ec0-3a205a76765f",                                                                                             |
|                       |   "device_owner": "network:gw_interface",                                                                                                             |
|                       |   "virtual_network": "52d7bef8-aa17-45c3-b63e-6a0e504603f0",                                                                                          |
|                       |   "uuid": "7abe783f-4837-417d-b76f-771ec4d38b97"                                                                                                      |
|                       | }                                                                                                                                                     |
| parent                | None                                                                                                                                                  |
| stack_name            | port_7abe783f-4837-417d-b76f-771ec4d38b97                                                                                                             |
| stack_owner           | admin                                                                                                                                                 |
| stack_status          | UPDATE_COMPLETE                                                                                                                                       |
| stack_status_reason   | Stack successfully updated                                                                                                                            |
| stack_user_project_id | 0b576f6f4cbf414f829cd12f008bf08f                                                                                                                      |
| template_description  | Virtual Machine Interface Template                                                                                                                    |
| timeout_mins          | 10                                                                                                                                                    |
| updated_time          | 2017-05-11T04:26:04Z                                                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "port" via heatclient.
```
$ heat template-show port_7abe783f-4837-417d-b76f-771ec4d38b97
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
      ip_address: 172.16.101.153
      name:
        str_replace:
          params:
            '%ip%': 172.16.101.153
            '%name%': {get_param: name}
            '%zone%': a510f785-7758-4ce5-8fd4-c107d11b8e40
          template: '%name%_%zone%_%ip%'
      network_id: {get_param: virtual_network}
      subnet_id: 435a94ee-ab64-4787-acbb-d2d7c95867e9
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
