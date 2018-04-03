# heat_template: vpn_interface
This is heat_template of "vpn_interface" which is provided by gohan via etcd

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/vpn_interface
{
    "body": {
        "handler": "heat_worker", 
        "watch": [], 
        "id": "vpn_interface", 
        "template_file": "heat_template_version: 2013-05-23\n\ndescription: >\n  Inet Address\n\nparameters:\n  primary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Primary Device.\n    label: Ip address of the device.\n    type: string\n  primary_device_port:\n    description: Port that will be used to establish ssh connection to the Primary Device.\n    label: Port of the ssh connection.\n    type: number\n  primary_device_username:\n    description: Name of the user which will be used to log onto the Primary Device.\n    label: User name to log on to device.\n    type: string\n  primary_device_password:\n    description: Password of the user which will be used to log onto the Primary Device.\n    label: Users password.\n    type: string\n    hidden: true\n  secondary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Secondary Device.\n    label: Ip address of the device.\n    type: string\n  secondary_device_port:\n    description: Port that will be used to establish ssh connection to the Secondary Device.\n    label: Port of the ssh connection.\n    type: number\n  secondary_device_username:\n    description: Name of the user which will be used to log onto the Secondary Device.\n    label: User name to log on to device.\n    type: string\n  secondary_device_password:\n    description: Password of the user which will be used to log onto the Secondary Device.\n    label: Users password.\n    type: string\n    hidden: true\n  primary_device_physical_interface:\n    description: MX physical port on which logical interface will be created\n    label: Underlying physical interface\n    type: string\n  secondary_device_physical_interface:\n    description: MX physical port on which logical interface will be created\n    label: Underlying physical interface\n    type: string\n  primary_device_logical_interface:\n    description: Name of the created logical uplink interface on the Primary device\n    label: Logical Interface name\n    type: string\n  secondary_device_logical_interface:\n    description: Name of the created logical uplink interface on the Secondary device\n    label: Logical Interface name\n    type: string\n  vrf_name:\n    description: Name of VRF (routing-instance) in MX config\n    label: VRF Name\n    type: string\n  local_as:\n    type: number\n    label: Local AS Number\n  primary_ebgp_config_group:\n    description: Name of MX config group for eBGP config\n    label: eBGP config group\n    type: string\n  secondary_ebgp_config_group:\n    description: Name of MX config group for eBGP config\n    label: eBGP config group\n    type: string\n  uplink_vlan:\n    description: VLAN ID used on uplink interfaces (same for both primary and secondary device)\n    label: Uplink VLAN ID\n    type: string\n  primary_peer_ip:\n    description: IP address of primary router eBGP neighbour\n    label: Primary device BGP peer\n    type: string\n  secondary_peer_ip:\n    description: IP address of secondary router eBGP neighbour\n    label: Secondary device BGP peer\n    type: string\n  primary_router_id:\n    description: Primary router VRF router id\n    label: Primary router id\n    type: string\n  secondary_router_id:\n    description: Secondary router VRF router id\n    label: Secondary router id\n    type: string\n  remote_as:\n    description: eBGP remote autonomous system\n    label: Remote AS\n    type: string\n  md5:\n    description: eBGP authentication key\n    label: eBGP authentication key\n    type: string\n  bgp_group_name:\n    description: Name of eBGP group\n    label: eBGP group name\n    type: string\n  gohan_id:\n    type: string\n    label: Gohan resource ID\n    description: UUID of the VPN Interface\n  tenant_id:\n    type: string\n    label: Tenant ID\n  version:\n    type: number\n    label: Config version\n\nresources:\n{% set primary_ip_uplink_split = jinja_primary_uplink_ip.split('/') %}\n{% set secondary_ip_uplink_split = jinja_secondary_uplink_ip.split('/') %}\n{% for device in [\"primary\", \"secondary\"] %}\n  netconf_configure_{{ device }}:\n    properties:\n      lock_timeout: 3000\n      configs:\n      - config: \"\"\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: interfaces\n          - config_type: name\n            xml_type: named_tag\n            tag: interface\n            name: { get_param: {{ device }}_device_physical_interface }\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: unit\n            name: { get_param: uplink_vlan }\n          - config_type: tag\n            xml_type: tag\n            tag: family\n          - config_type: tag\n            xml_type: tag\n            tag: inet\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: address\n            name: {% if device == \"primary\" %} {{ jinja_primary_uplink_ip }} {% else %} {{ jinja_secondary_uplink_ip }} {% endif %}\n      - config:\n          str_replace:\n            params:\n              $NEIGHBOR_IP:\n                    get_param: {{ device }}_peer_ip\n              $REMOTE_AS:\n                    get_param: remote_as\n              $APPLY_GROUP:\n                    get_param: {{ device }}_ebgp_config_group\n              $KEY:\n                    get_param: md5\n            template: |\n              apply-groups $APPLY_GROUP;\n              local-address {% if device == \"primary\" %} {{ primary_ip_uplink_split[0] }} {% else %} {{ secondary_ip_uplink_split[0] }} {% endif %};\n              peer-as $REMOTE_AS;\n              neighbor $NEIGHBOR_IP authentication-key $KEY;\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: routing-instances\n          - config_type: name\n            xml_type: named_tag\n            tag: instance\n            name: { get_param: vrf_name }\n          - config_type: tag\n            xml_type: tag\n            tag: protocols\n          - config_type: tag\n            xml_type: tag\n            tag: bgp\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: group\n            name: { get_param: bgp_group_name }\n      - config:\n          str_replace:\n            params:\n              $ROUTER_ID:\n                    get_param: {{device}}_router_id\n              $LOCAL_AS:\n                    get_param: local_as\n            template: |\n              router-id $ROUTER_ID;\n              autonomous-system $LOCAL_AS;\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: routing-instances\n          - config_type: name\n            xml_type: named_tag\n            tag: instance\n            name: { get_param: vrf_name }\n          - config_type: tag\n            xml_type: tag\n            tag: routing-options\n      device_ip:\n        get_param: {{ device }}_device_ip\n      password:\n        get_param: {{ device }}_device_password\n      port:\n        get_param: {{ device }}_device_port\n      username:\n        get_param: {{ device }}_device_username\n    {% if device == \"secondary\" %}depends_on: netconf_configure_primary{% endif %}\n    type: OS::Contrail::NetconfNamedConfigs\n{% endfor %}\n\n  bgp_monitor:\n    type: ESI::Monitoring::MonitoringTarget\n    properties:\n      type: bgp_pool\n      resource_type: vpn_interfaces\n      resource_id: { get_param: gohan_id }\n      tenant_id: { get_param: tenant_id }\n      version: { get_param: version }\n      field_name: status\n      properties:\n        instance: { get_param: vrf_name }\n        primary:\n          host: { get_param: primary_device_ip }\n          port: { get_param: primary_device_port }\n          login: { get_param: primary_device_username }\n          password: { get_param: primary_device_password }\n          peer_address: { get_param: primary_peer_ip }\n        secondary:\n          host: { get_param: secondary_device_ip }\n          port: { get_param: secondary_device_port }\n          login: { get_param: secondary_device_username }\n          password: { get_param: secondary_device_password }\n          peer_address: { get_param: secondary_peer_ip }\n      syncer_properties:\n        etcd:\n          status:\n            key: status\n    depends_on: netconf_configure_secondary\n\n{% for device in [\"primary\", \"secondary\"] %}\n  {{ device }}_interface_metric_monitor:\n    type: ESI::Monitoring::MonitoringTarget\n    properties:\n      type: snmp_ports_metric\n      resource_type: vpn_interfaces\n      resource_id: { get_param: gohan_id }\n      tenant_id: { get_param: tenant_id }\n      version: { get_param: version }\n      field_name: {{ device }}_router\n      properties:\n        device_ip: { get_param: {{ device }}_device_ip }\n        if_name: { get_param: {{ device }}_device_logical_interface }\n        community_name: EDGE_ROUTER_COMMUNITY\n      syncer_properties:\n        tsdb:\n          traffic.in:\n            metric: traffic.bytes\n            tags:\n              device_index: {{ device }}\n              resource_id: { get_param: gohan_id }\n              direction: in\n          traffic.out:\n            metric: traffic.bytes\n            tags:\n              device_index: {{ device }}\n              resource_id: { get_param: gohan_id }\n              direction: out\n    depends_on: bgp_monitor\n{% endfor %}\n\noutputs:\n  monitoring_target_id:\n    description: Monitoring Target ID\n    value: { get_resource: bgp_monitor}\n  monitoring_link:\n    description: Monitoring Process Link\n    value: { get_attr: [bgp_monitor, link]}\n{% for device in [\"primary\", \"secondary\"] %}\n  {{ device }}_interface_monitoring_target_id:\n    description: Monitoring Target ID\n    value: { get_resource: {{ device }}_interface_metric_monitor}\n  {{ device }}_interface_monitoring_link:\n    description: Monitoring Process Link\n    value: { get_attr: [{{ device }}_interface_metric_monitor, link]}\n{% endfor %}\n", 
        "parameter_mappings": {
            "secondary_router_id": "Osecondary:bgp_router_id", 
            "secondary_device_physical_interface": "Fvpn_gateway+vpn_gw_id:ha_interface+uplink_interface_id:er_physical_interface+secondary_interface_id:name", 
            "primary_peer_ip": "Oprimary:bgp_peer_ip", 
            "primary_device_logical_interface": "Fvpn_gateway+vpn_gw_id:primary_logical_uplink_interface_name", 
            "primary_device_password": "Fvpn_gateway+vpn_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:password", 
            "gohan_id": "Pid", 
            "bgp_group_name": "CCloudGW1", 
            "remote_as": "Pbgp_remote_as", 
            "jinja_primary_uplink_ip": "Oprimary:ip_address", 
            "primary_device_ip": "Fvpn_gateway+vpn_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:ip", 
            "secondary_ebgp_config_group": "Fvpn_gateway+vpn_gw_id:vpn_service+vpn_service_id:secondary_ebgp_config_group", 
            "version": "Vauto_filled", 
            "secondary_device_username": "Fvpn_gateway+vpn_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:login", 
            "secondary_device_logical_interface": "Fvpn_gateway+vpn_gw_id:secondary_logical_uplink_interface_name", 
            "local_as": "Fvpn_gateway+vpn_gw_id:local_as_number", 
            "primary_device_physical_interface": "Fvpn_gateway+vpn_gw_id:ha_interface+uplink_interface_id:er_physical_interface+primary_interface_id:name", 
            "uplink_vlan": "Fvpn_gateway+vpn_gw_id:uplink_vlan_id", 
            "md5": "Pbgp_md5", 
            "secondary_peer_ip": "Osecondary:bgp_peer_ip", 
            "primary_router_id": "Oprimary:bgp_router_id", 
            "primary_ebgp_config_group": "Fvpn_gateway+vpn_gw_id:vpn_service+vpn_service_id:primary_ebgp_config_group", 
            "tenant_id": "Ptenant_id", 
            "jinja_secondary_uplink_ip": "Osecondary:ip_address", 
            "secondary_device_port": "Fvpn_gateway+vpn_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:ssh_port", 
            "secondary_device_password": "Fvpn_gateway+vpn_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:password", 
            "heat_timeout": "C60", 
            "vrf_name": "Fvpn_gateway+vpn_gw_id:vrf_name", 
            "primary_device_username": "Fvpn_gateway+vpn_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:login", 
            "primary_device_port": "Fvpn_gateway+vpn_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:ssh_port", 
            "secondary_device_ip": "Fvpn_gateway+vpn_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:ip"
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
  primary_device_logical_interface:
    description: Name of the created logical uplink interface on the Primary device
    label: Logical Interface name
    type: string
  secondary_device_logical_interface:
    description: Name of the created logical uplink interface on the Secondary device
    label: Logical Interface name
    type: string
  vrf_name:
    description: Name of VRF (routing-instance) in MX config
    label: VRF Name
    type: string
  local_as:
    type: number
    label: Local AS Number
  primary_ebgp_config_group:
    description: Name of MX config group for eBGP config
    label: eBGP config group
    type: string
  secondary_ebgp_config_group:
    description: Name of MX config group for eBGP config
    label: eBGP config group
    type: string
  uplink_vlan:
    description: VLAN ID used on uplink interfaces (same for both primary and secondary device)
    label: Uplink VLAN ID
    type: string
  primary_peer_ip:
    description: IP address of primary router eBGP neighbour
    label: Primary device BGP peer
    type: string
  secondary_peer_ip:
    description: IP address of secondary router eBGP neighbour
    label: Secondary device BGP peer
    type: string
  primary_router_id:
    description: Primary router VRF router id
    label: Primary router id
    type: string
  secondary_router_id:
    description: Secondary router VRF router id
    label: Secondary router id
    type: string
  remote_as:
    description: eBGP remote autonomous system
    label: Remote AS
    type: string
  md5:
    description: eBGP authentication key
    label: eBGP authentication key
    type: string
  bgp_group_name:
    description: Name of eBGP group
    label: eBGP group name
    type: string
  gohan_id:
    type: string
    label: Gohan resource ID
    description: UUID of the VPN Interface
  tenant_id:
    type: string
    label: Tenant ID
  version:
    type: number
    label: Config version

resources:
{% set primary_ip_uplink_split = jinja_primary_uplink_ip.split('/') %}
{% set secondary_ip_uplink_split = jinja_secondary_uplink_ip.split('/') %}
{% for device in ["primary", "secondary"] %}
  netconf_configure_{{ device }}:
    properties:
      lock_timeout: 3000
      configs:
      - config: ""
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
            name: { get_param: uplink_vlan }
          - config_type: tag
            xml_type: tag
            tag: family
          - config_type: tag
            xml_type: tag
            tag: inet
          - config_type: named_tag
            xml_type: named_tag
            tag: address
            name: {% if device == "primary" %} {{ jinja_primary_uplink_ip }} {% else %} {{ jinja_secondary_uplink_ip }} {% endif %}
      - config:
          str_replace:
            params:
              $NEIGHBOR_IP:
                    get_param: {{ device }}_peer_ip
              $REMOTE_AS:
                    get_param: remote_as
              $APPLY_GROUP:
                    get_param: {{ device }}_ebgp_config_group
              $KEY:
                    get_param: md5
            template: |
              apply-groups $APPLY_GROUP;
              local-address {% if device == "primary" %} {{ primary_ip_uplink_split[0] }} {% else %} {{ secondary_ip_uplink_split[0] }} {% endif %};
              peer-as $REMOTE_AS;
              neighbor $NEIGHBOR_IP authentication-key $KEY;
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
      - config:
          str_replace:
            params:
              $ROUTER_ID:
                    get_param: {{device}}_router_id
              $LOCAL_AS:
                    get_param: local_as
            template: |
              router-id $ROUTER_ID;
              autonomous-system $LOCAL_AS;
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
            tag: routing-options
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

  bgp_monitor:
    type: ESI::Monitoring::MonitoringTarget
    properties:
      type: bgp_pool
      resource_type: vpn_interfaces
      resource_id: { get_param: gohan_id }
      tenant_id: { get_param: tenant_id }
      version: { get_param: version }
      field_name: status
      properties:
        instance: { get_param: vrf_name }
        primary:
          host: { get_param: primary_device_ip }
          port: { get_param: primary_device_port }
          login: { get_param: primary_device_username }
          password: { get_param: primary_device_password }
          peer_address: { get_param: primary_peer_ip }
        secondary:
          host: { get_param: secondary_device_ip }
          port: { get_param: secondary_device_port }
          login: { get_param: secondary_device_username }
          password: { get_param: secondary_device_password }
          peer_address: { get_param: secondary_peer_ip }
      syncer_properties:
        etcd:
          status:
            key: status
    depends_on: netconf_configure_secondary

{% for device in ["primary", "secondary"] %}
  {{ device }}_interface_metric_monitor:
    type: ESI::Monitoring::MonitoringTarget
    properties:
      type: snmp_ports_metric
      resource_type: vpn_interfaces
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
    depends_on: bgp_monitor
{% endfor %}

outputs:
  monitoring_target_id:
    description: Monitoring Target ID
    value: { get_resource: bgp_monitor}
  monitoring_link:
    description: Monitoring Process Link
    value: { get_attr: [bgp_monitor, link]}
{% for device in ["primary", "secondary"] %}
  {{ device }}_interface_monitoring_target_id:
    description: Monitoring Target ID
    value: { get_resource: {{ device }}_interface_metric_monitor}
  {{ device }}_interface_monitoring_link:
    description: Monitoring Process Link
    value: { get_attr: [{{ device }}_interface_metric_monitor, link]}
{% endfor %}
```
