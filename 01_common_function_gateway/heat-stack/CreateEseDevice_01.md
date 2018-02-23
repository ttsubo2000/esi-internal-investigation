# HTTP Methods for creating heat-stack: ESE Device (existing)

Checking heat-stack of "ese_device" via heatclient.
```
$ heat stack-show ese_device_9f05b260-26ca-46f7-98c3-ad88e411a989
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                       |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                          |
| creation_time         | 2017-05-11T03:04:04Z                                                                                                                                        |
| description           | ESE Device (existing) template                                                                                                                              |
| disable_rollback      | True                                                                                                                                                        |
| id                    | 51374b73-2350-45db-bfcd-4c5021dfd890                                                                                                                        |
| links                 | http://heat-api:8004/v1/0b576f6f4cbf414f829cd12f008bf08f/stacks/ese_device_9f05b260-26ca-46f7-98c3-ad88e411a989/51374b73-2350-45db-bfcd-4c5021dfd890 (self) |
| notification_topics   | []                                                                                                                                                          |
| outputs               | [                                                                                                                                                           |
|                       |   {                                                                                                                                                         |
|                       |     "output_value": [                                                                                                                                       |
|                       |       "default-global-system-config",                                                                                                                       |
|                       |       "QFX-NW02"                                                                                                                                            |
|                       |     ],                                                                                                                                                      |
|                       |     "description": "The FQ name of the physical router.",                                                                                                   |
|                       |     "output_key": "fq_name"                                                                                                                                 |
|                       |   },                                                                                                                                                        |
|                       |   {                                                                                                                                                         |
|                       |     "output_value": "physical_router",                                                                                                                      |
|                       |     "description": "A unique id for the physical router.",                                                                                                  |
|                       |     "output_key": "id"                                                                                                                                      |
|                       |   },                                                                                                                                                        |
|                       |   {                                                                                                                                                         |
|                       |     "output_value": "dummy",                                                                                                                                |
|                       |     "description": "The name of the physical router.",                                                                                                      |
|                       |     "output_key": "name"                                                                                                                                    |
|                       |   }                                                                                                                                                         |
|                       | ]                                                                                                                                                           |
| parameters            | {                                                                                                                                                           |
|                       |   "hostname": "QFX-NW02",                                                                                                                                   |
|                       |   "OS::stack_id": "51374b73-2350-45db-bfcd-4c5021dfd890",                                                                                                   |
|                       |   "OS::stack_name": "ese_device_9f05b260-26ca-46f7-98c3-ad88e411a989",                                                                                      |
|                       |   "name": "QFX-NW02"                                                                                                                                        |
|                       | }                                                                                                                                                           |
| parent                | None                                                                                                                                                        |
| stack_name            | ese_device_9f05b260-26ca-46f7-98c3-ad88e411a989                                                                                                             |
| stack_owner           | admin                                                                                                                                                       |
| stack_status          | CREATE_COMPLETE                                                                                                                                             |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                         |
| stack_user_project_id | 0b576f6f4cbf414f829cd12f008bf08f                                                                                                                            |
| template_description  | ESE Device (existing) template                                                                                                                              |
| timeout_mins          | 10                                                                                                                                                          |
| updated_time          | None                                                                                                                                                        |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "ese_device" via heatclient.
```
$ heat template-show ese_device_9f05b260-26ca-46f7-98c3-ad88e411a989
description: 'ESE Device (existing) template

  '
heat_template_version: '2013-05-23'
outputs:
  fq_name:
    description: The FQ name of the physical router.
    value:
      get_attr: [physical_router, fq_name]
  id:
    description: A unique id for the physical router.
    value: {get_resource: physical_router}
  name:
    description: The name of the physical router.
    value:
      get_attr: [physical_router, name]
parameters:
  hostname: {description: Name of host (vrouter) to create router on, label: Hostname,
    type: string}
  name: {description: Name of the physical router that will be created., label: Physical
      Router Name, type: string}
resources:
  physical_router:
    properties:
      fq_name:
      - default-global-system-config
      - {get_param: hostname}
      resource_type: physical_router
    type: OS::Contrail::ExistingResourc
```