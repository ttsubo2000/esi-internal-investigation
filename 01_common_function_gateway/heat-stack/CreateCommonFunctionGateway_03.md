# HTTP Methods for creating heat-stack: Common Function Gateway

Checking heat-stack of "common_function_gateway" via heatclient.
```
$ heat stack-show common_function_gateway_f649736d-1920-41eb-96af-d4e4fe192d0e
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                                 |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                                    |
| creation_time         | 2018-04-09T04:49:59Z                                                                                                                                                                                  |
| description           | Common Function Gateway                                                                                                                                                                               |
| disable_rollback      | True                                                                                                                                                                                                  |
| id                    | 8ccc6c5d-7757-4605-b34b-665ef8858cce                                                                                                                                                                  |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/c583ce78843344adbe5fd20f13620274/stacks/common_function_gateway_f649736d-1920-41eb-96af-d4e4fe192d0e/8ccc6c5d-7757-4605-b34b-665ef8858cce |
| notification_topics   | []                                                                                                                                                                                                    |
| outputs               | [                                                                                                                                                                                                     |
|                       |   {                                                                                                                                                                                                   |
|                       |     "output_value": "cfb54c6f-43cf-4e35-aff8-e2c2ec8adc7e",                                                                                                                                           |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                            |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                              |
|                       |   },                                                                                                                                                                                                  |
|                       |   {                                                                                                                                                                                                   |
|                       |     "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/cfb54c6f-43cf-4e35-aff8-e2c2ec8adc7e",                                                                  |
|                       |     "description": "Monitoring Process Link",                                                                                                                                                         |
|                       |     "output_key": "monitoring_link"                                                                                                                                                                   |
|                       |   }                                                                                                                                                                                                   |
|                       | ]                                                                                                                                                                                                     |
| parameters            | {                                                                                                                                                                                                     |
|                       |   "primary_device_ip": "10.79.5.185",                                                                                                                                                                 |
|                       |   "OS::stack_id": "8ccc6c5d-7757-4605-b34b-665ef8858cce",                                                                                                                                             |
|                       |   "OS::stack_name": "common_function_gateway_f649736d-1920-41eb-96af-d4e4fe192d0e",                                                                                                                   |
|                       |   "primary_device_logical_downlink_interface": "ae0.1025",                                                                                                                                            |
|                       |   "secondary_device_logical_downlink_interface": "ae0.1025",                                                                                                                                          |
|                       |   "secondary_device_port": "830",                                                                                                                                                                     |
|                       |   "secondary_device_password": "******",                                                                                                                                                              |
|                       |   "primary_device_password": "******",                                                                                                                                                                |
|                       |   "version": "1",                                                                                                                                                                                     |
|                       |   "primary_device_username": "esi",                                                                                                                                                                   |
|                       |   "primary_device_physical_downlink_interface": "ae0",                                                                                                                                                |
|                       |   "tenant_id": "c583ce78843344adbe5fd20f13620274",                                                                                                                                                    |
|                       |   "gohan_id": "f649736d-1920-41eb-96af-d4e4fe192d0e",                                                                                                                                                 |
|                       |   "primary_device_port": "830",                                                                                                                                                                       |
|                       |   "secondary_device_physical_downlink_interface": "ae0",                                                                                                                                              |
|                       |   "secondary_device_ip": "10.79.5.184",                                                                                                                                                               |
|                       |   "secondary_device_username": "esi"                                                                                                                                                                  |
|                       | }                                                                                                                                                                                                     |
| parent                | None                                                                                                                                                                                                  |
| stack_name            | common_function_gateway_f649736d-1920-41eb-96af-d4e4fe192d0e                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                                 |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                                       |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                                   |
| stack_user_project_id | c583ce78843344adbe5fd20f13620274                                                                                                                                                                      |
| template_description  | Common Function Gateway                                                                                                                                                                               |
| timeout_mins          | 60                                                                                                                                                                                                    |
| updated_time          | None                                                                                                                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "common_function_gateway" via heatclient.
```
$ heat template-show common_function_gateway_f649736d-1920-41eb-96af-d4e4fe192d0e
description: 'Common Function Gateway

  '
heat_template_version: '2013-05-23'
outputs:
  monitoring_link:
    description: Monitoring Process Link
    value:
      get_attr: [vrrp_monitor, link]
  monitoring_target_id:
    description: Monitoring Target ID
    value: {get_resource: vrrp_monitor}
parameters:
  gohan_id: {description: UUID of the Common Function Gateway, label: Gohan resource
      ID, type: string}
  primary_device_ip: {description: Ip address that will be used to establish ssh connection
      to the Primary Device., label: Ip address of the device., type: string}
  primary_device_logical_downlink_interface: {description: Name of the created logical
      downlink interface on the Primary device, label: Logical Interface name, type: string}
  primary_device_password: {description: Password of the user which will be used to
      log onto the Primary Device., hidden: true, label: Users password., type: string}
  primary_device_physical_downlink_interface: {description: Physical port on the Primary
      device on which the logical downlink port will be configured, label: Underlying
      physical interface, type: string}
  primary_device_port: {description: Port that will be used to establish ssh connection
      to the Primary Device., label: Port of the ssh connection., type: number}
  primary_device_username: {description: Name of the user which will be used to log
      onto the Primary Device., label: User name to log on to device., type: string}
  secondary_device_ip: {description: Ip address that will be used to establish ssh
      connection to the Secondary Device., label: Ip address of the device., type: string}
  secondary_device_logical_downlink_interface: {description: Name of the created logical
      downlink interface on the Secondary device, label: Logical Interface name, type: string}
  secondary_device_password: {description: Password of the user which will be used
      to log onto the Secondary Device., hidden: true, label: Users password., type: string}
  secondary_device_physical_downlink_interface: {description: Physical port on the
      Secondary device on which the logical downlink port will be configured, label: Underlying
      physical interface, type: string}
  secondary_device_port: {description: Port that will be used to establish ssh connection
      to the Secondary Device., label: Port of the ssh connection., type: number}
  secondary_device_username: {description: Name of the user which will be used to
      log onto the Secondary Device., label: User name to log on to device., type: string}
  tenant_id: {label: Tenant ID, type: string}
  version: {label: Config version, type: number}
resources:
  netconf_configure_primary:
    properties:
      configs:
      - config: 'nat-rules vrf_gw_sample-ha-router-downlink_1025-SNAPT;

          nat-rules vrf_gw_sample-ha-router-downlink_1025-DNAT;

          interface-service service-interface ms-0/2/0.1025;

          '
        path:
        - {config_type: tag, tag: services, xml_type: tag}
        - {config_type: named_tag, name: vrf_gw_sample-ha-router-downlink_1025, tag: service-set,
          xml_type: named_tag}
      - config: 'apply-groups SNAPT-POOL;

          address 100.64.0.10/32;

          '
        path:
        - {config_type: tag, tag: services, xml_type: tag}
        - {config_type: tag, tag: nat, xml_type: tag}
        - {config_type: named_tag, name: vrf_gw_sample-ha-router-downlink_1025-SNAPT-POOL,
          tag: pool, xml_type: named_tag}
      - config: 'apply-groups SNAPT-RULE;

          term source then translated source-pool vrf_gw_sample-ha-router-downlink_1025-SNAPT-POOL;

          '
        path:
        - {config_type: tag, tag: services, xml_type: tag}
        - {config_type: tag, tag: nat, xml_type: tag}
        - {config_type: named_tag, name: vrf_gw_sample-ha-router-downlink_1025-SNAPT,
          tag: rule, xml_type: named_tag}
      - config: 'apply-groups DNAT-POOL-1;

          '
        path:
        - {config_type: tag, tag: services, xml_type: tag}
        - {config_type: tag, tag: nat, xml_type: tag}
        - {config_type: named_tag, name: vrf_gw_sample-ha-router-downlink_1025-DNAT-POOL-1,
          tag: pool, xml_type: named_tag}
      - config: 'apply-groups DNAT-POOL-2;

          '
        path:
        - {config_type: tag, tag: services, xml_type: tag}
        - {config_type: tag, tag: nat, xml_type: tag}
        - {config_type: named_tag, name: vrf_gw_sample-ha-router-downlink_1025-DNAT-POOL-2,
          tag: pool, xml_type: named_tag}
      - config: 'apply-groups DNAT-RULE;


          term 1 then translated destination-pool vrf_gw_sample-ha-router-downlink_1025-DNAT-POOL-1;


          term 2 then translated destination-pool vrf_gw_sample-ha-router-downlink_1025-DNAT-POOL-2;

          '
        path:
        - {config_type: tag, tag: services, xml_type: tag}
        - {config_type: tag, tag: nat, xml_type: tag}
        - {config_type: named_tag, name: vrf_gw_sample-ha-router-downlink_1025-DNAT,
          tag: rule, xml_type: named_tag}
      - config: 'peer-unit 11025;

          family inet service input service-set vrf_gw_sample-ha-router-downlink_1025;

          family inet service output service-set vrf_gw_sample-ha-router-downlink_1025;

          '
        path:
        - {config_type: tag, tag: interfaces, xml_type: tag}
        - {config_type: name, name: lt-0/0/0, tag: interface, xml_type: named_tag}
        - {config_type: named_tag, name: 1025, tag: unit, xml_type: named_tag}
      - config: 'peer-unit 1025;

          '
        path:
        - {config_type: tag, tag: interfaces, xml_type: tag}
        - {config_type: name, name: lt-0/0/0, tag: interface, xml_type: named_tag}
        - {config_type: named_tag, name: 11025, tag: unit, xml_type: named_tag}
      - config: 'family inet;

          '
        path:
        - {config_type: tag, tag: interfaces, xml_type: tag}
        - {config_type: name, name: ms-0/2/0, tag: interface, xml_type: named_tag}
        - {config_type: named_tag, name: 1025, tag: unit, xml_type: named_tag}
      - config: 'apply-groups IF-USER-VRRP-ACT;

          description vrf_gw_sample-ha-router-downlink_1025;

          vlan-id 1025;

          family inet service input service-set vrf_gw_sample-ha-router-downlink_1025;

          family inet service output service-set vrf_gw_sample-ha-router-downlink_1025;

          '
        path:
        - {config_type: tag, tag: interfaces, xml_type: tag}
        - config_type: name
          name: {get_param: primary_device_physical_downlink_interface}
          tag: interface
          xml_type: named_tag
        - {config_type: named_tag, name: 1025, tag: unit, xml_type: named_tag}
      - config: ''
        path:
        - {config_type: tag, tag: routing-instances, xml_type: tag}
        - {config_type: name, name: SHARED-RESOURCE, tag: instance, xml_type: named_tag}
        - {config_type: named_tag, name: lt-0/0/0.11025, tag: interface, xml_type: named_tag}
      - config: next-hop lt-0/0/0.11025;
        path:
        - {config_type: tag, tag: routing-instances, xml_type: tag}
        - {config_type: name, name: SHARED-RESOURCE, tag: instance, xml_type: named_tag}
        - {config_type: tag, tag: routing-options, xml_type: tag}
        - {config_type: tag, tag: static, xml_type: tag}
        - {config_type: named_tag, name: 100.64.0.10/32, tag: route, xml_type: named_tag}
      - config:
          str_replace:
            params:
              $DOWNLINK_INTERFACE: {get_param: primary_device_logical_downlink_interface}
            template: 'instance-type virtual-router;

              interface lt-0/0/0.1025;

              interface ms-0/2/0.1025;

              interface $DOWNLINK_INTERFACE;

              routing-options static route 0.0.0.0/0 next-hop lt-0/0/0.1025;

              '
        path:
        - {config_type: tag, tag: routing-instances, xml_type: tag}
        - {config_type: name, name: vrf_gw_sample-ha-router-downlink_1025, tag: instance,
          xml_type: named_tag}
      device_ip: {get_param: primary_device_ip}
      lock_timeout: 3000
      password: {get_param: primary_device_password}
      port: {get_param: primary_device_port}
      username: {get_param: primary_device_username}
    type: OS::Contrail::NetconfNamedConfigs
  netconf_configure_secondary:
    depends_on: netconf_configure_primary
    properties:
      configs:
      - config: 'nat-rules vrf_gw_sample-ha-router-downlink_1025-SNAPT;

          nat-rules vrf_gw_sample-ha-router-downlink_1025-DNAT;

          interface-service service-interface ms-0/2/0.1025;

          '
        path:
        - {config_type: tag, tag: services, xml_type: tag}
        - {config_type: named_tag, name: vrf_gw_sample-ha-router-downlink_1025, tag: service-set,
          xml_type: named_tag}
      - config: 'apply-groups SNAPT-POOL;

          address 100.64.0.10/32;

          '
        path:
        - {config_type: tag, tag: services, xml_type: tag}
        - {config_type: tag, tag: nat, xml_type: tag}
        - {config_type: named_tag, name: vrf_gw_sample-ha-router-downlink_1025-SNAPT-POOL,
          tag: pool, xml_type: named_tag}
      - config: 'apply-groups SNAPT-RULE;

          term source then translated source-pool vrf_gw_sample-ha-router-downlink_1025-SNAPT-POOL;

          '
        path:
        - {config_type: tag, tag: services, xml_type: tag}
        - {config_type: tag, tag: nat, xml_type: tag}
        - {config_type: named_tag, name: vrf_gw_sample-ha-router-downlink_1025-SNAPT,
          tag: rule, xml_type: named_tag}
      - config: 'apply-groups DNAT-POOL-1;

          '
        path:
        - {config_type: tag, tag: services, xml_type: tag}
        - {config_type: tag, tag: nat, xml_type: tag}
        - {config_type: named_tag, name: vrf_gw_sample-ha-router-downlink_1025-DNAT-POOL-1,
          tag: pool, xml_type: named_tag}
      - config: 'apply-groups DNAT-POOL-2;

          '
        path:
        - {config_type: tag, tag: services, xml_type: tag}
        - {config_type: tag, tag: nat, xml_type: tag}
        - {config_type: named_tag, name: vrf_gw_sample-ha-router-downlink_1025-DNAT-POOL-2,
          tag: pool, xml_type: named_tag}
      - config: 'apply-groups DNAT-RULE;


          term 1 then translated destination-pool vrf_gw_sample-ha-router-downlink_1025-DNAT-POOL-1;


          term 2 then translated destination-pool vrf_gw_sample-ha-router-downlink_1025-DNAT-POOL-2;

          '
        path:
        - {config_type: tag, tag: services, xml_type: tag}
        - {config_type: tag, tag: nat, xml_type: tag}
        - {config_type: named_tag, name: vrf_gw_sample-ha-router-downlink_1025-DNAT,
          tag: rule, xml_type: named_tag}
      - config: 'peer-unit 11025;

          family inet service input service-set vrf_gw_sample-ha-router-downlink_1025;

          family inet service output service-set vrf_gw_sample-ha-router-downlink_1025;

          '
        path:
        - {config_type: tag, tag: interfaces, xml_type: tag}
        - {config_type: name, name: lt-0/0/0, tag: interface, xml_type: named_tag}
        - {config_type: named_tag, name: 1025, tag: unit, xml_type: named_tag}
      - config: 'peer-unit 1025;

          '
        path:
        - {config_type: tag, tag: interfaces, xml_type: tag}
        - {config_type: name, name: lt-0/0/0, tag: interface, xml_type: named_tag}
        - {config_type: named_tag, name: 11025, tag: unit, xml_type: named_tag}
      - config: 'family inet;

          '
        path:
        - {config_type: tag, tag: interfaces, xml_type: tag}
        - {config_type: name, name: ms-0/2/0, tag: interface, xml_type: named_tag}
        - {config_type: named_tag, name: 1025, tag: unit, xml_type: named_tag}
      - config: 'apply-groups IF-USER-VRRP-ACT;

          description vrf_gw_sample-ha-router-downlink_1025;

          vlan-id 1025;

          family inet service input service-set vrf_gw_sample-ha-router-downlink_1025;

          family inet service output service-set vrf_gw_sample-ha-router-downlink_1025;

          '
        path:
        - {config_type: tag, tag: interfaces, xml_type: tag}
        - config_type: name
          name: {get_param: secondary_device_physical_downlink_interface}
          tag: interface
          xml_type: named_tag
        - {config_type: named_tag, name: 1025, tag: unit, xml_type: named_tag}
      - config: ''
        path:
        - {config_type: tag, tag: routing-instances, xml_type: tag}
        - {config_type: name, name: SHARED-RESOURCE, tag: instance, xml_type: named_tag}
        - {config_type: named_tag, name: lt-0/0/0.11025, tag: interface, xml_type: named_tag}
      - config: next-hop lt-0/0/0.11025;
        path:
        - {config_type: tag, tag: routing-instances, xml_type: tag}
        - {config_type: name, name: SHARED-RESOURCE, tag: instance, xml_type: named_tag}
        - {config_type: tag, tag: routing-options, xml_type: tag}
        - {config_type: tag, tag: static, xml_type: tag}
        - {config_type: named_tag, name: 100.64.0.10/32, tag: route, xml_type: named_tag}
      - config:
          str_replace:
            params:
              $DOWNLINK_INTERFACE: {get_param: secondary_device_logical_downlink_interface}
            template: 'instance-type virtual-router;

              interface lt-0/0/0.1025;

              interface ms-0/2/0.1025;

              interface $DOWNLINK_INTERFACE;

              routing-options static route 0.0.0.0/0 next-hop lt-0/0/0.1025;

              '
        path:
        - {config_type: tag, tag: routing-instances, xml_type: tag}
        - {config_type: name, name: vrf_gw_sample-ha-router-downlink_1025, tag: instance,
          xml_type: named_tag}
      device_ip: {get_param: secondary_device_ip}
      lock_timeout: 3000
      password: {get_param: secondary_device_password}
      port: {get_param: secondary_device_port}
      username: {get_param: secondary_device_username}
    type: OS::Contrail::NetconfNamedConfigs
  vrrp_monitor:
    depends_on: netconf_configure_secondary
    properties:
      field_name: status
      properties:
        primary:
          host: {get_param: primary_device_ip}
          interface: {get_param: primary_device_logical_downlink_interface}
          login: {get_param: primary_device_username}
          password: {get_param: primary_device_password}
          port: {get_param: primary_device_port}
        secondary:
          host: {get_param: secondary_device_ip}
          interface: {get_param: secondary_device_logical_downlink_interface}
          login: {get_param: secondary_device_username}
          password: {get_param: secondary_device_password}
          port: {get_param: secondary_device_port}
        vrid: [41, 42]
      resource_id: {get_param: gohan_id}
      resource_type: common_function_gateways
      syncer_properties:
        etcd:
          hold_options:
            positive_status: {primary_vrid1: MASTER, primary_vrid2: MASTER, secondary_vrid1: BACKUP,
              secondary_vrid2: BACKUP}
            time_seconds: 360
          status: {key: status}
      tenant_id: {get_param: tenant_id}
      type: vrrp_pool
      version: {get_param: version}
    type: ESI::Monitoring::MonitoringTarget
```
