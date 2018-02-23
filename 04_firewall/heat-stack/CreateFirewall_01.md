# HTTP Methods for creating heat-stack: VNF Instance

Checking heat-stack of "vnf_instance" via heatclient.
```
$ heat stack-show vnf_instance_44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                      |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                         |
| creation_time         | 2018-02-12T07:40:05Z                                                                                                                                                                       |
| description           | VNF Instance                                                                                                                                                                               |
| disable_rollback      | True                                                                                                                                                                                       |
| id                    | 6c86b4aa-feb2-4005-9ad5-b1084ce8dd7c                                                                                                                                                       |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/0f40dffa48614d9baa7eaac7e7532099/stacks/vnf_instance_44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb/6c86b4aa-feb2-4005-9ad5-b1084ce8dd7c |
| notification_topics   | []                                                                                                                                                                                         |
| outputs               | [                                                                                                                                                                                          |
|                       |   {                                                                                                                                                                                        |
|                       |     "output_value": "2e555b09-e0d7-4cce-8854-c481a2363917",                                                                                                                                |
|                       |     "description": "A unique id for the nova server.",                                                                                                                                     |
|                       |     "output_key": "server_id"                                                                                                                                                              |
|                       |   },                                                                                                                                                                                       |
|                       |   {                                                                                                                                                                                        |
|                       |     "output_value": "4d5db024-8232-458d-bd72-7256fbceb446",                                                                                                                                |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                 |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                   |
|                       |   },                                                                                                                                                                                       |
|                       |   {                                                                                                                                                                                        |
|                       |     "output_value": "http://collector-agents-se:7070/targets/4d5db024-8232-458d-bd72-7256fbceb446",                                                                                        |
|                       |     "description": "Monitoring Process Link",                                                                                                                                              |
|                       |     "output_key": "monitoring_link"                                                                                                                                                        |
|                       |   }                                                                                                                                                                                        |
|                       | ]                                                                                                                                                                                          |
| parameters            | {                                                                                                                                                                                          |
|                       |   "user_data_format": "RAW",                                                                                                                                                               |
|                       |   "OS::stack_id": "6c86b4aa-feb2-4005-9ad5-b1084ce8dd7c",                                                                                                                                  |
|                       |   "OS::stack_name": "vnf_instance_44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb",                                                                                                                   |
|                       |   "availability_zone": "nova",                                                                                                                                                             |
|                       |   "tenant_id": "0f40dffa48614d9baa7eaac7e7532099",                                                                                                                                         |
|                       |   "image": "vyatta-0108-2016",                                                                                                                                                             |
|                       |   "reboot": "",                                                                                                                                                                            |
|                       |   "user_data": "",                                                                                                                                                                         |
|                       |   "version": "1",                                                                                                                                                                          |
|                       |   "gohan_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb",                                                                                                                                      |
|                       |   "flavor": "m1.large",                                                                                                                                                                    |
|                       |   "name": "firewall-8e4c20be-d221-43f4-8325-0162c1f06166",                                                                                                                                 |
|                       |   "networks": "[{\"port\": \"cdde9cfd-a898-4911-b812-b6849f611549\"}, {\"port\": \"dea87c7b-b43f-4936-8e32-8995b038b3f8\"}, {\"port\": \"fd09eda4-10b1-4534-984a-7124c338c69d\"}]",        |
|                       |   "config_drive": "False"                                                                                                                                                                  |
|                       | }                                                                                                                                                                                          |
| parent                | None                                                                                                                                                                                       |
| stack_name            | vnf_instance_44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                      |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                            |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                        |
| stack_user_project_id | 0f40dffa48614d9baa7eaac7e7532099                                                                                                                                                           |
| template_description  | VNF Instance                                                                                                                                                                               |
| timeout_mins          | 18                                                                                                                                                                                         |
| updated_time          | None                                                                                                                                                                                       |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "vnf_instance" via heatclient.
```
$ heat template-show vnf_instance_44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb
description: VNF Instance
heat_template_version: '2013-05-23'
outputs:
  monitoring_link:
    description: Monitoring Process Link
    value:
      get_attr: [server_monitor, link]
  monitoring_target_id:
    description: Monitoring Target ID
    value: {get_resource: server_monitor}
  server_id:
    description: A unique id for the nova server.
    value: {get_resource: server}
parameters:
  availability_zone: {default: '', type: string}
  config_drive: {type: boolean}
  flavor:
    constraints:
    - {custom_constraint: nova.flavor}
    type: string
  gohan_id: {description: UUID of the VNF Instance, label: Gohan resource ID, type: string}
  image:
    constraints:
    - {custom_constraint: glance.image}
    type: string
  name: {default: '', type: string}
  networks: {type: json}
  reboot: {default: '', type: string}
  tenant_id: {label: Tenant ID, type: string}
  user_data: {default: '', type: string}
  user_data_format: {type: string}
  version: {label: Config version, type: number}
resources:
  server:
    properties:
      availability_zone: {get_param: availability_zone}
      config_drive: {get_param: config_drive}
      flavor: {get_param: flavor}
      image: {get_param: image}
      name: {get_param: name}
      networks: {get_param: networks}
      reboot: {get_param: reboot}
      user_data: {get_param: user_data}
      user_data_format: {get_param: user_data_format}
    type: ESI::VNF::Instance
  server_monitor:
    depends_on: server
    properties:
      field_name: server
      properties:
        server_id: {get_resource: server}
      resource_id: {get_param: gohan_id}
      resource_type: vnf_instances
      syncer_properties:
        etcd:
          status: {key: server}
      tenant_id: {get_param: tenant_id}
      type: compute
      version: {get_param: version}
    type: ESI::Monitoring::MonitoringTarget
```
