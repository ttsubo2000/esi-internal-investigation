# HTTP Methods for creating heat-stack: Vyatta Firewall Configuration

Checking heat-stack of "firewall" via heatclient.
```
$ heat stack-show firewall_8e4c20be-d221-43f4-8325-0162c1f06166
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                  |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                     |
| creation_time         | 2018-02-12T07:44:48Z                                                                                                                                                                   |
| description           | Vyatta Firewall Configuration                                                                                                                                                          |
| disable_rollback      | True                                                                                                                                                                                   |
| id                    | 7d9e544c-cc5a-4a44-a625-c743357c137f                                                                                                                                                   |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/0f40dffa48614d9baa7eaac7e7532099/stacks/firewall_8e4c20be-d221-43f4-8325-0162c1f06166/7d9e544c-cc5a-4a44-a625-c743357c137f |
| notification_topics   | []                                                                                                                                                                                     |
| outputs               | [                                                                                                                                                                                      |
|                       |   {                                                                                                                                                                                    |
|                       |     "output_value": "346eb30d-1ae0-4375-a1d6-7d83c699e2d3",                                                                                                                            |
|                       |     "description": "Monitoring Target ID",                                                                                                                                             |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                               |
|                       |   },                                                                                                                                                                                   |
|                       |   {                                                                                                                                                                                    |
|                       |     "output_value": "http://collector-agents-se:7070/targets/346eb30d-1ae0-4375-a1d6-7d83c699e2d3",                                                                                    |
|                       |     "description": "Monitoring Process Link",                                                                                                                                          |
|                       |     "output_key": "monitoring_link"                                                                                                                                                    |
|                       |   }                                                                                                                                                                                    |
|                       | ]                                                                                                                                                                                      |
| parameters            | {                                                                                                                                                                                      |
|                       |   "OS::stack_id": "7d9e544c-cc5a-4a44-a625-c743357c137f",                                                                                                                              |
|                       |   "OS::stack_name": "firewall_8e4c20be-d221-43f4-8325-0162c1f06166",                                                                                                                   |
|                       |   "default_gateway": "192.168.1.1",                                                                                                                                                    |
|                       |   "tenant_id": "0f40dffa48614d9baa7eaac7e7532099",                                                                                                                                     |
|                       |   "user_password": "******",                                                                                                                                                           |
|                       |   "other_username": "",                                                                                                                                                                |
|                       |   "admin_username": "user-admin",                                                                                                                                                      |
|                       |   "user_username": "user-read",                                                                                                                                                        |
|                       |   "management_ip": "100.64.193.3",                                                                                                                                                     |
|                       |   "version": "1",                                                                                                                                                                      |
|                       |   "other_password": "******",                                                                                                                                                          |
|                       |   "admin_password": "******",                                                                                                                                                          |
|                       |   "credentials": "{\"username\": \"vfwadmin\", \"password\": \"password\"}",                                                                                                           |
|                       |   "gohan_id": "8e4c20be-d221-43f4-8325-0162c1f06166",                                                                                                                                  |
|                       |   "networks": "[{\"ifname\": \"dp0s4\", \"type\": \"disable\"}, {\"ifname\": \"dp0s5\", \"type\": \"disable\"}]"                                                                       |
|                       | }                                                                                                                                                                                      |
| parent                | None                                                                                                                                                                                   |
| stack_name            | firewall_8e4c20be-d221-43f4-8325-0162c1f06166                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                  |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                        |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                    |
| stack_user_project_id | 0f40dffa48614d9baa7eaac7e7532099                                                                                                                                                       |
| template_description  | Vyatta Firewall Configuration                                                                                                                                                          |
| timeout_mins          | 13                                                                                                                                                                                     |
| updated_time          | None                                                                                                                                                                                   |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "firewall" via heatclient.
```
$ heat template-show firewall_8e4c20be-d221-43f4-8325-0162c1f06166
description: Vyatta Firewall Configuration
heat_template_version: '2013-05-23'
outputs:
  monitoring_link:
    description: Monitoring Process Link
    value:
      get_attr: [fw_device_monitor, link]
  monitoring_target_id:
    description: Monitoring Target ID
    value: {get_resource: fw_device_monitor}
parameters:
  admin_password: {default: '', hidden: true, type: string}
  admin_username: {type: string}
  credentials: {type: json}
  default_gateway: {default: '', type: string}
  gohan_id: {description: UUID of the VNF Instance, label: Gohan resource ID, type: string}
  management_ip: {type: string}
  networks: {type: json}
  other_password: {default: '', hidden: true, type: string}
  other_username: {default: '', type: string}
  tenant_id: {label: Tenant ID, type: string}
  user_password: {default: '', hidden: true, type: string}
  user_username: {type: string}
  version: {label: Config version, type: number}
resources:
  fw_device_monitor:
    depends_on: server
    properties:
      field_name: firewall
      properties:
        community_name: FIREWALL_COMMUNITY
        device_ip: {get_param: management_ip}
      resource_id: {get_param: gohan_id}
      resource_type: firewalls
      syncer_properties:
        etcd:
          status: {key: firewall}
        tsdb:
          cpu.idle:
            metric: cpu.percents
            tags:
              resource_id: {get_param: gohan_id}
              type: idle
          cpu.system:
            metric: cpu.percents
            tags:
              resource_id: {get_param: gohan_id}
              type: system
          cpu.user:
            metric: cpu.percents
            tags:
              resource_id: {get_param: gohan_id}
              type: user
          memory.available:
            metric: memory.kbytes
            tags:
              resource_id: {get_param: gohan_id}
              type: available
          memory.total:
            metric: memory.kbytes
            tags:
              resource_id: {get_param: gohan_id}
              type: total
          tcp.active:
            metric: tcp.connections
            tags:
              open: active
              resource_id: {get_param: gohan_id}
          tcp.passive:
            metric: tcp.connections
            tags:
              open: passive
              resource_id: {get_param: gohan_id}
      tenant_id: {get_param: tenant_id}
      type: snmp_device_fw
      version: {get_param: version}
    type: ESI::Monitoring::MonitoringTarget
  server:
    properties:
      admin_password: {get_param: admin_password}
      admin_username: {get_param: admin_username}
      credentials: {get_param: credentials}
      default_gateway: {get_param: default_gateway}
      management_ip: {get_param: management_ip}
      networks: {get_param: networks}
      other_password: {get_param: other_password}
      other_username: {get_param: other_username}
      user_password: {get_param: user_password}
      user_username: {get_param: user_username}
    type: ESI::VNF::VyattaConfig
```
