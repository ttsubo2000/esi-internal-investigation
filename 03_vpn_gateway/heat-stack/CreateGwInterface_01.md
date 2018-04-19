# HTTP Methods for creating heat-stack: Inet Address

Checking heat-stack of "gw_interface" via heatclient.
```
$ heat stack-show gw_interface_3dbcfce5-bca5-4182-991a-c23de685fcf1
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                      |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                         |
| creation_time         | 2018-04-16T00:12:30Z                                                                                                                                                                       |
| description           | Inet Address                                                                                                                                                                               |
| disable_rollback      | True                                                                                                                                                                                       |
| id                    | 8be0df63-af3a-4d9c-a773-2334c72e858b                                                                                                                                                       |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/b3e3095c0a5b4383805efe9cf2a6b5ef/stacks/gw_interface_3dbcfce5-bca5-4182-991a-c23de685fcf1/8be0df63-af3a-4d9c-a773-2334c72e858b |
| notification_topics   | []                                                                                                                                                                                         |
| outputs               | [                                                                                                                                                                                          |
|                       |   {                                                                                                                                                                                        |
|                       |     "output_value": "8ac03032-a027-4965-b636-32a7b1281bfc",                                                                                                                                |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                 |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                   |
|                       |   },                                                                                                                                                                                       |
|                       |   {                                                                                                                                                                                        |
|                       |     "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/8ac03032-a027-4965-b636-32a7b1281bfc",                                                       |
|                       |     "description": "Monitoring Process Link",                                                                                                                                              |
|                       |     "output_key": "monitoring_link"                                                                                                                                                        |
|                       |   }                                                                                                                                                                                        |
|                       | ]                                                                                                                                                                                          |
| parameters            | {                                                                                                                                                                                          |
|                       |   "secondary_device_physical_interface": "ae0",                                                                                                                                            |
|                       |   "secondary_ibgp_config_group": "VPNGW2-RI-IBGP",                                                                                                                                         |
|                       |   "primary_device_password": "******",                                                                                                                                                     |
|                       |   "secondary_device_gw_ip": "172.16.101.153",                                                                                                                                              |
|                       |   "gohan_id": "3dbcfce5-bca5-4182-991a-c23de685fcf1",                                                                                                                                      |
|                       |   "bgp_group_name": "inet-gw-group",                                                                                                                                                       |
|                       |   "OS::stack_name": "gw_interface_3dbcfce5-bca5-4182-991a-c23de685fcf1",                                                                                                                   |
|                       |   "gw_vip": "172.16.101.151",                                                                                                                                                              |
|                       |   "primary_device_ip": "10.79.5.185",                                                                                                                                                      |
|                       |   "version": "1",                                                                                                                                                                          |
|                       |   "secondary_device_username": "esi",                                                                                                                                                      |
|                       |   "downlink_vlan_id": "1025",                                                                                                                                                              |
|                       |   "secondary_logical_interface_name": "ae0.1025",                                                                                                                                          |
|                       |   "primary_logical_interface_name": "ae0.1025",                                                                                                                                            |
|                       |   "local_as": "65101",                                                                                                                                                                     |
|                       |   "primary_device_gw_ip": "172.16.101.152",                                                                                                                                                |
|                       |   "netmask": "24",                                                                                                                                                                         |
|                       |   "primary_device_physical_interface": "ae0",                                                                                                                                              |
|                       |   "vrrp_group": "20",                                                                                                                                                                      |
|                       |   "primary_device_priority": "105",                                                                                                                                                        |
|                       |   "OS::stack_id": "8be0df63-af3a-4d9c-a773-2334c72e858b",                                                                                                                                  |
|                       |   "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",                                                                                                                                         |
|                       |   "secondary_device_port": "830",                                                                                                                                                          |
|                       |   "secondary_device_password": "******",                                                                                                                                                   |
|                       |   "vrf_name": "vrf_gw_sample-ha-router-downlink_1025",                                                                                                                                     |
|                       |   "primary_device_username": "esi",                                                                                                                                                        |
|                       |   "secondary_device_priority": "100",                                                                                                                                                      |
|                       |   "primary_ibgp_config_group": "VPNGW1-RI-IBGP",                                                                                                                                           |
|                       |   "primary_device_port": "830",                                                                                                                                                            |
|                       |   "secondary_device_ip": "10.79.5.184"                                                                                                                                                     |
|                       | }                                                                                                                                                                                          |
| parent                | None                                                                                                                                                                                       |
| stack_name            | gw_interface_3dbcfce5-bca5-4182-991a-c23de685fcf1                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                      |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                            |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                        |
| stack_user_project_id | b3e3095c0a5b4383805efe9cf2a6b5ef                                                                                                                                                           |
| template_description  | Inet Address                                                                                                                                                                               |
| timeout_mins          | 60                                                                                                                                                                                         |
| updated_time          | None                                                                                                                                                                                       |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "gw_interface" via heatclient.
```
$ heat template-show gw_interface_3dbcfce5-bca5-4182-991a-c23de685fcf1
description: 'Inet Address

  '
heat_template_version: '2013-05-23'
outputs:
  monitoring_link:
    description: Monitoring Process Link
    value:
      get_attr: [vrrp_monitor, link]
  monitoring_target_id:
    description: Monitoring Target ID
    value: {get_resource: vrrp_monitor}
parameters:
  bgp_group_name: {label: Name of BGP Group on VRF, type: string}
  downlink_vlan_id: {description: Vlan tag for mx logical downlink interface, label: Vlan
      Tag, type: string}
  gohan_id: {description: UUID of the GW Interface, label: Gohan resource ID, type: string}
  gw_vip: {description: Virtual IP configured on VRRP, label: Inet Address CIDR, type: string}
  local_as: {label: Local AS Number, type: string}
  netmask: {description: Netmask for gw_ip, label: Netmask, type: number}
  primary_device_gw_ip: {description: IP on primary device, label: Inet Address CIDR,
    type: string}
  primary_device_ip: {description: Ip address that will be used to establish ssh connection
      to the Primary Device., label: Ip address of the device., type: string}
  primary_device_password: {description: Password of the user which will be used to
      log onto the Primary Device., hidden: true, label: Users password., type: string}
  primary_device_physical_interface: {description: MX physical port on which logical
      interface will be created, label: Underlying physical interface, type: string}
  primary_device_port: {description: Port that will be used to establish ssh connection
      to the Primary Device., label: Port of the ssh connection., type: number}
  primary_device_priority: {label: Primary device priority, type: string}
  primary_device_username: {description: Name of the user which will be used to log
      onto the Primary Device., label: User name to log on to device., type: string}
  primary_ibgp_config_group: {description: Name for apply group to use for downlink
      interface, label: Apply group name, type: string}
  primary_logical_interface_name: {description: MX logical port, label: Underlying
      logical interface, type: string}
  secondary_device_gw_ip: {description: IP on secondary device, label: Inet Address
      CIDR, type: string}
  secondary_device_ip: {description: Ip address that will be used to establish ssh
      connection to the Secondary Device., label: Ip address of the device., type: string}
  secondary_device_password: {description: Password of the user which will be used
      to log onto the Secondary Device., hidden: true, label: Users password., type: string}
  secondary_device_physical_interface: {description: MX physical port on which logical
      interface will be created, label: Underlying physical interface, type: string}
  secondary_device_port: {description: Port that will be used to establish ssh connection
      to the Secondary Device., label: Port of the ssh connection., type: number}
  secondary_device_priority: {label: Secondary device priority, type: string}
  secondary_device_username: {description: Name of the user which will be used to
      log onto the Secondary Device., label: User name to log on to device., type: string}
  secondary_ibgp_config_group: {description: Name for apply group to use for downlink
      interface, label: Apply group name, type: string}
  secondary_logical_interface_name: {description: MX logical port, label: Underlying
      logical interface, type: string}
  tenant_id: {label: Tenant ID, type: string}
  version: {label: Config version, type: number}
  vrf_name: {label: VRF, type: string}
  vrrp_group: {label: VRRP Group, type: string}
resources:
  netconf_configure_primary:
    properties:
      configs:
      - config:
          str_replace:
            params:
              $PRIORITY: {get_param: primary_device_priority}
              $VIP: {get_param: gw_vip}
              $VRRP_GROUP: {get_param: vrrp_group}
            template: "vrrp-group $VRRP_GROUP {\n    virtual-address $VIP;\n    priority\
              \ $PRIORITY;\n}\n"
        path:
        - {config_type: tag, tag: interfaces, xml_type: tag}
        - config_type: name
          name: {get_param: primary_device_physical_interface}
          tag: interface
          xml_type: named_tag
        - config_type: named_tag
          name: {get_param: downlink_vlan_id}
          tag: unit
          xml_type: named_tag
        - {config_type: tag, tag: family, xml_type: tag}
        - {config_type: tag, tag: inet, xml_type: tag}
        - config_type: named_tag
          name:
            str_replace:
              params:
                $DEVICE_IP: {get_param: primary_device_gw_ip}
                $NETMASK: {get_param: netmask}
              template: '$DEVICE_IP/$NETMASK

                '
          tag: address
          xml_type: named_tag
      - config:
          str_replace:
            params:
              $APPLY_GROUP: {get_param: primary_ibgp_config_group}
              $DEVICE_GW_IP: {get_param: primary_device_gw_ip}
              $LOCAL_AS: {get_param: local_as}
              $NEIGHBOR_GW_IP: {get_param: secondary_device_gw_ip}
            template: 'apply-groups $APPLY_GROUP;

              local-address $DEVICE_GW_IP;

              peer-as $LOCAL_AS;

              neighbor $NEIGHBOR_GW_IP;

              '
        path:
        - {config_type: tag, tag: routing-instances, xml_type: tag}
        - config_type: name
          name: {get_param: vrf_name}
          tag: instance
          xml_type: named_tag
        - {config_type: tag, tag: protocols, xml_type: tag}
        - {config_type: tag, tag: bgp, xml_type: tag}
        - config_type: named_tag
          name: {get_param: bgp_group_name}
          tag: group
          xml_type: named_tag
      device_ip: {get_param: primary_device_ip}
      lock_timeout: 3000
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
              $PRIORITY: {get_param: secondary_device_priority}
              $VIP: {get_param: gw_vip}
              $VRRP_GROUP: {get_param: vrrp_group}
            template: "vrrp-group $VRRP_GROUP {\n    virtual-address $VIP;\n    priority\
              \ $PRIORITY;\n}\n"
        path:
        - {config_type: tag, tag: interfaces, xml_type: tag}
        - config_type: name
          name: {get_param: secondary_device_physical_interface}
          tag: interface
          xml_type: named_tag
        - config_type: named_tag
          name: {get_param: downlink_vlan_id}
          tag: unit
          xml_type: named_tag
        - {config_type: tag, tag: family, xml_type: tag}
        - {config_type: tag, tag: inet, xml_type: tag}
        - config_type: named_tag
          name:
            str_replace:
              params:
                $DEVICE_IP: {get_param: secondary_device_gw_ip}
                $NETMASK: {get_param: netmask}
              template: '$DEVICE_IP/$NETMASK

                '
          tag: address
          xml_type: named_tag
      - config:
          str_replace:
            params:
              $APPLY_GROUP: {get_param: secondary_ibgp_config_group}
              $DEVICE_GW_IP: {get_param: secondary_device_gw_ip}
              $LOCAL_AS: {get_param: local_as}
              $NEIGHBOR_GW_IP: {get_param: primary_device_gw_ip}
            template: 'apply-groups $APPLY_GROUP;

              local-address $DEVICE_GW_IP;

              peer-as $LOCAL_AS;

              neighbor $NEIGHBOR_GW_IP;

              '
        path:
        - {config_type: tag, tag: routing-instances, xml_type: tag}
        - config_type: name
          name: {get_param: vrf_name}
          tag: instance
          xml_type: named_tag
        - {config_type: tag, tag: protocols, xml_type: tag}
        - {config_type: tag, tag: bgp, xml_type: tag}
        - config_type: named_tag
          name: {get_param: bgp_group_name}
          tag: group
          xml_type: named_tag
      device_ip: {get_param: secondary_device_ip}
      lock_timeout: 3000
      password: {get_param: secondary_device_password}
      port: {get_param: secondary_device_port}
      username: {get_param: secondary_device_username}
    type: OS::Contrail::NetconfNamedConfigs
  vrrp_monitor:
    depends_on: netconf_configure_secondary
    properties:
      field_name: status
      properties:
        primary:
          host: {get_param: primary_device_ip}
          interface: {get_param: primary_logical_interface_name}
          login: {get_param: primary_device_username}
          password: {get_param: primary_device_password}
          port: {get_param: primary_device_port}
        secondary:
          host: {get_param: secondary_device_ip}
          interface: {get_param: secondary_logical_interface_name}
          login: {get_param: secondary_device_username}
          password: {get_param: secondary_device_password}
          port: {get_param: secondary_device_port}
        vrid:
        - {get_param: vrrp_group}
      resource_id: {get_param: gohan_id}
      resource_type: gw_interfaces
      syncer_properties:
        etcd:
          hold_options:
            positive_status: {primary: MASTER, secondary: BACKUP}
            time_seconds: 360
          status: {key: status}
      tenant_id: {get_param: tenant_id}
      type: vrrp_pool
      version: {get_param: version}
    type: ESI::Monitoring::MonitoringTarget
```
