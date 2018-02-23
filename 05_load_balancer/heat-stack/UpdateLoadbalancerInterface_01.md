# HTTP Methods for updating heat-stack: Virtual Machine Interface

Checking heat-stack of "vnf_instance" via heatclient.
```
$ heat stack-show vnf_instance_398d65ba-0060-456e-b415-5bc954450717
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                      |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                         |
| creation_time         | 2018-02-19T05:17:10Z                                                                                                                                                                       |
| description           | VNF Instance                                                                                                                                                                               |
| disable_rollback      | True                                                                                                                                                                                       |
| id                    | 7461d1b4-6e2e-4168-a3ff-574af81e9de5                                                                                                                                                       |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/fe3a4a1a72c04479bb6c19c2c0ccba4c/stacks/vnf_instance_398d65ba-0060-456e-b415-5bc954450717/7461d1b4-6e2e-4168-a3ff-574af81e9de5 |
| notification_topics   | []                                                                                                                                                                                         |
| outputs               | [                                                                                                                                                                                          |
|                       |   {                                                                                                                                                                                        |
|                       |     "output_value": "47531b14-72e9-439d-8949-fd941457ecde",                                                                                                                                |
|                       |     "description": "A unique id for the nova server.",                                                                                                                                     |
|                       |     "output_key": "server_id"                                                                                                                                                              |
|                       |   },                                                                                                                                                                                       |
|                       |   {                                                                                                                                                                                        |
|                       |     "output_value": "ed1b9e59-0d6f-44d9-83bc-07ba4a236598",                                                                                                                                |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                 |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                   |
|                       |   },                                                                                                                                                                                       |
|                       |   {                                                                                                                                                                                        |
|                       |     "output_value": "http://collector-agents-se:7070/targets/ed1b9e59-0d6f-44d9-83bc-07ba4a236598",                                                                                        |
|                       |     "description": "Monitoring Process Link",                                                                                                                                              |
|                       |     "output_key": "monitoring_link"                                                                                                                                                        |
|                       |   }                                                                                                                                                                                        |
|                       | ]                                                                                                                                                                                          |
| parameters            | {                                                                                                                                                                                          |
|                       |   "user_data_format": "RAW",                                                                                                                                                               |
|                       |   "OS::stack_id": "7461d1b4-6e2e-4168-a3ff-574af81e9de5",                                                                                                                                  |
|                       |   "OS::stack_name": "vnf_instance_398d65ba-0060-456e-b415-5bc954450717",                                                                                                                   |
|                       |   "availability_zone": "nova",                                                                                                                                                             |
|                       |   "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c",                                                                                                                                         |
|                       |   "image": "NSVPX-KVM-10.5-57.7_nc",                                                                                                                                                       |
|                       |   "reboot": "",                                                                                                                                                                            |
|                       |   "user_data": "",                                                                                                                                                                         |
|                       |   "version": "2",                                                                                                                                                                          |
|                       |   "gohan_id": "398d65ba-0060-456e-b415-5bc954450717",                                                                                                                                      |
|                       |   "flavor": "m1.xlarge",                                                                                                                                                                   |
|                       |   "name": "load_balancer-b311c470-d878-4fea-8466-a4393938f2d4",                                                                                                                            |
|                       |   "networks": "[{\"port\": \"ddc14be4-3480-4e97-a978-817b18f9904c\"}, {\"port\": \"23464cbc-d910-430a-93f7-3776ea07f992\"}, {\"port\": \"a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f\"}]",        |
|                       |   "config_drive": "False"                                                                                                                                                                  |
|                       | }                                                                                                                                                                                          |
| parent                | None                                                                                                                                                                                       |
| stack_name            | vnf_instance_398d65ba-0060-456e-b415-5bc954450717                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                      |
| stack_status          | UPDATE_COMPLETE                                                                                                                                                                            |
| stack_status_reason   | Stack successfully updated                                                                                                                                                                 |
| stack_user_project_id | fe3a4a1a72c04479bb6c19c2c0ccba4c                                                                                                                                                           |
| template_description  | VNF Instance                                                                                                                                                                               |
| timeout_mins          | 18                                                                                                                                                                                         |
| updated_time          | 2018-02-19T05:24:12Z                                                                                                                                                                       |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "vnf_instance" via heatclient.
```
$ heat template-show vnf_instance_398d65ba-0060-456e-b415-5bc954450717
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
