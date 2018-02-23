# heat_template: network
This is heat_template of "network" which is provided by gohan via etcd

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/network
{
    "body": {
        "handler": "heat_worker",
        "watch": [],
        "id": "network",
        "template_file": "heat_template_version: 2013-05-23\n\ndescription: >\n  Network template\n\nparameters:\n  uuid:\n    type: string\n    label: Virtual Network UUID\n    description: UUID of the virtual network that will be created.\n    default: \"\"\n  name:\n    type: string\n    label: Virtual Network Name\n    description: Name of the virtual network that will be created.\n  forwarding_mode:\n    type: string\n    label: Forwarding Mode\n    description: Forwarding Mode.\n    default: 'l2_l3'\n  route_targets:\n    type: comma_delimited_list\n    label: Route Targets list\n    default: []\n  shared:\n    type: boolean\n    label: Shared Network\n    default: false\n  external:\n    type: boolean\n    label: External Network\n    default: true\n  allow_transit:\n    type: boolean\n    label: Allow Transit\n    default: false\n  admin_state_up:\n    type: boolean\n    label: Admin state up\n    default: true\n\nresources:\n  network:\n    type: OS::Contrail::VirtualNetwork\n    properties:\n      uuid: { get_param: uuid }\n      name: { get_param: name }\n      forwarding_mode: { get_param: forwarding_mode }\n      route_targets: { get_param: route_targets }\n      shared: { get_param: shared }\n      admin_state_up: { get_param: admin_state_up }\n\noutputs:\n  id:\n    description: A unique id for the virtual network.\n    value: { get_resource: network }\n  name:\n    description: The name of the virtual network.\n    value: { get_attr: [network, name] }\n  fq_name:\n    description: The FQ name of the virtual network.\n    value: { get_attr: [network, fq_name] }\n  route_targets:\n    description: The name of the virtual network.\n    value: { get_attr: [network, route_targets] }\n",
        "parameter_mappings": {
            "uuid": "Pid",
            "heat_timeout": "C3",
            "name": "Pid",
            "admin_state_up": "Padmin_state_up"
        }
    },
    "version": 1,
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* OS::Contrail::VirtualNetwork

```
heat_template_version: 2013-05-23

description: >
  Network template

parameters:
  uuid:
    type: string
    label: Virtual Network UUID
    description: UUID of the virtual network that will be created.
    default: ""
  name:
    type: string
    label: Virtual Network Name
    description: Name of the virtual network that will be created.
  forwarding_mode:
    type: string
    label: Forwarding Mode
    description: Forwarding Mode.
    default: 'l2_l3'
  route_targets:
    type: comma_delimited_list
    label: Route Targets list
    default: []
  shared:
    type: boolean
    label: Shared Network
    default: false
  external:
    type: boolean
    label: External Network
    default: true
  allow_transit:
    type: boolean
    label: Allow Transit
    default: false
  admin_state_up:
    type: boolean
    label: Admin state up
    default: true

resources:
  network:
    type: OS::Contrail::VirtualNetwork
    properties:
      uuid: { get_param: uuid }
      name: { get_param: name }
      forwarding_mode: { get_param: forwarding_mode }
      route_targets: { get_param: route_targets }
      shared: { get_param: shared }
      admin_state_up: { get_param: admin_state_up }

outputs:
  id:
    description: A unique id for the virtual network.
    value: { get_resource: network }
  name:
    description: The name of the virtual network.
    value: { get_attr: [network, name] }
  fq_name:
    description: The FQ name of the virtual network.
    value: { get_attr: [network, fq_name] }
  route_targets:
    description: The name of the virtual network.
    value: { get_attr: [network, route_targets] }
```
