# heat_template: azure_gateway
This is heat_template of "azure_gateway" which is provided by gohan via etcd

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/azure_gateway
{
    "body": {
        "handler": "heat_worker", 
        "watch": [], 
        "id": "azure_gateway", 
        "template_file": "heat_template_version: 2013-05-23\n\ndescription: >\n  AZURE Gateway\n\nparameters:\n  primary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Primary Device.\n    label: Ip address of the device.\n    type: string\n  primary_device_port:\n    description: Port that will be used to establish ssh connection to the Primary Device.\n    label: Port of the ssh connection.\n    type: number\n  primary_device_username:\n    description: Name of the user which will be used to log onto the Primary Device.\n    label: User name to log on to device.\n    type: string\n  primary_device_password:\n    description: Password of the user which will be used to log onto the Primary Device.\n    label: Users password.\n    type: string\n    hidden: true\n  primary_device_logical_downlink_interface:\n    description: Name of the created logical downlink interface on the Primary device\n    label: Logical Interface name\n    type: string\n  primary_device_physical_downlink_interface:\n    description: Physical port on the Primary device on which the logical downlink port will be configured\n    label: Underlying physical interface\n    type: string\n  primary_device_logical_uplink_interface:\n    description: Name of the created logical uplink interface on the Primary device\n    label: Logical Interface name\n    type: string\n  primary_device_physical_uplink_interface:\n    description: Physical port on the Primary device on which the logical uplink port will be configured\n    label: Underlying physical interface\n    type: string\n  secondary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Secondary Device.\n    label: Ip address of the device.\n    type: string\n  secondary_device_port:\n    description: Port that will be used to establish ssh connection to the Secondary Device.\n    label: Port of the ssh connection.\n    type: number\n  secondary_device_username:\n    description: Name of the user which will be used to log onto the Secondary Device.\n    label: User name to log on to device.\n    type: string\n  secondary_device_password:\n    description: Password of the user which will be used to log onto the Secondary Device.\n    label: Users password.\n    type: string\n    hidden: true\n  secondary_device_logical_downlink_interface:\n    description: Name of the created logical downlink interface on the Secondary device\n    label: Logical Interface name\n    type: string\n  secondary_device_physical_downlink_interface:\n    description: Physical port on the Secondary device on which the logical downlink port will be configured\n    label: Underlying physical interface\n    type: string\n  secondary_device_logical_uplink_interface:\n    description: Name of the created logical uplink interface on the Secondary device\n    label: Logical Interface name\n    type: string\n  secondary_device_physical_uplink_interface:\n    description: Physical port on the Secondary device on which the logical uplink port will be configured\n    label: Underlying physical interface\n    type: string\n  downlink_vlan:\n    description: vlan tag used by logical downlink interface\n    label: VLAN ID\n    type: string\n  uplink_vlan:\n    description: vlan tag used by logical uplink interface\n    label: VLAN ID\n    type: string\n  vrf_name:\n    description: Name for VRF used by logical interfaces\n    label: VRF name\n    type: string\n  input_filter_name:\n    description: Name for policer used for input\n    label: Input filter name\n    type: string\n  output_filter_name:\n    description: Name for policer used for output\n    label: Output filter name\n    type: string\n  primary_downlink_vrrp_config_group:\n    description: Name for apply group to use for downlink interface for VRRP\n    label: Apply group name\n    type: string\n  secondary_downlink_vrrp_config_group:\n    description: Name for apply group to use for downlink interface for VRRP\n    label: Apply group name\n    type: string\n\nresources:\n{% for device in [\"primary\", \"secondary\"] %}\n  netconf_configure_{{ device }}:\n    type: OS::Contrail::NetconfNamedConfigs\n    {% if device == \"secondary\" %}depends_on: netconf_configure_primary{% endif %}\n    properties:\n      lock_timeout: 3000\n      device_ip:\n        get_param: {{ device }}_device_ip\n      password:\n        get_param: {{ device }}_device_password\n      port:\n        get_param: {{ device }}_device_port\n      username:\n        get_param: {{ device }}_device_username\n      on_update: merge\n      configs:\n      - config:\n          str_replace:\n            params:\n              $VLAN:\n                get_param: downlink_vlan\n              $INPUT_FILTER:\n                get_param: input_filter_name\n              $OUTPUT_FILTER:\n                get_param: output_filter_name\n              $APPLY_GROUP:\n                get_param: {{ device }}_downlink_vrrp_config_group\n            template: |\n              apply-groups $APPLY_GROUP;\n              vlan-id $VLAN;\n              description AZURE_Downlink;\n              family inet {\n                  filter {\n                      input $INPUT_FILTER;\n                      output $OUTPUT_FILTER;\n                  }\n              }\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: interfaces\n          - config_type: name\n            xml_type: named_tag\n            tag: interface\n            name: { get_param: {{ device }}_device_physical_downlink_interface }\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: unit\n            name: { get_param: downlink_vlan }\n      - config:\n          str_replace:\n            params:\n              $LIFD:\n                get_param: {{ device }}_device_logical_downlink_interface\n              $LIFU:\n                get_param: {{ device }}_device_logical_uplink_interface\n            template: |\n                instance-type virtual-router;\n                interface $LIFD;\n                interface $LIFU;\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: routing-instances\n          - config_type: name\n            xml_type: named_tag\n            tag: instance\n            name: { get_param: vrf_name }\n      - config:\n          str_replace:\n            params:\n              $VLAN:\n                get_param: uplink_vlan\n            template: |\n              vlan-id $VLAN;\n              description AZURE_Uplink;\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: interfaces\n          - config_type: name\n            xml_type: named_tag\n            tag: interface\n            name: { get_param: {{ device }}_device_physical_uplink_interface }\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: unit\n            name: { get_param: uplink_vlan }\n{% endfor %}\n", 
        "parameter_mappings": {
            "primary_device_logical_uplink_interface": "Pprimary_logical_uplink_interface_name", 
            "primary_device_logical_downlink_interface": "Pprimary_logical_downlink_interface_name", 
            "primary_device_password": "Fha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:password", 
            "output_filter_name": "ACFILTER_&Fqos_option+qos_option_id:outgoing_policer_name", 
            "primary_device_ip": "Fha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:ip", 
            "secondary_device_physical_downlink_interface": "Fha_interface+downlink_interface_id:er_physical_interface+secondary_interface_id:name", 
            "secondary_device_username": "Fha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:login", 
            "primary_device_physical_uplink_interface": "Fha_interface+uplink_interface_id:er_physical_interface+primary_interface_id:name", 
            "secondary_device_logical_uplink_interface": "Psecondary_logical_uplink_interface_name", 
            "downlink_vlan": "Pdownlink_vlan_id", 
            "secondary_device_logical_downlink_interface": "Psecondary_logical_downlink_interface_name", 
            "input_filter_name": "ACFILTER_&Fqos_option+qos_option_id:incoming_policer_name", 
            "uplink_vlan": "Puplink_vlan_id", 
            "secondary_device_port": "Fha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:ssh_port", 
            "primary_downlink_vrrp_config_group": "Fazure_service+azure_service_id:primary_downlink_vrrp_config_group", 
            "secondary_device_password": "Fha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:password", 
            "heat_timeout": "C60", 
            "vrf_name": "Pvrf_name", 
            "primary_device_username": "Fha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:login", 
            "primary_device_physical_downlink_interface": "Fha_interface+downlink_interface_id:er_physical_interface+primary_interface_id:name", 
            "secondary_downlink_vrrp_config_group": "Fazure_service+azure_service_id:secondary_downlink_vrrp_config_group", 
            "primary_device_port": "Fha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:ssh_port", 
            "secondary_device_physical_uplink_interface": "Fha_interface+uplink_interface_id:er_physical_interface+secondary_interface_id:name", 
            "secondary_device_ip": "Fha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:ip"
        }
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* OS::Contrail::NetconfNamedConfigs

```
heat_template_version: 2013-05-23

description: >
  AZURE Gateway

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
  primary_device_logical_downlink_interface:
    description: Name of the created logical downlink interface on the Primary device
    label: Logical Interface name
    type: string
  primary_device_physical_downlink_interface:
    description: Physical port on the Primary device on which the logical downlink port will be configured
    label: Underlying physical interface
    type: string
  primary_device_logical_uplink_interface:
    description: Name of the created logical uplink interface on the Primary device
    label: Logical Interface name
    type: string
  primary_device_physical_uplink_interface:
    description: Physical port on the Primary device on which the logical uplink port will be configured
    label: Underlying physical interface
    type: string
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
  secondary_device_logical_downlink_interface:
    description: Name of the created logical downlink interface on the Secondary device
    label: Logical Interface name
    type: string
  secondary_device_physical_downlink_interface:
    description: Physical port on the Secondary device on which the logical downlink port will be configured
    label: Underlying physical interface
    type: string
  secondary_device_logical_uplink_interface:
    description: Name of the created logical uplink interface on the Secondary device
    label: Logical Interface name
    type: string
  secondary_device_physical_uplink_interface:
    description: Physical port on the Secondary device on which the logical uplink port will be configured
    label: Underlying physical interface
    type: string
  downlink_vlan:
    description: vlan tag used by logical downlink interface
    label: VLAN ID
    type: string
  uplink_vlan:
    description: vlan tag used by logical uplink interface
    label: VLAN ID
    type: string
  vrf_name:
    description: Name for VRF used by logical interfaces
    label: VRF name
    type: string
  input_filter_name:
    description: Name for policer used for input
    label: Input filter name
    type: string
  output_filter_name:
    description: Name for policer used for output
    label: Output filter name
    type: string
  primary_downlink_vrrp_config_group:
    description: Name for apply group to use for downlink interface for VRRP
    label: Apply group name
    type: string
  secondary_downlink_vrrp_config_group:
    description: Name for apply group to use for downlink interface for VRRP
    label: Apply group name
    type: string

resources:
{% for device in ["primary", "secondary"] %}
  netconf_configure_{{ device }}:
    type: OS::Contrail::NetconfNamedConfigs
    {% if device == "secondary" %}depends_on: netconf_configure_primary{% endif %}
    properties:
      lock_timeout: 3000
      device_ip:
        get_param: {{ device }}_device_ip
      password:
        get_param: {{ device }}_device_password
      port:
        get_param: {{ device }}_device_port
      username:
        get_param: {{ device }}_device_username
      on_update: merge
      configs:
      - config:
          str_replace:
            params:
              $VLAN:
                get_param: downlink_vlan
              $INPUT_FILTER:
                get_param: input_filter_name
              $OUTPUT_FILTER:
                get_param: output_filter_name
              $APPLY_GROUP:
                get_param: {{ device }}_downlink_vrrp_config_group
            template: |
              apply-groups $APPLY_GROUP;
              vlan-id $VLAN;
              description AZURE_Downlink;
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
            name: { get_param: {{ device }}_device_physical_downlink_interface }
          - config_type: named_tag
            xml_type: named_tag
            tag: unit
            name: { get_param: downlink_vlan }
      - config:
          str_replace:
            params:
              $LIFD:
                get_param: {{ device }}_device_logical_downlink_interface
              $LIFU:
                get_param: {{ device }}_device_logical_uplink_interface
            template: |
                instance-type virtual-router;
                interface $LIFD;
                interface $LIFU;
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
              $VLAN:
                get_param: uplink_vlan
            template: |
              vlan-id $VLAN;
              description AZURE_Uplink;
        path:
          - config_type: tag
            xml_type: tag
            tag: interfaces
          - config_type: name
            xml_type: named_tag
            tag: interface
            name: { get_param: {{ device }}_device_physical_uplink_interface }
          - config_type: named_tag
            xml_type: named_tag
            tag: unit
            name: { get_param: uplink_vlan }
{% endfor %}
```
