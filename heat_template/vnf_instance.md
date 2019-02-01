# heat_template: vnf_instance
This is heat_template of "vnf_instance" which is provided by gohan via etcd

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/vnf_instance
{
    "body": {
        "handler": "heat_worker",
        "watch": [],
        "id": "vnf_instance",
        "template_file": "heat_template_version: 2013-05-23\ndescription: VNF Instance\nparameters:\n  name:\n    default: \"\"\n    type: string\n  image:\n    type: string\n    constraints:\n    - custom_constraint: glance.image\n  flavor:\n    type: string\n    constraints:\n    - custom_constraint: nova.flavor\n  availability_zone:\n    type: string\n    default: \"\"\n  networks:\n    type: json\n  reboot:\n    type: string\n    default: \"\"\n  user_data:\n    type: string\n    default: \"\"\n  user_data_format:\n    type: string\n  config_drive:\n    type: boolean\n  gohan_id:\n    type: string\n    label: Gohan resource ID\n    description: UUID of the VNF Instance\n  tenant_id:\n    type: string\n    label: Tenant ID\n  version:\n    type: number\n    label: Config version\nresources:\n  server:\n    type: ESI::VNF::Instance\n    properties:\n      name: { get_param: name }\n      flavor: { get_param: flavor }\n      image: { get_param: image }\n      networks: { get_param: networks }\n      availability_zone: { get_param: availability_zone }\n      reboot: { get_param: reboot }\n      user_data: { get_param: user_data }\n      user_data_format: { get_param: user_data_format }\n      config_drive: { get_param: config_drive }\n  server_monitor:\n    type: ESI::Monitoring::MonitoringTarget\n    properties:\n      type: compute\n      resource_type: vnf_instances\n      resource_id: { get_param: gohan_id }\n      field_name: server\n      tenant_id: { get_param: tenant_id }\n      version: { get_param: version }\n      properties:\n        server_id: { get_resource: server }\n      syncer_properties:\n        etcd:\n          status:\n            key: server\n    depends_on: server\noutputs:\n  server_id:\n    description: A unique id for the nova server.\n    value: { get_resource: server }\n  monitoring_target_id:\n    description: Monitoring Target ID\n    value: { get_resource: server_monitor}\n  monitoring_link:\n    description: Monitoring Process Link\n    value: { get_attr: [server_monitor, link]}\n",
        "parameter_mappings": {
            "user_data_format": "Puser_data_format",
            "name": "Pname",
            "availability_zone": "Pavailability_zone",
            "tenant_id": "Ptenant_id",
            "image": "Fvnf_template+vnf_template_id:image",
            "reboot": "Preboot",
            "user_data": "Puser_data",
            "heat_timeout": "C30",
            "version": "Vauto_filled",
            "gohan_id": "Pid",
            "flavor": "Fvnf_plan+vnf_plan_id:flavor",
            "networks": "Pnetworks",
            "config_drive": "Pconfig_drive"
        }
    },
    "version": 1,
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* ESI::VNF::Instance
* ESI::Monitoring::MonitoringTarget

```
heat_template_version: 2013-05-23
description: VNF Instance
parameters:
  name:
    default: ""
    type: string
  image:
    type: string
    constraints:
    - custom_constraint: glance.image
  flavor:
    type: string
    constraints:
    - custom_constraint: nova.flavor
  availability_zone:
    type: string
    default: ""
  networks:
    type: json
  reboot:
    type: string
    default: ""
  user_data:
    type: string
    default: ""
  user_data_format:
    type: string
  config_drive:
    type: boolean
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
    type: ESI::VNF::Instance
    properties:
      name: { get_param: name }
      flavor: { get_param: flavor }
      image: { get_param: image }
      networks: { get_param: networks }
      availability_zone: { get_param: availability_zone }
      reboot: { get_param: reboot }
      user_data: { get_param: user_data }
      user_data_format: { get_param: user_data_format }
      config_drive: { get_param: config_drive }
  server_monitor:
    type: ESI::Monitoring::MonitoringTarget
    properties:
      type: compute
      resource_type: vnf_instances
      resource_id: { get_param: gohan_id }
      field_name: server
      tenant_id: { get_param: tenant_id }
      version: { get_param: version }
      properties:
        server_id: { get_resource: server }
      syncer_properties:
        etcd:
          status:
            key: server
    depends_on: server
outputs:
  server_id:
    description: A unique id for the nova server.
    value: { get_resource: server }
  monitoring_target_id:
    description: Monitoring Target ID
    value: { get_resource: server_monitor}
  monitoring_link:
    description: Monitoring Process Link
    value: { get_attr: [server_monitor, link]}
```
