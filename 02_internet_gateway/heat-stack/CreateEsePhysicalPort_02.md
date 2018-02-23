# HTTP Methods for creating heat-stack: Physical port

Checking heat-stack of "ese_physical_port" via heatclient.
```
$ heat stack-show ese_physical_port_8a4bbfe0-5aae-42f5-8b94-c4c14b9e7306
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                              |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                 |
| creation_time         | 2017-05-11T04:23:26Z                                                                                                                                               |
| description           | Physical port template                                                                                                                                             |
| disable_rollback      | True                                                                                                                                                               |
| id                    | 092b33b0-168a-4897-806d-a266936c5049                                                                                                                               |
| links                 | http://heat-api:8004/v1/0b576f6f4cbf414f829cd12f008bf08f/stacks/ese_physical_port_8a4bbfe0-5aae-42f5-8b94-c4c14b9e7306/092b33b0-168a-4897-806d-a266936c5049 (self) |
| notification_topics   | []                                                                                                                                                                 |
| outputs               | [                                                                                                                                                                  |
|                       |   {                                                                                                                                                                |
|                       |     "output_value": "dddddddd-dddd-dddd-dddd-dddddddddddd",                                                                                                        |
|                       |     "description": "A unique id for the physical interface",                                                                                                       |
|                       |     "output_key": "id"                                                                                                                                             |
|                       |   },                                                                                                                                                               |
|                       |   {                                                                                                                                                                |
|                       |     "output_value": null,                                                                                                                                          |
|                       |     "output_error": "'ContrailPhysicalInterface' object has no attribute 'pi_uuid'",                                                                               |
|                       |     "description": "The name of the physical interface.",                                                                                                          |
|                       |     "output_key": "name"                                                                                                                                           |
|                       |   }                                                                                                                                                                |
|                       | ]                                                                                                                                                                  |
| parameters            | {                                                                                                                                                                  |
|                       |   "physical_port_name": "xe-0/0/4",                                                                                                                                |
|                       |   "OS::stack_id": "092b33b0-168a-4897-806d-a266936c5049",                                                                                                          |
|                       |   "OS::stack_name": "ese_physical_port_8a4bbfe0-5aae-42f5-8b94-c4c14b9e7306",                                                                                      |
|                       |   "physical_device": "physical_router"                                                                                                                             |
|                       | }                                                                                                                                                                  |
| parent                | None                                                                                                                                                               |
| stack_name            | ese_physical_port_8a4bbfe0-5aae-42f5-8b94-c4c14b9e7306                                                                                                             |
| stack_owner           | admin                                                                                                                                                              |
| stack_status          | CREATE_COMPLETE                                                                                                                                                    |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                |
| stack_user_project_id | 0b576f6f4cbf414f829cd12f008bf08f                                                                                                                                   |
| template_description  | Physical port template                                                                                                                                             |
| timeout_mins          | 10                                                                                                                                                                 |
| updated_time          | None                                                                                                                                                               |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "ese_physical_port" via heatclient.
```
$ heat template-show ese_physical_port_8a4bbfe0-5aae-42f5-8b94-c4c14b9e7306
description: 'Physical port template

  '
heat_template_version: '2013-05-23'
outputs:
  id:
    description: A unique id for the physical interface
    value: {get_resource: physical_interface}
  name:
    description: The name of the physical interface.
    value:
      get_attr: [physical_interface, name]
parameters:
  physical_device: {description: Id of the physical device on which physical port
      will be created., label: Physical Device Id, type: string}
  physical_port_name: {description: Name of the physical port., label: Physical Interface
      Name, type: string}
resources:
  physical_interface:
    properties:
      name: {get_param: physical_port_name}
      physical_router: {get_param: physical_device}
    type: OS::Contrail::PhysicalInterface
```
