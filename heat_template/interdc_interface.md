# heat_template: interdc_interface
This is heat_template of "interdc_interface" which is provided by gohan via etcd

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/interdc_interface
{
    "body": {
        "handler": "heat_worker",
        "watch": [],
        "id": "interdc_interface",
        "template_file": "heat_template_version: 2013-05-23\n\ndescription: >\n  Interdc Interface\n\nparameters:\n  primary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Primary Device.\n    label: Ip address of the device.\n    type: string\n  primary_device_port:\n    description: Port that will be used to establish ssh connection to the Primary Device.\n    label: Port of the ssh connection.\n    type: number\n  primary_device_username:\n    description: Name of the user which will be used to log onto the Primary Device.\n    label: User name to log on to device.\n    type: string\n  primary_device_password:\n    description: Password of the user which will be used to log onto the Primary Device.\n    label: Users password.\n    type: string\n    hidden: true\n  secondary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Secondary Device.\n    label: Ip address of the device.\n    type: string\n  secondary_device_port:\n    description: Port that will be used to establish ssh connection to the Secondary Device.\n    label: Port of the ssh connection.\n    type: number\n  secondary_device_username:\n    description: Name of the user which will be used to log onto the Secondary Device.\n    label: User name to log on to device.\n    type: string\n  secondary_device_password:\n    description: Password of the user which will be used to log onto the Secondary Device.\n    label: Users password.\n    type: string\n    hidden: true\n  primary_device_physical_interface:\n    description: MX physical port on which logical interface will be created\n    label: Underlying physical interface\n    type: string\n  primary_device_logical_interface:\n    description: Name of the created logical uplink interface on the Primary device\n    label: Logical Interface name\n    type: string\n  primary_device_downlink_physical_interface:\n    description: MX physical port on which logical downlink interface will be created\n    label: Underlying physical interface\n    type: string\n  secondary_device_physical_interface:\n    description: MX physical port on which logical interface will be created\n    label: Underlying physical interface\n    type: string\n  secondary_device_logical_interface:\n    description: Name of the created logical uplink interface on the Secondary device\n    label: Logical Interface name\n    type: string\n  secondary_device_downlink_physical_interface:\n    description: MX physical port on which downlink logical interface will be created\n    label: Underlying physical interface\n    type: string\n  primary_device_gw_ip:\n    description: IP on primary device\n    label: Inet Address CIDR\n    type: string\n  secondary_device_gw_ip:\n    description: IP on secondary device\n    label: Inet Address CIDR\n    type: string\n  primary_device_priority:\n    type: string\n    label: Primary device priority\n  secondary_device_priority:\n    type: string\n    label: Secondary device priority\n  vrf_name:\n    description: Name of VRF (routing-instance) in MX config\n    label: VRF Name\n    type: string\n  netmask:\n    description: Netmask for gw_ip\n    label: Netmask\n    type: number\n  uplink_vlan_id:\n    description: VLAN ID used on uplink interfaces (same for both primary and secondary device)\n    label: Uplink VLAN ID\n    type: string\n  downlink_vlan_id:\n    description: VLAN ID used on downlink interfaces (same for both primary and secondary device)\n    label: Downlink VLAN ID\n    type: string\n  gw_vip:\n    description: Virtual IP configured on VRRP\n    label: Inet Address CIDR\n    type: string\n  primary_device_gw_ip:\n    description: IP on primary device\n    label: Inet Address CIDR\n    type: string\n  secondary_device_gw_ip:\n    description: IP on secondary device\n    label: Inet Address CIDR\n    type: string\n  vrrp_group:\n    type: string\n    label: VRRP Group\n  primary_logical_interface_name:\n    description: MX logical port\n    label: Underlying logical interface\n    type: string\n  secondary_logical_interface_name:\n    description: MX logical port\n    label: Underlying logical interface\n    type: string\n  gohan_id:\n    type: string\n    label: Gohan resource ID\n    description: UUID of the InterDC Interface\n  tenant_id:\n    type: string\n    label: Tenant ID\n  version:\n    type: number\n    label: Config version\nresources:\n{% for device in [\"primary\", \"secondary\"] %}\n  netconf_configure_{{ device }}:\n    type: OS::Contrail::NetconfNamedConfigs\n    {% if device == \"secondary\" %}depends_on: netconf_configure_primary{% endif %}\n    properties:\n      lock_timeout: 3000\n      device_ip:\n        get_param: {{ device }}_device_ip\n      password:\n        get_param: {{ device }}_device_password\n      port:\n        get_param: {{ device }}_device_port\n      username:\n        get_param: {{ device }}_device_username\n      configs:\n      - config:\n          str_replace:\n            params:\n              $VRRP_GROUP:\n                get_param: vrrp_group\n              $VIP:\n                get_param: gw_vip\n              $PRIORITY:\n                get_param: {{ device }}_device_priority\n              $DOWNLINK_IF:\n                get_param: secondary_device_downlink_physical_interface\n              $DOWNLINK_VLAN_ID:\n                get_param: downlink_vlan_id\n            template: |\n              vrrp-group $VRRP_GROUP {\n                virtual-address $VIP;\n                priority $PRIORITY;\n                track {\n                  interface $DOWNLINK_IF.$DOWNLINK_VLAN_ID {\n                    priority-cost 10;\n                  }\n                }\n              }\n        path:\n        - config_type: tag\n          xml_type: tag\n          tag: interfaces\n        - config_type: name\n          xml_type: named_tag\n          tag: interface\n          name: { get_param: {{ device }}_device_physical_interface }\n        - config_type: named_tag\n          xml_type: named_tag\n          tag: unit\n          name: { get_param: uplink_vlan_id }\n        - config_type: tag\n          xml_type: tag\n          tag: family\n        - config_type: tag\n          xml_type: tag\n          tag: inet\n        - config_type: named_tag\n          xml_type: named_tag\n          tag: address\n          name:\n            str_replace:\n              params:\n                $DEVICE_IP:\n                  get_param: {{ device }}_device_gw_ip\n                $NETMASK:\n                  get_param: netmask\n              template: |\n                $DEVICE_IP/$NETMASK\n{% endfor %}\n\n  vrrp_monitor:\n    type: ESI::Monitoring::MonitoringTarget\n    properties:\n      type: vrrp_pool\n      resource_type: interdc_interfaces\n      resource_id: { get_param: gohan_id }\n      tenant_id: { get_param: tenant_id }\n      version: { get_param: version }\n      field_name: status\n      properties:\n        vrid:\n          - { get_param: vrrp_group }\n        primary:\n          host: { get_param: primary_device_ip }\n          port: { get_param: primary_device_port }\n          login: { get_param: primary_device_username }\n          password: { get_param: primary_device_password }\n          interface: { get_param: primary_logical_interface_name }\n        secondary:\n          host: { get_param: secondary_device_ip }\n          port: { get_param: secondary_device_port }\n          login: { get_param: secondary_device_username }\n          password: { get_param: secondary_device_password }\n          interface: { get_param: secondary_logical_interface_name }\n      syncer_properties:\n        etcd:\n          status:\n            key: status\n          hold_options:\n            positive_status:\n              - primary: MASTER\n                secondary: BACKUP\n            time_seconds: 360\n    depends_on: netconf_configure_secondary\n\n{% for device in [\"primary\", \"secondary\"] %}\n  {{ device }}_interface_metric_monitor:\n    type: ESI::Monitoring::MonitoringTarget\n    properties:\n      type: snmp_ports_metric\n      resource_type: interdc_interfaces\n      resource_id: { get_param: gohan_id }\n      tenant_id: { get_param: tenant_id }\n      version: { get_param: version }\n      field_name: {{ device }}_router\n      properties:\n        device_ip: { get_param: {{ device }}_device_ip }\n        if_name: { get_param: {{ device }}_device_logical_interface }\n        community_name: EDGE_ROUTER_COMMUNITY\n      syncer_properties:\n        tsdb:\n          traffic.in:\n            metric: traffic.bytes\n            tags:\n              device_index: {{ device }}\n              resource_id: { get_param: gohan_id }\n              direction: in\n          traffic.out:\n            metric: traffic.bytes\n            tags:\n              device_index: {{ device }}\n              resource_id: { get_param: gohan_id }\n              direction: out\n    depends_on: vrrp_monitor\n{% endfor %}\n\noutputs:\n  monitoring_target_id:\n    description: Monitoring Target ID\n    value: { get_resource: vrrp_monitor}\n  monitoring_link:\n    description: Monitoring Process Link\n    value: { get_attr: [vrrp_monitor, link]}\n{% for device in [\"primary\", \"secondary\"] %}\n  {{ device }}_interface_monitoring_target_id:\n    description: Monitoring Target ID\n    value: { get_resource: {{ device }}_interface_metric_monitor}\n  {{ device }}_interface_monitoring_link:\n    description: Monitoring Process Link\n    value: { get_attr: [{{ device }}_interface_metric_monitor, link]}\n{% endfor %}\n",
        "parameter_mappings": {
            "secondary_device_physical_interface": {
                "field": "name",
                "path": [
                    "interdc_gw_id",
                    "uplink_interface_id",
                    "secondary_interface_id"
                ]
            },
            "primary_device_logical_interface": {
                "field": "primary_logical_uplink_interface_name",
                "path": [
                    "interdc_gw_id"
                ]
            },
            "primary_device_password": {
                "field": "password",
                "path": [
                    "interdc_gw_id",
                    "downlink_interface_id",
                    "ha_router_id",
                    "primary_router_id"
                ]
            },
            "secondary_device_gw_ip": {
                "field": "secondary_ipv4"
            },
            "gohan_id": {
                "field": "id"
            },
            "primary_device_downlink_physical_interface": {
                "field": "name",
                "path": [
                    "interdc_gw_id",
                    "downlink_interface_id",
                    "primary_interface_id"
                ]
            },
            "gw_vip": {
                "field": "gw_vipv4"
            },
            "primary_device_ip": {
                "field": "ip",
                "path": [
                    "interdc_gw_id",
                    "downlink_interface_id",
                    "ha_router_id",
                    "primary_router_id"
                ]
            },
            "version": {
                "version": "auto_filled"
            },
            "secondary_device_username": {
                "field": "login",
                "path": [
                    "interdc_gw_id",
                    "downlink_interface_id",
                    "ha_router_id",
                    "secondary_router_id"
                ]
            },
            "downlink_vlan_id": {
                "field": "downlink_vlan_id",
                "path": [
                    "interdc_gw_id"
                ]
            },
            "secondary_device_logical_interface": {
                "field": "secondary_logical_uplink_interface_name",
                "path": [
                    "interdc_gw_id"
                ]
            },
            "secondary_logical_interface_name": {
                "field": "secondary_logical_uplink_interface_name",
                "path": [
                    "interdc_gw_id"
                ]
            },
            "primary_logical_interface_name": {
                "field": "primary_logical_uplink_interface_name",
                "path": [
                    "interdc_gw_id"
                ]
            },
            "primary_device_physical_interface": {
                "field": "name",
                "path": [
                    "interdc_gw_id",
                    "uplink_interface_id",
                    "primary_interface_id"
                ]
            },
            "netmask": {
                "field": "netmask"
            },
            "secondary_device_downlink_physical_interface": {
                "field": "name",
                "path": [
                    "interdc_gw_id",
                    "downlink_interface_id",
                    "secondary_interface_id"
                ]
            },
            "primary_device_gw_ip": {
                "field": "primary_ipv4"
            },
            "vrrp_group": {
                "field": "vrid"
            },
            "primary_device_priority": {
                "constant": 105
            },
            "tenant_id": {
                "field": "tenant_id"
            },
            "secondary_device_port": {
                "field": "ssh_port",
                "path": [
                    "interdc_gw_id",
                    "downlink_interface_id",
                    "ha_router_id",
                    "secondary_router_id"
                ]
            },
            "secondary_device_password": {
                "field": "password",
                "path": [
                    "interdc_gw_id",
                    "downlink_interface_id",
                    "ha_router_id",
                    "secondary_router_id"
                ]
            },
            "uplink_vlan_id": {
                "field": "uplink_vlan_id",
                "path": [
                    "interdc_gw_id"
                ]
            },
            "heat_timeout": {
                "constant": 60
            },
            "vrf_name": {
                "field": "vrf_name",
                "path": [
                    "interdc_gw_id"
                ]
            },
            "primary_device_username": {
                "field": "login",
                "path": [
                    "interdc_gw_id",
                    "downlink_interface_id",
                    "ha_router_id",
                    "primary_router_id"
                ]
            },
            "secondary_device_priority": {
                "constant": 100
            },
            "primary_device_port": {
                "field": "ssh_port",
                "path": [
                    "interdc_gw_id",
                    "downlink_interface_id",
                    "ha_router_id",
                    "primary_router_id"
                ]
            },
            "secondary_device_ip": {
                "field": "ip",
                "path": [
                    "interdc_gw_id",
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
  Interdc Interface

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
    description: MX physical port on which logical interface will be created
    label: Underlying physical interface
    type: string
  primary_device_logical_interface:
    description: Name of the created logical uplink interface on the Primary device
    label: Logical Interface name
    type: string
  primary_device_downlink_physical_interface:
    description: MX physical port on which logical downlink interface will be created
    label: Underlying physical interface
    type: string
  secondary_device_physical_interface:
    description: MX physical port on which logical interface will be created
    label: Underlying physical interface
    type: string
  secondary_device_logical_interface:
    description: Name of the created logical uplink interface on the Secondary device
    label: Logical Interface name
    type: string
  secondary_device_downlink_physical_interface:
    description: MX physical port on which downlink logical interface will be created
    label: Underlying physical interface
    type: string
  primary_device_gw_ip:
    description: IP on primary device
    label: Inet Address CIDR
    type: string
  secondary_device_gw_ip:
    description: IP on secondary device
    label: Inet Address CIDR
    type: string
  primary_device_priority:
    type: string
    label: Primary device priority
  secondary_device_priority:
    type: string
    label: Secondary device priority
  vrf_name:
    description: Name of VRF (routing-instance) in MX config
    label: VRF Name
    type: string
  netmask:
    description: Netmask for gw_ip
    label: Netmask
    type: number
  uplink_vlan_id:
    description: VLAN ID used on uplink interfaces (same for both primary and secondary device)
    label: Uplink VLAN ID
    type: string
  downlink_vlan_id:
    description: VLAN ID used on downlink interfaces (same for both primary and secondary device)
    label: Downlink VLAN ID
    type: string
  gw_vip:
    description: Virtual IP configured on VRRP
    label: Inet Address CIDR
    type: string
  primary_device_gw_ip:
    description: IP on primary device
    label: Inet Address CIDR
    type: string
  secondary_device_gw_ip:
    description: IP on secondary device
    label: Inet Address CIDR
    type: string
  vrrp_group:
    type: string
    label: VRRP Group
  primary_logical_interface_name:
    description: MX logical port
    label: Underlying logical interface
    type: string
  secondary_logical_interface_name:
    description: MX logical port
    label: Underlying logical interface
    type: string
  gohan_id:
    type: string
    label: Gohan resource ID
    description: UUID of the InterDC Interface
  tenant_id:
    type: string
    label: Tenant ID
  version:
    type: number
    label: Config version
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
      configs:
      - config:
          str_replace:
            params:
              $VRRP_GROUP:
                get_param: vrrp_group
              $VIP:
                get_param: gw_vip
              $PRIORITY:
                get_param: {{ device }}_device_priority
              $DOWNLINK_IF:
                get_param: secondary_device_downlink_physical_interface
              $DOWNLINK_VLAN_ID:
                get_param: downlink_vlan_id
            template: |
              vrrp-group $VRRP_GROUP {
                virtual-address $VIP;
                priority $PRIORITY;
                track {
                  interface $DOWNLINK_IF.$DOWNLINK_VLAN_ID {
                    priority-cost 10;
                  }
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
          name: { get_param: uplink_vlan_id }
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
                $DEVICE_IP:
                  get_param: {{ device }}_device_gw_ip
                $NETMASK:
                  get_param: netmask
              template: |
                $DEVICE_IP/$NETMASK
{% endfor %}

  vrrp_monitor:
    type: ESI::Monitoring::MonitoringTarget
    properties:
      type: vrrp_pool
      resource_type: interdc_interfaces
      resource_id: { get_param: gohan_id }
      tenant_id: { get_param: tenant_id }
      version: { get_param: version }
      field_name: status
      properties:
        vrid:
          - { get_param: vrrp_group }
        primary:
          host: { get_param: primary_device_ip }
          port: { get_param: primary_device_port }
          login: { get_param: primary_device_username }
          password: { get_param: primary_device_password }
          interface: { get_param: primary_logical_interface_name }
        secondary:
          host: { get_param: secondary_device_ip }
          port: { get_param: secondary_device_port }
          login: { get_param: secondary_device_username }
          password: { get_param: secondary_device_password }
          interface: { get_param: secondary_logical_interface_name }
      syncer_properties:
        etcd:
          status:
            key: status
          hold_options:
            positive_status:
              - primary: MASTER
                secondary: BACKUP
            time_seconds: 360
    depends_on: netconf_configure_secondary

{% for device in ["primary", "secondary"] %}
  {{ device }}_interface_metric_monitor:
    type: ESI::Monitoring::MonitoringTarget
    properties:
      type: snmp_ports_metric
      resource_type: interdc_interfaces
      resource_id: { get_param: gohan_id }
      tenant_id: { get_param: tenant_id }
      version: { get_param: version }
      field_name: {{ device }}_router
      properties:
        device_ip: { get_param: {{ device }}_device_ip }
        if_name: { get_param: {{ device }}_device_logical_interface }
        community_name: EDGE_ROUTER_COMMUNITY
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
    depends_on: vrrp_monitor
{% endfor %}

outputs:
  monitoring_target_id:
    description: Monitoring Target ID
    value: { get_resource: vrrp_monitor}
  monitoring_link:
    description: Monitoring Process Link
    value: { get_attr: [vrrp_monitor, link]}
{% for device in ["primary", "secondary"] %}
  {{ device }}_interface_monitoring_target_id:
    description: Monitoring Target ID
    value: { get_resource: {{ device }}_interface_metric_monitor}
  {{ device }}_interface_monitoring_link:
    description: Monitoring Process Link
    value: { get_attr: [{{ device }}_interface_metric_monitor, link]}
{% endfor %}
```
