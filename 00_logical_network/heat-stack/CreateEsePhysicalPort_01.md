# HTTP Methods for creating heat-stack: Physical port

Checking heat-stack of "ese_physical_port" via heatclient.
```
$ heat stack-show ese_physical_port_24dd42cf-b343-47a9-966a-8f7486378c46
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                           |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                              |
| creation_time         | 2018-02-15T06:53:59Z                                                                                                                                                                            |
| description           | Physical port template                                                                                                                                                                          |
| disable_rollback      | True                                                                                                                                                                                            |
| id                    | 6047992a-45bc-4aae-9c42-e2bcd0c09c26                                                                                                                                                            |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/ae69b52f46ba480bb9636f62736436f4/stacks/ese_physical_port_24dd42cf-b343-47a9-966a-8f7486378c46/6047992a-45bc-4aae-9c42-e2bcd0c09c26 |
| notification_topics   | []                                                                                                                                                                                              |
| outputs               | [                                                                                                                                                                                               |
|                       |   {                                                                                                                                                                                             |
|                       |     "output_value": "a481c2c4-e9cd-41f3-8e27-3a4184119abf",                                                                                                                                     |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                      |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                        |
|                       |   },                                                                                                                                                                                            |
|                       |   {                                                                                                                                                                                             |
|                       |     "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457",                                                                                                                                     |
|                       |     "description": "A unique id for the physical interface",                                                                                                                                    |
|                       |     "output_key": "id"                                                                                                                                                                          |
|                       |   },                                                                                                                                                                                            |
|                       |   {                                                                                                                                                                                             |
|                       |     "output_value": "http://collector-agents-se:7070/targets/a481c2c4-e9cd-41f3-8e27-3a4184119abf",                                                                                             |
|                       |     "description": "Monitoring Process Link",                                                                                                                                                   |
|                       |     "output_key": "monitoring_link"                                                                                                                                                             |
|                       |   },                                                                                                                                                                                            |
|                       |   {                                                                                                                                                                                             |
|                       |     "output_value": "xe-0/0/38",                                                                                                                                                                |
|                       |     "description": "The name of the physical interface.",                                                                                                                                       |
|                       |     "output_key": "name"                                                                                                                                                                        |
|                       |   }                                                                                                                                                                                             |
|                       | ]                                                                                                                                                                                               |
| parameters            | {                                                                                                                                                                                               |
|                       |   "physical_port_name": "xe-0/0/1",                                                                                                                                                             |
|                       |   "physical_device_hostname": "QFX-NW01",                                                                                                                                                       |
|                       |   "OS::stack_id": "6047992a-45bc-4aae-9c42-e2bcd0c09c26",                                                                                                                                       |
|                       |   "OS::stack_name": "ese_physical_port_24dd42cf-b343-47a9-966a-8f7486378c46",                                                                                                                   |
|                       |   "tenant_id": "ae69b52f46ba480bb9636f62736436f4",                                                                                                                                              |
|                       |   "device_ip": "10.161.0.33",                                                                                                                                                                   |
|                       |   "version": "1",                                                                                                                                                                               |
|                       |   "gohan_id": "24dd42cf-b343-47a9-966a-8f7486378c46"                                                                                                                                            |
|                       | }                                                                                                                                                                                               |
| parent                | None                                                                                                                                                                                            |
| stack_name            | ese_physical_port_24dd42cf-b343-47a9-966a-8f7486378c46                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                           |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                                 |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                             |
| stack_user_project_id | ae69b52f46ba480bb9636f62736436f4                                                                                                                                                                |
| template_description  | Physical port template                                                                                                                                                                          |
| timeout_mins          | 6                                                                                                                                                                                               |
| updated_time          | None                                                                                                                                                                                            |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "ese_physical_port" via heatclient.
```
$ heat template-show ese_physical_port_24dd42cf-b343-47a9-966a-8f7486378c46
description: 'Physical port template

  '
heat_template_version: '2013-05-23'
outputs:
  id:
    description: A unique id for the physical interface
    value: {get_resource: physical_interface}
  monitoring_link:
    description: Monitoring Process Link
    value:
      get_attr: [interface_monitor, link]
  monitoring_target_id:
    description: Monitoring Target ID
    value: {get_resource: interface_monitor}
  name:
    description: The name of the physical interface.
    value:
      get_attr: [physical_interface, name]
parameters:
  device_ip: {description: Device IP Address., label: Device IP Address, type: string}
  gohan_id: {description: UUID of the ESE Physical Port, label: Gohan resource ID,
    type: string}
  physical_device_hostname: {description: Hostname of the physical device on which
      physical port will be created., label: Physical Device Hostname, type: string}
  physical_port_name: {description: Name of the physical port., label: Physical Interface
      Name, type: string}
  tenant_id: {label: Tenant ID, type: string}
  version: {label: Config version, type: number}
resources:
  interface_monitor:
    depends_on: physical_interface
    properties:
      field_name: port
      properties:
        community_name: ESE_NODE_COMMUNITY
        device_ip: {get_param: device_ip}
        if_name: {get_param: physical_port_name}
      resource_id: {get_param: gohan_id}
      resource_type: ese_physical_ports
      syncer_properties:
        etcd:
          status: {key: port}
      tenant_id: {get_param: tenant_id}
      type: snmp_ports_status
      version: {get_param: version}
    type: ESI::Monitoring::MonitoringTarget
  physical_interface:
    properties:
      fq_name:
      - default-global-system-config
      - {get_param: physical_device_hostname}
      - {get_param: physical_port_name}
      resource_type: physical_interface
    type: OS::Contrail::ExistingResource
```
