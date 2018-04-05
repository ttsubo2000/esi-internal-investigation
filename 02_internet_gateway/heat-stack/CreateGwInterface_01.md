# HTTP Methods for creating heat-stack: Inet Address

Checking heat-stack of "gw_interface" via heatclient.
```
$ heat stack-show gw_interface_ce8831fd-d30c-41e3-95de-feaee0b95405
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                      |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                         |
| creation_time         | 2018-04-04T05:02:04Z                                                                                                                                                                       |
| description           | Inet Address                                                                                                                                                                               |
| disable_rollback      | True                                                                                                                                                                                       |
| id                    | 705f6aad-011f-4af8-800f-fc4f5417d052                                                                                                                                                       |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/06d6b792b31c40daa546fb0f4e35980d/stacks/gw_interface_ce8831fd-d30c-41e3-95de-feaee0b95405/705f6aad-011f-4af8-800f-fc4f5417d052 |
| notification_topics   | []                                                                                                                                                                                         |
| outputs               | [                                                                                                                                                                                          |
|                       |   {                                                                                                                                                                                        |
|                       |     "output_value": "921a9234-0ae4-44f5-89b0-2f68dcaaae5b",                                                                                                                                |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                 |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                   |
|                       |   },                                                                                                                                                                                       |
|                       |   {                                                                                                                                                                                        |
|                       |     "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/921a9234-0ae4-44f5-89b0-2f68dcaaae5b",                                                       |
|                       |     "description": "Monitoring Process Link",                                                                                                                                              |
|                       |     "output_key": "monitoring_link"                                                                                                                                                        |
|                       |   }                                                                                                                                                                                        |
|                       | ]                                                                                                                                                                                          |
| parameters            | {                                                                                                                                                                                          |
|                       |   "secondary_device_physical_interface": "ae0",                                                                                                                                            |
|                       |   "secondary_ibgp_config_group": "InetGW1-RI-IBGP",                                                                                                                                        |
|                       |   "primary_device_password": "******",                                                                                                                                                     |
|                       |   "secondary_device_gw_ip": "172.16.101.153",                                                                                                                                              |
|                       |   "gohan_id": "ce8831fd-d30c-41e3-95de-feaee0b95405",                                                                                                                                      |
|                       |   "bgp_group_name": "inet-gw-group",                                                                                                                                                       |
|                       |   "OS::stack_name": "gw_interface_ce8831fd-d30c-41e3-95de-feaee0b95405",                                                                                                                   |
|                       |   "gw_vip": "172.16.101.151",                                                                                                                                                              |
|                       |   "primary_device_ip": "10.79.5.185",                                                                                                                                                      |
|                       |   "version": "1",                                                                                                                                                                          |
|                       |   "secondary_device_username": "esi",                                                                                                                                                      |
|                       |   "secondary_logical_interface_name": "ae0.1025",                                                                                                                                          |
|                       |   "primary_logical_interface_name": "ae0.1025",                                                                                                                                            |
|                       |   "vlan": "1025",                                                                                                                                                                          |
|                       |   "primary_device_gw_ip": "172.16.101.152",                                                                                                                                                |
|                       |   "netmask": "24",                                                                                                                                                                         |
|                       |   "primary_device_physical_interface": "ae0",                                                                                                                                              |
|                       |   "vrrp_group": "20",                                                                                                                                                                      |
|                       |   "primary_device_priority": "105",                                                                                                                                                        |
|                       |   "OS::stack_id": "705f6aad-011f-4af8-800f-fc4f5417d052",                                                                                                                                  |
|                       |   "tenant_id": "06d6b792b31c40daa546fb0f4e35980d",                                                                                                                                         |
|                       |   "secondary_device_port": "830",                                                                                                                                                          |
|                       |   "secondary_device_password": "******",                                                                                                                                                   |
|                       |   "vrf_name": "vrf_gw_sample-ha-router-downlink_1025",                                                                                                                                     |
|                       |   "primary_device_username": "esi",                                                                                                                                                        |
|                       |   "secondary_device_priority": "100",                                                                                                                                                      |
|                       |   "primary_ibgp_config_group": "InetGW2-RI-IBGP",                                                                                                                                          |
|                       |   "primary_device_port": "830",                                                                                                                                                            |
|                       |   "secondary_device_ip": "10.79.5.184"                                                                                                                                                     |
|                       | }                                                                                                                                                                                          |
| parent                | None                                                                                                                                                                                       |
| stack_name            | gw_interface_ce8831fd-d30c-41e3-95de-feaee0b95405                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                      |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                            |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                        |
| stack_user_project_id | 06d6b792b31c40daa546fb0f4e35980d                                                                                                                                                           |
| template_description  | Inet Address                                                                                                                                                                               |
| timeout_mins          | 60                                                                                                                                                                                         |
| updated_time          | None                                                                                                                                                                                       |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "gw_interface" via heatclient.
```
$ heat template-show gw_interface_ce8831fd-d30c-41e3-95de-feaee0b95405
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
  gohan_id: {description: UUID of the GW Interface, label: Gohan resource ID, type: string}
  gw_vip: {description: Virtual IP configured on VRRP, label: Inet Address CIDR, type: string}
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
  vlan: {description: Vlan tag for mx logical interface, label: Vlan Tag, type: string}
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
          name: {get_param: vlan}
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
              $NEIGHBOR_GW_IP: {get_param: secondary_device_gw_ip}
            template: 'apply-groups $APPLY_GROUP

              local-address $DEVICE_GW_IP;

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
          name: {get_param: vlan}
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
              $NEIGHBOR_GW_IP: {get_param: primary_device_gw_ip}
            template: 'apply-groups $APPLY_GROUP

              local-address $DEVICE_GW_IP;

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
