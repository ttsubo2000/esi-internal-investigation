# HTTP Methods for creating heat-stack: Vyatta Firewall Configuration
  
Checking heat-stack of "firewall_interface (dp0s5)" via heatclient.
```
$ heat stack-show firewall_interface_cdf30a48-8cf7-4935-9f8a-5b51f1177704
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                            |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                               |
| creation_time         | 2018-02-12T07:44:52Z                                                                                                                                                                             |
| description           | Vyatta Firewall Interface                                                                                                                                                                        |
| disable_rollback      | True                                                                                                                                                                                             |
| id                    | e82523ac-54d5-4c36-8300-6f0efa99da34                                                                                                                                                             |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/0f40dffa48614d9baa7eaac7e7532099/stacks/firewall_interface_cdf30a48-8cf7-4935-9f8a-5b51f1177704/e82523ac-54d5-4c36-8300-6f0efa99da34 |
| notification_topics   | []                                                                                                                                                                                               |
| outputs               | [                                                                                                                                                                                                |
|                       |   {                                                                                                                                                                                              |
|                       |     "output_value": "9d7a43c7-40e2-4703-9205-d76939462572",                                                                                                                                      |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                       |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                         |
|                       |   },                                                                                                                                                                                             |
|                       |   {                                                                                                                                                                                              |
|                       |     "output_value": "http://collector-agents-se:7070/targets/9d7a43c7-40e2-4703-9205-d76939462572",                                                                                              |
|                       |     "description": "Monitoring Process Link",                                                                                                                                                    |
|                       |     "output_key": "monitoring_link"                                                                                                                                                              |
|                       |   }                                                                                                                                                                                              |
|                       | ]                                                                                                                                                                                                |
| parameters            | {                                                                                                                                                                                                |
|                       |   "OS::stack_id": "e82523ac-54d5-4c36-8300-6f0efa99da34",                                                                                                                                        |
|                       |   "OS::stack_name": "firewall_interface_cdf30a48-8cf7-4935-9f8a-5b51f1177704",                                                                                                                   |
|                       |   "tenant_id": "0f40dffa48614d9baa7eaac7e7532099",                                                                                                                                               |
|                       |   "management_ip": "100.64.193.3",                                                                                                                                                               |
|                       |   "version": "1",                                                                                                                                                                                |
|                       |   "gohan_id": "cdf30a48-8cf7-4935-9f8a-5b51f1177704"                                                                                                                                             |
|                       | }                                                                                                                                                                                                |
| parent                | None                                                                                                                                                                                             |
| stack_name            | firewall_interface_cdf30a48-8cf7-4935-9f8a-5b51f1177704                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                            |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                                  |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                              |
| stack_user_project_id | 0f40dffa48614d9baa7eaac7e7532099                                                                                                                                                                 |
| template_description  | Vyatta Firewall Interface                                                                                                                                                                        |
| timeout_mins          | 3                                                                                                                                                                                                |
| updated_time          | None                                                                                                                                                                                             |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "firewall_interface (dp0s5)" via heatclient.
```
$ heat template-show firewall_interface_cdf30a48-8cf7-4935-9f8a-5b51f1177704
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
        if_name: dp0s5
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
