# HTTP Methods for creating heat-stack: Common Function Gateway

Checking heat-stack of "common_function_gateway" via heatclient.
```
$ heat stack-show common_function_gateway_5c241c51-2003-407a-a239-689fabd19022
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                    |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                       |
| creation_time         | 2017-05-11T03:05:37Z                                                                                                                                                     |
| description           | Common Function Gateway                                                                                                                                                  |
| disable_rollback      | True                                                                                                                                                                     |
| id                    | 1d03f6d9-3d61-44b0-a250-247c0b50cf70                                                                                                                                     |
| links                 | http://heat-api:8004/v1/0b576f6f4cbf414f829cd12f008bf08f/stacks/common_function_gateway_5c241c51-2003-407a-a239-689fabd19022/1d03f6d9-3d61-44b0-a250-247c0b50cf70 (self) |
| notification_topics   | []                                                                                                                                                                       |
| outputs               | []                                                                                                                                                                       |
| parameters            | {                                                                                                                                                                        |
|                       |   "primary_device_ip": "10.79.5.185",                                                                                                                                    |
|                       |   "OS::stack_id": "1d03f6d9-3d61-44b0-a250-247c0b50cf70",                                                                                                                |
|                       |   "OS::stack_name": "common_function_gateway_5c241c51-2003-407a-a239-689fabd19022",                                                                                      |
|                       |   "primary_device_logical_downlink_interface": "ae0.1025",                                                                                                               |
|                       |   "secondary_device_logical_downlink_interface": "ae0.1025",                                                                                                             |
|                       |   "secondary_device_port": "830",                                                                                                                                        |
|                       |   "secondary_device_password": "esiesi0000",                                                                                                                             |
|                       |   "primary_device_password": "esiesi0000",                                                                                                                               |
|                       |   "primary_device_username": "esi",                                                                                                                                      |
|                       |   "primary_device_physical_downlink_interface": "ae0",                                                                                                                   |
|                       |   "primary_device_port": "830",                                                                                                                                          |
|                       |   "secondary_device_physical_downlink_interface": "ae0",                                                                                                                 |
|                       |   "secondary_device_ip": "10.79.5.184",                                                                                                                                  |
|                       |   "secondary_device_username": "esi"                                                                                                                                     |
|                       | }                                                                                                                                                                        |
| parent                | None                                                                                                                                                                     |
| stack_name            | common_function_gateway_5c241c51-2003-407a-a239-689fabd19022                                                                                                             |
| stack_owner           | admin                                                                                                                                                                    |
| stack_status          | CREATE_COMPLETE                                                                                                                                                          |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                      |
| stack_user_project_id | 0b576f6f4cbf414f829cd12f008bf08f                                                                                                                                         |
| template_description  | Common Function Gateway                                                                                                                                                  |
| timeout_mins          | 60                                                                                                                                                                       |
| updated_time          | None                                                                                                                                                                     |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "common_function_gateway" via heatclient.
```
$ heat template-show common_function_gateway_5c241c51-2003-407a-a239-689fabd19022
description: 'Common Function Gateway

  '
heat_template_version: '2013-05-23'
parameters:
  primary_device_ip: {description: Ip address that will be used to establish ssh connection
      to the Primary Device., label: Ip address of the device., type: string}
  primary_device_logical_downlink_interface: {description: Name of the created logical
      downlink interface on the Primary device, label: Logical Interface name, type: string}
  primary_device_password: {description: Password of the user which will be used to
      log onto the Primary Device., label: Users password., type: string}
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
      to log onto the Secondary Device., label: Users password., type: string}
  secondary_device_physical_downlink_interface: {description: Physical port on the
      Secondary device on which the logical downlink port will be configured, label: Underlying
      physical interface, type: string}
  secondary_device_port: {description: Port that will be used to establish ssh connection
      to the Secondary Device., label: Port of the ssh connection., type: number}
  secondary_device_username: {description: Name of the user which will be used to
      log onto the Secondary Device., label: User name to log on to device., type: string}
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
```
