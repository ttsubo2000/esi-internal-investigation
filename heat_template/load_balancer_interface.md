# heat_template: load_balancer_interface
This is heat_template of "load_balancer_interface" which is provided by gohan via etcd

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/load_balancer_interface
{
    "body": {
        "handler": "heat_worker",
        "watch": [],
        "id": "load_balancer_interface",
        "template_file": "heat_template_version: 2013-05-23\ndescription: Load Balancer Interface\nparameters:\n  management_ip:\n    type: string\n  gohan_id:\n    type: string\n    label: Gohan resource ID\n    description: UUID of the VNF Instance\n  tenant_id:\n    type: string\n    label: Tenant ID\n  version:\n    type: number\n    label: Config version\nresources:\n  lb_interface_monitor:\n    type: ESI::Monitoring::MonitoringTarget\n    properties:\n      type: snmp_ports\n      resource_type: load_balancer_interfaces\n      resource_id: { get_param: gohan_id }\n      field_name: interface\n      tenant_id: { get_param: tenant_id }\n      version: { get_param: version }\n      properties:\n        device_ip: { get_param: management_ip }\n        {% if jinja_slot_number == 0  %}\n        if_name: 0/1\n        {% else %}\n        if_name: 1/{{ jinja_slot_number }}\n        {% endif %}\n        community_name: LOAD_BALANCER_COMMUNITY\n      syncer_properties:\n        etcd:\n          status:\n            key: interface\n        tsdb:\n          traffic.in:\n            metric: traffic.bytes\n            tags:\n              resource_id: { get_param: gohan_id }\n              direction: in\n          traffic.out:\n            metric: traffic.bytes\n            tags:\n              resource_id: { get_param: gohan_id }\n              direction: out\noutputs:\n  monitoring_target_id:\n    description: Monitoring Target ID\n    value: { get_resource: lb_interface_monitor}\n  monitoring_link:\n    description: Monitoring Process Link\n    value: { get_attr: [lb_interface_monitor, link]}\n",
        "parameter_mappings": {
            "jinja_slot_number": {
                "field": "slot_number"
            },
            "tenant_id": {
                "field": "tenant_id"
            },
            "management_ip": {
                "field": "management_ip",
                "path": [
                    "load_balancer_id",
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
description: Load Balancer Interface
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
  lb_interface_monitor:
    type: ESI::Monitoring::MonitoringTarget
    properties:
      type: snmp_ports
      resource_type: load_balancer_interfaces
      resource_id: { get_param: gohan_id }
      field_name: interface
      tenant_id: { get_param: tenant_id }
      version: { get_param: version }
      properties:
        device_ip: { get_param: management_ip }
        {% if jinja_slot_number == 0  %}
        if_name: 0/1
        {% else %}
        if_name: 1/{{ jinja_slot_number }}
        {% endif %}
        community_name: LOAD_BALANCER_COMMUNITY
      syncer_properties:
        etcd:
          status:
            key: interface
        tsdb:
          traffic.in:
            metric: traffic.bytes
            tags:
              resource_id: { get_param: gohan_id }
              direction: in
          traffic.out:
            metric: traffic.bytes
            tags:
              resource_id: { get_param: gohan_id }
              direction: out
outputs:
  monitoring_target_id:
    description: Monitoring Target ID
    value: { get_resource: lb_interface_monitor}
  monitoring_link:
    description: Monitoring Process Link
    value: { get_attr: [lb_interface_monitor, link]}
```
