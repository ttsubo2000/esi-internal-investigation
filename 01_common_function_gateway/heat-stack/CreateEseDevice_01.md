# HTTP Methods for creating heat-stack: ESE Device (existing)

Checking heat-stack of "ese_device" via heatclient.
```
$ heat stack-show ese_device_cc214b6a-2f09-4094-b7cd-a9590f64b854
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                    |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                       |
| creation_time         | 2018-04-09T04:41:21Z                                                                                                                                                                     |
| description           | ESE Device (existing) template                                                                                                                                                           |
| disable_rollback      | True                                                                                                                                                                                     |
| id                    | 83145b8c-af3d-400a-a3fe-922116bd9f01                                                                                                                                                     |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/c583ce78843344adbe5fd20f13620274/stacks/ese_device_cc214b6a-2f09-4094-b7cd-a9590f64b854/83145b8c-af3d-400a-a3fe-922116bd9f01 |
| notification_topics   | []                                                                                                                                                                                       |
| outputs               | [                                                                                                                                                                                        |
|                       |   {                                                                                                                                                                                      |
|                       |     "output_value": "2762cfcb-575c-45cc-a07b-ca19f5b007cd",                                                                                                                              |
|                       |     "description": "Monitoring Target ID",                                                                                                                                               |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                 |
|                       |   },                                                                                                                                                                                     |
|                       |   {                                                                                                                                                                                      |
|                       |     "output_value": [                                                                                                                                                                    |
|                       |       "default-global-system-config",                                                                                                                                                    |
|                       |       "NWSDP-JNPR-02"                                                                                                                                                                    |
|                       |     ],                                                                                                                                                                                   |
|                       |     "description": "The FQ name of the physical router.",                                                                                                                                |
|                       |     "output_key": "fq_name"                                                                                                                                                              |
|                       |   },                                                                                                                                                                                     |
|                       |   {                                                                                                                                                                                      |
|                       |     "output_value": "7e5c78fa-71c0-427e-947f-586b1fc3c470",                                                                                                                              |
|                       |     "description": "A unique id for the physical router.",                                                                                                                               |
|                       |     "output_key": "id"                                                                                                                                                                   |
|                       |   },                                                                                                                                                                                     |
|                       |   {                                                                                                                                                                                      |
|                       |     "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/2762cfcb-575c-45cc-a07b-ca19f5b007cd",                                                     |
|                       |     "description": "Monitoring Process Link",                                                                                                                                            |
|                       |     "output_key": "monitoring_link"                                                                                                                                                      |
|                       |   },                                                                                                                                                                                     |
|                       |   {                                                                                                                                                                                      |
|                       |     "output_value": "NWSDP-JNPR-02",                                                                                                                                                     |
|                       |     "description": "The name of the physical router.",                                                                                                                                   |
|                       |     "output_key": "name"                                                                                                                                                                 |
|                       |   }                                                                                                                                                                                      |
|                       | ]                                                                                                                                                                                        |
| parameters            | {                                                                                                                                                                                        |
|                       |   "device_ip": "10.161.0.34",                                                                                                                                                            |
|                       |   "OS::stack_id": "83145b8c-af3d-400a-a3fe-922116bd9f01",                                                                                                                                |
|                       |   "OS::stack_name": "ese_device_cc214b6a-2f09-4094-b7cd-a9590f64b854",                                                                                                                   |
|                       |   "tenant_id": "c583ce78843344adbe5fd20f13620274",                                                                                                                                       |
|                       |   "hostname": "QFX-NW02",                                                                                                                                                                |
|                       |   "version": "1",                                                                                                                                                                        |
|                       |   "gohan_id": "cc214b6a-2f09-4094-b7cd-a9590f64b854",                                                                                                                                    |
|                       |   "name": "QFX-NW02"                                                                                                                                                                     |
|                       | }                                                                                                                                                                                        |
| parent                | None                                                                                                                                                                                     |
| stack_name            | ese_device_cc214b6a-2f09-4094-b7cd-a9590f64b854                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                    |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                          |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                      |
| stack_user_project_id | c583ce78843344adbe5fd20f13620274                                                                                                                                                         |
| template_description  | ESE Device (existing) template                                                                                                                                                           |
| timeout_mins          | 6                                                                                                                                                                                        |
| updated_time          | None                                                                                                                                                                                     |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "ese_device" via heatclient.
```
$ heat template-show ese_device_cc214b6a-2f09-4094-b7cd-a9590f64b854
description: 'ESE Device (existing) template

  '
heat_template_version: '2013-05-23'
outputs:
  fq_name:
    description: The FQ name of the physical router.
    value:
      get_attr: [physical_router, fq_name]
  id:
    description: A unique id for the physical router.
    value: {get_resource: physical_router}
  monitoring_link:
    description: Monitoring Process Link
    value:
      get_attr: [device_monitor, link]
  monitoring_target_id:
    description: Monitoring Target ID
    value: {get_resource: device_monitor}
  name:
    description: The name of the physical router.
    value:
      get_attr: [physical_router, name]
parameters:
  device_ip: {description: Device IP Address., label: Device IP Address, type: string}
  gohan_id: {description: UUID of the ESE Device, label: Gohan resource ID, type: string}
  hostname: {description: Name of host (vrouter) to create router on, label: Hostname,
    type: string}
  name: {description: Name of the physical router that will be created., label: Physical
      Router Name, type: string}
  tenant_id: {label: Tenant ID, type: string}
  version: {label: Config version, type: number}
resources:
  device_monitor:
    depends_on: physical_router
    properties:
      field_name: switch
      properties:
        community_name: ESE_NODE_COMMUNITY
        device_ip: {get_param: device_ip}
      resource_id: {get_param: gohan_id}
      resource_type: ese_devices
      syncer_properties:
        etcd:
          status: {key: switch}
      tenant_id: {get_param: tenant_id}
      type: snmp_device
      version: {get_param: version}
    type: ESI::Monitoring::MonitoringTarget
  physical_router:
    properties:
      fq_name:
      - default-global-system-config
      - {get_param: hostname}
      resource_type: physical_router
    type: OS::Contrail::ExistingResource
```
