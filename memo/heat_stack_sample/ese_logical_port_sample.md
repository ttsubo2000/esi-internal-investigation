## Sample of heat-stack of ese_logical_port

* Checking heat-stack of ese_logical_port in heat-engine
```
$ openstack stack show ese_logical_port_c6997498-6064-4346-a07b-1b6235229dc4
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                 | Value                                                                                                                                                            |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| id                    | b3698728-d246-4b98-8440-330f6a95c56d                                                                                                                             |
| stack_name            | ese_logical_port_c6997498-6064-4346-a07b-1b6235229dc4                                                                                                            |
| description           | Logical port template                                                                                                                                            |
|                       |                                                                                                                                                                  |
| creation_time         | 2016-11-07T06:17:44Z                                                                                                                                             |
| updated_time          | None                                                                                                                                                             |
| stack_status          | CREATE_COMPLETE                                                                                                                                                  |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                              |
| parameters            | OS::stack_id: b3698728-d246-4b98-8440-330f6a95c56d                                                                                                               |
|                       | OS::stack_name: ese_logical_port_c6997498-6064-4346-a07b-1b6235229dc4                                                                                            |
|                       | logical_port_name: xe-0/0/0.11                                                                                                                                   |
|                       | logical_port_type: L2                                                                                                                                            |
|                       | logical_port_vlan_id: '11'                                                                                                                                       |
|                       | physical_port_id: 5638e478-cc55-490c-97dc-00fae54c9fb3                                                                                                           |
|                       | virtual_machine_interface_ids: 82b37a87-b6ca-4906-82a1-3a8db86b26ac                                                                                              |
|                       |                                                                                                                                                                  |
| outputs               | - description: A unique id for the logical interface                                                                                                             |
|                       |   output_key: id                                                                                                                                                 |
|                       |   output_value: 8beb9af0-29dc-4030-8110-12368fa80d18                                                                                                             |
|                       | - description: The name of the logical interface.                                                                                                                |
|                       |   output_key: name                                                                                                                                               |
|                       |   output_value: xe-0/0/0.11                                                                                                                                      |
|                       |                                                                                                                                                                  |
| links                 | - href: http://172.23.16.61:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/ese_logical_port_c6997498-6064-4346-a07b-                                            |
|                       | 1b6235229dc4/b3698728-d246-4b98-8440-330f6a95c56d                                                                                                                |
|                       |   rel: self                                                                                                                                                      |
|                       |                                                                                                                                                                  |
| parent                | None                                                                                                                                                             |
| disable_rollback      | True                                                                                                                                                             |
| stack_user_project_id | aee85dff980f4b0f94bed7861765acc7                                                                                                                                 |
| stack_owner           | sdp_esi_admin                                                                                                                                                    |
| capabilities          | []                                                                                                                                                               |
| notification_topics   | []                                                                                                                                                               |
| timeout_mins          | 10                                                                                                                                                               |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

* Checking heat-template of ese_logical_port in heat-engine
```
$ openstack stack template show ese_logical_port_c6997498-6064-4346-a07b-1b6235229dc4
description: 'Logical port template

  '
heat_template_version: '2013-05-23'
outputs:
  id:
    description: A unique id for the logical interface
    value:
      get_resource: logical_interface
  name:
    description: The name of the logical interface.
    value:
      get_attr:
      - logical_interface
      - name
parameters:
  logical_port_name:
    description: Name of the logical port.
    label: Logical Port Name
    type: string
  logical_port_type:
    description: Type of the logical port.
    label: Logical Port Type
    type: string
  logical_port_vlan_id:
    default: 0
    description: VLAN id to use for logical port creation.
    label: VLAN id for Logical Port
    type: number
  physical_port_id:
    description: A unique id for the Physical Interface.
    label: Physical Interface ID
    type: string
  virtual_machine_interface_ids:
    description: Virtual Machine Interface ID.
    label: Virtual Machine Interface ID
    type: comma_delimited_list
resources:
  logical_interface:
    properties:
      name:
        get_param: logical_port_name
      physical_interface:
        get_param: physical_port_id
      type:
        get_param: logical_port_type
      virtual_machine_interfaces:
        get_param: virtual_machine_interface_ids
      vlan:
        get_param: logical_port_vlan_id
    type: OS::Contrail::LogicalInterface
```

* Checking resource-list of ese_logical_port in heat-engine
```
$ openstack stack resource list ese_logical_port_c6997498-6064-4346-a07b-1b6235229dc4
+-------------------+--------------------------------------+--------------------------------+-----------------+----------------------+
| resource_name     | physical_resource_id                 | resource_type                  | resource_status | updated_time         |
+-------------------+--------------------------------------+--------------------------------+-----------------+----------------------+
| logical_interface | 8beb9af0-29dc-4030-8110-12368fa80d18 | OS::Contrail::LogicalInterface | CREATE_COMPLETE | 2016-11-07T06:17:44Z |
+-------------------+--------------------------------------+--------------------------------+-----------------+----------------------+
```

* Checking resource-show of logical_interface in heat-engine
```
$ openstack stack resource show ese_logical_port_c6997498-6064-4346-a07b-1b6235229dc4 logical_interface
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                  | Value                                                                                                                                                           |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| description            |                                                                                                                                                                 |
| links                  | [{u'href': u'http://172.23.16.61:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/ese_logical_port_c6997498-6064-4346-a07b-                                      |
|                        | 1b6235229dc4/b3698728-d246-4b98-8440-330f6a95c56d/resources/logical_interface', u'rel': u'self'}, {u'href':                                                     |
|                        | u'http://172.23.16.61:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/ese_logical_port_c6997498-6064-4346-a07b-                                                 |
|                        | 1b6235229dc4/b3698728-d246-4b98-8440-330f6a95c56d', u'rel': u'stack'}]                                                                                          |
| logical_resource_id    | logical_interface                                                                                                                                               |
| physical_resource_id   | 8beb9af0-29dc-4030-8110-12368fa80d18                                                                                                                            |
| required_by            | []                                                                                                                                                              |
| resource_name          | logical_interface                                                                                                                                               |
| resource_status        | CREATE_COMPLETE                                                                                                                                                 |
| resource_status_reason | state changed                                                                                                                                                   |
| resource_type          | OS::Contrail::LogicalInterface                                                                                                                                  |
| updated_time           | 2016-11-07T06:17:44Z                                                                                                                                            |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
