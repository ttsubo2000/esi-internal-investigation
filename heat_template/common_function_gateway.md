# heat_template: common_function_gateway
This is heat_template of "common_function_gateway" which is provided by gohan via etcd

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/common_function_gateway
{
    "body": {
        "handler": "heat_worker", 
        "watch": [], 
        "id": "common_function_gateway", 
        "template_file": "heat_template_version: 2013-05-23\n\ndescription: >\n  Common Function Gateway\n\nparameters:\n  primary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Primary Device.\n    label: Ip address of the device.\n    type: string\n  primary_device_port:\n    description: Port that will be used to establish ssh connection to the Primary Device.\n    label: Port of the ssh connection.\n    type: number\n  primary_device_username:\n    description: Name of the user which will be used to log onto the Primary Device.\n    label: User name to log on to device.\n    type: string\n  primary_device_password:\n    description: Password of the user which will be used to log onto the Primary Device.\n    label: Users password.\n    type: string\n    hidden: true\n  primary_device_logical_downlink_interface:\n    description: Name of the created logical downlink interface on the Primary device\n    label: Logical Interface name\n    type: string\n  primary_device_physical_downlink_interface:\n    description: Physical port on the Primary device on which the logical downlink port will be configured\n    label: Underlying physical interface\n    type: string\n  secondary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Secondary Device.\n    label: Ip address of the device.\n    type: string\n  secondary_device_port:\n    description: Port that will be used to establish ssh connection to the Secondary Device.\n    label: Port of the ssh connection.\n    type: number\n  secondary_device_username:\n    description: Name of the user which will be used to log onto the Secondary Device.\n    label: User name to log on to device.\n    type: string\n  secondary_device_password:\n    description: Password of the user which will be used to log onto the Secondary Device.\n    label: Users password.\n    type: string\n    hidden: true\n  secondary_device_logical_downlink_interface:\n    description: Name of the created logical downlink interface on the Secondary device\n    label: Logical Interface name\n    type: string\n  secondary_device_physical_downlink_interface:\n    description: Physical port on the Secondary device on which the logical downlink port will be configured\n    label: Underlying physical interface\n    type: string\n  gohan_id:\n    type: string\n    label: Gohan resource ID\n    description: UUID of the Common Function Gateway\n  tenant_id:\n    type: string\n    label: Tenant ID\n  version:\n    type: number\n    label: Config version\n\nresources:\n{% for device in [\"primary\", \"secondary\"] %}\n  netconf_configure_{{ device }}:\n    properties:\n      lock_timeout: 3000\n      configs:\n      - config: |\n          nat-rules {{ jinja_vrf_name }}-SNAPT;\n          nat-rules {{ jinja_vrf_name }}-DNAT;\n          interface-service service-interface {{ jinja_service_interface_name }}.{{ jinja_vlan_id }};\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: services\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: service-set\n            name: {{ jinja_vrf_name }}\n      - config: |\n          apply-groups {{ jinja_snapt_pool_group_name }};\n          address {{ jinja_nat_ip }}/32;\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: services\n          - config_type: tag\n            xml_type: tag\n            tag: nat\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: pool\n            name: {{ jinja_vrf_name }}-SNAPT-POOL\n      - config: |\n          apply-groups {{ jinja_snapt_group_name }};\n          term source then translated source-pool {{ jinja_vrf_name }}-SNAPT-POOL;\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: services\n          - config_type: tag\n            xml_type: tag\n            tag: nat\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: rule\n            name: {{ jinja_vrf_name }}-SNAPT\n      {% for service_number in jinja_common_service_numbers %}\n      - config: |\n          apply-groups {{ jinja_dnat_pool_group_name }}-{{ service_number }};\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: services\n          - config_type: tag\n            xml_type: tag\n            tag: nat\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: pool\n            name: {{ jinja_vrf_name }}-{{ jinja_dnat_pool_group_name }}-{{ service_number }}\n      {% endfor %}\n      - config: |\n          apply-groups {{ jinja_dnat_group_name }};\n          {% for service_number in jinja_common_service_numbers %}\n          term {{ service_number }} then translated destination-pool {{ jinja_vrf_name }}-{{ jinja_dnat_pool_group_name }}-{{ service_number }};\n          {% endfor %}\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: services\n          - config_type: tag\n            xml_type: tag\n            tag: nat\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: rule\n            name: {{ jinja_vrf_name }}-DNAT\n      - config: |\n          peer-unit {{ jinja_logical_tunnel_unit_service }};\n          family inet service input service-set {{ jinja_vrf_name }};\n          family inet service output service-set {{ jinja_vrf_name }};\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: interfaces\n          - config_type: name\n            xml_type: named_tag\n            tag: interface\n            name: {{ jinja_logical_tunnel_interface_name }}\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: unit\n            name: {{ jinja_logical_tunnel_unit_user }}\n      - config: |\n          peer-unit {{ jinja_logical_tunnel_unit_user }};\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: interfaces\n          - config_type: name\n            xml_type: named_tag\n            tag: interface\n            name: {{ jinja_logical_tunnel_interface_name }}\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: unit\n            name: {{ jinja_logical_tunnel_unit_service }}\n      - config: |\n          family inet;\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: interfaces\n          - config_type: name\n            xml_type: named_tag\n            tag: interface\n            name: {{ jinja_service_interface_name }}\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: unit\n            name: {{ jinja_vlan_id }}\n      - config: |\n          apply-groups {{ jinja_vrrp_group_name }};\n          description {{ jinja_vrf_name }};\n          vlan-id {{ jinja_vlan_id }};\n          family inet service input service-set {{ jinja_vrf_name }};\n          family inet service output service-set {{ jinja_vrf_name }};\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: interfaces\n          - config_type: name\n            xml_type: named_tag\n            tag: interface\n            name: { get_param: {{ device }}_device_physical_downlink_interface }\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: unit\n            name: {{ jinja_vlan_id }}\n      - config: \"\"\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: routing-instances\n          - config_type: name\n            xml_type: named_tag\n            tag: instance\n            name: {{ jinja_service_vrf_name }}\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: interface\n            name: {{ jinja_logical_tunnel_interface_name }}.{{ jinja_logical_tunnel_unit_service }}\n      - config:\n          next-hop {{ jinja_logical_tunnel_interface_name }}.{{ jinja_logical_tunnel_unit_service }};\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: routing-instances\n          - config_type: name\n            xml_type: named_tag\n            tag: instance\n            name: {{ jinja_service_vrf_name }}\n          - config_type: tag\n            xml_type: tag\n            tag: routing-options\n          - config_type: tag\n            xml_type: tag\n            tag: static\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: route\n            name: {{ jinja_nat_ip }}/32\n      - config:\n          str_replace:\n            params:\n              $DOWNLINK_INTERFACE:\n                get_param: {{ device }}_device_logical_downlink_interface\n            template: |\n              instance-type virtual-router;\n              interface {{ jinja_logical_tunnel_interface_name }}.{{ jinja_logical_tunnel_unit_user}};\n              interface {{ jinja_service_interface_name}}.{{ jinja_vlan_id }};\n              interface $DOWNLINK_INTERFACE;\n              routing-options static route 0.0.0.0/0 next-hop {{ jinja_logical_tunnel_interface_name }}.{{ jinja_logical_tunnel_unit_user }};\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: routing-instances\n          - config_type: name\n            xml_type: named_tag\n            tag: instance\n            name: {{ jinja_vrf_name }}\n      device_ip:\n        get_param: {{ device }}_device_ip\n      password:\n        get_param: {{ device }}_device_password\n      port:\n        get_param: {{ device }}_device_port\n      username:\n        get_param: {{ device }}_device_username\n    {% if device == \"secondary\" %}depends_on: netconf_configure_primary{% endif %}\n    type: OS::Contrail::NetconfNamedConfigs\n{% endfor %}\n\n  vrrp_monitor:\n    type: ESI::Monitoring::MonitoringTarget\n    properties:\n      type: vrrp_pool\n      resource_type: common_function_gateways\n      resource_id: { get_param: gohan_id }\n      tenant_id: { get_param: tenant_id }\n      version: { get_param: version }\n      field_name: status\n      properties:\n        vrid:\n        {% for vrid in jinja_vrids %}\n          - {{ vrid }}\n        {% endfor %}\n        primary:\n          host: { get_param: primary_device_ip }\n          port: { get_param: primary_device_port }\n          login: { get_param: primary_device_username }\n          password: { get_param: primary_device_password }\n          interface: { get_param: primary_device_logical_downlink_interface }\n        secondary:\n          host: { get_param: secondary_device_ip }\n          port: { get_param: secondary_device_port }\n          login: { get_param: secondary_device_username }\n          password: { get_param: secondary_device_password }\n          interface: { get_param: secondary_device_logical_downlink_interface }\n      syncer_properties:\n        etcd:\n          status:\n            key: status\n          hold_options:\n            positive_status:\n              primary_vrid1: MASTER\n              secondary_vrid1: BACKUP\n              primary_vrid2: MASTER\n              secondary_vrid2: BACKUP\n            time_seconds: 360\n    depends_on: netconf_configure_secondary\n\noutputs:\n  monitoring_target_id:\n    description: Monitoring Target ID\n    value: { get_resource: vrrp_monitor}\n  monitoring_link:\n    description: Monitoring Process Link\n    value: { get_attr: [vrrp_monitor, link]}\n", 
        "parameter_mappings": {
            "jinja_vrids": {
                "for_mapping": {
                    "field": "vrid"
                }, 
                "for_field": {
                    "field": "vrrp_config", 
                    "path": [
                        "common_function_pool_id"
                    ]
                }
            }, 
            "primary_device_logical_downlink_interface": {
                "field": "primary_logical_interface_name"
            }, 
            "jinja_common_service_numbers": {
                "for_mapping": {
                    "field": "common_function_number", 
                    "path": [
                        {
                            "type": "common_function", 
                            "id": "common_function_id"
                        }
                    ]
                }, 
                "for_field": "common_functions"
            }, 
            "jinja_vlan_id": {
                "field": "vlan_id"
            }, 
            "primary_device_password": {
                "field": "password", 
                "path": [
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "gohan_id": {
                "field": "id"
            }, 
            "jinja_service_vrf_name": {
                "field": "service_vrf_name", 
                "path": [
                    "common_function_pool_id"
                ]
            }, 
            "jinja_dnat_group_name": {
                "field": "dnat_group_name", 
                "path": [
                    "common_function_pool_id"
                ]
            }, 
            "heat_timeout": "C60", 
            "primary_device_ip": {
                "field": "ip", 
                "path": [
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "jinja_logical_tunnel_unit_user": {
                "field": "logical_tunnel_unit_user"
            }, 
            "version": {
                "version": "auto_filled"
            }, 
            "secondary_device_logical_downlink_interface": {
                "field": "secondary_logical_interface_name"
            }, 
            "secondary_device_physical_downlink_interface": {
                "field": "name", 
                "path": [
                    "downlink_interface_id", 
                    "secondary_interface_id"
                ]
            }, 
            "secondary_device_username": {
                "field": "login", 
                "path": [
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "secondary_router_id"
                ]
            }, 
            "jinja_dnat_pool_group_name": {
                "field": "dnat_pool_group_name", 
                "path": [
                    "common_function_pool_id"
                ]
            }, 
            "jinja_nat_ip": {
                "field": "nat_ip"
            }, 
            "jinja_dummy_dependency": {
                "field": "id", 
                "path": [
                    {
                        "type": "subnet", 
                        "id": "subnet_id"
                    }
                ], 
                "ignore_missing": true
            }, 
            "jinja_vrf_name": {
                "field": "vrf_name"
            }, 
            "jinja_vrrp_group_name": {
                "field": "vrrp_group_name", 
                "path": [
                    "common_function_pool_id"
                ]
            }, 
            "jinja_snapt_group_name": {
                "field": "snapt_group_name", 
                "path": [
                    "common_function_pool_id"
                ]
            }, 
            "jinja_logical_tunnel_interface_name": {
                "field": "logical_tunnel_interface_name", 
                "path": [
                    "common_function_pool_id"
                ]
            }, 
            "tenant_id": {
                "field": "tenant_id"
            }, 
            "secondary_device_port": {
                "field": "ssh_port", 
                "path": [
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "secondary_router_id"
                ]
            }, 
            "jinja_logical_tunnel_unit_service": {
                "field": "logical_tunnel_unit_service"
            }, 
            "secondary_device_password": {
                "field": "password", 
                "path": [
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "secondary_router_id"
                ]
            }, 
            "jinja_service_interface_name": {
                "field": "service_interface_name", 
                "path": [
                    "common_function_pool_id"
                ]
            }, 
            "primary_device_username": {
                "field": "login", 
                "path": [
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "primary_device_physical_downlink_interface": {
                "field": "name", 
                "path": [
                    "downlink_interface_id", 
                    "primary_interface_id"
                ]
            }, 
            "jinja_snapt_pool_group_name": {
                "field": "snapt_pool_group_name", 
                "path": [
                    "common_function_pool_id"
                ]
            }, 
            "primary_device_port": {
                "field": "ssh_port", 
                "path": [
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "secondary_device_ip": {
                "field": "ip", 
                "path": [
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "secondary_router_id"
                ]
            }
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
  Common Function Gateway

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
  gohan_id:
    type: string
    label: Gohan resource ID
    description: UUID of the Common Function Gateway
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
      lock_timeout: 3000
      configs:
      - config: |
          nat-rules {{ jinja_vrf_name }}-SNAPT;
          nat-rules {{ jinja_vrf_name }}-DNAT;
          interface-service service-interface {{ jinja_service_interface_name }}.{{ jinja_vlan_id }};
        path:
          - config_type: tag
            xml_type: tag
            tag: services
          - config_type: named_tag
            xml_type: named_tag
            tag: service-set
            name: {{ jinja_vrf_name }}
      - config: |
          apply-groups {{ jinja_snapt_pool_group_name }};
          address {{ jinja_nat_ip }}/32;
        path:
          - config_type: tag
            xml_type: tag
            tag: services
          - config_type: tag
            xml_type: tag
            tag: nat
          - config_type: named_tag
            xml_type: named_tag
            tag: pool
            name: {{ jinja_vrf_name }}-SNAPT-POOL
      - config: |
          apply-groups {{ jinja_snapt_group_name }};
          term source then translated source-pool {{ jinja_vrf_name }}-SNAPT-POOL;
        path:
          - config_type: tag
            xml_type: tag
            tag: services
          - config_type: tag
            xml_type: tag
            tag: nat
          - config_type: named_tag
            xml_type: named_tag
            tag: rule
            name: {{ jinja_vrf_name }}-SNAPT
      {% for service_number in jinja_common_service_numbers %}
      - config: |
          apply-groups {{ jinja_dnat_pool_group_name }}-{{ service_number }};
        path:
          - config_type: tag
            xml_type: tag
            tag: services
          - config_type: tag
            xml_type: tag
            tag: nat
          - config_type: named_tag
            xml_type: named_tag
            tag: pool
            name: {{ jinja_vrf_name }}-{{ jinja_dnat_pool_group_name }}-{{ service_number }}
      {% endfor %}
      - config: |
          apply-groups {{ jinja_dnat_group_name }};
          {% for service_number in jinja_common_service_numbers %}
          term {{ service_number }} then translated destination-pool {{ jinja_vrf_name }}-{{ jinja_dnat_pool_group_name }}-{{ service_number }};
          {% endfor %}
        path:
          - config_type: tag
            xml_type: tag
            tag: services
          - config_type: tag
            xml_type: tag
            tag: nat
          - config_type: named_tag
            xml_type: named_tag
            tag: rule
            name: {{ jinja_vrf_name }}-DNAT
      - config: |
          peer-unit {{ jinja_logical_tunnel_unit_service }};
          family inet service input service-set {{ jinja_vrf_name }};
          family inet service output service-set {{ jinja_vrf_name }};
        path:
          - config_type: tag
            xml_type: tag
            tag: interfaces
          - config_type: name
            xml_type: named_tag
            tag: interface
            name: {{ jinja_logical_tunnel_interface_name }}
          - config_type: named_tag
            xml_type: named_tag
            tag: unit
            name: {{ jinja_logical_tunnel_unit_user }}
      - config: |
          peer-unit {{ jinja_logical_tunnel_unit_user }};
        path:
          - config_type: tag
            xml_type: tag
            tag: interfaces
          - config_type: name
            xml_type: named_tag
            tag: interface
            name: {{ jinja_logical_tunnel_interface_name }}
          - config_type: named_tag
            xml_type: named_tag
            tag: unit
            name: {{ jinja_logical_tunnel_unit_service }}
      - config: |
          family inet;
        path:
          - config_type: tag
            xml_type: tag
            tag: interfaces
          - config_type: name
            xml_type: named_tag
            tag: interface
            name: {{ jinja_service_interface_name }}
          - config_type: named_tag
            xml_type: named_tag
            tag: unit
            name: {{ jinja_vlan_id }}
      - config: |
          apply-groups {{ jinja_vrrp_group_name }};
          description {{ jinja_vrf_name }};
          vlan-id {{ jinja_vlan_id }};
          family inet service input service-set {{ jinja_vrf_name }};
          family inet service output service-set {{ jinja_vrf_name }};
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
            name: {{ jinja_vlan_id }}
      - config: ""
        path:
          - config_type: tag
            xml_type: tag
            tag: routing-instances
          - config_type: name
            xml_type: named_tag
            tag: instance
            name: {{ jinja_service_vrf_name }}
          - config_type: named_tag
            xml_type: named_tag
            tag: interface
            name: {{ jinja_logical_tunnel_interface_name }}.{{ jinja_logical_tunnel_unit_service }}
      - config:
          next-hop {{ jinja_logical_tunnel_interface_name }}.{{ jinja_logical_tunnel_unit_service }};
        path:
          - config_type: tag
            xml_type: tag
            tag: routing-instances
          - config_type: name
            xml_type: named_tag
            tag: instance
            name: {{ jinja_service_vrf_name }}
          - config_type: tag
            xml_type: tag
            tag: routing-options
          - config_type: tag
            xml_type: tag
            tag: static
          - config_type: named_tag
            xml_type: named_tag
            tag: route
            name: {{ jinja_nat_ip }}/32
      - config:
          str_replace:
            params:
              $DOWNLINK_INTERFACE:
                get_param: {{ device }}_device_logical_downlink_interface
            template: |
              instance-type virtual-router;
              interface {{ jinja_logical_tunnel_interface_name }}.{{ jinja_logical_tunnel_unit_user}};
              interface {{ jinja_service_interface_name}}.{{ jinja_vlan_id }};
              interface $DOWNLINK_INTERFACE;
              routing-options static route 0.0.0.0/0 next-hop {{ jinja_logical_tunnel_interface_name }}.{{ jinja_logical_tunnel_unit_user }};
        path:
          - config_type: tag
            xml_type: tag
            tag: routing-instances
          - config_type: name
            xml_type: named_tag
            tag: instance
            name: {{ jinja_vrf_name }}
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

  vrrp_monitor:
    type: ESI::Monitoring::MonitoringTarget
    properties:
      type: vrrp_pool
      resource_type: common_function_gateways
      resource_id: { get_param: gohan_id }
      tenant_id: { get_param: tenant_id }
      version: { get_param: version }
      field_name: status
      properties:
        vrid:
        {% for vrid in jinja_vrids %}
          - {{ vrid }}
        {% endfor %}
        primary:
          host: { get_param: primary_device_ip }
          port: { get_param: primary_device_port }
          login: { get_param: primary_device_username }
          password: { get_param: primary_device_password }
          interface: { get_param: primary_device_logical_downlink_interface }
        secondary:
          host: { get_param: secondary_device_ip }
          port: { get_param: secondary_device_port }
          login: { get_param: secondary_device_username }
          password: { get_param: secondary_device_password }
          interface: { get_param: secondary_device_logical_downlink_interface }
      syncer_properties:
        etcd:
          status:
            key: status
          hold_options:
            positive_status:
              primary_vrid1: MASTER
              secondary_vrid1: BACKUP
              primary_vrid2: MASTER
              secondary_vrid2: BACKUP
            time_seconds: 360
    depends_on: netconf_configure_secondary

outputs:
  monitoring_target_id:
    description: Monitoring Target ID
    value: { get_resource: vrrp_monitor}
  monitoring_link:
    description: Monitoring Process Link
    value: { get_attr: [vrrp_monitor, link]}
```
