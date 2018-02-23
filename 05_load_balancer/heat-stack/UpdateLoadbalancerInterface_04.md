# HTTP Methods for updating heat-stack: Load Balancer Configuration

Checking heat-stack of "load_balancer_interface" via heatclient.
```
$ heat stack-show load_balancer_interface_63121c05-53c3-4cff-9c27-5d4055541a63
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                                 |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                                    |
| creation_time         | 2018-02-19T05:22:00Z                                                                                                                                                                                  |
| description           | Load Balancer Interface                                                                                                                                                                               |
| disable_rollback      | True                                                                                                                                                                                                  |
| id                    | b9b0c0bf-07d4-4ff5-b2b6-2325d4c1f919                                                                                                                                                                  |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/fe3a4a1a72c04479bb6c19c2c0ccba4c/stacks/load_balancer_interface_63121c05-53c3-4cff-9c27-5d4055541a63/b9b0c0bf-07d4-4ff5-b2b6-2325d4c1f919 |
| notification_topics   | []                                                                                                                                                                                                    |
| outputs               | [                                                                                                                                                                                                     |
|                       |   {                                                                                                                                                                                                   |
|                       |     "output_value": "130f173c-2799-4337-8ee5-d1a93a9882a9",                                                                                                                                           |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                            |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                              |
|                       |   },                                                                                                                                                                                                  |
|                       |   {                                                                                                                                                                                                   |
|                       |     "output_value": "http://collector-agents-se:7070/targets/130f173c-2799-4337-8ee5-d1a93a9882a9",                                                                                                   |
|                       |     "description": "Monitoring Process Link",                                                                                                                                                         |
|                       |     "output_key": "monitoring_link"                                                                                                                                                                   |
|                       |   }                                                                                                                                                                                                   |
|                       | ]                                                                                                                                                                                                     |
| parameters            | {                                                                                                                                                                                                     |
|                       |   "OS::stack_id": "b9b0c0bf-07d4-4ff5-b2b6-2325d4c1f919",                                                                                                                                             |
|                       |   "OS::stack_name": "load_balancer_interface_63121c05-53c3-4cff-9c27-5d4055541a63",                                                                                                                   |
|                       |   "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c",                                                                                                                                                    |
|                       |   "management_ip": "100.64.193.3",                                                                                                                                                                    |
|                       |   "version": "1",                                                                                                                                                                                     |
|                       |   "gohan_id": "63121c05-53c3-4cff-9c27-5d4055541a63"                                                                                                                                                  |
|                       | }                                                                                                                                                                                                     |
| parent                | None                                                                                                                                                                                                  |
| stack_name            | load_balancer_interface_63121c05-53c3-4cff-9c27-5d4055541a63                                                                                                                                          |
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
$ heat template-show load_balancer_interface_63121c05-53c3-4cff-9c27-5d4055541a63
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
        if_name: 0/1
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
