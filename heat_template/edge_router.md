# monitoring_template: edge_router
This is monitoring_template of "edge_router" which is provided by gohan via etcd

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/edge_router
{
    "body": {
        "handler": "heat_worker",
        "watch": [],
        "id": "edge_router",
        "template_file": "heat_template_version: 2013-05-23\n\ndescription: >\n  Physical port template\n\nparameters:\n  gohan_id:\n    type: string\n    label: Gohan resource ID\n    description: UUID of the Edge Router\n  device_ip:\n    type: string\n    label: Device IP Address\n    description: Device IP Address\n  tenant_id:\n    type: string\n    label: Tenant ID\n  version:\n    type: number\n    label: Config version\n\nresources:\n  device_monitor:\n    type: ESI::Monitoring::MonitoringTarget\n    properties:\n      type: snmp_device\n      resource_type: edge_routers\n      resource_id: { get_param: gohan_id }\n      tenant_id: { get_param: tenant_id }\n      version: { get_param: version }\n      field_name: router\n      properties:\n        device_ip: { get_param: device_ip }\n        community_name: EDGE_ROUTER_COMMUNITY\n      syncer_properties:\n        etcd:\n          status:\n            key: router\n\noutputs:\n  monitoring_target_id:\n    description: Monitoring Target ID\n    value: { get_resource: device_monitor}\n  monitoring_link:\n    description: Monitoring Process Link\n    value: { get_attr: [device_monitor, link]}\n",
        "parameter_mappings": {
            "gohan_id": "Pid",
            "heat_timeout": "C3",
            "device_ip": "Pip",
            "version": "Vauto_filled",
            "tenant_id": "Ptenant_id"
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
  gohan_id:
    type: string
    label: Gohan resource ID
    description: UUID of the Edge Router
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
  device_monitor:
    type: ESI::Monitoring::MonitoringTarget
    properties:
      type: snmp_device
      resource_type: edge_routers
      resource_id: { get_param: gohan_id }
      tenant_id: { get_param: tenant_id }
      version: { get_param: version }
      field_name: router
      properties:
        device_ip: { get_param: device_ip }
        community_name: EDGE_ROUTER_COMMUNITY
      syncer_properties:
        etcd:
          status:
            key: router

outputs:
  monitoring_target_id:
    description: Monitoring Target ID
    value: { get_resource: device_monitor}
  monitoring_link:
    description: Monitoring Process Link
    value: { get_attr: [device_monitor, link]}
```
