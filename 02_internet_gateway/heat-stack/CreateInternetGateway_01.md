# HTTP Methods for creating heat-stack: Internet GW Instance

Checking heat-stack of "internet_gateway" via heatclient.
```
$ heat stack-show internet_gateway_f6e8c695-c4c1-4a93-9b7e-1663aee6dec9
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                          |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                             |
| creation_time         | 2018-04-04T05:00:29Z                                                                                                                                                                           |
| description           | Internet GW Instance                                                                                                                                                                           |
| disable_rollback      | True                                                                                                                                                                                           |
| id                    | cc36f14a-4224-4cd7-bf49-c8014783a399                                                                                                                                                           |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/06d6b792b31c40daa546fb0f4e35980d/stacks/internet_gateway_f6e8c695-c4c1-4a93-9b7e-1663aee6dec9/cc36f14a-4224-4cd7-bf49-c8014783a399 |
| notification_topics   | []                                                                                                                                                                                             |
| outputs               | [                                                                                                                                                                                              |
|                       |   {                                                                                                                                                                                            |
|                       |     "output_value": "ca354a39-f48c-4698-9cdd-9e106e2a5bf4",                                                                                                                                    |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                     |
|                       |     "output_key": "primary_monitoring_target_id"                                                                                                                                               |
|                       |   },                                                                                                                                                                                           |
|                       |   {                                                                                                                                                                                            |
|                       |     "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/e4609dae-5c88-494a-bdb5-19187026ccfc",                                                           |
|                       |     "description": "Monitoring Process Link",                                                                                                                                                  |
|                       |     "output_key": "secondary_monitoring_link"                                                                                                                                                  |
|                       |   },                                                                                                                                                                                           |
|                       |   {                                                                                                                                                                                            |
|                       |     "output_value": "e4609dae-5c88-494a-bdb5-19187026ccfc",                                                                                                                                    |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                     |
|                       |     "output_key": "secondary_monitoring_target_id"                                                                                                                                             |
|                       |   },                                                                                                                                                                                           |
|                       |   {                                                                                                                                                                                            |
|                       |     "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/ca354a39-f48c-4698-9cdd-9e106e2a5bf4",                                                           |
|                       |     "description": "Monitoring Process Link",                                                                                                                                                  |
|                       |     "output_key": "primary_monitoring_link"                                                                                                                                                    |
|                       |   }                                                                                                                                                                                            |
|                       | ]                                                                                                                                                                                              |
| parameters            | {                                                                                                                                                                                              |
|                       |   "vrf_export_policy": "INSTANCE-USER_OUT",                                                                                                                                                    |
|                       |   "secondary_device_physical_interface": "ae0",                                                                                                                                                |
|                       |   "counter_name_out": "vrf_gw_sample-ha-router-downlink_1025_OUT",                                                                                                                             |
|                       |   "primary_device_username": "esi",                                                                                                                                                            |
|                       |   "primary_device_logical_interface": "ae0.1025",                                                                                                                                              |
|                       |   "primary_device_password": "******",                                                                                                                                                         |
|                       |   "gohan_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9",                                                                                                                                          |
|                       |   "vrf_import_policy": "INSTANCE-USER_IN",                                                                                                                                                     |
|                       |   "prefix_list_name": "vrf_gw_sample-ha-router-downlink_1025_prefix",                                                                                                                          |
|                       |   "output_filter_name": "FILTER_10M-GA-DOWN-INET",                                                                                                                                             |
|                       |   "secondary_vrrp_config_group": "InetGW2-VRRP",                                                                                                                                               |
|                       |   "primary_device_ip": "10.79.5.185",                                                                                                                                                          |
|                       |   "version": "1",                                                                                                                                                                              |
|                       |   "inet_in_filter": "INET_IN",                                                                                                                                                                 |
|                       |   "secondary_device_username": "esi",                                                                                                                                                          |
|                       |   "secondary_device_logical_interface": "ae0.1025",                                                                                                                                            |
|                       |   "counter_name_in": "vrf_gw_sample-ha-router-downlink_1025_IN",                                                                                                                               |
|                       |   "OS::stack_name": "internet_gateway_f6e8c695-c4c1-4a93-9b7e-1663aee6dec9",                                                                                                                   |
|                       |   "inet_out_filter": "INET_OUT",                                                                                                                                                               |
|                       |   "vlan": "1025",                                                                                                                                                                              |
|                       |   "primary_device_physical_interface": "ae0",                                                                                                                                                  |
|                       |   "uplink_import_policy": "INSTANCE-MASTER_IN",                                                                                                                                                |
|                       |   "input_filter_name": "FILTER_10M-GA-UP-INET",                                                                                                                                                |
|                       |   "filter_term_name": "vrf_gw_sample-ha-router-downlink_1025_filter",                                                                                                                          |
|                       |   "OS::stack_id": "cc36f14a-4224-4cd7-bf49-c8014783a399",                                                                                                                                      |
|                       |   "tenant_id": "06d6b792b31c40daa546fb0f4e35980d",                                                                                                                                             |
|                       |   "secondary_device_port": "830",                                                                                                                                                              |
|                       |   "secondary_device_password": "******",                                                                                                                                                       |
|                       |   "vrf_name": "vrf_gw_sample-ha-router-downlink_1025",                                                                                                                                         |
|                       |   "primary_vrrp_config_group": "InetGW1-VRRP",                                                                                                                                                 |
|                       |   "primary_device_port": "830",                                                                                                                                                                |
|                       |   "secondary_device_ip": "10.79.5.184"                                                                                                                                                         |
|                       | }                                                                                                                                                                                              |
| parent                | None                                                                                                                                                                                           |
| stack_name            | internet_gateway_f6e8c695-c4c1-4a93-9b7e-1663aee6dec9                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                          |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                                |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                            |
| stack_user_project_id | 06d6b792b31c40daa546fb0f4e35980d                                                                                                                                                               |
| template_description  | Internet GW Instance                                                                                                                                                                           |
| timeout_mins          | 60                                                                                                                                                                                             |
| updated_time          | None                                                                                                                                                                                           |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "internet_gateway" via heatclient.
```
$ heat template-show internet_gateway_f6e8c695-c4c1-4a93-9b7e-1663aee6dec9
description: 'Internet GW Instance

  '
heat_template_version: '2013-05-23'
outputs:
  primary_monitoring_link:
    description: Monitoring Process Link
    value:
      get_attr: [primary_igs_metric_monitor, link]
  primary_monitoring_target_id:
    description: Monitoring Target ID
    value: {get_resource: primary_igs_metric_monitor}
  secondary_monitoring_link:
    description: Monitoring Process Link
    value:
      get_attr: [secondary_igs_metric_monitor, link]
  secondary_monitoring_target_id:
    description: Monitoring Target ID
    value: {get_resource: secondary_igs_metric_monitor}
parameters:
  counter_name_in: {label: Input counter name, type: string}
  counter_name_out: {label: Output counter name, type: string}
  filter_term_name: {label: Filter term name, type: string}
  gohan_id: {description: UUID of the GW Interface, label: Gohan resource ID, type: string}
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
      log onto the Primary Device., hidden: true, label: Users password., type: string}
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
      to log onto the Secondary Device., hidden: true, label: Users password., type: string}
  secondary_device_physical_interface: {description: Physical port on the Secondary
      device on which the logical port will be configured, label: Underlying physical
      interface, type: string}
  secondary_device_port: {description: Port that will be used to establish ssh connection
      to the Secondary Device., label: Port of the ssh connection., type: number}
  secondary_device_username: {description: Name of the user which will be used to
      log onto the Secondary Device., label: User name to log on to device., type: string}
  secondary_vrrp_config_group: {description: Name for apply group to use for interface
      for VRRP, label: Apply group name, type: string}
  tenant_id: {label: Tenant ID, type: string}
  uplink_import_policy: {description: Uplink Import Policy for IGS, label: Uplink
      Import Policy, type: string}
  version: {label: Config version, type: number}
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
    depends_on: netconf_configure_primary
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
  primary_igs_metric_monitor:
    depends_on: netconf_configure_secondary
    properties:
      field_name: primary_counter
      properties:
        counter_name_in: {get_param: counter_name_in}
        counter_name_out: {get_param: counter_name_out}
        host: {get_param: primary_device_ip}
        login: {get_param: primary_device_username}
        password: {get_param: primary_device_password}
        port: {get_param: primary_device_port}
        primary_device_ip: {get_param: primary_device_ip}
        secondary_device_ip: {get_param: secondary_device_ip}
      resource_id: {get_param: gohan_id}
      resource_type: internet_gateways
      syncer_properties:
        tsdb:
          traffic.in:
            metric: traffic.bytes
            tags:
              device_index: primary
              direction: in
              resource_id: {get_param: gohan_id}
          traffic.out:
            metric: traffic.bytes
            tags:
              device_index: primary
              direction: out
              resource_id: {get_param: gohan_id}
      tenant_id: {get_param: tenant_id}
      type: igs_counter
      version: {get_param: version}
    type: ESI::Monitoring::MonitoringTarget
  secondary_igs_metric_monitor:
    depends_on: netconf_configure_secondary
    properties:
      field_name: secondary_counter
      properties:
        counter_name_in: {get_param: counter_name_in}
        counter_name_out: {get_param: counter_name_out}
        host: {get_param: secondary_device_ip}
        login: {get_param: secondary_device_username}
        password: {get_param: secondary_device_password}
        port: {get_param: secondary_device_port}
        primary_device_ip: {get_param: primary_device_ip}
        secondary_device_ip: {get_param: secondary_device_ip}
      resource_id: {get_param: gohan_id}
      resource_type: internet_gateways
      syncer_properties:
        tsdb:
          traffic.in:
            metric: traffic.bytes
            tags:
              device_index: secondary
              direction: in
              resource_id: {get_param: gohan_id}
          traffic.out:
            metric: traffic.bytes
            tags:
              device_index: secondary
              direction: out
              resource_id: {get_param: gohan_id}
      tenant_id: {get_param: tenant_id}
      type: igs_counter
      version: {get_param: version}
    type: ESI::Monitoring::MonitoringTarget
```
