# heat_template: ese_physical_port_existing
This is heat_template of "ese_physical_port_existing" which is provided by gohan via etcd

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/ese_physical_port_existing
{
    "body": {
        "handler": "heat_worker",
        "watch": [],
        "id": "ese_physical_port_existing",
        "template_file": "heat_template_version: 2013-05-23\n\ndescription: >\n  Physical port template\n\nparameters:\n  physical_device_hostname:\n    type: string\n    label: Physical Device Hostname\n    description: Hostname of the physical device on which physical port will be created.\n  physical_port_name:\n    type: string\n    label: Physical Interface Name\n    description: Name of the physical port.\n  gohan_id:\n    type: string\n    label: Gohan resource ID\n    description: UUID of the ESE Physical Port\n  device_ip:\n    type: string\n    label: Device IP Address\n    description: Device IP Address.\n  tenant_id:\n    type: string\n    label: Tenant ID\n  version:\n    type: number\n    label: Config version\n\nresources:\n  physical_interface:\n    type: OS::Contrail::ExistingResource\n    properties:\n      fq_name:\n        - \"default-global-system-config\"\n        - { get_param: physical_device_hostname }\n        - { get_param: physical_port_name }\n      resource_type: \"physical_interface\"\n\n  interface_monitor:\n    type: ESI::Monitoring::MonitoringTarget\n    properties:\n      type: snmp_ports_status\n      resource_type: ese_physical_ports\n      resource_id: { get_param: gohan_id }\n      tenant_id: { get_param: tenant_id }\n      version: { get_param: version }\n      field_name: port\n      properties:\n        device_ip: { get_param: device_ip }\n        if_name: { get_param: physical_port_name }\n        community_name: ESE_NODE_COMMUNITY\n      syncer_properties:\n        etcd:\n          status:\n            key: port\n    depends_on: physical_interface\n\noutputs:\n  id:\n    description: A unique id for the physical interface\n    value: { get_resource: physical_interface }\n  name:\n    description: The name of the physical interface.\n    value: { get_attr: [physical_interface, name] }\n  monitoring_target_id:\n    description: Monitoring Target ID\n    value: { get_resource: interface_monitor }\n  monitoring_link:\n    description: Monitoring Process Link\n    value: { get_attr: [interface_monitor, link] }\n",
        "parameter_mappings": {
            "physical_port_name": "Pname",
            "physical_device_hostname": "Fese_device+ese_device_id:hostname",
            "tenant_id": "Ptenant_id",
            "device_ip": "Fese_device+ese_device_id:management_ip_address",
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
  Physical port template

parameters:
  physical_device_hostname:
    type: string
    label: Physical Device Hostname
    description: Hostname of the physical device on which physical port will be created.
  physical_port_name:
    type: string
    label: Physical Interface Name
    description: Name of the physical port.
  gohan_id:
    type: string
    label: Gohan resource ID
    description: UUID of the ESE Physical Port
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
  physical_interface:
    type: OS::Contrail::ExistingResource
    properties:
      fq_name:
        - "default-global-system-config"
        - { get_param: physical_device_hostname }
        - { get_param: physical_port_name }
      resource_type: "physical_interface"

  interface_monitor:
    type: ESI::Monitoring::MonitoringTarget
    properties:
      type: snmp_ports_status
      resource_type: ese_physical_ports
      resource_id: { get_param: gohan_id }
      tenant_id: { get_param: tenant_id }
      version: { get_param: version }
      field_name: port
      properties:
        device_ip: { get_param: device_ip }
        if_name: { get_param: physical_port_name }
        community_name: ESE_NODE_COMMUNITY
      syncer_properties:
        etcd:
          status:
            key: port
    depends_on: physical_interface

outputs:
  id:
    description: A unique id for the physical interface
    value: { get_resource: physical_interface }
  name:
    description: The name of the physical interface.
    value: { get_attr: [physical_interface, name] }
  monitoring_target_id:
    description: Monitoring Target ID
    value: { get_resource: interface_monitor }
  monitoring_link:
    description: Monitoring Process Link
    value: { get_attr: [interface_monitor, link] }
```
