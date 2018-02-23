# HTTP Methods for creating heat-stack: Internet GW Instance

Checking heat-stack of "internet_gateway" via heatclient.
```
$ heat stack-show internet_gateway_429e24b5-a2f0-4fb8-b467-e335857e9476
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                             |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                |
| creation_time         | 2017-05-11T04:24:07Z                                                                                                                                              |
| description           | Internet GW Instance                                                                                                                                              |
| disable_rollback      | True                                                                                                                                                              |
| id                    | d6e8740b-3293-484e-965d-0a9b0b02328a                                                                                                                              |
| links                 | http://heat-api:8004/v1/0b576f6f4cbf414f829cd12f008bf08f/stacks/internet_gateway_429e24b5-a2f0-4fb8-b467-e335857e9476/d6e8740b-3293-484e-965d-0a9b0b02328a (self) |
| notification_topics   | []                                                                                                                                                                |
| outputs               | []                                                                                                                                                                |
| parameters            | {                                                                                                                                                                 |
|                       |   "vrf_export_policy": "INSTANCE-USER_OUT",                                                                                                                       |
|                       |   "secondary_device_physical_interface": "ae0",                                                                                                                   |
|                       |   "primary_device_username": "esi",                                                                                                                               |
|                       |   "primary_device_logical_interface": "ae0.1025",                                                                                                                 |
|                       |   "primary_device_password": "esiesi0000",                                                                                                                        |
|                       |   "vrf_import_policy": "INSTANCE-USER_IN",                                                                                                                        |
|                       |   "prefix_list_name": "vrf_gw_sample-ha-router-downlink_1025_prefix",                                                                                             |
|                       |   "output_filter_name": "FILTER_10M-GA-DOWN-INET",                                                                                                                |
|                       |   "secondary_vrrp_config_group": "InetGW2-VRRP",                                                                                                                  |
|                       |   "primary_device_ip": "10.79.5.185",                                                                                                                             |
|                       |   "inet_in_filter": "INET_IN",                                                                                                                                    |
|                       |   "secondary_device_username": "esi",                                                                                                                             |
|                       |   "secondary_device_logical_interface": "ae0.1025",                                                                                                               |
|                       |   "OS::stack_name": "internet_gateway_429e24b5-a2f0-4fb8-b467-e335857e9476",                                                                                      |
|                       |   "inet_out_filter": "INET_OUT",                                                                                                                                  |
|                       |   "vlan": "1025",                                                                                                                                                 |
|                       |   "primary_device_physical_interface": "ae0",                                                                                                                     |
|                       |   "uplink_import_policy": "INSTANCE-MASTER_IN",                                                                                                                   |
|                       |   "input_filter_name": "FILTER_10M-GA-UP-INET",                                                                                                                   |
|                       |   "filter_term_name": "vrf_gw_sample-ha-router-downlink_1025_filter",                                                                                             |
|                       |   "OS::stack_id": "d6e8740b-3293-484e-965d-0a9b0b02328a",                                                                                                         |
|                       |   "secondary_device_port": "830",                                                                                                                                 |
|                       |   "secondary_device_password": "esiesi0000",                                                                                                                      |
|                       |   "vrf_name": "vrf_gw_sample-ha-router-downlink_1025",                                                                                                            |
|                       |   "primary_vrrp_config_group": "InetGW1-VRRP",                                                                                                                    |
|                       |   "primary_device_port": "830",                                                                                                                                   |
|                       |   "secondary_device_ip": "10.79.5.184"                                                                                                                            |
|                       | }                                                                                                                                                                 |
| parent                | None                                                                                                                                                              |
| stack_name            | internet_gateway_429e24b5-a2f0-4fb8-b467-e335857e9476                                                                                                             |
| stack_owner           | admin                                                                                                                                                             |
| stack_status          | CREATE_COMPLETE                                                                                                                                                   |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                               |
| stack_user_project_id | 0b576f6f4cbf414f829cd12f008bf08f                                                                                                                                  |
| template_description  | Internet GW Instance                                                                                                                                              |
| timeout_mins          | 60                                                                                                                                                                |
| updated_time          | None                                                                                                                                                              |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "internet_gateway" via heatclient.
```
$ heat template-show internet_gateway_429e24b5-a2f0-4fb8-b467-e335857e9476
description: 'Internet GW Instance

  '
heat_template_version: '2013-05-23'
parameters:
  filter_term_name: {label: Filter term name, type: string}
  inet_in_filter: {label: Internet Input Filter, type: string}
  inet_out_filter: {label: Internet Output Filter, type: string}
  input_filter_name: {description: Policer name to use as input policer, label: Input
      policer name, type: string}
  output_filter_name: {description: Policer name to use as output policer, label: Output
      policer name, type: string}
  prefix_list_name: {label: Prefix list name, type: string}
  primary_device_ip: {description: Ip address that will be used to establish ssh connection
      to the Primary Device., label: Ip address of the device., type: string}
  primary_device_logical_interface: {description: Name of the created logical interface
      on the Primary device, label: Logical Interface name, type: string}
  primary_device_password: {description: Password of the user which will be used to
      log onto the Primary Device., label: Users password., type: string}
  primary_device_physical_interface: {description: Physical port on the Primary device
      on which the logical port will be configured, label: Underlying physical interface,
    type: string}
  primary_device_port: {description: Port that will be used to establish ssh connection
      to the Primary Device., label: Port of the ssh connection., type: number}
  primary_device_username: {description: Name of the user which will be used to log
      onto the Primary Device., label: User name to log on to device., type: string}
  primary_vrrp_config_group: {description: Name for apply group to use for interface
      for VRRP, label: Apply group name, type: string}
  secondary_device_ip: {description: Ip address that will be used to establish ssh
      connection to the Secondary Device., label: Ip address of the device., type: string}
  secondary_device_logical_interface: {description: Name of the created logical interface
      on the Secondary device, label: Logical Interface name, type: string}
  secondary_device_password: {description: Password of the user which will be used
      to log onto the Secondary Device., label: Users password., type: string}
  secondary_device_physical_interface: {description: Physical port on the Secondary
      device on which the logical port will be configured, label: Underlying physical
      interface, type: string}
  secondary_device_port: {description: Port that will be used to establish ssh connection
      to the Secondary Device., label: Port of the ssh connection., type: number}
  secondary_device_username: {description: Name of the user which will be used to
      log onto the Secondary Device., label: User name to log on to device., type: string}
  secondary_vrrp_config_group: {description: Name for apply group to use for interface
      for VRRP, label: Apply group name, type: string}
  uplink_import_policy: {description: Uplink Import Policy for IGS, label: Uplink
      Import Policy, type: string}
  vlan: {description: vlan tag used by logical interface, label: VLAN ID, type: string}
  vrf_export_policy: {description: Export Policy for IGS, label: Export Policy, type: string}
  vrf_import_policy: {description: Import Policy for IGS, label: Import Policy, type: string}
  vrf_name: {description: Name for VRF used by logical interface, label: VRF name,
    type: string}
resources:
  netconf_configure_primary:
    properties:
      configs:
      - config:
          str_replace:
            params:
              $APPLY_GROUP: {get_param: primary_vrrp_config_group}
              $INPUT_FILTER: {get_param: input_filter_name}
              $OUTPUT_FILTER: {get_param: output_filter_name}
              $VLAN: {get_param: vlan}
            template: "apply-groups $APPLY_GROUP\nvlan-id $VLAN;\ndescription inet_gw;\n\
              family inet {\n    filter {\n        input $INPUT_FILTER;\n        output\
              \ $OUTPUT_FILTER;\n    }\n}\n"
        path:
        - {config_type: tag, tag: interfaces, xml_type: tag}
        - config_type: name
          name: {get_param: primary_device_physical_interface}
          tag: interface
          xml_type: named_tag
        - config_type: named_tag
          name: {get_param: vlan}
          tag: unit
          xml_type: named_tag
      - config:
          str_replace:
            params:
              $EXPORT_POLICY: {get_param: vrf_export_policy}
              $IMPORT_POLICY: {get_param: vrf_import_policy}
              $LIF: {get_param: primary_device_logical_interface}
            template: 'instance-type virtual-router;

              interface $LIF;

              routing-options instance-import $IMPORT_POLICY;

              routing-options instance-export $EXPORT_POLICY;

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
              $VRF_NAME: {get_param: vrf_name}
            template: 'from instance $VRF_NAME;

              then accept;

              '
        path:
        - {config_type: tag, tag: policy-options, xml_type: tag}
        - config_type: named_tag
          name: {get_param: uplink_import_policy}
          tag: policy-statement
          xml_type: named_tag
        - config_type: named_tag
          name: {get_param: vrf_name}
          tag: term
          xml_type: named_tag
      - config: ''
        path:
        - {config_type: tag, tag: policy-options, xml_type: tag}
        - config_type: named_tag
          name: {get_param: prefix_list_name}
          tag: prefix-list
          xml_type: named_tag
      - additional_commands:
          str_replace:
            params:
              $INET_IN: {get_param: inet_in_filter}
              $TERM_NAME: {get_param: filter_term_name}
            template: 'insert firewall family inet filter $INET_IN term $TERM_NAME
              before term all-accept

              '
        config:
          str_replace:
            params:
              $PREFIX_LIST_NAME: {get_param: prefix_list_name}
              $VRF_NAME: {get_param: vrf_name}
            template: "from {\n   destination-prefix-list {\n        $PREFIX_LIST_NAME;\n\
              \   }\n}\nthen {\n     count $VRF_NAME_IN;\n     accept;\n}\n"
        path:
        - {config_type: tag, tag: firewall, xml_type: tag}
        - {config_type: tag, tag: family, xml_type: tag}
        - {config_type: tag, tag: inet, xml_type: tag}
        - config_type: named_tag
          name: {get_param: inet_in_filter}
          tag: filter
          xml_type: named_tag
        - config_type: named_tag
          name: {get_param: filter_term_name}
          tag: term
          xml_type: named_tag
      - additional_commands:
          str_replace:
            params:
              $INET_OUT: {get_param: inet_out_filter}
              $TERM_NAME: {get_param: filter_term_name}
            template: 'insert firewall family inet filter $INET_OUT term $TERM_NAME
              before term all-accept

              '
        config:
          str_replace:
            params:
              $PREFIX_LIST_NAME: {get_param: prefix_list_name}
              $VRF_NAME: {get_param: vrf_name}
            template: "from {\n   source-prefix-list {\n        $PREFIX_LIST_NAME;\n\
              \   }\n}\nthen {\n     count $VRF_NAME_OUT;\n     accept;\n}\n"
        path:
        - {config_type: tag, tag: firewall, xml_type: tag}
        - {config_type: tag, tag: family, xml_type: tag}
        - {config_type: tag, tag: inet, xml_type: tag}
        - config_type: named_tag
          name: {get_param: inet_out_filter}
          tag: filter
          xml_type: named_tag
        - config_type: named_tag
          name: {get_param: filter_term_name}
          tag: term
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
              $APPLY_GROUP: {get_param: secondary_vrrp_config_group}
              $INPUT_FILTER: {get_param: input_filter_name}
              $OUTPUT_FILTER: {get_param: output_filter_name}
              $VLAN: {get_param: vlan}
            template: "apply-groups $APPLY_GROUP\nvlan-id $VLAN;\ndescription inet_gw;\n\
              family inet {\n    filter {\n        input $INPUT_FILTER;\n        output\
              \ $OUTPUT_FILTER;\n    }\n}\n"
        path:
        - {config_type: tag, tag: interfaces, xml_type: tag}
        - config_type: name
          name: {get_param: secondary_device_physical_interface}
          tag: interface
          xml_type: named_tag
        - config_type: named_tag
          name: {get_param: vlan}
          tag: unit
          xml_type: named_tag
      - config:
          str_replace:
            params:
              $EXPORT_POLICY: {get_param: vrf_export_policy}
              $IMPORT_POLICY: {get_param: vrf_import_policy}
              $LIF: {get_param: secondary_device_logical_interface}
            template: 'instance-type virtual-router;

              interface $LIF;

              routing-options instance-import $IMPORT_POLICY;

              routing-options instance-export $EXPORT_POLICY;

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
              $VRF_NAME: {get_param: vrf_name}
            template: 'from instance $VRF_NAME;

              then accept;

              '
        path:
        - {config_type: tag, tag: policy-options, xml_type: tag}
        - config_type: named_tag
          name: {get_param: uplink_import_policy}
          tag: policy-statement
          xml_type: named_tag
        - config_type: named_tag
          name: {get_param: vrf_name}
          tag: term
          xml_type: named_tag
      - config: ''
        path:
        - {config_type: tag, tag: policy-options, xml_type: tag}
        - config_type: named_tag
          name: {get_param: prefix_list_name}
          tag: prefix-list
          xml_type: named_tag
      - additional_commands:
          str_replace:
            params:
              $INET_IN: {get_param: inet_in_filter}
              $TERM_NAME: {get_param: filter_term_name}
            template: 'insert firewall family inet filter $INET_IN term $TERM_NAME
              before term all-accept

              '
        config:
          str_replace:
            params:
              $PREFIX_LIST_NAME: {get_param: prefix_list_name}
              $VRF_NAME: {get_param: vrf_name}
            template: "from {\n   destination-prefix-list {\n        $PREFIX_LIST_NAME;\n\
              \   }\n}\nthen {\n     count $VRF_NAME_IN;\n     accept;\n}\n"
        path:
        - {config_type: tag, tag: firewall, xml_type: tag}
        - {config_type: tag, tag: family, xml_type: tag}
        - {config_type: tag, tag: inet, xml_type: tag}
        - config_type: named_tag
          name: {get_param: inet_in_filter}
          tag: filter
          xml_type: named_tag
        - config_type: named_tag
          name: {get_param: filter_term_name}
          tag: term
          xml_type: named_tag
      - additional_commands:
          str_replace:
            params:
              $INET_OUT: {get_param: inet_out_filter}
              $TERM_NAME: {get_param: filter_term_name}
            template: 'insert firewall family inet filter $INET_OUT term $TERM_NAME
              before term all-accept

              '
        config:
          str_replace:
            params:
              $PREFIX_LIST_NAME: {get_param: prefix_list_name}
              $VRF_NAME: {get_param: vrf_name}
            template: "from {\n   source-prefix-list {\n        $PREFIX_LIST_NAME;\n\
              \   }\n}\nthen {\n     count $VRF_NAME_OUT;\n     accept;\n}\n"
        path:
        - {config_type: tag, tag: firewall, xml_type: tag}
        - {config_type: tag, tag: family, xml_type: tag}
        - {config_type: tag, tag: inet, xml_type: tag}
        - config_type: named_tag
          name: {get_param: inet_out_filter}
          tag: filter
          xml_type: named_tag
        - config_type: named_tag
          name: {get_param: filter_term_name}
          tag: term
          xml_type: named_tag
      device_ip: {get_param: secondary_device_ip}
      lock_timeout: 3000
      on_update: merge
      password: {get_param: secondary_device_password}
      port: {get_param: secondary_device_port}
      username: {get_param: secondary_device_username}
    type: OS::Contrail::NetconfNamedConfigs
```
