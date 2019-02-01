# heat_template: internet_gateway
This is heat_template of "internet_gateway" which is provided by gohan via etcd

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/internet_gateway
{
    "body": {
        "handler": "heat_worker",
        "watch": [],
        "id": "internet_gateway",
        "template_file": "heat_template_version: 2013-05-23\n\ndescription: >\n  Internet GW Instance\n\nparameters:\n  primary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Primary Device.\n    label: Ip address of the device.\n    type: string\n  primary_device_port:\n    description: Port that will be used to establish ssh connection to the Primary Device.\n    label: Port of the ssh connection.\n    type: number\n  primary_device_username:\n    description: Name of the user which will be used to log onto the Primary Device.\n    label: User name to log on to device.\n    type: string\n  primary_device_password:\n    description: Password of the user which will be used to log onto the Primary Device.\n    label: Users password.\n    type: string\n    hidden: true\n  secondary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Secondary Device.\n    label: Ip address of the device.\n    type: string\n  secondary_device_port:\n    description: Port that will be used to establish ssh connection to the Secondary Device.\n    label: Port of the ssh connection.\n    type: number\n  secondary_device_username:\n    description: Name of the user which will be used to log onto the Secondary Device.\n    label: User name to log on to device.\n    type: string\n  secondary_device_password:\n    description: Password of the user which will be used to log onto the Secondary Device.\n    label: Users password.\n    type: string\n    hidden: true\n  primary_device_physical_interface:\n    description: Physical port on the Primary device on which the logical port will be configured\n    label: Underlying physical interface\n    type: string\n  primary_device_logical_interface:\n    description: Name of the created logical interface on the Primary device\n    label: Logical Interface name\n    type: string\n  secondary_device_physical_interface:\n    description: Physical port on the Secondary device on which the logical port will be configured\n    label: Underlying physical interface\n    type: string\n  secondary_device_logical_interface:\n    description: Name of the created logical interface on the Secondary device\n    label: Logical Interface name\n    type: string\n  vlan:\n    description: vlan tag used by logical interface\n    label: VLAN ID\n    type: string\n  vrf_name:\n    description: Name for VRF used by logical interface\n    label: VRF name\n    type: string\n  vrf_import_policy:\n    description: Import Policy for IGS\n    label: Import Policy\n    type: string\n  vrf_export_policy:\n    description: Export Policy for IGS\n    label: Export Policy\n    type: string\n  uplink_import_policy:\n    description: Uplink Import Policy for IGS\n    label: Uplink Import Policy\n    type: string\n  input_filter_name:\n    description: Policer name to use as input policer\n    label: Input policer name\n    type: string\n  output_filter_name:\n    description: Policer name to use as output policer\n    label: Output policer name\n    type: string\n  primary_vrrp_config_group:\n    description: Name for apply group to use for interface for VRRP\n    label: Apply group name\n    type: string\n  secondary_vrrp_config_group:\n    description: Name for apply group to use for interface for VRRP\n    label: Apply group name\n    type: string\n  inet_in_filter:\n    label: Internet Input Filter\n    type: string\n  inet_out_filter:\n    label: Internet Output Filter\n    type: string\n  prefix_list_name:\n    label: Prefix list name\n    type: string\n  filter_term_name:\n    label: Filter term name\n    type: string\n  counter_name_in:\n    type: string\n    label: Input counter name\n  counter_name_out:\n    type: string\n    label: Output counter name\n  gohan_id:\n    type: string\n    label: Gohan resource ID\n    description: UUID of the GW Interface\n  tenant_id:\n    type: string\n    label: Tenant ID\n  version:\n    type: number\n    label: Config version\n\nresources:\n{% for device in [\"primary\", \"secondary\"] %}\n  netconf_configure_{{ device }}:\n    properties:\n      on_update: merge\n      lock_timeout: 3000\n      configs:\n      - config:\n          str_replace:\n            params:\n              $APPLY_GROUP:\n                get_param: {{ device }}_vrrp_config_group\n              $VLAN:\n                get_param: vlan\n              $INPUT_FILTER:\n                get_param: input_filter_name\n              $OUTPUT_FILTER:\n                get_param: output_filter_name\n            template: |\n              apply-groups $APPLY_GROUP\n              vlan-id $VLAN;\n              description inet_gw;\n              family inet {\n                  filter {\n                      input $INPUT_FILTER;\n                      output $OUTPUT_FILTER;\n                  }\n              }\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: interfaces\n          - config_type: name\n            xml_type: named_tag\n            tag: interface\n            name: { get_param: {{ device }}_device_physical_interface }\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: unit\n            name: { get_param: vlan }\n      - config:\n          str_replace:\n            params:\n              $LIF:\n                get_param: {{ device }}_device_logical_interface\n              $IMPORT_POLICY:\n                get_param: vrf_import_policy\n              $EXPORT_POLICY:\n                get_param: vrf_export_policy\n            template: |\n                instance-type virtual-router;\n                interface $LIF;\n                routing-options instance-import $IMPORT_POLICY;\n                routing-options instance-export $EXPORT_POLICY;{% if jinja_vrf_config %}\n                {{ jinja_vrf_config }}{% endif %}\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: routing-instances\n          - config_type: name\n            xml_type: named_tag\n            tag: instance\n            name: { get_param: vrf_name }\n      - config:\n          str_replace:\n            params:\n              $VRF_NAME:\n                get_param: vrf_name\n            template: |\n              from instance $VRF_NAME;\n              then accept;\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: policy-options\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: policy-statement\n            name: { get_param: uplink_import_policy }\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: term\n            name: { get_param: vrf_name }\n      - config: \"\"\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: policy-options\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: prefix-list\n            name: { get_param: prefix_list_name }\n      - config:\n          str_replace:\n            params:\n              $PREFIX_LIST_NAME:\n                get_param: prefix_list_name\n              $VRF_NAME:\n                get_param: vrf_name\n            template: |\n               from {\n                  destination-prefix-list {\n                       $PREFIX_LIST_NAME;\n                  }\n               }\n               then {\n                    count $VRF_NAME_IN;\n                    accept;\n               }\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: firewall\n          - config_type: tag\n            xml_type: tag\n            tag: family\n          - config_type: tag\n            xml_type: tag\n            tag: inet\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: filter\n            name: { get_param: inet_in_filter }\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: term\n            name: { get_param: filter_term_name }\n        additional_commands:\n          str_replace:\n            params:\n              $TERM_NAME:\n                get_param: filter_term_name\n              $INET_IN:\n                get_param: inet_in_filter\n            template: |\n              insert firewall family inet filter $INET_IN term $TERM_NAME before term all-accept\n      - config:\n          str_replace:\n            params:\n              $PREFIX_LIST_NAME:\n                get_param: prefix_list_name\n              $VRF_NAME:\n                get_param: vrf_name\n            template: |\n               from {\n                  source-prefix-list {\n                       $PREFIX_LIST_NAME;\n                  }\n               }\n               then {\n                    count $VRF_NAME_OUT;\n                    accept;\n               }\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: firewall\n          - config_type: tag\n            xml_type: tag\n            tag: family\n          - config_type: tag\n            xml_type: tag\n            tag: inet\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: filter\n            name: { get_param: inet_out_filter }\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: term\n            name: { get_param: filter_term_name }\n        additional_commands:\n          str_replace:\n            params:\n              $TERM_NAME:\n                get_param: filter_term_name\n              $INET_OUT:\n                get_param: inet_out_filter\n            template: |\n              insert firewall family inet filter $INET_OUT term $TERM_NAME before term all-accept\n      device_ip:\n        get_param: {{ device }}_device_ip\n      password:\n        get_param: {{ device }}_device_password\n      port:\n        get_param: {{ device }}_device_port\n      username:\n        get_param: {{ device }}_device_username\n    {% if device == \"secondary\" %}depends_on: netconf_configure_primary{% endif %}\n    type: OS::Contrail::NetconfNamedConfigs\n{% endfor %}\n\n{% for device in [\"primary\", \"secondary\"] %}\n  {{ device }}_igs_metric_monitor:\n    type: ESI::Monitoring::MonitoringTarget\n    properties:\n      type: igs_counter\n      resource_type: internet_gateways\n      resource_id: { get_param: gohan_id }\n      tenant_id: { get_param: tenant_id }\n      version: { get_param: version }\n      field_name: {{ device }}_counter\n      properties:\n        counter_name_in: { get_param: counter_name_in }\n        counter_name_out: { get_param: counter_name_out }\n        host: { get_param: {{ device }}_device_ip }\n        port: { get_param: {{ device }}_device_port }\n        login: { get_param: {{ device }}_device_username }\n        password: { get_param: {{ device }}_device_password }\n        primary_device_ip: { get_param: primary_device_ip }\n        secondary_device_ip: { get_param: secondary_device_ip }\n      syncer_properties:\n        tsdb:\n          traffic.in:\n            metric: traffic.bytes\n            tags:\n              device_index: {{ device }}\n              resource_id: { get_param: gohan_id }\n              direction: in\n          traffic.out:\n            metric: traffic.bytes\n            tags:\n              device_index: {{ device }}\n              resource_id: { get_param: gohan_id }\n              direction: out\n    depends_on: netconf_configure_secondary\n{% endfor %}\n\noutputs:\n{% for device in [\"primary\", \"secondary\"] %}\n  {{ device }}_monitoring_target_id:\n    description: Monitoring Target ID\n    value: { get_resource: {{ device }}_igs_metric_monitor}\n  {{ device }}_monitoring_link:\n    description: Monitoring Process Link\n    value: { get_attr: [{{ device }}_igs_metric_monitor, link]}\n{% endfor %}\n",
        "parameter_mappings": {
            "vrf_export_policy": "Finternet_service+internet_service_id:vrf_export_policy",
            "secondary_device_physical_interface": "Fha_interface+downlink_interface_id:er_physical_interface+secondary_interface_id:name",
            "counter_name_out": "APvrf_name&C_OUT",
            "primary_device_logical_interface": "Pprimary_logical_interface_name",
            "primary_device_password": "Fha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:password",
            "gohan_id": "Pid",
            "vrf_import_policy": "Finternet_service+internet_service_id:vrf_import_policy",
            "prefix_list_name": "APvrf_name&C_prefix",
            "jinja_vrf_config": "Finternet_service+internet_service_id:vrf_config",
            "output_filter_name": "ACFILTER_&Fqos_option+qos_option_id:outgoing_policer_name",
            "secondary_vrrp_config_group": "Finternet_service+internet_service_id:secondary_vrrp_config_group",
            "primary_device_ip": "Fha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:ip",
            "version": "Vauto_filled",
            "inet_in_filter": "Finternet_service+internet_service_id:inet_in_filter",
            "primary_device_username": "Fha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:login",
            "secondary_device_logical_interface": "Psecondary_logical_interface_name",
            "counter_name_in": "APvrf_name&C_IN",
            "inet_out_filter": "Finternet_service+internet_service_id:inet_out_filter",
            "vlan": "Pvlan_id",
            "primary_device_physical_interface": "Fha_interface+downlink_interface_id:er_physical_interface+primary_interface_id:name",
            "uplink_import_policy": "Finternet_service+internet_service_id:uplink_import_policy",
            "input_filter_name": "ACFILTER_&Fqos_option+qos_option_id:incoming_policer_name",
            "filter_term_name": "APvrf_name&C_filter",
            "tenant_id": "Ptenant_id",
            "secondary_device_port": "Fha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:ssh_port",
            "secondary_device_password": "Fha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:password",
            "heat_timeout": "C60",
            "vrf_name": "Pvrf_name",
            "primary_vrrp_config_group": "Finternet_service+internet_service_id:primary_vrrp_config_group",
            "secondary_device_username": "Fha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:login",
            "primary_device_port": "Fha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:ssh_port",
            "secondary_device_ip": "Fha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:ip"
        }
    },
    "version": 1,
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* OS::Contrail::NetconfNamedConfigs
* ESI::Monitoring::MonitoringTarget

```
heat_template_version: 2013-05-23

description: >
  Internet GW Instance

parameters:
  primary_device_ip:
    description: Ip address that will be used to establish ssh connection to the Primary Device.
    label: Ip address of the device.
    type: string
  primary_device_port:
    description: Port that will be used to establish ssh connection to the Primary Device.
    label: Port of the ssh connection.
    type: number
  primary_device_username:
    description: Name of the user which will be used to log onto the Primary Device.
    label: User name to log on to device.
    type: string
  primary_device_password:
    description: Password of the user which will be used to log onto the Primary Device.
    label: Users password.
    type: string
    hidden: true
  secondary_device_ip:
    description: Ip address that will be used to establish ssh connection to the Secondary Device.
    label: Ip address of the device.
    type: string
  secondary_device_port:
    description: Port that will be used to establish ssh connection to the Secondary Device.
    label: Port of the ssh connection.
    type: number
  secondary_device_username:
    description: Name of the user which will be used to log onto the Secondary Device.
    label: User name to log on to device.
    type: string
  secondary_device_password:
    description: Password of the user which will be used to log onto the Secondary Device.
    label: Users password.
    type: string
    hidden: true
  primary_device_physical_interface:
    description: Physical port on the Primary device on which the logical port will be configured
    label: Underlying physical interface
    type: string
  primary_device_logical_interface:
    description: Name of the created logical interface on the Primary device
    label: Logical Interface name
    type: string
  secondary_device_physical_interface:
    description: Physical port on the Secondary device on which the logical port will be configured
    label: Underlying physical interface
    type: string
  secondary_device_logical_interface:
    description: Name of the created logical interface on the Secondary device
    label: Logical Interface name
    type: string
  vlan:
    description: vlan tag used by logical interface
    label: VLAN ID
    type: string
  vrf_name:
    description: Name for VRF used by logical interface
    label: VRF name
    type: string
  vrf_import_policy:
    description: Import Policy for IGS
    label: Import Policy
    type: string
  vrf_export_policy:
    description: Export Policy for IGS
    label: Export Policy
    type: string
  uplink_import_policy:
    description: Uplink Import Policy for IGS
    label: Uplink Import Policy
    type: string
  input_filter_name:
    description: Policer name to use as input policer
    label: Input policer name
    type: string
  output_filter_name:
    description: Policer name to use as output policer
    label: Output policer name
    type: string
  primary_vrrp_config_group:
    description: Name for apply group to use for interface for VRRP
    label: Apply group name
    type: string
  secondary_vrrp_config_group:
    description: Name for apply group to use for interface for VRRP
    label: Apply group name
    type: string
  inet_in_filter:
    label: Internet Input Filter
    type: string
  inet_out_filter:
    label: Internet Output Filter
    type: string
  prefix_list_name:
    label: Prefix list name
    type: string
  filter_term_name:
    label: Filter term name
    type: string
  counter_name_in:
    type: string
    label: Input counter name
  counter_name_out:
    type: string
    label: Output counter name
  gohan_id:
    type: string
    label: Gohan resource ID
    description: UUID of the GW Interface
  tenant_id:
    type: string
    label: Tenant ID
  version:
    type: number
    label: Config version

resources:
{% for device in ["primary", "secondary"] %}
  netconf_configure_{{ device }}:
    properties:
      on_update: merge
      lock_timeout: 3000
      configs:
      - config:
          str_replace:
            params:
              $APPLY_GROUP:
                get_param: {{ device }}_vrrp_config_group
              $VLAN:
                get_param: vlan
              $INPUT_FILTER:
                get_param: input_filter_name
              $OUTPUT_FILTER:
                get_param: output_filter_name
            template: |
              apply-groups $APPLY_GROUP
              vlan-id $VLAN;
              description inet_gw;
              family inet {
                  filter {
                      input $INPUT_FILTER;
                      output $OUTPUT_FILTER;
                  }
              }
        path:
          - config_type: tag
            xml_type: tag
            tag: interfaces
          - config_type: name
            xml_type: named_tag
            tag: interface
            name: { get_param: {{ device }}_device_physical_interface }
          - config_type: named_tag
            xml_type: named_tag
            tag: unit
            name: { get_param: vlan }
      - config:
          str_replace:
            params:
              $LIF:
                get_param: {{ device }}_device_logical_interface
              $IMPORT_POLICY:
                get_param: vrf_import_policy
              $EXPORT_POLICY:
                get_param: vrf_export_policy
            template: |
                instance-type virtual-router;
                interface $LIF;
                routing-options instance-import $IMPORT_POLICY;
                routing-options instance-export $EXPORT_POLICY;{% if jinja_vrf_config %}
                {{ jinja_vrf_config }}{% endif %}
        path:
          - config_type: tag
            xml_type: tag
            tag: routing-instances
          - config_type: name
            xml_type: named_tag
            tag: instance
            name: { get_param: vrf_name }
      - config:
          str_replace:
            params:
              $VRF_NAME:
                get_param: vrf_name
            template: |
              from instance $VRF_NAME;
              then accept;
        path:
          - config_type: tag
            xml_type: tag
            tag: policy-options
          - config_type: named_tag
            xml_type: named_tag
            tag: policy-statement
            name: { get_param: uplink_import_policy }
          - config_type: named_tag
            xml_type: named_tag
            tag: term
            name: { get_param: vrf_name }
      - config: ""
        path:
          - config_type: tag
            xml_type: tag
            tag: policy-options
          - config_type: named_tag
            xml_type: named_tag
            tag: prefix-list
            name: { get_param: prefix_list_name }
      - config:
          str_replace:
            params:
              $PREFIX_LIST_NAME:
                get_param: prefix_list_name
              $VRF_NAME:
                get_param: vrf_name
            template: |
               from {
                  destination-prefix-list {
                       $PREFIX_LIST_NAME;
                  }
               }
               then {
                    count $VRF_NAME_IN;
                    accept;
               }
        path:
          - config_type: tag
            xml_type: tag
            tag: firewall
          - config_type: tag
            xml_type: tag
            tag: family
          - config_type: tag
            xml_type: tag
            tag: inet
          - config_type: named_tag
            xml_type: named_tag
            tag: filter
            name: { get_param: inet_in_filter }
          - config_type: named_tag
            xml_type: named_tag
            tag: term
            name: { get_param: filter_term_name }
        additional_commands:
          str_replace:
            params:
              $TERM_NAME:
                get_param: filter_term_name
              $INET_IN:
                get_param: inet_in_filter
            template: |
              insert firewall family inet filter $INET_IN term $TERM_NAME before term all-accept
      - config:
          str_replace:
            params:
              $PREFIX_LIST_NAME:
                get_param: prefix_list_name
              $VRF_NAME:
                get_param: vrf_name
            template: |
               from {
                  source-prefix-list {
                       $PREFIX_LIST_NAME;
                  }
               }
               then {
                    count $VRF_NAME_OUT;
                    accept;
               }
        path:
          - config_type: tag
            xml_type: tag
            tag: firewall
          - config_type: tag
            xml_type: tag
            tag: family
          - config_type: tag
            xml_type: tag
            tag: inet
          - config_type: named_tag
            xml_type: named_tag
            tag: filter
            name: { get_param: inet_out_filter }
          - config_type: named_tag
            xml_type: named_tag
            tag: term
            name: { get_param: filter_term_name }
        additional_commands:
          str_replace:
            params:
              $TERM_NAME:
                get_param: filter_term_name
              $INET_OUT:
                get_param: inet_out_filter
            template: |
              insert firewall family inet filter $INET_OUT term $TERM_NAME before term all-accept
      device_ip:
        get_param: {{ device }}_device_ip
      password:
        get_param: {{ device }}_device_password
      port:
        get_param: {{ device }}_device_port
      username:
        get_param: {{ device }}_device_username
    {% if device == "secondary" %}depends_on: netconf_configure_primary{% endif %}
    type: OS::Contrail::NetconfNamedConfigs
{% endfor %}

{% for device in ["primary", "secondary"] %}
  {{ device }}_igs_metric_monitor:
    type: ESI::Monitoring::MonitoringTarget
    properties:
      type: igs_counter
      resource_type: internet_gateways
      resource_id: { get_param: gohan_id }
      tenant_id: { get_param: tenant_id }
      version: { get_param: version }
      field_name: {{ device }}_counter
      properties:
        counter_name_in: { get_param: counter_name_in }
        counter_name_out: { get_param: counter_name_out }
        host: { get_param: {{ device }}_device_ip }
        port: { get_param: {{ device }}_device_port }
        login: { get_param: {{ device }}_device_username }
        password: { get_param: {{ device }}_device_password }
        primary_device_ip: { get_param: primary_device_ip }
        secondary_device_ip: { get_param: secondary_device_ip }
      syncer_properties:
        tsdb:
          traffic.in:
            metric: traffic.bytes
            tags:
              device_index: {{ device }}
              resource_id: { get_param: gohan_id }
              direction: in
          traffic.out:
            metric: traffic.bytes
            tags:
              device_index: {{ device }}
              resource_id: { get_param: gohan_id }
              direction: out
    depends_on: netconf_configure_secondary
{% endfor %}

outputs:
{% for device in ["primary", "secondary"] %}
  {{ device }}_monitoring_target_id:
    description: Monitoring Target ID
    value: { get_resource: {{ device }}_igs_metric_monitor}
  {{ device }}_monitoring_link:
    description: Monitoring Process Link
    value: { get_attr: [{{ device }}_igs_metric_monitor, link]}
{% endfor %}
```
