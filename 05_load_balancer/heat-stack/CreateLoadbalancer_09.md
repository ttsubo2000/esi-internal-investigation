# HTTP Methods for updating heat-stack: Virtual Machine Interface

Checking heat-stack of "port" via heatclient.
```
$ heat stack-show port_ddc14be4-3480-4e97-a978-817b18f9904c
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                              |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                 |
| creation_time         | 2018-02-19T05:17:08Z                                                                                                                                                               |
| description           | Virtual Machine Interface Template                                                                                                                                                 |
| disable_rollback      | True                                                                                                                                                                               |
| id                    | 0415a579-7398-4843-98b9-bd1867a0bbc6                                                                                                                                               |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/fe3a4a1a72c04479bb6c19c2c0ccba4c/stacks/port_ddc14be4-3480-4e97-a978-817b18f9904c/0415a579-7398-4843-98b9-bd1867a0bbc6 |
| notification_topics   | []                                                                                                                                                                                 |
| outputs               | [                                                                                                                                                                                  |
|                       |   {                                                                                                                                                                                |
|                       |     "output_value": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7",                                                                                                   |
|                       |     "description": "Fully Qualified Name of the VMI",                                                                                                                              |
|                       |     "output_key": "fq_name"                                                                                                                                                        |
|                       |   },                                                                                                                                                                               |
|                       |   {                                                                                                                                                                                |
|                       |     "output_value": {                                                                                                                                                              |
|                       |       "allowed_address_pair": []                                                                                                                                                   |
|                       |     },                                                                                                                                                                             |
|                       |     "description": "Virtual machine allowed address pairs.",                                                                                                                       |
|                       |     "output_key": "allowed_address_pairs"                                                                                                                                          |
|                       |   },                                                                                                                                                                               |
|                       |   {                                                                                                                                                                                |
|                       |     "output_value": "cc987cdf-428c-446c-a390-540c5af4449d",                                                                                                                        |
|                       |     "description": "Monitoring Target ID",                                                                                                                                         |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                           |
|                       |   },                                                                                                                                                                               |
|                       |   {                                                                                                                                                                                |
|                       |     "output_value": [                                                                                                                                                              |
|                       |       "fa:16:3e:f7:60:7f"                                                                                                                                                          |
|                       |     ],                                                                                                                                                                             |
|                       |     "description": "Virtual machine interface mac address.",                                                                                                                       |
|                       |     "output_key": "mac_address"                                                                                                                                                    |
|                       |   },                                                                                                                                                                               |
|                       |   {                                                                                                                                                                                |
|                       |     "output_value": [                                                                                                                                                              |
|                       |       [                                                                                                                                                                            |
|                       |         "default-domain",                                                                                                                                                          |
|                       |         "admin",                                                                                                                                                                   |
|                       |         "b62eefe0-0872-478d-adfe-1a606320f0e7"                                                                                                                                     |
|                       |       ]                                                                                                                                                                            |
|                       |     ],                                                                                                                                                                             |
|                       |     "description": "Virtual network.",                                                                                                                                             |
|                       |     "output_key": "virtual_network"                                                                                                                                                |
|                       |   },                                                                                                                                                                               |
|                       |   {                                                                                                                                                                                |
|                       |     "output_value": "f68d0924-ef20-4c1b-ac45-0e6b879af5e7",                                                                                                                        |
|                       |     "description": "A unique id for the virtual machine interface.",                                                                                                               |
|                       |     "output_key": "id"                                                                                                                                                             |
|                       |   },                                                                                                                                                                               |
|                       |   {                                                                                                                                                                                |
|                       |     "output_value": "http://collector-agents-se:7070/targets/cc987cdf-428c-446c-a390-540c5af4449d",                                                                                |
|                       |     "description": "Monitoring Process Link",                                                                                                                                      |
|                       |     "output_key": "monitoring_link"                                                                                                                                                |
|                       |   }                                                                                                                                                                                |
|                       | ]                                                                                                                                                                                  |
| parameters            | {                                                                                                                                                                                  |
|                       |   "virtual_machine": "47531b14-72e9-439d-8949-fd941457ecde",                                                                                                                       |
|                       |   "uuid": "ddc14be4-3480-4e97-a978-817b18f9904c",                                                                                                                                  |
|                       |   "OS::stack_name": "port_ddc14be4-3480-4e97-a978-817b18f9904c",                                                                                                                   |
|                       |   "admin_state_up": "True",                                                                                                                                                        |
|                       |   "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c",                                                                                                                                 |
|                       |   "virtual_machine_interface_allowed_address_pairs": "null",                                                                                                                       |
|                       |   "virtual_machine_interface_mac_address": "fa:16:3e:cf:b0:c4",                                                                                                                    |
|                       |   "OS::stack_id": "0415a579-7398-4843-98b9-bd1867a0bbc6",                                                                                                                          |
|                       |   "device_owner": "compute:nova",                                                                                                                                                  |
|                       |   "version": "3",                                                                                                                                                                  |
|                       |   "virtual_network": "168c1535-9001-49c7-bb05-21844570a83c",                                                                                                                       |
|                       |   "security_groups": "[]",                                                                                                                                                         |
|                       |   "name": "ddc14be4-3480-4e97-a978-817b18f9904c"                                                                                                                                   |
|                       | }                                                                                                                                                                                  |
| parent                | None                                                                                                                                                                               |
| stack_name            | port_ddc14be4-3480-4e97-a978-817b18f9904c                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                              |
| stack_status          | UPDATE_COMPLETE                                                                                                                                                                    |
| stack_status_reason   | Stack successfully updated                                                                                                                                                         |
| stack_user_project_id | fe3a4a1a72c04479bb6c19c2c0ccba4c                                                                                                                                                   |
| template_description  | Virtual Machine Interface Template                                                                                                                                                 |
| timeout_mins          | 13                                                                                                                                                                                 |
| updated_time          | 2018-02-19T05:17:28Z                                                                                                                                                               |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "port" via heatclient.
```
$ heat template-show port_ddc14be4-3480-4e97-a978-817b18f9904c
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
  monitoring_link:
    description: Monitoring Process Link
    value:
      get_attr: [vmi_monitor, link]
  monitoring_target_id:
    description: Monitoring Target ID
    value: {get_resource: vmi_monitor}
  virtual_network:
    description: Virtual network.
    value:
      get_attr: [virtual_machine_interface, virtual_networks]
parameters:
  admin_state_up: {default: true, label: Admin state up, type: boolean}
  device_owner: {default: '', label: Device Owner, type: string}
  name: {description: A unique id for the Physical Interface., label: Physical Interface
      ID, type: string}
  security_groups:
    default: []
    description: The IDs of security groups applied to the port.
    label: Security Groups List
    type: json
  tenant_id: {label: Tenant ID, type: string}
  uuid: {description: A unique id for the Virtual Machine Interface., label: Backend
      Virtual Machine Interface UUID, type: string}
  version: {label: Config version, type: number}
  virtual_machine: {default: '', label: Virtual Machine., type: string}
  virtual_machine_interface_allowed_address_pairs: {label: Virtual machine interface
      allowed address pairs., type: json}
  virtual_machine_interface_mac_address: {default: 'fe:ff:ff:ff:ff:ff', label: Virtual
      machine interface mac address., type: string}
  virtual_network: {label: Virtual Network., type: string}
resources:
  instance_ip_0:
    properties:
      ip_address: 100.64.193.3
      name:
        str_replace:
          params:
            '%ip%': 100.64.193.3
            '%name%': {get_param: name}
            '%zone%': 707847d0-89d9-4b98-93a2-8b376709c5f3
          template: '%name%_%zone%_%ip%'
      network_id: {get_param: virtual_network}
      subnet_id: a2fc1444-c7f4-4a72-8376-a920889c4a43
      virtual_machine_interfaces:
      - {get_resource: virtual_machine_interface}
    type: OS::Contrail::InstanceIp
  virtual_machine_interface:
    properties:
      admin_state_up: {get_param: admin_state_up}
      device_owner: {get_param: device_owner}
      name: {get_param: name}
      security_groups: {get_param: security_groups}
      uuid: {get_param: uuid}
      virtual_machine: {get_param: virtual_machine}
      virtual_machine_interface_allowed_address_pairs: {get_param: virtual_machine_interface_allowed_address_pairs}
      virtual_machine_interface_mac_addresses:
      - {get_param: virtual_machine_interface_mac_address}
      virtual_networks:
      - {get_param: virtual_network}
    type: OS::Contrail::VirtualMachineInterface
  vmi_monitor:
    depends_on: virtual_machine_interface
    properties:
      field_name: vmi
      properties:
        fq_name:
          get_attr: [virtual_machine_interface, fq_name]
      resource_id: {get_param: uuid}
      resource_type: ports
      syncer_properties:
        etcd:
          status: {key: vmi}
        tsdb:
          traffic.in:
            metric: traffic.contrail_bytes
            tags:
              direction: in
              resource_id: {get_param: uuid}
          traffic.out:
            metric: traffic.contrail_bytes
            tags:
              direction: out
              resource_id: {get_param: uuid}
      tenant_id: {get_param: tenant_id}
      type: virtual_machine_interface
      version: {get_param: version}
    type: ESI::Monitoring::MonitoringTarget
```
