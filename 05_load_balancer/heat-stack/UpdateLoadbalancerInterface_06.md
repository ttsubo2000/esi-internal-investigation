# HTTP Methods for updating heat-stack: Load Balancer Configuration

Checking heat-stack of "load_balancer_interface" via heatclient.
```
$ heat stack-show load_balancer_interface_7f2bef0a-26f3-4ec9-89de-1aee7f04f998
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                                 |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                                    |
| creation_time         | 2018-02-19T05:22:00Z                                                                                                                                                                                  |
| description           | Load Balancer Interface                                                                                                                                                                               |
| disable_rollback      | True                                                                                                                                                                                                  |
| id                    | c3786773-ec5e-483d-8f86-c59b5dcaed0f                                                                                                                                                                  |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/fe3a4a1a72c04479bb6c19c2c0ccba4c/stacks/load_balancer_interface_7f2bef0a-26f3-4ec9-89de-1aee7f04f998/c3786773-ec5e-483d-8f86-c59b5dcaed0f |
| notification_topics   | []                                                                                                                                                                                                    |
| outputs               | [                                                                                                                                                                                                     |
|                       |   {                                                                                                                                                                                                   |
|                       |     "output_value": "c2ad3511-dcc2-4e31-9702-a2e01ea39b27",                                                                                                                                           |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                            |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                              |
|                       |   },                                                                                                                                                                                                  |
|                       |   {                                                                                                                                                                                                   |
|                       |     "output_value": "http://collector-agents-se:7070/targets/c2ad3511-dcc2-4e31-9702-a2e01ea39b27",                                                                                                   |
|                       |     "description": "Monitoring Process Link",                                                                                                                                                         |
|                       |     "output_key": "monitoring_link"                                                                                                                                                                   |
|                       |   }                                                                                                                                                                                                   |
|                       | ]                                                                                                                                                                                                     |
| parameters            | {                                                                                                                                                                                                     |
|                       |   "OS::stack_id": "c3786773-ec5e-483d-8f86-c59b5dcaed0f",                                                                                                                                             |
|                       |   "OS::stack_name": "load_balancer_interface_7f2bef0a-26f3-4ec9-89de-1aee7f04f998",                                                                                                                   |
|                       |   "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c",                                                                                                                                                    |
|                       |   "management_ip": "100.64.193.3",                                                                                                                                                                    |
|                       |   "version": "1",                                                                                                                                                                                     |
|                       |   "gohan_id": "7f2bef0a-26f3-4ec9-89de-1aee7f04f998"                                                                                                                                                  |
|                       | }                                                                                                                                                                                                     |
| parent                | None                                                                                                                                                                                                  |
| stack_name            | load_balancer_interface_7f2bef0a-26f3-4ec9-89de-1aee7f04f998                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                                 |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                                       |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                                   |
| stack_user_project_id | fe3a4a1a72c04479bb6c19c2c0ccba4c                                                                                                                                                                      |
| template_description  | Load Balancer Interface                                                                                                                                                                               |
| timeout_mins          | 3                                                                                                                                                                                                     |
| updated_time          | None                                                                                                                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "load_balancer_interface" via heatclient.
```
$ heat template-show load_balancer_interface_7f2bef0a-26f3-4ec9-89de-1aee7f04f998
description: Load Balancer Interface
heat_template_version: '2013-05-23'
outputs:
  monitoring_link:
    description: Monitoring Process Link
    value:
      get_attr: [lb_interface_monitor, link]
  monitoring_target_id:
    description: Monitoring Target ID
    value: {get_resource: lb_interface_monitor}
parameters:
  gohan_id: {description: UUID of the VNF Instance, label: Gohan resource ID, type: string}
  management_ip: {type: string}
  tenant_id: {label: Tenant ID, type: string}
  version: {label: Config version, type: number}
resources:
  lb_interface_monitor:
    properties:
      field_name: interface
      properties:
        community_name: LOAD_BALANCER_COMMUNITY
        device_ip: {get_param: management_ip}
        if_name: 1/2
      resource_id: {get_param: gohan_id}
      resource_type: load_balancer_interfaces
      syncer_properties:
        etcd:
          status: {key: interface}
        tsdb:
          traffic.in:
            metric: traffic.bytes
            tags:
              direction: in
              resource_id: {get_param: gohan_id}
          traffic.out:
            metric: traffic.bytes
            tags:
              direction: out
              resource_id: {get_param: gohan_id}
      tenant_id: {get_param: tenant_id}
      type: snmp_ports
      version: {get_param: version}
    type: ESI::Monitoring::MonitoringTarget
```
