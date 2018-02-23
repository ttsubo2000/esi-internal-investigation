# HTTP Methods for updating heat-stack: VPN Gateway

Checking heat-stack of "vpn_gateway" via heatclient.
```
$ heat stack-show vpn_gateway_4fab887d-8f73-40e6-b2d8-2426255231bf
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                        |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                           |
| creation_time         | 2017-05-11T05:00:10Z                                                                                                                                         |
| description           | VPN Gateway                                                                                                                                                  |
| disable_rollback      | True                                                                                                                                                         |
| id                    | 8b8fd087-b322-41fb-8751-63042be0c8f7                                                                                                                         |
| links                 | http://heat-api:8004/v1/0b576f6f4cbf414f829cd12f008bf08f/stacks/vpn_gateway_4fab887d-8f73-40e6-b2d8-2426255231bf/8b8fd087-b322-41fb-8751-63042be0c8f7 (self) |
| notification_topics   | []                                                                                                                                                           |
| outputs               | []                                                                                                                                                           |
| parameters            | {                                                                                                                                                            |
|                       |   "primary_device_logical_uplink_interface": "ge-0/0/1.122",                                                                                                 |
|                       |   "primary_device_logical_downlink_interface": "ae0.1025",                                                                                                   |
|                       |   "primary_device_password": "esiesi0000",                                                                                                                   |
|                       |   "output_filter_name": "FILTER_10M-GA-DOWN-VPN",                                                                                                            |
|                       |   "primary_device_ip": "10.79.5.185",                                                                                                                        |
|                       |   "secondary_device_physical_downlink_interface": "ae0",                                                                                                     |
|                       |   "secondary_device_username": "esi",                                                                                                                        |
|                       |   "primary_device_physical_uplink_interface": "ge-0/0/1",                                                                                                    |
|                       |   "secondary_device_logical_uplink_interface": "ge-0/0/1.122",                                                                                               |
|                       |   "downlink_vlan": "1025",                                                                                                                                   |
|                       |   "OS::stack_name": "vpn_gateway_4fab887d-8f73-40e6-b2d8-2426255231bf",                                                                                      |
|                       |   "secondary_device_logical_downlink_interface": "ae0.1025",                                                                                                 |
|                       |   "input_filter_name": "FILTER_10M-GA-UP-VPN",                                                                                                               |
|                       |   "uplink_vlan": "122",                                                                                                                                      |
|                       |   "OS::stack_id": "8b8fd087-b322-41fb-8751-63042be0c8f7",                                                                                                    |
|                       |   "secondary_device_port": "830",                                                                                                                            |
|                       |   "primary_downlink_vrrp_config_group": "VPNGW1-VRRP",                                                                                                       |
|                       |   "secondary_device_password": "esiesi0000",                                                                                                                 |
|                       |   "vrf_name": "vrf_gw_sample-ha-router-downlink_1025",                                                                                                       |
|                       |   "primary_device_username": "esi",                                                                                                                          |
|                       |   "primary_device_physical_downlink_interface": "ae0",                                                                                                       |
|                       |   "secondary_downlink_vrrp_config_group": "VPNGW2-VRRP",                                                                                                     |
|                       |   "primary_device_port": "830",                                                                                                                              |
|                       |   "secondary_device_physical_uplink_interface": "ge-0/0/1",                                                                                                  |
|                       |   "secondary_device_ip": "10.79.5.184"                                                                                                                       |
|                       | }                                                                                                                                                            |
| parent                | None                                                                                                                                                         |
| stack_name            | vpn_gateway_4fab887d-8f73-40e6-b2d8-2426255231bf                                                                                                             |
| stack_owner           | admin                                                                                                                                                        |
| stack_status          | UPDATE_COMPLETE                                                                                                                                              |
| stack_status_reason   | Stack successfully updated                                                                                                                                   |
| stack_user_project_id | 0b576f6f4cbf414f829cd12f008bf08f                                                                                                                             |
| template_description  | VPN Gateway                                                                                                                                                  |
| timeout_mins          | 60                                                                                                                                                           |
| updated_time          | 2017-05-11T05:00:59Z                                                                                                                                         |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "vpn_gateway" via heatclient.
```
$ heat template-show vpn_gateway_4fab887d-8f73-40e6-b2d8-2426255231bf
description: 'VPN Gateway

  '
heat_template_version: '2013-05-23'
parameters:
  downlink_vlan: {description: vlan tag used by logical downlink interface, label: VLAN
      ID, type: string}
  input_filter_name: {description: Name for policer used for input, label: Input filter
      name, type: string}
  output_filter_name: {description: Name for policer used for output, label: Output
      filter name, type: string}
  primary_device_ip: {description: Ip address that will be used to establish ssh connection
      to the Primary Device., label: Ip address of the device., type: string}
  primary_device_logical_downlink_interface: {description: Name of the created logical
      downlink interface on the Primary device, label: Logical Interface name, type: string}
  primary_device_logical_uplink_interface: {description: Name of the created logical
      uplink interface on the Primary device, label: Logical Interface name, type: string}
  primary_device_password: {description: Password of the user which will be used to
      log onto the Primary Device., label: Users password., type: string}
  primary_device_physical_downlink_interface: {description: Physical port on the Primary
      device on which the logical downlink port will be configured, label: Underlying
      physical interface, type: string}
  primary_device_physical_uplink_interface: {description: Physical port on the Primary
      device on which the logical uplink port will be configured, label: Underlying
      physical interface, type: string}
  primary_device_port: {description: Port that will be used to establish ssh connection
      to the Primary Device., label: Port of the ssh connection., type: number}
  primary_device_username: {description: Name of the user which will be used to log
      onto the Primary Device., label: User name to log on to device., type: string}
  primary_downlink_vrrp_config_group: {description: Name for apply group to use for
      downlink interface for VRRP, label: Apply group name, type: string}
  secondary_device_ip: {description: Ip address that will be used to establish ssh
      connection to the Secondary Device., label: Ip address of the device., type: string}
  secondary_device_logical_downlink_interface: {description: Name of the created logical
      downlink interface on the Secondary device, label: Logical Interface name, type: string}
  secondary_device_logical_uplink_interface: {description: Name of the created logical
      uplink interface on the Secondary device, label: Logical Interface name, type: string}
  secondary_device_password: {description: Password of the user which will be used
      to log onto the Secondary Device., label: Users password., type: string}
  secondary_device_physical_downlink_interface: {description: Physical port on the
      Secondary device on which the logical downlink port will be configured, label: Underlying
      physical interface, type: string}
  secondary_device_physical_uplink_interface: {description: Physical port on the Secondary
      device on which the logical uplink port will be configured, label: Underlying
      physical interface, type: string}
  secondary_device_port: {description: Port that will be used to establish ssh connection
      to the Secondary Device., label: Port of the ssh connection., type: number}
  secondary_device_username: {description: Name of the user which will be used to
      log onto the Secondary Device., label: User name to log on to device., type: string}
  secondary_downlink_vrrp_config_group: {description: Name for apply group to use
      for downlink interface for VRRP, label: Apply group name, type: string}
  uplink_vlan: {description: vlan tag used by logical uplink interface, label: VLAN
      ID, type: string}
  vrf_name: {description: Name for VRF used by logical interfaces, label: VRF name,
    type: string}
resources:
  netconf_configure_primary:
    properties:
      configs:
      - config:
          str_replace:
            params:
              $APPLY_GROUP: {get_param: primary_downlink_vrrp_config_group}
              $INPUT_FILTER: {get_param: input_filter_name}
              $OUTPUT_FILTER: {get_param: output_filter_name}
              $VLAN: {get_param: downlink_vlan}
            template: "apply-groups $APPLY_GROUP\nvlan-id $VLAN;\ndescription vpn_gw;\n\
              family inet {\n    filter {\n        input $INPUT_FILTER;\n        output\
              \ $OUTPUT_FILTER;\n    }\n}\n"
        path:
        - {config_type: tag, tag: interfaces, xml_type: tag}
        - config_type: name
          name: {get_param: primary_device_physical_downlink_interface}
          tag: interface
          xml_type: named_tag
        - config_type: named_tag
          name: {get_param: downlink_vlan}
          tag: unit
          xml_type: named_tag
      - config:
          str_replace:
            params:
              $LIFD: {get_param: primary_device_logical_downlink_interface}
              $LIFU: {get_param: primary_device_logical_uplink_interface}
            template: 'instance-type virtual-router;

              interface $LIFD;

              interface $LIFU;

              '
        path:
        - {config_type: tag, tag: routing-instances, xml_type: tag}
        - config_type: name
          name: {get_param: vrf_name}
          tag: instance
          xml_type: named_tag
      - config:
          str_replace:
            params:
              $VLAN: {get_param: uplink_vlan}
            template: 'vlan-id $VLAN;

              description CloudGW_vpn;

              '
        path:
        - {config_type: tag, tag: interfaces, xml_type: tag}
        - config_type: name
          name: {get_param: primary_device_physical_uplink_interface}
          tag: interface
          xml_type: named_tag
        - config_type: named_tag
          name: {get_param: uplink_vlan}
          tag: unit
          xml_type: named_tag
      device_ip: {get_param: primary_device_ip}
      lock_timeout: 3000
      on_update: merge
      password: {get_param: primary_device_password}
      port: {get_param: primary_device_port}
      username: {get_param: primary_device_username}
    type: OS::Contrail::NetconfNamedConfigs
  netconf_configure_secondary:
    properties:
      configs:
      - config:
          str_replace:
            params:
              $APPLY_GROUP: {get_param: secondary_downlink_vrrp_config_group}
              $INPUT_FILTER: {get_param: input_filter_name}
              $OUTPUT_FILTER: {get_param: output_filter_name}
              $VLAN: {get_param: downlink_vlan}
            template: "apply-groups $APPLY_GROUP\nvlan-id $VLAN;\ndescription vpn_gw;\n\
              family inet {\n    filter {\n        input $INPUT_FILTER;\n        output\
              \ $OUTPUT_FILTER;\n    }\n}\n"
        path:
        - {config_type: tag, tag: interfaces, xml_type: tag}
        - config_type: name
          name: {get_param: secondary_device_physical_downlink_interface}
          tag: interface
          xml_type: named_tag
        - config_type: named_tag
          name: {get_param: downlink_vlan}
          tag: unit
          xml_type: named_tag
      - config:
          str_replace:
            params:
              $LIFD: {get_param: secondary_device_logical_downlink_interface}
              $LIFU: {get_param: secondary_device_logical_uplink_interface}
            template: 'instance-type virtual-router;

              interface $LIFD;

              interface $LIFU;

              '
        path:
        - {config_type: tag, tag: routing-instances, xml_type: tag}
        - config_type: name
          name: {get_param: vrf_name}
          tag: instance
          xml_type: named_tag
      - config:
          str_replace:
            params:
              $VLAN: {get_param: uplink_vlan}
            template: 'vlan-id $VLAN;

              description CloudGW_vpn;

              '
        path:
        - {config_type: tag, tag: interfaces, xml_type: tag}
        - config_type: name
          name: {get_param: secondary_device_physical_uplink_interface}
          tag: interface
          xml_type: named_tag
        - config_type: named_tag
          name: {get_param: uplink_vlan}
          tag: unit
          xml_type: named_tag
      device_ip: {get_param: secondary_device_ip}
      lock_timeout: 3000
      on_update: merge
      password: {get_param: secondary_device_password}
      port: {get_param: secondary_device_port}
      username: {get_param: secondary_device_username}
    type: OS::Contrail::NetconfNamedConfigs
```
