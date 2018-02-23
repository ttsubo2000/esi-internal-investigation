# HTTP Methods for creating heat-stack: Vyatta Firewall Configuration
  
Checking heat-stack of "firewall_interface (dp0s3)" via heatclient.
```
$ heat stack-show firewall_interface_1c351257-d185-40b7-b04a-6272de75d434
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                            |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                               |
| creation_time         | 2018-02-12T07:44:52Z                                                                                                                                                                             |
| description           | Vyatta Firewall Interface                                                                                                                                                                        |
| disable_rollback      | True                                                                                                                                                                                             |
| id                    | aca233ed-4f80-443a-bbc5-55116560d4f1                                                                                                                                                             |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/0f40dffa48614d9baa7eaac7e7532099/stacks/firewall_interface_1c351257-d185-40b7-b04a-6272de75d434/aca233ed-4f80-443a-bbc5-55116560d4f1 |
| notification_topics   | []                                                                                                                                                                                               |
| outputs               | [                                                                                                                                                                                                |
|                       |   {                                                                                                                                                                                              |
|                       |     "output_value": "ecbc7461-e883-4c21-bcf6-b91a105a533c",                                                                                                                                      |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                       |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                         |
|                       |   },                                                                                                                                                                                             |
|                       |   {                                                                                                                                                                                              |
|                       |     "output_value": "http://collector-agents-se:7070/targets/ecbc7461-e883-4c21-bcf6-b91a105a533c",                                                                                              |
|                       |     "description": "Monitoring Process Link",                                                                                                                                                    |
|                       |     "output_key": "monitoring_link"                                                                                                                                                              |
|                       |   }                                                                                                                                                                                              |
|                       | ]                                                                                                                                                                                                |
| parameters            | {                                                                                                                                                                                                |
|                       |   "OS::stack_id": "aca233ed-4f80-443a-bbc5-55116560d4f1",                                                                                                                                        |
|                       |   "OS::stack_name": "firewall_interface_1c351257-d185-40b7-b04a-6272de75d434",                                                                                                                   |
|                       |   "tenant_id": "0f40dffa48614d9baa7eaac7e7532099",                                                                                                                                               |
|                       |   "management_ip": "100.64.193.3",                                                                                                                                                               |
|                       |   "version": "1",                                                                                                                                                                                |
|                       |   "gohan_id": "1c351257-d185-40b7-b04a-6272de75d434"                                                                                                                                             |
|                       | }                                                                                                                                                                                                |
| parent                | None                                                                                                                                                                                             |
| stack_name            | firewall_interface_1c351257-d185-40b7-b04a-6272de75d434                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                            |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                                  |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                              |
| stack_user_project_id | 0f40dffa48614d9baa7eaac7e7532099                                                                                                                                                                 |
| template_description  | Vyatta Firewall Interface                                                                                                                                                                        |
| timeout_mins          | 3                                                                                                                                                                                                |
| updated_time          | None                                                                                                                                                                                             |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "firewall_interface (dp0s3)" via heatclient.
```
$ heat template-show firewall_interface_1c351257-d185-40b7-b04a-6272de75d434
description: Vyatta Firewall Interface
heat_template_version: '2013-05-23'
outputs:
  monitoring_link:
    description: Monitoring Process Link
    value:
      get_attr: [fw_interface_monitor, link]
  monitoring_target_id:
    description: Monitoring Target ID
    value: {get_resource: fw_interface_monitor}
parameters:
  gohan_id: {description: UUID of the VNF Instance, label: Gohan resource ID, type: string}
  management_ip: {type: string}
  tenant_id: {label: Tenant ID, type: string}
  version: {label: Config version, type: number}
resources:
  fw_interface_monitor:
    properties:
      field_name: interface
      properties:
        community_name: FIREWALL_COMMUNITY
        device_ip: {get_param: management_ip}
        if_name: dp0s3
      resource_id: {get_param: gohan_id}
      resource_type: firewall_interfaces
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

