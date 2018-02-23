## Sample of heat-stack of ese_physical_port

* Checking heat-stack of ese_physical_port in heat-engine
```
$ openstack stack show ese_physical_port_054a331c-5095-4aff-93f1-fc2b517522ac
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                 | Value                                                                                                                                                            |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| id                    | ed4e58dc-abce-4ef8-8e97-507652427ccc                                                                                                                             |
| stack_name            | ese_physical_port_054a331c-5095-4aff-93f1-fc2b517522ac                                                                                                           |
| description           | Physical port template                                                                                                                                           |
|                       |                                                                                                                                                                  |
| creation_time         | 2016-11-07T06:17:27Z                                                                                                                                             |
| updated_time          | None                                                                                                                                                             |
| stack_status          | CREATE_COMPLETE                                                                                                                                                  |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                              |
| parameters            | OS::stack_id: ed4e58dc-abce-4ef8-8e97-507652427ccc                                                                                                               |
|                       | OS::stack_name: ese_physical_port_054a331c-5095-4aff-93f1-fc2b517522ac                                                                                           |
|                       | physical_device_hostname: NWSDP-JNPR-04                                                                                                                          |
|                       | physical_port_name: xe-0/0/0                                                                                                                                     |
|                       |                                                                                                                                                                  |
| outputs               | - description: A unique id for the physical interface                                                                                                            |
|                       |   output_key: id                                                                                                                                                 |
|                       |   output_value: 5638e478-cc55-490c-97dc-00fae54c9fb3                                                                                                             |
|                       | - description: The name of the physical interface.                                                                                                               |
|                       |   output_key: name                                                                                                                                               |
|                       |   output_value: xe-0/0/0                                                                                                                                         |
|                       |                                                                                                                                                                  |
| links                 | - href: http://172.23.16.61:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/ese_physical_port_054a331c-5095-4aff-93f1-fc2b517522ac/ed4e58dc-abce-                |
|                       | 4ef8-8e97-507652427ccc                                                                                                                                           |
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

* Checking heat-template of ese_physical_port in heat-engine
```
$ openstack stack template show ese_physical_port_054a331c-5095-4aff-93f1-fc2b517522ac
description: 'Physical port template

  '
heat_template_version: '2013-05-23'
outputs:
  id:
    description: A unique id for the physical interface
    value:
      get_resource: physical_interface
  name:
    description: The name of the physical interface.
    value:
      get_attr:
      - physical_interface
      - name
parameters:
  physical_device_hostname:
    description: Hostname of the physical device on which physical port will be created.
    label: Physical Device Hostname
    type: string
  physical_port_name:
    description: Name of the physical port.
    label: Physical Interface Name
    type: string
resources:
  physical_interface:
    properties:
      fq_name:
      - default-global-system-config
      - get_param: physical_device_hostname
      - get_param: physical_port_name
      resource_type: physical_interface
    type: OS::Contrail::ExistingResource
```

* Checking resource-list of ese_physical_port in heat-engine
```
$ openstack stack resource list ese_physical_port_054a331c-5095-4aff-93f1-fc2b517522ac
+--------------------+--------------------------------------+--------------------------------+-----------------+----------------------+
| resource_name      | physical_resource_id                 | resource_type                  | resource_status | updated_time         |
+--------------------+--------------------------------------+--------------------------------+-----------------+----------------------+
| physical_interface | 5638e478-cc55-490c-97dc-00fae54c9fb3 | OS::Contrail::ExistingResource | CREATE_COMPLETE | 2016-11-07T06:17:27Z |
+--------------------+--------------------------------------+--------------------------------+-----------------+----------------------+
```

* Checking resource-show of physical_interface in heat-engine
```
$ openstack stack resource show ese_physical_port_054a331c-5095-4aff-93f1-fc2b517522ac physical_interface
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                  | Value                                                                                                                                                           |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| description            |                                                                                                                                                                 |
| links                  | [{u'href': u'http://172.23.16.61:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/ese_physical_port_054a331c-5095-4aff-93f1-fc2b517522ac/ed4e58dc-abce-          |
|                        | 4ef8-8e97-507652427ccc/resources/physical_interface', u'rel': u'self'}, {u'href':                                                                               |
|                        | u'http://172.23.16.61:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/ese_physical_port_054a331c-5095-4aff-93f1-fc2b517522ac/ed4e58dc-abce-                     |
|                        | 4ef8-8e97-507652427ccc', u'rel': u'stack'}]                                                                                                                     |
| logical_resource_id    | physical_interface                                                                                                                                              |
| physical_resource_id   | 5638e478-cc55-490c-97dc-00fae54c9fb3                                                                                                                            |
| required_by            | []                                                                                                                                                              |
| resource_name          | physical_interface                                                                                                                                              |
| resource_status        | CREATE_COMPLETE                                                                                                                                                 |
| resource_status_reason | state changed                                                                                                                                                   |
| resource_type          | OS::Contrail::ExistingResource                                                                                                                                  |
| updated_time           | 2016-11-07T06:17:27Z                                                                                                                                            |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
