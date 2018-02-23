# heat_template: load_balancer
This is heat_template of "load_balancer" which is provided by gohan via etcd

![scope](../images/esi_interface.002.png)

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/load_balancer
{
    "body": {
        "handler": "heat_worker",
        "watch": [],
        "id": "load_balancer",
        "template_file": "heat_template_version: 2013-05-23\ndescription: Load Balancer\nparameters:\n  management_ip:\n    type: string\n  gohan_id:\n    type: string\n    label: Gohan resource ID\n    description: UUID of the VNF Instance\n  tenant_id:\n    type: string\n    label: Tenant ID\n  version:\n    type: number\n    label: Config version\nresources:\n  lb_device_monitor:\n    type: ESI::Monitoring::MonitoringTarget\n    properties:\n      type: snmp_device_lb\n      resource_type: load_balancers\n      resource_id: { get_param: gohan_id }\n      field_name: load_balancer\n      tenant_id: { get_param: tenant_id }\n      version: { get_param: version }\n      properties:\n        device_ip: { get_param: management_ip }\n        community_name: LOAD_BALANCER_COMMUNITY\n      syncer_properties:\n        etcd:\n          status:\n            key: load_balancer\n        tsdb:\n          cpu.usage:\n            metric: cpu.percents\n            tags:\n              resource_id: { get_param: gohan_id }\n              type: usage\n          memory.usage:\n            metric: memory.percents\n            tags:\n              resource_id: { get_param: gohan_id }\n              type: usage\n          http.request:\n            metric: http.request.connections\n            tags:\n              resource_id: { get_param: gohan_id }\n          tcp.client:\n            metric: tcp.connections\n            tags:\n              resource_id: { get_param: gohan_id }\n              owner: client\n          tcp.server:\n            metric: tcp.connections\n            tags:\n              resource_id: { get_param: gohan_id }\n              owner: server\noutputs:\n  monitoring_target_id:\n    description: Monitoring Target ID\n    value: { get_resource: lb_device_monitor}\n  monitoring_link:\n    description: Monitoring Process Link\n    value: { get_attr: [lb_device_monitor, link]}\n",
        "parameter_mappings": {
            "jinja_force_dependency": {
                "field": "id",
                "path": [
                    "load_balancer_conf_id"
                ]
            },
            "tenant_id": {
                "field": "tenant_id"
            },
            "management_ip": {
                "field": "management_ip",
                "path": [
                    "vnf_instance_id"
                ]
            },
            "heat_timeout": {
                "constant": 3
            },
            "version": {
                "version": "auto_filled"
            },
            "gohan_id": {
                "field": "id"
            }
        }
    },
    "version": 1,
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* ESI::Monitoring::MonitoringTarget

```
heat_template_version: 2013-05-23
description: Load Balancer
parameters:
  management_ip:
    type: string
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
  lb_device_monitor:
    type: ESI::Monitoring::MonitoringTarget
    properties:
      type: snmp_device_lb
      resource_type: load_balancers
      resource_id: { get_param: gohan_id }
      field_name: load_balancer
      tenant_id: { get_param: tenant_id }
      version: { get_param: version }
      properties:
        device_ip: { get_param: management_ip }
        community_name: LOAD_BALANCER_COMMUNITY
      syncer_properties:
        etcd:
          status:
            key: load_balancer
        tsdb:
          cpu.usage:
            metric: cpu.percents
            tags:
              resource_id: { get_param: gohan_id }
              type: usage
          memory.usage:
            metric: memory.percents
            tags:
              resource_id: { get_param: gohan_id }
              type: usage
          http.request:
            metric: http.request.connections
            tags:
              resource_id: { get_param: gohan_id }
          tcp.client:
            metric: tcp.connections
            tags:
              resource_id: { get_param: gohan_id }
              owner: client
          tcp.server:
            metric: tcp.connections
            tags:
              resource_id: { get_param: gohan_id }
              owner: server
outputs:
  monitoring_target_id:
    description: Monitoring Target ID
    value: { get_resource: lb_device_monitor}
  monitoring_link:
    description: Monitoring Process Link
    value: { get_attr: [lb_device_monitor, link]}
```
