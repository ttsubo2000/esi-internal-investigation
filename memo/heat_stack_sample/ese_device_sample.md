## Sample of heat-stack of ese_device

* Checking heat-stack of ese_device in heat-engine
```
$ openstack stack show ese_device_0b521a9f-fb10-47f4-8929-9d43363ac3b7
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                 | Value                                                                                                                                                            |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| id                    | 9b5ef88a-3d21-4794-a14f-8af0a14026ba                                                                                                                             |
| stack_name            | ese_device_0b521a9f-fb10-47f4-8929-9d43363ac3b7                                                                                                                  |
| description           | ESE Device (existing) template                                                                                                                                   |
|                       |                                                                                                                                                                  |
| creation_time         | 2016-11-07T04:01:58Z                                                                                                                                             |
| updated_time          | None                                                                                                                                                             |
| stack_status          | CREATE_COMPLETE                                                                                                                                                  |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                              |
| parameters            | OS::stack_id: 9b5ef88a-3d21-4794-a14f-8af0a14026ba                                                                                                               |
|                       | OS::stack_name: ese_device_0b521a9f-fb10-47f4-8929-9d43363ac3b7                                                                                                  |
|                       | hostname: NWSDP-JNPR-03                                                                                                                                          |
|                       | name: NWSDP-JNPR-03                                                                                                                                              |
|                       |                                                                                                                                                                  |
| outputs               | - description: The FQ name of the physical router.                                                                                                               |
|                       |   output_key: fq_name                                                                                                                                            |
|                       |   output_value:                                                                                                                                                  |
|                       |   - default-global-system-config                                                                                                                                 |
|                       |   - NWSDP-JNPR-03                                                                                                                                                |
|                       | - description: A unique id for the physical router.                                                                                                              |
|                       |   output_key: id                                                                                                                                                 |
|                       |   output_value: 89265d86-a0ed-4fa5-b098-4e8358405c93                                                                                                             |
|                       | - description: The name of the physical router.                                                                                                                  |
|                       |   output_key: name                                                                                                                                               |
|                       |   output_value: NWSDP-JNPR-03                                                                                                                                    |
|                       |                                                                                                                                                                  |
| links                 | - href: http://172.23.16.61:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/ese_device_0b521a9f-fb10-47f4-8929-9d43363ac3b7/9b5ef88a-3d21-4794-a14f-8af0a14026ba |
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

* Checking heat-template of ese_device in heat-engine
```
$ openstack stack template show ese_device_0b521a9f-fb10-47f4-8929-9d43363ac3b7
description: 'ESE Device (existing) template

  '
heat_template_version: '2013-05-23'
outputs:
  fq_name:
    description: The FQ name of the physical router.
    value:
      get_attr:
      - physical_router
      - fq_name
  id:
    description: A unique id for the physical router.
    value:
      get_resource: physical_router
  name:
    description: The name of the physical router.
    value:
      get_attr:
      - physical_router
      - name
parameters:
  hostname:
    description: Name of host (vrouter) to create router on
    label: Hostname
    type: string
  name:
    description: Name of the physical router that will be created.
    label: Physical Router Name
    type: string
resources:
  physical_router:
    properties:
      fq_name:
      - default-global-system-config
      - get_param: hostname
      resource_type: physical_router
    type: OS::Contrail::ExistingResource
```

* Checking resource-list of ese_device in heat-engine
```
$ openstack stack resource list ese_device_0b521a9f-fb10-47f4-8929-9d43363ac3b7
+-----------------+--------------------------------------+--------------------------------+-----------------+----------------------+
| resource_name   | physical_resource_id                 | resource_type                  | resource_status | updated_time         |
+-----------------+--------------------------------------+--------------------------------+-----------------+----------------------+
| physical_router | 89265d86-a0ed-4fa5-b098-4e8358405c93 | OS::Contrail::ExistingResource | CREATE_COMPLETE | 2016-11-07T04:01:58Z |
+-----------------+--------------------------------------+--------------------------------+-----------------+----------------------+
```

* Checking resource-show of physical_router in heat-engine
```
$ openstack stack resource show ese_device_0b521a9f-fb10-47f4-8929-9d43363ac3b7 physical_router
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                  | Value                                                                                                                                                           |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| description            |                                                                                                                                                                 |
| links                  | [{u'href': u'http://172.23.16.61:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/ese_device_0b521a9f-fb10-47f4-8929-9d43363ac3b7/9b5ef88a-3d21-4794-a14f-       |
|                        | 8af0a14026ba/resources/physical_router', u'rel': u'self'}, {u'href': u'http://172.23.16.61:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/ese_device_0b521a9f- |
|                        | fb10-47f4-8929-9d43363ac3b7/9b5ef88a-3d21-4794-a14f-8af0a14026ba', u'rel': u'stack'}]                                                                           |
| logical_resource_id    | physical_router                                                                                                                                                 |
| physical_resource_id   | 89265d86-a0ed-4fa5-b098-4e8358405c93                                                                                                                            |
| required_by            | []                                                                                                                                                              |
| resource_name          | physical_router                                                                                                                                                 |
| resource_status        | CREATE_COMPLETE                                                                                                                                                 |
| resource_status_reason | state changed                                                                                                                                                   |
| resource_type          | OS::Contrail::ExistingResource                                                                                                                                  |
| updated_time           | 2016-11-07T04:01:58Z                                                                                                                                            |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
