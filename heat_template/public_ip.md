# heat_template: public_ip
This is heat_template of "public_ip" which is provided by gohan via etcd

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/public_ip
{
    "body": {
        "handler": "heat_worker", 
        "watch": [], 
        "id": "public_ip", 
        "template_file": "heat_template_version: 2013-05-23\n\ndescription: >\n  QoS Option\n\nparameters:\n  primary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Primary Device.\n    label: Ip address of the device.\n    type: string\n  primary_device_port:\n    description: Port that will be used to establish ssh connection to the Primary Device.\n    label: Port of the ssh connection.\n    type: number\n  primary_device_username:\n    description: Name of the user which will be used to log onto the Primary Device.\n    label: User name to log on to device.\n    type: string\n  primary_device_password:\n    description: Password of the user which will be used to log onto the Primary Device.\n    label: Users password.\n    type: string\n    hidden: true\n  secondary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Secondary Device.\n    label: Ip address of the device.\n    type: string\n  secondary_device_port:\n    description: Port that will be used to establish ssh connection to the Secondary Device.\n    label: Port of the ssh connection.\n    type: number\n  secondary_device_username:\n    description: Name of the user which will be used to log onto the Secondary Device.\n    label: User name to log on to device.\n    type: string\n  secondary_device_password:\n    description: Password of the user which will be used to log onto the Secondary Device.\n    label: Users password.\n    type: string\n    hidden: true\n  prefix_list_name:\n    label: Prefix List name.\n    type: string\n  ip_cidr:\n    label: Public IP CIDR\n    type: string\n  ip_mask:\n    label: Public IP CIDR\n    type: string\nresources:\n{% for device in [\"primary\", \"secondary\"] %}\n  netconf_configure_{{ device }}:\n    properties:\n      lock_timeout: 3000\n      configs:\n      - config: \"\"\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: policy-options\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: prefix-list\n            name: { get_param: prefix_list_name }\n          - config_type: name\n            xml_type: named_tag\n            tag: prefix-list-item\n            name:\n              str_replace:\n                params:\n                  $CIDR:\n                    { get_param: ip_cidr }\n                  $MASK:\n                    { get_param: ip_mask }\n                template: |\n                  $CIDR/$MASK\n      device_ip:\n        get_param: {{ device }}_device_ip\n      password:\n        get_param: {{ device }}_device_password\n      port:\n        get_param: {{ device }}_device_port\n      username:\n        get_param: {{ device }}_device_username\n    {% if device == \"secondary\" %}depends_on: netconf_configure_primary{% endif %}\n    type: OS::Contrail::NetconfNamedConfigs\n{% endfor %}\n", 
        "parameter_mappings": {
            "secondary_device_password": "Finternet_gateway+internet_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:password", 
            "primary_device_password": "Finternet_gateway+internet_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:password", 
            "secondary_device_port": "Finternet_gateway+internet_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:ssh_port", 
            "primary_device_ip": "Finternet_gateway+internet_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:ip", 
            "ip_mask": "Psubmask_length", 
            "heat_timeout": "C60", 
            "ip_cidr": "Pcidr", 
            "primary_device_username": "Finternet_gateway+internet_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:login", 
            "secondary_device_username": "Finternet_gateway+internet_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:login", 
            "primary_device_port": "Finternet_gateway+internet_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:ssh_port", 
            "secondary_device_ip": "Finternet_gateway+internet_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:ip", 
            "prefix_list_name": "AFinternet_gateway+internet_gw_id:vrf_name&C_prefix"
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
  QoS Option

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
  prefix_list_name:
    label: Prefix List name.
    type: string
  ip_cidr:
    label: Public IP CIDR
    type: string
  ip_mask:
    label: Public IP CIDR
    type: string
resources:
{% for device in ["primary", "secondary"] %}
  netconf_configure_{{ device }}:
    properties:
      lock_timeout: 3000
      configs:
      - config: ""
        path:
          - config_type: tag
            xml_type: tag
            tag: policy-options
          - config_type: named_tag
            xml_type: named_tag
            tag: prefix-list
            name: { get_param: prefix_list_name }
          - config_type: name
            xml_type: named_tag
            tag: prefix-list-item
            name:
              str_replace:
                params:
                  $CIDR:
                    { get_param: ip_cidr }
                  $MASK:
                    { get_param: ip_mask }
                template: |
                  $CIDR/$MASK
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
```
