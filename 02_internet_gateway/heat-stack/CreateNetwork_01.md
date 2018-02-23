# HTTP Methods for creating heat-stack: Network

Checking heat-stack of "network" via heatclient.
```
$ heat stack-show network_52d7bef8-aa17-45c3-b63e-6a0e504603f0
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                    |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                       |
| creation_time         | 2017-05-11T04:25:01Z                                                                                                                                     |
| description           | Network template                                                                                                                                         |
| disable_rollback      | True                                                                                                                                                     |
| id                    | 345e3601-b0c7-428b-8b7b-0787ab682615                                                                                                                     |
| links                 | http://heat-api:8004/v1/0b576f6f4cbf414f829cd12f008bf08f/stacks/network_52d7bef8-aa17-45c3-b63e-6a0e504603f0/345e3601-b0c7-428b-8b7b-0787ab682615 (self) |
| notification_topics   | []                                                                                                                                                       |
| outputs               | [                                                                                                                                                        |
|                       |   {                                                                                                                                                      |
|                       |     "output_value": "[]",                                                                                                                                |
|                       |     "description": "The name of the virtual network.",                                                                                                   |
|                       |     "output_key": "route_targets"                                                                                                                        |
|                       |   },                                                                                                                                                     |
|                       |   {                                                                                                                                                      |
|                       |     "output_value": "default-domain:admin:52d7bef8-aa17-45c3-b63e-6a0e504603f0",                                                                         |
|                       |     "description": "The FQ name of the virtual network.",                                                                                                |
|                       |     "output_key": "fq_name"                                                                                                                              |
|                       |   },                                                                                                                                                     |
|                       |   {                                                                                                                                                      |
|                       |     "output_value": "52d7bef8-aa17-45c3-b63e-6a0e504603f0",                                                                                              |
|                       |     "description": "A unique id for the virtual network.",                                                                                               |
|                       |     "output_key": "id"                                                                                                                                   |
|                       |   },                                                                                                                                                     |
|                       |   {                                                                                                                                                      |
|                       |     "output_value": "52d7bef8-aa17-45c3-b63e-6a0e504603f0",                                                                                              |
|                       |     "description": "The name of the virtual network.",                                                                                                   |
|                       |     "output_key": "name"                                                                                                                                 |
|                       |   }                                                                                                                                                      |
|                       | ]                                                                                                                                                        |
| parameters            | {                                                                                                                                                        |
|                       |   "forwarding_mode": "l2_l3",                                                                                                                            |
|                       |   "allow_transit": "False",                                                                                                                              |
|                       |   "name": "52d7bef8-aa17-45c3-b63e-6a0e504603f0",                                                                                                        |
|                       |   "OS::stack_name": "network_52d7bef8-aa17-45c3-b63e-6a0e504603f0",                                                                                      |
|                       |   "admin_state_up": "True",                                                                                                                              |
|                       |   "OS::stack_id": "345e3601-b0c7-428b-8b7b-0787ab682615",                                                                                                |
|                       |   "external": "True",                                                                                                                                    |
|                       |   "shared": "False",                                                                                                                                     |
|                       |   "route_targets": "",                                                                                                                                   |
|                       |   "uuid": "52d7bef8-aa17-45c3-b63e-6a0e504603f0"                                                                                                         |
|                       | }                                                                                                                                                        |
| parent                | None                                                                                                                                                     |
| stack_name            | network_52d7bef8-aa17-45c3-b63e-6a0e504603f0                                                                                                             |
| stack_owner           | admin                                                                                                                                                    |
| stack_status          | CREATE_COMPLETE                                                                                                                                          |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                      |
| stack_user_project_id | 0b576f6f4cbf414f829cd12f008bf08f                                                                                                                         |
| template_description  | Network template                                                                                                                                         |
| timeout_mins          | 10                                                                                                                                                       |
| updated_time          | None                                                                                                                                                     |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "network" via heatclient.
```
$ heat template-show network_52d7bef8-aa17-45c3-b63e-6a0e504603f0
description: 'Network template

  '
heat_template_version: '2013-05-23'
outputs:
  fq_name:
    description: The FQ name of the virtual network.
    value:
      get_attr: [network, fq_name]
  id:
    description: A unique id for the virtual network.
    value: {get_resource: network}
  name:
    description: The name of the virtual network.
    value:
      get_attr: [network, name]
  route_targets:
    description: The name of the virtual network.
    value:
      get_attr: [network, route_targets]
parameters:
  admin_state_up: {default: true, label: Admin state up, type: boolean}
  allow_transit: {default: false, label: Allow Transit, type: boolean}
  external: {default: true, label: External Network, type: boolean}
  forwarding_mode: {default: l2_l3, description: Forwarding Mode., label: Forwarding
      Mode, type: string}
  name: {description: Name of the virtual network that will be created., label: Virtual
      Network Name, type: string}
  route_targets:
    default: []
    label: Route Targets list
    type: comma_delimited_list
  shared: {default: false, label: Shared Network, type: boolean}
  uuid: {default: '', description: UUID of the virtual network that will be created.,
    label: Virtual Network UUID, type: string}
resources:
  network:
    properties:
      admin_state_up: {get_param: admin_state_up}
      forwarding_mode: {get_param: forwarding_mode}
      name: {get_param: name}
      route_targets: {get_param: route_targets}
      shared: {get_param: shared}
      uuid: {get_param: uuid}
    type: OS::Contrail::VirtualNetwork
```
