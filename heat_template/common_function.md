# heat_template: common_function
This is heat_template of "common_function" which is provided by gohan via etcd

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/common_function
{
    "body": {
        "handler": "heat_worker",
        "watch": [],
        "id": "common_function",
        "template_file": "heat_template_version: 2013-05-23\n\ndescription: >\n  Common Function\n\nparameters:\n  primary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Primary Device.\n    label: Ip address of the device.\n    type: string\n  primary_device_port:\n    description: Port that will be used to establish ssh connection to the Primary Device.\n    label: Port of the ssh connection.\n    type: number\n  primary_device_username:\n    description: Name of the user which will be used to log onto the Primary Device.\n    label: User name to log on to device.\n    type: string\n  primary_device_password:\n    description: Password of the user which will be used to log onto the Primary Device.\n    label: Users password.\n    type: string\n    hidden: true\n  primary_vrrp_ip:\n    description: Local ip in VRRP group on primary device.\n    label: Primary VRRP ip.\n    type: string\n  secondary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Secondary Device.\n    label: Ip address of the device.\n    type: string\n  secondary_device_port:\n    description: Port that will be used to establish ssh connection to the Secondary Device.\n    label: Port of the ssh connection.\n    type: number\n  secondary_device_username:\n    description: Name of the user which will be used to log onto the Secondary Device.\n    label: User name to log on to device.\n    type: string\n  secondary_device_password:\n    description: Password of the user which will be used to log onto the Secondary Device.\n    label: Users password.\n    type: string\n    hidden: true\n  secondary_vrrp_ip:\n    description: Local ip in VRRP group on secondary device.\n    label: Secondary VRRP ip.\n    type: string\n  netmask:\n    description: Netmask used in link local network.\n    label: Link-local netmask.\n    type: string\n\nresources:\n{% for device in [\"primary\", \"secondary\"] %}\n  netconf_configure_{{ device }}:\n    properties:\n      lock_timeout: 3000\n      configs:\n      - config: \"\"\n        path:\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: groups\n            name: {{ jinja_vrrp_group_name }}\n          - config_type: tag\n            xml_type: tag\n            tag: interfaces\n          - config_type: name\n            xml_type: named_tag\n            tag: interface\n            name: <*>\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: unit\n            name: <*>\n          - config_type: tag\n            xml_type: tag\n            tag: family\n          - config_type: tag\n            xml_type: tag\n            tag: inet\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: address\n            name:\n              str_replace:\n                params:\n                  $VIP:\n                    get_param: {{ device }}_vrrp_ip\n                  $NETMASK:\n                    get_param: netmask\n                template: |\n                  $VIP/$NETMASK\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: vrrp-group\n            name: {{ jinja_vrid }}\n          - config_type: named_tag\n            xml_type: named_tag # FIXME: this is probably not true, as far as i can see we don't support that in plugin at all :(\n            tag: virtual-address\n            name: {{ jinja_link_local_ip_address }}\n      - config: |\n          from {\n            destination-address {\n              {{ jinja_link_local_ip_address }}/32;\n            }\n          }\n          then {\n            translated {\n              translation-type {\n                dnat-44;\n              }\n            }\n          }\n        path:\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: groups\n            name: {{ jinja_dnat_group_name }}\n          - config_type: tag\n            xml_type: tag\n            tag: services\n          - config_type: tag\n            xml_type: tag\n            tag: nat\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: rule\n            name: <*>\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: term\n            name: {{ jinja_service_number }}\n      - config: |\n          services {\n            nat {\n              pool <*> {\n                address {{ jinja_shared_ip_address }}/32;\n              }\n            }\n          }\n        path:\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: groups\n            name: {{ jinja_dnat_pool_group_name }}-{{ jinja_service_number }}\n      device_ip:\n        get_param: {{ device }}_device_ip\n      password:\n        get_param: {{ device }}_device_password\n      port:\n        get_param: {{ device }}_device_port\n      username:\n        get_param: {{ device }}_device_username\n    {% if device == \"secondary\" %}depends_on: netconf_configure_primary{% endif %}\n    type: OS::Contrail::NetconfNamedConfigs\n{% endfor %}\n",
        "parameter_mappings": {
            "jinja_dnat_pool_group_name": {
                "field": "dnat_pool_group_name",
                "path": [
                    "common_function_pool_id"
                ]
            },
            "primary_vrrp_ip": {
                "field": "primary_vrrp_ip"
            },
            "jinja_dnat_group_name": {
                "field": "dnat_group_name",
                "path": [
                    "common_function_pool_id"
                ]
            },
            "secondary_vrrp_ip": {
                "field": "secondary_vrrp_ip"
            },
            "secondary_device_ip": {
                "field": "ip",
                "path": [
                    "ha_router_id",
                    "secondary_router_id"
                ]
            },
            "primary_device_port": {
                "field": "ssh_port",
                "path": [
                    "ha_router_id",
                    "primary_router_id"
                ]
            },
            "netmask": {
                "field": "link_local_netmask",
                "path": [
                    "common_function_pool_id"
                ]
            },
            "jinja_shared_ip_address": {
                "field": "shared_ip_address"
            },
            "primary_device_ip": {
                "field": "ip",
                "path": [
                    "ha_router_id",
                    "primary_router_id"
                ]
            },
            "secondary_device_password": {
                "field": "password",
                "path": [
                    "ha_router_id",
                    "secondary_router_id"
                ]
            },
            "heat_timeout": "C60",
            "primary_device_username": {
                "field": "login",
                "path": [
                    "ha_router_id",
                    "primary_router_id"
                ]
            },
            "primary_device_password": {
                "field": "password",
                "path": [
                    "ha_router_id",
                    "primary_router_id"
                ]
            },
            "jinja_service_number": {
                "field": "common_function_number"
            },
            "secondary_device_username": {
                "field": "login",
                "path": [
                    "ha_router_id",
                    "secondary_router_id"
                ]
            },
            "jinja_vrrp_group_name": {
                "field": "vrrp_group_name",
                "path": [
                    "common_function_pool_id"
                ]
            },
            "secondary_device_port": {
                "field": "ssh_port",
                "path": [
                    "ha_router_id",
                    "secondary_router_id"
                ]
            },
            "jinja_vrid": {
                "field": "vrid"
            },
            "jinja_link_local_ip_address": {
                "field": "link_local_ip_address"
            }
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
  Common Function

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
  primary_vrrp_ip:
    description: Local ip in VRRP group on primary device.
    label: Primary VRRP ip.
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
  secondary_vrrp_ip:
    description: Local ip in VRRP group on secondary device.
    label: Secondary VRRP ip.
    type: string
  netmask:
    description: Netmask used in link local network.
    label: Link-local netmask.
    type: string

resources:
{% for device in ["primary", "secondary"] %}
  netconf_configure_{{ device }}:
    properties:
      lock_timeout: 3000
      configs:
      - config: ""
        path:
          - config_type: named_tag
            xml_type: named_tag
            tag: groups
            name: {{ jinja_vrrp_group_name }}
          - config_type: tag
            xml_type: tag
            tag: interfaces
          - config_type: name
            xml_type: named_tag
            tag: interface
            name: <*>
          - config_type: named_tag
            xml_type: named_tag
            tag: unit
            name: <*>
          - config_type: tag
            xml_type: tag
            tag: family
          - config_type: tag
            xml_type: tag
            tag: inet
          - config_type: named_tag
            xml_type: named_tag
            tag: address
            name:
              str_replace:
                params:
                  $VIP:
                    get_param: {{ device }}_vrrp_ip
                  $NETMASK:
                    get_param: netmask
                template: |
                  $VIP/$NETMASK
          - config_type: named_tag
            xml_type: named_tag
            tag: vrrp-group
            name: {{ jinja_vrid }}
          - config_type: named_tag
            xml_type: named_tag # FIXME: this is probably not true, as far as i can see we don't support that in plugin at all :(
            tag: virtual-address
            name: {{ jinja_link_local_ip_address }}
      - config: |
          from {
            destination-address {
              {{ jinja_link_local_ip_address }}/32;
            }
          }
          then {
            translated {
              translation-type {
                dnat-44;
              }
            }
          }
        path:
          - config_type: named_tag
            xml_type: named_tag
            tag: groups
            name: {{ jinja_dnat_group_name }}
          - config_type: tag
            xml_type: tag
            tag: services
          - config_type: tag
            xml_type: tag
            tag: nat
          - config_type: named_tag
            xml_type: named_tag
            tag: rule
            name: <*>
          - config_type: named_tag
            xml_type: named_tag
            tag: term
            name: {{ jinja_service_number }}
      - config: |
          services {
            nat {
              pool <*> {
                address {{ jinja_shared_ip_address }}/32;
              }
            }
          }
        path:
          - config_type: named_tag
            xml_type: named_tag
            tag: groups
            name: {{ jinja_dnat_pool_group_name }}-{{ jinja_service_number }}
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
