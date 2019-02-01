# heat_template: ese_logical_port
This is heat_template of "ese_logical_port" which is provided by gohan via etcd

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/ese_logical_port
{
    "body": {
        "handler": "heat_worker",
        "watch": [],
        "id": "ese_logical_port",
        "template_file": "heat_template_version: 2013-05-23\n\ndescription: >\n  Logical port template\n\nparameters:\n  physical_port_id:\n    type: string\n    label: Physical Interface ID\n    description: A unique id for the Physical Interface.\n  logical_port_name:\n    type: string\n    label: Logical Port Name\n    description: Name of the logical port.\n  logical_port_type:\n    type: string\n    label: Logical Port Type\n    description: Type of the logical port.\n  logical_port_vlan_id:\n    type: number\n    label: VLAN id for Logical Port\n    description: VLAN id to use for logical port creation.\n    default: 0\n  virtual_machine_interface_ids:\n    type: comma_delimited_list\n    label: Virtual Machine Interface ID\n    description: Virtual Machine Interface ID.\n  gohan_id:\n    type: string\n    label: Gohan resource ID\n    description: UUID of the ESE Physical Port\n  device_ip:\n    type: string\n    label: Device IP Address\n    description: Device IP Address.\n  tenant_id:\n    type: string\n    label: Tenant ID\n  version:\n    type: number\n    label: Config version\n\nresources:\n  logical_interface:\n    type: OS::Contrail::LogicalInterface\n    properties:\n      name: { get_param: logical_port_name }\n      physical_interface: { get_param: physical_port_id }\n      virtual_machine_interfaces: { get_param: virtual_machine_interface_ids }\n      type: { get_param: logical_port_type }\n      vlan: { get_param: logical_port_vlan_id }\n\n  interface_monitor:\n    type: ESI::Monitoring::MonitoringTarget\n    properties:\n      type: snmp_ports\n      resource_type: ese_logical_ports\n      resource_id: { get_param: gohan_id }\n      tenant_id: { get_param: tenant_id }\n      version: { get_param: version }\n      field_name: logical_port\n      properties:\n        device_ip: { get_param: device_ip }\n        if_name: { get_param: logical_port_name }\n        community_name: ESE_NODE_COMMUNITY\n      syncer_properties:\n        etcd:\n          status:\n            key: logical_port\n          hold_options:\n            positive_status:\n              - UP\n              - DOWN\n            time_seconds: 30\n        tsdb:\n          traffic.in:\n            metric: traffic.bytes\n            tags:\n              {% for port_id in jinja_port_ids %}\n              -  resource_id: { get_param: gohan_id }\n                 port_id: {{ port_id }}\n                 direction: in\n              {% endfor %}\n          traffic.out:\n            metric: traffic.bytes\n            tags:\n              {% for port_id in jinja_port_ids %}\n              -  resource_id: { get_param: gohan_id }\n                 port_id: {{ port_id }}\n                 direction: out\n              {% endfor %}\n    depends_on: logical_interface\n\noutputs:\n  id:\n    description: A unique id for the logical interface\n    value: { get_resource: logical_interface }\n  name:\n    description: The name of the logical interface.\n    value: { get_attr: [logical_interface, name] }\n  monitoring_target_id:\n    description: Monitoring Target ID\n    value: { get_resource: interface_monitor }\n  monitoring_link:\n    description: Monitoring Process Link\n    value: { get_attr: [interface_monitor, link] }\n",
        "parameter_mappings": {
            "logical_port_type": "Ptype",
            "logical_port_vlan_id": "Pvlan_id",
            "tenant_id": "Ptenant_id",
            "device_ip": "Fese_physical_port+ese_physical_port_id:ese_device+ese_device_id:management_ip_address",
            "heat_timeout": "C6",
            "jinja_port_ids": "Pport_ids",
            "version": "Vauto_filled",
            "virtual_machine_interface_ids": {
                "for_mapping": {
                    "path": [
                        {
                            "type": "port",
                            "id": ""
                        }
                    ],
                    "output_key": "id"
                },
                "for_field": "port_ids"
            },
            "logical_port_name": "Pname",
            "gohan_id": "Pid",
            "physical_port_id": "Mese_physical_port:ese_physical_port_id:id"
        }
    },
    "version": 1,
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* OS::Contrail::LogicalInterface
* ESI::Monitoring::MonitoringTarget

```
heat_template_version: 2013-05-23

description: >
  Logical port template

parameters:
  physical_port_id:
    type: string
    label: Physical Interface ID
    description: A unique id for the Physical Interface.
  logical_port_name:
    type: string
    label: Logical Port Name
    description: Name of the logical port.
  logical_port_type:
    type: string
    label: Logical Port Type
    description: Type of the logical port.
  logical_port_vlan_id:
    type: number
    label: VLAN id for Logical Port
    description: VLAN id to use for logical port creation.
    default: 0
  virtual_machine_interface_ids:
    type: comma_delimited_list
    label: Virtual Machine Interface ID
    description: Virtual Machine Interface ID.
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
  logical_interface:
    type: OS::Contrail::LogicalInterface
    properties:
      name: { get_param: logical_port_name }
      physical_interface: { get_param: physical_port_id }
      virtual_machine_interfaces: { get_param: virtual_machine_interface_ids }
      type: { get_param: logical_port_type }
      vlan: { get_param: logical_port_vlan_id }

  interface_monitor:
    type: ESI::Monitoring::MonitoringTarget
    properties:
      type: snmp_ports
      resource_type: ese_logical_ports
      resource_id: { get_param: gohan_id }
      tenant_id: { get_param: tenant_id }
      version: { get_param: version }
      field_name: logical_port
      properties:
        device_ip: { get_param: device_ip }
        if_name: { get_param: logical_port_name }
        community_name: ESE_NODE_COMMUNITY
      syncer_properties:
        etcd:
          status:
            key: logical_port
          hold_options:
            positive_status:
              - UP
              - DOWN
            time_seconds: 30
        tsdb:
          traffic.in:
            metric: traffic.bytes
            tags:
              {% for port_id in jinja_port_ids %}
              -  resource_id: { get_param: gohan_id }
                 port_id: {{ port_id }}
                 direction: in
              {% endfor %}
          traffic.out:
            metric: traffic.bytes
            tags:
              {% for port_id in jinja_port_ids %}
              -  resource_id: { get_param: gohan_id }
                 port_id: {{ port_id }}
                 direction: out
              {% endfor %}
    depends_on: logical_interface

outputs:
  id:
    description: A unique id for the logical interface
    value: { get_resource: logical_interface }
  name:
    description: The name of the logical interface.
    value: { get_attr: [logical_interface, name] }
  monitoring_target_id:
    description: Monitoring Target ID
    value: { get_resource: interface_monitor }
  monitoring_link:
    description: Monitoring Process Link
    value: { get_attr: [interface_monitor, link] }
```
