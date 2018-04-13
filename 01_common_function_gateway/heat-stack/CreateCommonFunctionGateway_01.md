# HTTP Methods for creating heat-stack: Network

Checking heat-stack of "network" via heatclient.
```
$ heat stack-show network_fc8814a7-eb1e-4f59-8422-7de500e72782
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                 |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                    |
| creation_time         | 2018-04-09T04:49:52Z                                                                                                                                                                  |
| description           | Network template                                                                                                                                                                      |
| disable_rollback      | True                                                                                                                                                                                  |
| id                    | e2574663-12a4-4845-b95b-01cf7df978b9                                                                                                                                                  |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/c583ce78843344adbe5fd20f13620274/stacks/network_fc8814a7-eb1e-4f59-8422-7de500e72782/e2574663-12a4-4845-b95b-01cf7df978b9 |
| notification_topics   | []                                                                                                                                                                                    |
| outputs               | [                                                                                                                                                                                     |
|                       |   {                                                                                                                                                                                   |
|                       |     "output_value": [],                                                                                                                                                               |
|                       |     "description": "The name of the virtual network.",                                                                                                                                |
|                       |     "output_key": "route_targets"                                                                                                                                                     |
|                       |   },                                                                                                                                                                                  |
|                       |   {                                                                                                                                                                                   |
|                       |     "output_value": "default-domain:usertenant:fc8814a7-eb1e-4f59-8422-7de500e72782",                                                                                                 |
|                       |     "description": "The FQ name of the virtual network.",                                                                                                                             |
|                       |     "output_key": "fq_name"                                                                                                                                                           |
|                       |   },                                                                                                                                                                                  |
|                       |   {                                                                                                                                                                                   |
|                       |     "output_value": "fc8814a7-eb1e-4f59-8422-7de500e72782",                                                                                                                           |
|                       |     "description": "A unique id for the virtual network.",                                                                                                                            |
|                       |     "output_key": "id"                                                                                                                                                                |
|                       |   },                                                                                                                                                                                  |
|                       |   {                                                                                                                                                                                   |
|                       |     "output_value": "fc8814a7-eb1e-4f59-8422-7de500e72782",                                                                                                                           |
|                       |     "description": "The name of the virtual network.",                                                                                                                                |
|                       |     "output_key": "name"                                                                                                                                                              |
|                       |   }                                                                                                                                                                                   |
|                       | ]                                                                                                                                                                                     |
| parameters            | {                                                                                                                                                                                     |
|                       |   "forwarding_mode": "l2_l3",                                                                                                                                                         |
|                       |   "allow_transit": "False",                                                                                                                                                           |
|                       |   "name": "fc8814a7-eb1e-4f59-8422-7de500e72782",                                                                                                                                     |
|                       |   "OS::stack_name": "network_fc8814a7-eb1e-4f59-8422-7de500e72782",                                                                                                                   |
|                       |   "admin_state_up": "True",                                                                                                                                                           |
|                       |   "OS::stack_id": "e2574663-12a4-4845-b95b-01cf7df978b9",                                                                                                                             |
|                       |   "external": "True",                                                                                                                                                                 |
|                       |   "shared": "False",                                                                                                                                                                  |
|                       |   "route_targets": "",                                                                                                                                                                |
|                       |   "uuid": "fc8814a7-eb1e-4f59-8422-7de500e72782"                                                                                                                                      |
|                       | }                                                                                                                                                                                     |
| parent                | None                                                                                                                                                                                  |
| stack_name            | network_fc8814a7-eb1e-4f59-8422-7de500e72782                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                 |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                       |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                   |
| stack_user_project_id | c583ce78843344adbe5fd20f13620274                                                                                                                                                      |
| template_description  | Network template                                                                                                                                                                      |
| timeout_mins          | 3                                                                                                                                                                                     |
| updated_time          | None                                                                                                                                                                                  |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "network" via heatclient.
```
$ heat template-show network_fc8814a7-eb1e-4f59-8422-7de500e72782
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
