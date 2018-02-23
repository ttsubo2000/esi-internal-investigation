# HTTP Methods for creating heat-stack: Network

Checking heat-stack of "network" via heatclient.
```
$ heat stack-show network_bb69041d-c654-4e9f-a763-afd4333275bc
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                    |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                       |
| creation_time         | 2017-05-11T05:01:45Z                                                                                                                                     |
| description           | Network template                                                                                                                                         |
| disable_rollback      | True                                                                                                                                                     |
| id                    | f73bedd0-b5d5-4abb-ac41-0804910e848c                                                                                                                     |
| links                 | http://heat-api:8004/v1/0b576f6f4cbf414f829cd12f008bf08f/stacks/network_bb69041d-c654-4e9f-a763-afd4333275bc/f73bedd0-b5d5-4abb-ac41-0804910e848c (self) |
| notification_topics   | []                                                                                                                                                       |
| outputs               | [                                                                                                                                                        |
|                       |   {                                                                                                                                                      |
|                       |     "output_value": "[]",                                                                                                                                |
|                       |     "description": "The name of the virtual network.",                                                                                                   |
|                       |     "output_key": "route_targets"                                                                                                                        |
|                       |   },                                                                                                                                                     |
|                       |   {                                                                                                                                                      |
|                       |     "output_value": "default-domain:admin:bb69041d-c654-4e9f-a763-afd4333275bc",                                                                         |
|                       |     "description": "The FQ name of the virtual network.",                                                                                                |
|                       |     "output_key": "fq_name"                                                                                                                              |
|                       |   },                                                                                                                                                     |
|                       |   {                                                                                                                                                      |
|                       |     "output_value": "bb69041d-c654-4e9f-a763-afd4333275bc",                                                                                              |
|                       |     "description": "A unique id for the virtual network.",                                                                                               |
|                       |     "output_key": "id"                                                                                                                                   |
|                       |   },                                                                                                                                                     |
|                       |   {                                                                                                                                                      |
|                       |     "output_value": "bb69041d-c654-4e9f-a763-afd4333275bc",                                                                                              |
|                       |     "description": "The name of the virtual network.",                                                                                                   |
|                       |     "output_key": "name"                                                                                                                                 |
|                       |   }                                                                                                                                                      |
|                       | ]                                                                                                                                                        |
| parameters            | {                                                                                                                                                        |
|                       |   "forwarding_mode": "l2_l3",                                                                                                                            |
|                       |   "allow_transit": "False",                                                                                                                              |
|                       |   "name": "bb69041d-c654-4e9f-a763-afd4333275bc",                                                                                                        |
|                       |   "OS::stack_name": "network_bb69041d-c654-4e9f-a763-afd4333275bc",                                                                                      |
|                       |   "admin_state_up": "True",                                                                                                                              |
|                       |   "OS::stack_id": "f73bedd0-b5d5-4abb-ac41-0804910e848c",                                                                                                |
|                       |   "external": "True",                                                                                                                                    |
|                       |   "shared": "False",                                                                                                                                     |
|                       |   "route_targets": "",                                                                                                                                   |
|                       |   "uuid": "bb69041d-c654-4e9f-a763-afd4333275bc"                                                                                                         |
|                       | }                                                                                                                                                        |
| parent                | None                                                                                                                                                     |
| stack_name            | network_bb69041d-c654-4e9f-a763-afd4333275bc                                                                                                             |
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
$ heat template-show network_bb69041d-c654-4e9f-a763-afd4333275bc
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
