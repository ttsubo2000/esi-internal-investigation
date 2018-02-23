## Sample of heat-stack of network

* Checking heat-stack of network in heat-engine
```
$ openstack stack show network_23489ede-80ae-429f-a187-20586e8ba0f4
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                 | Value                                                                                                                                                         |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| id                    | 278930d7-45e1-4f31-b395-48970a5a238d                                                                                                                          |
| stack_name            | network_23489ede-80ae-429f-a187-20586e8ba0f4                                                                                                                  |
| description           | Network template                                                                                                                                              |
|                       |                                                                                                                                                               |
| creation_time         | 2016-11-07T06:17:28Z                                                                                                                                          |
| updated_time          | None                                                                                                                                                          |
| stack_status          | CREATE_COMPLETE                                                                                                                                               |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                           |
| parameters            | OS::stack_id: 278930d7-45e1-4f31-b395-48970a5a238d                                                                                                            |
|                       | OS::stack_name: network_23489ede-80ae-429f-a187-20586e8ba0f4                                                                                                  |
|                       | admin_state_up: 'True'                                                                                                                                        |
|                       | allow_transit: 'False'                                                                                                                                        |
|                       | external: 'True'                                                                                                                                              |
|                       | forwarding_mode: l2_l3                                                                                                                                        |
|                       | name: 23489ede-80ae-429f-a187-20586e8ba0f4                                                                                                                    |
|                       | route_targets: ''                                                                                                                                             |
|                       | shared: 'False'                                                                                                                                               |
|                       | uuid: 23489ede-80ae-429f-a187-20586e8ba0f4                                                                                                                    |
|                       |                                                                                                                                                               |
| outputs               | - description: The name of the virtual network.                                                                                                               |
|                       |   output_key: route_targets                                                                                                                                   |
|                       |   output_value: []                                                                                                                                            |
|                       | - description: The FQ name of the virtual network.                                                                                                            |
|                       |   output_key: fq_name                                                                                                                                         |
|                       |   output_value: default-domain:admin:23489ede-80ae-429f-a187-20586e8ba0f4                                                                                     |
|                       | - description: A unique id for the virtual network.                                                                                                           |
|                       |   output_key: id                                                                                                                                              |
|                       |   output_value: 23489ede-80ae-429f-a187-20586e8ba0f4                                                                                                          |
|                       | - description: The name of the virtual network.                                                                                                               |
|                       |   output_key: name                                                                                                                                            |
|                       |   output_value: 23489ede-80ae-429f-a187-20586e8ba0f4                                                                                                          |
|                       |                                                                                                                                                               |
| links                 | - href: http://172.23.16.61:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/network_23489ede-80ae-429f-a187-20586e8ba0f4/278930d7-45e1-4f31-b395-48970a5a238d |
|                       |   rel: self                                                                                                                                                   |
|                       |                                                                                                                                                               |
| parent                | None                                                                                                                                                          |
| disable_rollback      | True                                                                                                                                                          |
| stack_user_project_id | aee85dff980f4b0f94bed7861765acc7                                                                                                                              |
| stack_owner           | sdp_esi_admin                                                                                                                                                 |
| capabilities          | []                                                                                                                                                            |
| notification_topics   | []                                                                                                                                                            |
| timeout_mins          | 10                                                                                                                                                            |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

* Checking heat-template of network in heat-engine
```
$ openstack stack template show network_23489ede-80ae-429f-a187-20586e8ba0f4
description: 'Network template

  '
heat_template_version: '2013-05-23'
outputs:
  fq_name:
    description: The FQ name of the virtual network.
    value:
      get_attr:
      - network
      - fq_name
  id:
    description: A unique id for the virtual network.
    value:
      get_resource: network
  name:
    description: The name of the virtual network.
    value:
      get_attr:
      - network
      - name
  route_targets:
    description: The name of the virtual network.
    value:
      get_attr:
      - network
      - route_targets
parameters:
  admin_state_up:
    default: true
    label: Admin state up
    type: boolean
  allow_transit:
    default: false
    label: Allow Transit
    type: boolean
  external:
    default: true
    label: External Network
    type: boolean
  forwarding_mode:
    default: l2_l3
    description: Forwarding Mode.
    label: Forwarding Mode
    type: string
  name:
    description: Name of the virtual network that will be created.
    label: Virtual Network Name
    type: string
  route_targets:
    default: []
    label: Route Targets list
    type: comma_delimited_list
  shared:
    default: false
    label: Shared Network
    type: boolean
  uuid:
    default: ''
    description: UUID of the virtual network that will be created.
    label: Virtual Network UUID
    type: string
resources:
  network:
    properties:
      admin_state_up:
        get_param: admin_state_up
      forwarding_mode:
        get_param: forwarding_mode
      name:
        get_param: name
      route_targets:
        get_param: route_targets
      shared:
        get_param: shared
      uuid:
        get_param: uuid
    type: OS::Contrail::VirtualNetwork
```

* Checking resource-list of network in heat-engine
```
$ openstack stack resource list network_23489ede-80ae-429f-a187-20586e8ba0f4
+---------------+--------------------------------------+------------------------------+-----------------+----------------------+
| resource_name | physical_resource_id                 | resource_type                | resource_status | updated_time         |
+---------------+--------------------------------------+------------------------------+-----------------+----------------------+
| network       | 23489ede-80ae-429f-a187-20586e8ba0f4 | OS::Contrail::VirtualNetwork | CREATE_COMPLETE | 2016-11-07T06:17:29Z |
+---------------+--------------------------------------+------------------------------+-----------------+----------------------+
```

* Checking resource-show of network in heat-engine
```
$ openstack stack resource show network_23489ede-80ae-429f-a187-20586e8ba0f4 network
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                  | Value                                                                                                                                                           |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| description            |                                                                                                                                                                 |
| links                  | [{u'href': u'http://172.23.16.61:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/network_23489ede-80ae-                                                         |
|                        | 429f-a187-20586e8ba0f4/278930d7-45e1-4f31-b395-48970a5a238d/resources/network', u'rel': u'self'}, {u'href':                                                     |
|                        | u'http://172.23.16.61:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/network_23489ede-80ae-429f-a187-20586e8ba0f4/278930d7-45e1-4f31-b395-48970a5a238d',       |
|                        | u'rel': u'stack'}]                                                                                                                                              |
| logical_resource_id    | network                                                                                                                                                         |
| physical_resource_id   | 23489ede-80ae-429f-a187-20586e8ba0f4                                                                                                                            |
| required_by            | []                                                                                                                                                              |
| resource_name          | network                                                                                                                                                         |
| resource_status        | CREATE_COMPLETE                                                                                                                                                 |
| resource_status_reason | state changed                                                                                                                                                   |
| resource_type          | OS::Contrail::VirtualNetwork                                                                                                                                    |
| updated_time           | 2016-11-07T06:17:29Z                                                                                                                                            |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
