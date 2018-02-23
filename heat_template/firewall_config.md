# heat_template: firewall_config
This is heat_template of "firewall_config" which is provided by gohan via etcd

![scope](../images/esi_interface.002.png)

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/firewall_config
{
    "body": {
        "handler": "heat_worker",
        "watch": [],
        "id": "firewall_config",
        "template_file": "heat_template_version: 2013-05-23\ndescription: Vyatta Firewall Configuration\nparameters:\n  management_ip:\n    type: string\n  credentials:\n    type: json\n  default_gateway:\n    type: string\n    default: \"\"\n  user_username:\n    type: string\n  user_password:\n    type: string\n    default: \"\"\n    hidden: true\n  admin_username:\n    type: string\n  admin_password:\n    type: string\n    default: \"\"\n    hidden: true\n  other_username:\n    type: string\n    default: \"\"\n  other_password:\n    type: string\n    default: \"\"\n    hidden: true\n  networks:\n    type: json\n  gohan_id:\n    type: string\n    label: Gohan resource ID\n    description: UUID of the VNF Instance\n  tenant_id:\n    type: string\n    label: Tenant ID\n  version:\n    type: number\n    label: Config version\nresources:\n  server:\n    type: ESI::VNF::VyattaConfig\n    properties:\n      management_ip: { get_param: management_ip }\n      credentials: { get_param: credentials }\n      default_gateway: { get_param: default_gateway }\n      user_username: { get_param: user_username }\n      user_password: { get_param: user_password }\n      admin_username: { get_param: admin_username }\n      admin_password: { get_param: admin_password }\n      other_username: { get_param: other_username }\n      other_password: { get_param: other_password }\n      networks: { get_param: networks }\n  fw_device_monitor:\n    type: ESI::Monitoring::MonitoringTarget\n    properties:\n      type: snmp_device_fw\n      resource_type: firewalls\n      resource_id: { get_param: gohan_id }\n      field_name: firewall\n      tenant_id: { get_param: tenant_id }\n      version: { get_param: version }\n      properties:\n        device_ip: { get_param: management_ip }\n        community_name: FIREWALL_COMMUNITY\n      syncer_properties:\n        etcd:\n          status:\n            key: firewall\n        tsdb:\n          cpu.user:\n            metric: cpu.percents\n            tags:\n              resource_id: { get_param: gohan_id }\n              type: user\n          cpu.system:\n            metric: cpu.percents\n            tags:\n              resource_id: { get_param: gohan_id }\n              type: system\n          cpu.idle:\n            metric: cpu.percents\n            tags:\n              resource_id: { get_param: gohan_id }\n              type: idle\n          memory.total:\n            metric: memory.kbytes\n            tags:\n              resource_id: { get_param: gohan_id }\n              type: total\n          memory.available:\n            metric: memory.kbytes\n            tags:\n              resource_id: { get_param: gohan_id }\n              type: available\n          tcp.active:\n            metric: tcp.connections\n            tags:\n              resource_id: { get_param: gohan_id }\n              open: active\n          tcp.passive:\n            metric: tcp.connections\n            tags:\n              resource_id: { get_param: gohan_id }\n              open: passive\n    depends_on: server\noutputs:\n  monitoring_target_id:\n    description: Monitoring Target ID\n    value: { get_resource: fw_device_monitor}\n  monitoring_link:\n    description: Monitoring Process Link\n    value: { get_attr: [fw_device_monitor, link]}\n",
        "parameter_mappings": {
            "default_gateway": {
                "field": "default_gateway"
            },
            "tenant_id": {
                "field": "tenant_id"
            },
            "user_password": {
                "field": "user_password"
            },
            "other_username": {
                "field": "other_username"
            },
            "management_ip": {
                "field": "management_ip",
                "path": [
                    "vnf_instance_id"
                ]
            },
            "admin_username": {
                "field": "admin_username"
            },
            "user_username": {
                "field": "user_username"
            },
            "heat_timeout": {
                "constant": 13
            },
            "version": {
                "version": "auto_filled"
            },
            "other_password": {
                "field": "other_password"
            },
            "admin_password": {
                "field": "admin_password"
            },
            "credentials": {
                "field": "credentials",
                "path": [
                    "vnf_instance_id",
                    "vnf_template_id"
                ]
            },
            "gohan_id": {
                "field": "id"
            },
            "networks": {
                "field": "networks"
            }
        }
    },
    "version": 1,
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* ESI::VNF::VyattaConfig
* ESI::Monitoring::MonitoringTarget

```
heat_template_version: 2013-05-23
description: Vyatta Firewall Configuration
parameters:
  management_ip:
    type: string
  credentials:
    type: json
  default_gateway:
    type: string
    default: ""
  user_username:
    type: string
  user_password:
    type: string
    default: ""
    hidden: true
  admin_username:
    type: string
  admin_password:
    type: string
    default: ""
    hidden: true
  other_username:
    type: string
    default: ""
  other_password:
    type: string
    default: ""
    hidden: true
  networks:
    type: json
  gohan_id:
    type: string
    label: Gohan resource ID
    description: UUID of the VNF Instance
  tenant_id:
    type: string
    label: Tenant ID
  version:
    type: number
    label: Config version
resources:
  server:
    type: ESI::VNF::VyattaConfig
    properties:
      management_ip: { get_param: management_ip }
      credentials: { get_param: credentials }
      default_gateway: { get_param: default_gateway }
      user_username: { get_param: user_username }
      user_password: { get_param: user_password }
      admin_username: { get_param: admin_username }
      admin_password: { get_param: admin_password }
      other_username: { get_param: other_username }
      other_password: { get_param: other_password }
      networks: { get_param: networks }
  fw_device_monitor:
    type: ESI::Monitoring::MonitoringTarget
    properties:
      type: snmp_device_fw
      resource_type: firewalls
      resource_id: { get_param: gohan_id }
      field_name: firewall
      tenant_id: { get_param: tenant_id }
      version: { get_param: version }
      properties:
        device_ip: { get_param: management_ip }
        community_name: FIREWALL_COMMUNITY
      syncer_properties:
        etcd:
          status:
            key: firewall
        tsdb:
          cpu.user:
            metric: cpu.percents
            tags:
              resource_id: { get_param: gohan_id }
              type: user
          cpu.system:
            metric: cpu.percents
            tags:
              resource_id: { get_param: gohan_id }
              type: system
          cpu.idle:
            metric: cpu.percents
            tags:
              resource_id: { get_param: gohan_id }
              type: idle
          memory.total:
            metric: memory.kbytes
            tags:
              resource_id: { get_param: gohan_id }
              type: total
          memory.available:
            metric: memory.kbytes
            tags:
              resource_id: { get_param: gohan_id }
              type: available
          tcp.active:
            metric: tcp.connections
            tags:
              resource_id: { get_param: gohan_id }
              open: active
          tcp.passive:
            metric: tcp.connections
            tags:
              resource_id: { get_param: gohan_id }
              open: passive
    depends_on: server
outputs:
  monitoring_target_id:
    description: Monitoring Target ID
    value: { get_resource: fw_device_monitor}
  monitoring_link:
    description: Monitoring Process Link
    value: { get_attr: [fw_device_monitor, link]}
```
