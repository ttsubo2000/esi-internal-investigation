# heat_template: ese_device_existing
This is heat_template of "ese_device_existing" which is provided by gohan via etcd

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/ese_device_existing
{
    "body": {
        "handler": "heat_worker",
        "watch": [],
        "id": "ese_device_existing",
        "template_file": "heat_template_version: 2013-05-23\n\ndescription: >\n  ESE Device (existing) template\n\nparameters:\n  name:\n    type: string\n    label: Physical Router Name\n    description: Name of the physical router that will be created.\n  hostname:\n    type: string\n    label: Hostname\n    description: Name of host (vrouter) to create router on\n  gohan_id:\n    type: string\n    label: Gohan resource ID\n    description: UUID of the ESE Device\n  device_ip:\n    type: string\n    label: Device IP Address\n    description: Device IP Address.\n  tenant_id:\n    type: string\n    label: Tenant ID\n  version:\n    type: number\n    label: Config version\n\nresources:\n  physical_router:\n    type: OS::Contrail::ExistingResource\n    properties:\n      fq_name:\n        - \"default-global-system-config\"\n        - { get_param: hostname }\n      resource_type: \"physical_router\"\n\n  device_monitor:\n    type: ESI::Monitoring::MonitoringTarget\n    properties:\n      type: snmp_device\n      resource_type: ese_devices\n      resource_id: { get_param: gohan_id }\n      tenant_id: { get_param: tenant_id }\n      version: { get_param: version }\n      field_name: switch\n      properties:\n        device_ip: { get_param: device_ip }\n        community_name: ESE_NODE_COMMUNITY\n      syncer_properties:\n        etcd:\n          status:\n            key: switch\n    depends_on: physical_router\n\noutputs:\n  id:\n    description: A unique id for the physical router.\n    value: { get_resource: physical_router }\n  name:\n    description: The name of the physical router.\n    value: { get_attr: [physical_router, name] }\n  fq_name:\n    description: The FQ name of the physical router.\n    value: { get_attr: [physical_router, fq_name] }\n  monitoring_target_id:\n    description: Monitoring Target ID\n    value: { get_resource: device_monitor }\n  monitoring_link:\n    description: Monitoring Process Link\n    value: { get_attr: [device_monitor, link] }\n",
        "parameter_mappings": {
            "hostname": "Phostname",
            "name": "Pname",
            "tenant_id": "Ptenant_id",
            "device_ip": "Pmanagement_ip_address",
            "heat_timeout": "C6",
            "version": "Vauto_filled",
            "gohan_id": "Pid"
        }
    },
    "version": 1,
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* OS::Contrail::ExistingResource
* ESI::Monitoring::MonitoringTarget

```
heat_template_version: 2013-05-23

description: >
  ESE Device (existing) template

parameters:
  name:
    type: string
    label: Physical Router Name
    description: Name of the physical router that will be created.
  hostname:
    type: string
    label: Hostname
    description: Name of host (vrouter) to create router on
  gohan_id:
    type: string
    label: Gohan resource ID
    description: UUID of the ESE Device
  device_ip:
    type: string
    label: Device IP Address
    description: Device IP Address.
  tenant_id:
    type: string
    label: Tenant ID
  version:
    type: number
    label: Config version

resources:
  physical_router:
    type: OS::Contrail::ExistingResource
    properties:
      fq_name:
        - "default-global-system-config"
        - { get_param: hostname }
      resource_type: "physical_router"

  device_monitor:
    type: ESI::Monitoring::MonitoringTarget
    properties:
      type: snmp_device
      resource_type: ese_devices
      resource_id: { get_param: gohan_id }
      tenant_id: { get_param: tenant_id }
      version: { get_param: version }
      field_name: switch
      properties:
        device_ip: { get_param: device_ip }
        community_name: ESE_NODE_COMMUNITY
      syncer_properties:
        etcd:
          status:
            key: switch
    depends_on: physical_router

outputs:
  id:
    description: A unique id for the physical router.
    value: { get_resource: physical_router }
  name:
    description: The name of the physical router.
    value: { get_attr: [physical_router, name] }
  fq_name:
    description: The FQ name of the physical router.
    value: { get_attr: [physical_router, fq_name] }
  monitoring_target_id:
    description: Monitoring Target ID
    value: { get_resource: device_monitor }
  monitoring_link:
    description: Monitoring Process Link
    value: { get_attr: [device_monitor, link] }
```
