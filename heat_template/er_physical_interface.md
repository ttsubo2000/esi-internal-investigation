# monitoring_template: er_physical_interface
This is monitoring_template of "er_physical_interface" which is provided by gohan via etcd

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/er_physical_interface
{
    "body": {
        "handler": "heat_worker",
        "watch": [],
        "id": "er_physical_interface",
        "template_file": "heat_template_version: 2013-05-23\n\ndescription: >\n  Physical port template\n\nparameters:\n  if_name:\n    type: string\n    label: Interface Name\n    description: Name of the ER Physical Interface\n  gohan_id:\n    type: string\n    label: Gohan resource ID\n    description: UUID of the ER Physical Interface\n  device_ip:\n    type: string\n    label: Device IP Address\n    description: Device IP Address\n  tenant_id:\n    type: string\n    label: Tenant ID\n  version:\n    type: number\n    label: Config version\n\nresources:\n  interface_monitor:\n    type: ESI::Monitoring::MonitoringTarget\n    properties:\n      type: snmp_ports_status\n      resource_type: er_physical_interfaces\n      resource_id: { get_param: gohan_id }\n      tenant_id: { get_param: tenant_id }\n      version: { get_param: version }\n      field_name: interface\n      properties:\n        device_ip: { get_param: device_ip }\n        if_name: { get_param: if_name }\n        community_name: EDGE_ROUTER_COMMUNITY\n      syncer_properties:\n        etcd:\n          status:\n            key: interface\n\noutputs:\n  monitoring_target_id:\n    description: Monitoring Target ID\n    value: { get_resource: interface_monitor}\n  monitoring_link:\n    description: Monitoring Process Link\n    value: { get_attr: [interface_monitor, link]}\n",
        "parameter_mappings": {
            "tenant_id": "Ptenant_id",
            "device_ip": "Fedge_router+device_id:ip",
            "if_name": "Pname",
            "heat_timeout": "C3",
            "version": "Vauto_filled",
            "gohan_id": "Pid"
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

description: >
  Physical port template

parameters:
  if_name:
    type: string
    label: Interface Name
    description: Name of the ER Physical Interface
  gohan_id:
    type: string
    label: Gohan resource ID
    description: UUID of the ER Physical Interface
  device_ip:
    type: string
    label: Device IP Address
    description: Device IP Address
  tenant_id:
    type: string
    label: Tenant ID
  version:
    type: number
    label: Config version

resources:
  interface_monitor:
    type: ESI::Monitoring::MonitoringTarget
    properties:
      type: snmp_ports_status
      resource_type: er_physical_interfaces
      resource_id: { get_param: gohan_id }
      tenant_id: { get_param: tenant_id }
      version: { get_param: version }
      field_name: interface
      properties:
        device_ip: { get_param: device_ip }
        if_name: { get_param: if_name }
        community_name: EDGE_ROUTER_COMMUNITY
      syncer_properties:
        etcd:
          status:
            key: interface

outputs:
  monitoring_target_id:
    description: Monitoring Target ID
    value: { get_resource: interface_monitor}
  monitoring_link:
    description: Monitoring Process Link
    value: { get_attr: [interface_monitor, link]}
```
