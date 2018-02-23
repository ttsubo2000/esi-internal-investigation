# heat_template: port
This is heat_template of "port" which is provided by gohan via etcd

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/port
{
    "body": {
        "handler": "heat_worker",
        "watch": [],
        "id": "port",
        "template_file": "heat_template_version: 2013-05-23\n\ndescription: >\n  Virtual Machine Interface Template\n\nparameters:\n  uuid:\n    type: string\n    label: Backend Virtual Machine Interface UUID\n    description: A unique id for the Virtual Machine Interface.\n  name:\n    type: string\n    label: Physical Interface ID\n    description: A unique id for the Physical Interface.\n  security_groups:\n    type: json\n    default: []\n    label: Security Groups List\n    description: The IDs of security groups applied to the port.\n  virtual_machine_interface_allowed_address_pairs:\n    type: json\n    label: Virtual machine interface allowed address pairs.\n  virtual_machine_interface_mac_address:\n    type: string\n    default: \"fe:ff:ff:ff:ff:ff\"\n    label: Virtual machine interface mac address.\n  virtual_network:\n    type: string\n    label: Virtual Network.\n  virtual_machine:\n    type: string\n    label: Virtual Machine.\n    default: \"\"\n  device_owner:\n    type: string\n    label: Device Owner\n    default: \"\"\n  admin_state_up:\n    type: boolean\n    label: Admin state up\n    default: true\n  tenant_id:\n    type: string\n    label: Tenant ID\n  version:\n    type: number\n    label: Config version\n\nresources:\n  virtual_machine_interface:\n    type: OS::Contrail::VirtualMachineInterface\n    properties:\n      uuid: { get_param: uuid }\n      name: { get_param: name }\n      virtual_machine_interface_allowed_address_pairs: { get_param: virtual_machine_interface_allowed_address_pairs }\n      virtual_machine_interface_mac_addresses: [ { get_param: virtual_machine_interface_mac_address } ]\n      virtual_networks: [ { get_param: virtual_network } ]\n      virtual_machine: { get_param: virtual_machine }\n      device_owner: { get_param: device_owner }\n      admin_state_up: { get_param: admin_state_up }\n      security_groups: { get_param: security_groups }\n\n{% for fixed_ip in jinja_fixed_ips %}\n{% set instance_ip_id = 'instance_ip_' + (loop.index0|string) %}\n  {{ instance_ip_id }}:\n    type: OS::Contrail::InstanceIp\n    properties:\n      name:\n        str_replace:\n          template: '%name%_%zone%_%ip%'\n          params:\n            \"%name%\": { get_param: name }\n            \"%zone%\": {{ fixed_ip.subnet_id }}\n            \"%ip%\": {{ fixed_ip.ip_address }}\n      ip_address: {{ fixed_ip.ip_address }}\n      subnet_id: {{ jinja_subnets[loop.index0] }}\n      network_id: { get_param: virtual_network }\n      virtual_machine_interfaces: [ { get_resource: virtual_machine_interface } ]\n{% endfor %}\n\n{% if jinja_device_owner and jinja_attached %}\n  vmi_monitor:\n    type: ESI::Monitoring::MonitoringTarget\n    properties:\n      type: virtual_machine_interface\n      resource_type: ports\n      resource_id: { get_param: uuid }\n      field_name: vmi\n      tenant_id: { get_param: tenant_id }\n      version: { get_param: version }\n      properties:\n        fq_name: { get_attr: [virtual_machine_interface, fq_name] }\n      syncer_properties:\n        etcd:\n          status:\n            key: vmi\n        tsdb:\n          traffic.in:\n            metric: traffic.contrail_bytes\n            tags:\n              resource_id: { get_param: uuid }\n              direction: in\n          traffic.out:\n            metric: traffic.contrail_bytes\n            tags:\n              resource_id: { get_param: uuid }\n              direction: out\n    depends_on: virtual_machine_interface\n{% endif %}\n\noutputs:\n  id:\n    description: A unique id for the virtual machine interface.\n    value: { get_resource: virtual_machine_interface }\n  mac_address:\n    description: Virtual machine interface mac address.\n    value: { get_attr: [virtual_machine_interface, virtual_machine_interface_mac_addresses] }\n  allowed_address_pairs:\n    description: Virtual machine allowed address pairs.\n    value: { get_attr: [virtual_machine_interface, virtual_machine_interface_allowed_address_pairs] }\n  virtual_network:\n    description: Virtual network.\n    value: { get_attr: [virtual_machine_interface, virtual_networks] }\n  fq_name:\n    description: Fully Qualified Name of the VMI\n    value: { get_attr: [virtual_machine_interface, fq_name] }\n{% if jinja_device_owner and jinja_attached %}\n  monitoring_target_id:\n    description: Monitoring Target ID\n    value: { get_resource: vmi_monitor }\n  monitoring_link:\n    description: Monitoring Process Link\n    value: { get_attr: [vmi_monitor, link] }\n{% endif %}\n",
        "parameter_mappings": {
            "jinja_attached": "Pattached",
            "virtual_network": "Mnetwork:network_id:id",
            "virtual_machine": "Pdevice_id",
            "name": "Pid",
            "admin_state_up": "Padmin_state_up",
            "tenant_id": "Ptenant_id",
            "heat_timeout": "C13",
            "virtual_machine_interface_allowed_address_pairs": "Pallowed_address_pairs",
            "virtual_machine_interface_mac_address": "Pmac_address",
            "device_owner": "Pdevice_owner",
            "version": "Vauto_filled",
            "security_groups": "Psecurity_groups",
            "jinja_force_dependency_gw_interface": {
                "else_mapping": {
                    "constant": null
                },
                "if_mapping": {
                    "equal": [
                        {
                            "field": "device_owner"
                        },
                        {
                            "constant": "network:gw_interface"
                        }
                    ]
                },
                "then_mapping": {
                    "field": "id",
                    "path": [
                        {
                            "type": "gw_interface",
                            "id": "device_id"
                        }
                    ]
                }
            },
            "jinja_fixed_ips": "Pfixed_ips",
            "jinja_force_dependency_cfg": {
                "else_mapping": {
                    "constant": null
                },
                "if_mapping": {
                    "equal": [
                        {
                            "field": "device_owner"
                        },
                        {
                            "constant": "network:common_function_gateway"
                        }
                    ]
                },
                "then_mapping": {
                    "field": "id",
                    "path": [
                        {
                            "type": "common_function_gateway",
                            "id": "device_id"
                        }
                    ],
                    "ignore_missing": true
                }
            },
            "jinja_device_owner": "Pdevice_owner",
            "jinja_subnets": {
                "for_mapping": {
                    "path": [
                        {
                            "type": "subnet",
                            "id": "subnet_id"
                        }
                    ],
                    "output_key": "id"
                },
                "for_field": "fixed_ips"
            },
            "uuid": "Pid"
        }
    },
    "version": 1,
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* OS::Contrail::VirtualMachineInterface
* OS::Contrail::InstanceIp
* ESI::Monitoring::MonitoringTarget

```
heat_template_version: 2013-05-23

description: >
  Virtual Machine Interface Template

parameters:
  uuid:
    type: string
    label: Backend Virtual Machine Interface UUID
    description: A unique id for the Virtual Machine Interface.
  name:
    type: string
    label: Physical Interface ID
    description: A unique id for the Physical Interface.
  security_groups:
    type: json
    default: []
    label: Security Groups List
    description: The IDs of security groups applied to the port.
  virtual_machine_interface_allowed_address_pairs:
    type: json
    label: Virtual machine interface allowed address pairs.
  virtual_machine_interface_mac_address:
    type: string
    default: "fe:ff:ff:ff:ff:ff"
    label: Virtual machine interface mac address.
  virtual_network:
    type: string
    label: Virtual Network.
  virtual_machine:
    type: string
    label: Virtual Machine.
    default: ""
  device_owner:
    type: string
    label: Device Owner
    default: ""
  admin_state_up:
    type: boolean
    label: Admin state up
    default: true
  tenant_id:
    type: string
    label: Tenant ID
  version:
    type: number
    label: Config version

resources:
  virtual_machine_interface:
    type: OS::Contrail::VirtualMachineInterface
    properties:
      uuid: { get_param: uuid }
      name: { get_param: name }
      virtual_machine_interface_allowed_address_pairs: { get_param: virtual_machine_interface_allowed_address_pairs }
      virtual_machine_interface_mac_addresses: [ { get_param: virtual_machine_interface_mac_address } ]
      virtual_networks: [ { get_param: virtual_network } ]
      virtual_machine: { get_param: virtual_machine }
      device_owner: { get_param: device_owner }
      admin_state_up: { get_param: admin_state_up }
      security_groups: { get_param: security_groups }

{% for fixed_ip in jinja_fixed_ips %}
{% set instance_ip_id = 'instance_ip_' + (loop.index0|string) %}
  {{ instance_ip_id }}:
    type: OS::Contrail::InstanceIp
    properties:
      name:
        str_replace:
          template: '%name%_%zone%_%ip%'
          params:
            "%name%": { get_param: name }
            "%zone%": {{ fixed_ip.subnet_id }}
            "%ip%": {{ fixed_ip.ip_address }}
      ip_address: {{ fixed_ip.ip_address }}
      subnet_id: {{ jinja_subnets[loop.index0] }}
      network_id: { get_param: virtual_network }
      virtual_machine_interfaces: [ { get_resource: virtual_machine_interface } ]
{% endfor %}

{% if jinja_device_owner and jinja_attached %}
  vmi_monitor:
    type: ESI::Monitoring::MonitoringTarget
    properties:
      type: virtual_machine_interface
      resource_type: ports
      resource_id: { get_param: uuid }
      field_name: vmi
      tenant_id: { get_param: tenant_id }
      version: { get_param: version }
      properties:
        fq_name: { get_attr: [virtual_machine_interface, fq_name] }
      syncer_properties:
        etcd:
          status:
            key: vmi
        tsdb:
          traffic.in:
            metric: traffic.contrail_bytes
            tags:
              resource_id: { get_param: uuid }
              direction: in
          traffic.out:
            metric: traffic.contrail_bytes
            tags:
              resource_id: { get_param: uuid }
              direction: out
    depends_on: virtual_machine_interface
{% endif %}

outputs:
  id:
    description: A unique id for the virtual machine interface.
    value: { get_resource: virtual_machine_interface }
  mac_address:
    description: Virtual machine interface mac address.
    value: { get_attr: [virtual_machine_interface, virtual_machine_interface_mac_addresses] }
  allowed_address_pairs:
    description: Virtual machine allowed address pairs.
    value: { get_attr: [virtual_machine_interface, virtual_machine_interface_allowed_address_pairs] }
  virtual_network:
    description: Virtual network.
    value: { get_attr: [virtual_machine_interface, virtual_networks] }
  fq_name:
    description: Fully Qualified Name of the VMI
    value: { get_attr: [virtual_machine_interface, fq_name] }
{% if jinja_device_owner and jinja_attached %}
  monitoring_target_id:
    description: Monitoring Target ID
    value: { get_resource: vmi_monitor }
  monitoring_link:
    description: Monitoring Process Link
    value: { get_attr: [vmi_monitor, link] }
{% endif %}
```
