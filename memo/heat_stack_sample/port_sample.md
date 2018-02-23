## Sample of heat-stack of port

* Checking heat-stack of port in heat-engine
```
$ openstack stack show port_82b37a87-b6ca-4906-82a1-3a8db86b26ac
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                 | Value                                                                                                                                                      |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| id                    | b3571d44-eb8d-40a6-adae-d9f65b62ee05                                                                                                                       |
| stack_name            | port_82b37a87-b6ca-4906-82a1-3a8db86b26ac                                                                                                                  |
| description           | Virtual Machine Interface Template                                                                                                                         |
|                       |                                                                                                                                                            |
| creation_time         | 2016-11-07T06:17:39Z                                                                                                                                       |
| updated_time          | 2016-11-07T06:18:03Z                                                                                                                                       |
| stack_status          | UPDATE_COMPLETE                                                                                                                                            |
| stack_status_reason   | Stack successfully updated                                                                                                                                 |
| parameters            | OS::stack_id: b3571d44-eb8d-40a6-adae-d9f65b62ee05                                                                                                         |
|                       | OS::stack_name: port_82b37a87-b6ca-4906-82a1-3a8db86b26ac                                                                                                  |
|                       | admin_state_up: 'True'                                                                                                                                     |
|                       | device_owner: physical_port                                                                                                                                |
|                       | name: 82b37a87-b6ca-4906-82a1-3a8db86b26ac                                                                                                                 |
|                       | uuid: 82b37a87-b6ca-4906-82a1-3a8db86b26ac                                                                                                                 |
|                       | virtual_machine: 135b03e0-9d63-4bd3-9951-9fbda6ddb42f                                                                                                      |
|                       | virtual_machine_interface_allowed_address_pairs: 'null'                                                                                                    |
|                       | virtual_machine_interface_mac_address: 42:9e:64:ce:8b:9a                                                                                                   |
|                       | virtual_network: 23489ede-80ae-429f-a187-20586e8ba0f4                                                                                                      |
|                       |                                                                                                                                                            |
| outputs               | - description: Virtual network.                                                                                                                            |
|                       |   output_key: virtual_network                                                                                                                              |
|                       |   output_value:                                                                                                                                            |
|                       |   - - default-domain                                                                                                                                       |
|                       |     - admin                                                                                                                                                |
|                       |     - 23489ede-80ae-429f-a187-20586e8ba0f4                                                                                                                 |
|                       | - description: Fully Qualified Name of the VMI                                                                                                             |
|                       |   output_key: fq_name                                                                                                                                      |
|                       |   output_value: default-domain:admin:82b37a87-b6ca-4906-82a1-3a8db86b26ac                                                                                  |
|                       | - description: A unique id for the virtual machine interface.                                                                                              |
|                       |   output_key: id                                                                                                                                           |
|                       |   output_value: 82b37a87-b6ca-4906-82a1-3a8db86b26ac                                                                                                       |
|                       | - description: Virtual machine allowed address pairs.                                                                                                      |
|                       |   output_key: allowed_address_pairs                                                                                                                        |
|                       |   output_value:                                                                                                                                            |
|                       |     allowed_address_pair: []                                                                                                                               |
|                       | - description: Virtual machine interface mac address.                                                                                                      |
|                       |   output_key: mac_address                                                                                                                                  |
|                       |   output_value:                                                                                                                                            |
|                       |   - 42:9e:64:ce:8b:9a                                                                                                                                      |
|                       |                                                                                                                                                            |
| links                 | - href: http://172.23.16.61:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/port_82b37a87-b6ca-4906-82a1-3a8db86b26ac/b3571d44-eb8d-40a6-adae-d9f65b62ee05 |
|                       |   rel: self                                                                                                                                                |
|                       |                                                                                                                                                            |
| parent                | None                                                                                                                                                       |
| disable_rollback      | True                                                                                                                                                       |
| stack_user_project_id | aee85dff980f4b0f94bed7861765acc7                                                                                                                           |
| stack_owner           | sdp_esi_admin                                                                                                                                              |
| capabilities          | []                                                                                                                                                         |
| notification_topics   | []                                                                                                                                                         |
| timeout_mins          | 10                                                                                                                                                         |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

* Checking heat-template of port in heat-engine
```
$ openstack stack template show port_82b37a87-b6ca-4906-82a1-3a8db86b26ac
description: 'Virtual Machine Interface Template

  '
heat_template_version: '2013-05-23'
outputs:
  allowed_address_pairs:
    description: Virtual machine allowed address pairs.
    value:
      get_attr:
      - virtual_machine_interface
      - virtual_machine_interface_allowed_address_pairs
  fq_name:
    description: Fully Qualified Name of the VMI
    value:
      get_attr:
      - virtual_machine_interface
      - fq_name
  id:
    description: A unique id for the virtual machine interface.
    value:
      get_resource: virtual_machine_interface
  mac_address:
    description: Virtual machine interface mac address.
    value:
      get_attr:
      - virtual_machine_interface
      - virtual_machine_interface_mac_addresses
  virtual_network:
    description: Virtual network.
    value:
      get_attr:
      - virtual_machine_interface
      - virtual_networks
parameters:
  admin_state_up:
    default: true
    label: Admin state up
    type: boolean
  device_owner:
    default: ''
    label: Device Owner
    type: string
  name:
    description: A unique id for the Physical Interface.
    label: Physical Interface ID
    type: string
  uuid:
    description: A unique id for the Virtual Machine Interface.
    label: Backend Virtual Machine Interface UUID
    type: string
  virtual_machine:
    default: ''
    label: Virtual Machine.
    type: string
  virtual_machine_interface_allowed_address_pairs:
    label: Virtual machine interface allowed address pairs.
    type: json
  virtual_machine_interface_mac_address:
    default: fe:ff:ff:ff:ff:ff
    label: Virtual machine interface mac address.
    type: string
  virtual_network:
    label: Virtual Network.
    type: string
resources:
  instance_ip_0:
    properties:
      ip_address: 192.168.11.36
      name:
        str_replace:
          params:
            '%ip%': 192.168.11.36
            '%name%':
              get_param: name
            '%zone%': ce0aeabc-a509-4834-a198-d25ed582092c
          template: '%name%_%zone%_%ip%'
      network_id:
        get_param: virtual_network
      subnet_id: 498d2eb1-1eab-4a0a-bb58-8a979d5f5363
      virtual_machine_interfaces:
      - get_resource: virtual_machine_interface
    type: OS::Contrail::InstanceIp
  virtual_machine_interface:
    properties:
      admin_state_up:
        get_param: admin_state_up
      device_owner:
        get_param: device_owner
      name:
        get_param: name
      uuid:
        get_param: uuid
      virtual_machine:
        get_param: virtual_machine
      virtual_machine_interface_allowed_address_pairs:
        get_param: virtual_machine_interface_allowed_address_pairs
      virtual_machine_interface_mac_addresses:
      - get_param: virtual_machine_interface_mac_address
      virtual_networks:
      - get_param: virtual_network
    type: OS::Contrail::VirtualMachineInterface
```

* Checking resource-list of port in heat-engine
```
$ openstack stack resource list port_82b37a87-b6ca-4906-82a1-3a8db86b26ac
+---------------------------+--------------------------------------+---------------------------------------+-----------------+----------------------+
| resource_name             | physical_resource_id                 | resource_type                         | resource_status | updated_time         |
+---------------------------+--------------------------------------+---------------------------------------+-----------------+----------------------+
| virtual_machine_interface | 82b37a87-b6ca-4906-82a1-3a8db86b26ac | OS::Contrail::VirtualMachineInterface | CREATE_COMPLETE | 2016-11-07T06:17:39Z |
| instance_ip_0             | c80b2bb6-381d-44ed-a49f-cf277b60ef82 | OS::Contrail::InstanceIp              | CREATE_COMPLETE | 2016-11-07T06:17:40Z |
+---------------------------+--------------------------------------+---------------------------------------+-----------------+----------------------+
```

* Checking resource-show of virtual_machine_interface in heat-engine
```
$ openstack stack resource show port_82b37a87-b6ca-4906-82a1-3a8db86b26ac virtual_machine_interface
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                  | Value                                                                                                                                                           |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| description            |                                                                                                                                                                 |
| links                  | [{u'href': u'http://172.23.16.61:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/port_82b37a87-b6ca-4906-82a1-3a8db86b26ac/b3571d44-eb8d-40a6-adae-             |
|                        | d9f65b62ee05/resources/virtual_machine_interface', u'rel': u'self'}, {u'href':                                                                                  |
|                        | u'http://172.23.16.61:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/port_82b37a87-b6ca-4906-82a1-3a8db86b26ac/b3571d44-eb8d-40a6-adae-d9f65b62ee05', u'rel':  |
|                        | u'stack'}]                                                                                                                                                      |
| logical_resource_id    | virtual_machine_interface                                                                                                                                       |
| physical_resource_id   | 82b37a87-b6ca-4906-82a1-3a8db86b26ac                                                                                                                            |
| required_by            | [u'instance_ip_0']                                                                                                                                              |
| resource_name          | virtual_machine_interface                                                                                                                                       |
| resource_status        | CREATE_COMPLETE                                                                                                                                                 |
| resource_status_reason | state changed                                                                                                                                                   |
| resource_type          | OS::Contrail::VirtualMachineInterface                                                                                                                           |
| updated_time           | 2016-11-07T06:17:39Z                                                                                                                                            |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

* Checking resource-show of instance_ip_0 in heat-engine
```
$ openstack stack resource show port_82b37a87-b6ca-4906-82a1-3a8db86b26ac instance_ip_0
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                  | Value                                                                                                                                                           |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| description            |                                                                                                                                                                 |
| links                  | [{u'href': u'http://172.23.16.61:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/port_82b37a87-b6ca-4906-82a1-3a8db86b26ac/b3571d44-eb8d-40a6-adae-             |
|                        | d9f65b62ee05/resources/instance_ip_0', u'rel': u'self'}, {u'href':                                                                                              |
|                        | u'http://172.23.16.61:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/port_82b37a87-b6ca-4906-82a1-3a8db86b26ac/b3571d44-eb8d-40a6-adae-d9f65b62ee05', u'rel':  |
|                        | u'stack'}]                                                                                                                                                      |
| logical_resource_id    | instance_ip_0                                                                                                                                                   |
| physical_resource_id   | c80b2bb6-381d-44ed-a49f-cf277b60ef82                                                                                                                            |
| required_by            | []                                                                                                                                                              |
| resource_name          | instance_ip_0                                                                                                                                                   |
| resource_status        | CREATE_COMPLETE                                                                                                                                                 |
| resource_status_reason | state changed                                                                                                                                                   |
| resource_type          | OS::Contrail::InstanceIp                                                                                                                                        |
| updated_time           | 2016-11-07T06:17:40Z                                                                                                                                            |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
