# heat_template: gw_interface_aws
This is heat_template of "gw_interface_aws" which is provided by gohan via etcd

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/gw_interface_aws
{
    "body": {
        "handler": "heat_worker",
        "watch": [],
        "id": "gw_interface_aws",
        "template_file": "heat_template_version: 2013-05-23\n\ndescription: >\n  Inet Address\n\nparameters:\n  primary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Primary Device.\n    label: Ip address of the device.\n    type: string\n  primary_device_port:\n    description: Port that will be used to establish ssh connection to the Primary Device.\n    label: Port of the ssh connection.\n    type: number\n  primary_device_username:\n    description: Name of the user which will be used to log onto the Primary Device.\n    label: User name to log on to device.\n    type: string\n  primary_device_password:\n    description: Password of the user which will be used to log onto the Primary Device.\n    label: Users password.\n    type: string\n    hidden: true\n  secondary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Secondary Device.\n    label: Ip address of the device.\n    type: string\n  secondary_device_port:\n    description: Port that will be used to establish ssh connection to the Secondary Device.\n    label: Port of the ssh connection.\n    type: number\n  secondary_device_username:\n    description: Name of the user which will be used to log onto the Secondary Device.\n    label: User name to log on to device.\n    type: string\n  secondary_device_password:\n    description: Password of the user which will be used to log onto the Secondary Device.\n    label: Users password.\n    type: string\n    hidden: true\n  primary_device_physical_interface:\n    description: MX physical port on which logical interface will be created\n    label: Underlying physical interface\n    type: string\n  secondary_device_physical_interface:\n    description: MX physical port on which logical interface will be created\n    label: Underlying physical interface\n    type: string\n  downlink_vlan_id:\n    description: Vlan tag for mx logical downlink interface\n    label: Vlan Tag\n    type: string\n  gw_vip:\n    description: Virtual IP configured on VRRP\n    label: Inet Address CIDR\n    type: string\n  primary_device_gw_ip:\n    description: IP on primary device\n    label: Inet Address CIDR\n    type: string\n  secondary_device_gw_ip:\n    description: IP on secondary device\n    label: Inet Address CIDR\n    type: string\n  netmask:\n    description: Netmask for gw_ip\n    label: Netmask\n    type: number\n  vrrp_group:\n    type: string\n    label: VRRP Group\n  primary_device_priority:\n    type: string\n    label: Primary device priority\n  secondary_device_priority:\n    type: string\n    label: Secondary device priority\n  vrf_name:\n    type: string\n    label: VRF\n  bgp_group_name:\n    type: string\n    label: Name of BGP Group on VRF\n  local_as:\n    type: string\n    label: Local AS Number\n  primary_ibgp_config_group:\n    description: Name for apply group to use for downlink interface\n    label: Apply group name\n    type: string\n  secondary_ibgp_config_group:\n    description: Name for apply group to use for downlink interface\n    label: Apply group name\n    type: string\n  primary_logical_interface_name:\n    description: MX logical port\n    label: Underlying logical interface\n    type: string\n  secondary_logical_interface_name:\n    description: MX logical port\n    label: Underlying logical interface\n    type: string\n  gohan_id:\n    type: string\n    label: Gohan resource ID\n    description: UUID of the GW Interface\n  tenant_id:\n    type: string\n    label: Tenant ID\n  version:\n    type: number\n    label: Config version\nresources:\n{% for device in [\"primary\", \"secondary\"] %}\n  netconf_configure_{{ device }}:\n    type: OS::Contrail::NetconfNamedConfigs\n    {% if device == \"secondary\" %}depends_on: netconf_configure_primary{% endif %}\n    properties:\n      lock_timeout: 3000\n      device_ip:\n        get_param: {{ device }}_device_ip\n      password:\n        get_param: {{ device }}_device_password\n      port:\n        get_param: {{ device }}_device_port\n      username:\n        get_param: {{ device }}_device_username\n      configs:\n      - config:\n          str_replace:\n            params:\n              $VRRP_GROUP:\n                    get_param: vrrp_group\n              $PRIORITY:\n                    get_param: {{ device }}_device_priority\n              $VIP:\n                    get_param: gw_vip\n            template: |\n                vrrp-group $VRRP_GROUP {\n                    virtual-address $VIP;\n                    priority $PRIORITY;\n                }\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: interfaces\n          - config_type: name\n            xml_type: named_tag\n            tag: interface\n            name: { get_param: {{ device }}_device_physical_interface }\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: unit\n            name: { get_param: downlink_vlan_id }\n          - config_type: tag\n            xml_type: tag\n            tag: family\n          - config_type: tag\n            xml_type: tag\n            tag: inet\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: address\n            name:\n              str_replace:\n                params:\n                  $DEVICE_IP:\n                    get_param: {{ device }}_device_gw_ip\n                  $NETMASK:\n                    get_param: netmask\n                template: |\n                  $DEVICE_IP/$NETMASK\n      - config:\n          str_replace:\n            params:\n              $DEVICE_GW_IP:\n                    get_param: {{ device }}_device_gw_ip\n              $NEIGHBOR_GW_IP:\n                    get_param: {% if device == \"secondary\" %}primary{% else %}secondary{% endif %}_device_gw_ip\n              $LOCAL_AS:\n                    get_param: local_as\n              $APPLY_GROUP:\n                    get_param: {{ device }}_ibgp_config_group\n            template: |\n              apply-groups $APPLY_GROUP;\n              local-address $DEVICE_GW_IP;\n              peer-as $LOCAL_AS;\n              neighbor $NEIGHBOR_GW_IP;\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: routing-instances\n          - config_type: name\n            xml_type: named_tag\n            tag: instance\n            name: { get_param: vrf_name }\n          - config_type: tag\n            xml_type: tag\n            tag: protocols\n          - config_type: tag\n            xml_type: tag\n            tag: bgp\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: group\n            name: { get_param: bgp_group_name }\n{% endfor %}\n\n  vrrp_monitor:\n    type: ESI::Monitoring::MonitoringTarget\n    properties:\n      type: vrrp_pool\n      resource_type: gw_interfaces\n      resource_id: { get_param: gohan_id }\n      tenant_id: { get_param: tenant_id }\n      version: { get_param: version }\n      field_name: status\n      properties:\n        vrid:\n          - { get_param: vrrp_group }\n        primary:\n          host: { get_param: primary_device_ip }\n          port: { get_param: primary_device_port }\n          login: { get_param: primary_device_username }\n          password: { get_param: primary_device_password }\n          interface: { get_param: primary_logical_interface_name }\n        secondary:\n          host: { get_param: secondary_device_ip }\n          port: { get_param: secondary_device_port }\n          login: { get_param: secondary_device_username }\n          password: { get_param: secondary_device_password }\n          interface: { get_param: secondary_logical_interface_name }\n      syncer_properties:\n        etcd:\n          status:\n            key: status\n          hold_options:\n            positive_status:\n              - primary: MASTER\n                secondary: BACKUP\n            time_seconds: 360\n    depends_on: netconf_configure_secondary\n\noutputs:\n  monitoring_target_id:\n    description: Monitoring Target ID\n    value: { get_resource: vrrp_monitor}\n  monitoring_link:\n    description: Monitoring Process Link\n    value: { get_attr: [vrrp_monitor, link]}\n",
        "parameter_mappings": {
            "secondary_device_physical_interface": "Faws_gateway+aws_gw_id:ha_interface+downlink_interface_id:er_physical_interface+secondary_interface_id:name",
            "secondary_ibgp_config_group": "Faws_gateway+aws_gw_id:aws_service+aws_service_id:secondary_ibgp_config_group",
            "primary_device_password": "Faws_gateway+aws_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:password",
            "secondary_device_gw_ip": "Psecondary_ipv4",
            "gohan_id": "Pid",
            "bgp_group_name": "Cinet-gw-group",
            "gw_vip": "Pgw_vipv4",
            "primary_device_ip": "Faws_gateway+aws_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:ip",
            "version": "Vauto_filled",
            "secondary_device_username": "Faws_gateway+aws_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:login",
            "primary_device_username": "Faws_gateway+aws_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:login",
            "downlink_vlan_id": "Faws_gateway+aws_gw_id:downlink_vlan_id",
            "secondary_logical_interface_name": "Faws_gateway+aws_gw_id:secondary_logical_downlink_interface_name",
            "primary_logical_interface_name": "Faws_gateway+aws_gw_id:primary_logical_downlink_interface_name",
            "local_as": "Faws_gateway+aws_gw_id:local_as_number",
            "primary_device_physical_interface": "Faws_gateway+aws_gw_id:ha_interface+downlink_interface_id:er_physical_interface+primary_interface_id:name",
            "netmask": "Pnetmask",
            "primary_device_gw_ip": "Pprimary_ipv4",
            "vrrp_group": "Pvrid",
            "primary_device_priority": "C105",
            "jinja_force_dependency": "Faws_gateway+aws_gw_id:aws_interface+connected_aws_interface:id",
            "tenant_id": "Ptenant_id",
            "secondary_device_port": "Faws_gateway+aws_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:ssh_port",
            "secondary_device_password": "Faws_gateway+aws_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:password",
            "heat_timeout": "C60",
            "vrf_name": "Faws_gateway+aws_gw_id:vrf_name",
            "jinja_force_dependency2": {
                "field": "id",
                "path": [
                    {
                        "type": "network",
                        "id": "network_id"
                    }
                ]
            },
            "secondary_device_priority": "C100",
            "primary_ibgp_config_group": "Faws_gateway+aws_gw_id:aws_service+aws_service_id:primary_ibgp_config_group",
            "primary_device_port": "Faws_gateway+aws_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:ssh_port",
            "secondary_device_ip": "Faws_gateway+aws_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:ip"
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
  Inet Address

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
  secondary_device_physical_interface:
    description: MX physical port on which logical interface will be created
    label: Underlying physical interface
    type: string
  downlink_vlan_id:
    description: Vlan tag for mx logical downlink interface
    label: Vlan Tag
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
  netmask:
    description: Netmask for gw_ip
    label: Netmask
    type: number
  vrrp_group:
    type: string
    label: VRRP Group
  primary_device_priority:
    type: string
    label: Primary device priority
  secondary_device_priority:
    type: string
    label: Secondary device priority
  vrf_name:
    type: string
    label: VRF
  bgp_group_name:
    type: string
    label: Name of BGP Group on VRF
  local_as:
    type: string
    label: Local AS Number
  primary_ibgp_config_group:
    description: Name for apply group to use for downlink interface
    label: Apply group name
    type: string
  secondary_ibgp_config_group:
    description: Name for apply group to use for downlink interface
    label: Apply group name
    type: string
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
              $PRIORITY:
                    get_param: {{ device }}_device_priority
              $VIP:
                    get_param: gw_vip
            template: |
                vrrp-group $VRRP_GROUP {
                    virtual-address $VIP;
                    priority $PRIORITY;
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
            name: { get_param: downlink_vlan_id }
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
      - config:
          str_replace:
            params:
              $DEVICE_GW_IP:
                    get_param: {{ device }}_device_gw_ip
              $NEIGHBOR_GW_IP:
                    get_param: {% if device == "secondary" %}primary{% else %}secondary{% endif %}_device_gw_ip
              $LOCAL_AS:
                    get_param: local_as
              $APPLY_GROUP:
                    get_param: {{ device }}_ibgp_config_group
            template: |
              apply-groups $APPLY_GROUP;
              local-address $DEVICE_GW_IP;
              peer-as $LOCAL_AS;
              neighbor $NEIGHBOR_GW_IP;
        path:
          - config_type: tag
            xml_type: tag
            tag: routing-instances
          - config_type: name
            xml_type: named_tag
            tag: instance
            name: { get_param: vrf_name }
          - config_type: tag
            xml_type: tag
            tag: protocols
          - config_type: tag
            xml_type: tag
            tag: bgp
          - config_type: named_tag
            xml_type: named_tag
            tag: group
            name: { get_param: bgp_group_name }
{% endfor %}

  vrrp_monitor:
    type: ESI::Monitoring::MonitoringTarget
    properties:
      type: vrrp_pool
      resource_type: gw_interfaces
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

outputs:
  monitoring_target_id:
    description: Monitoring Target ID
    value: { get_resource: vrrp_monitor}
  monitoring_link:
    description: Monitoring Process Link
    value: { get_attr: [vrrp_monitor, link]}
```
