# HTTP Methods for creating heat-stack: Inet Address

Checking heat-stack of "vpn_interface" via heatclient.
```
$ heat stack-show vpn_interface_07d4f1fc-5142-4fae-b115-627fc009e222
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                       |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                          |
| creation_time         | 2018-04-16T00:09:51Z                                                                                                                                                                        |
| description           | Inet Address                                                                                                                                                                                |
| disable_rollback      | True                                                                                                                                                                                        |
| id                    | d74ec7b4-930f-422a-a306-1695cb268680                                                                                                                                                        |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/b3e3095c0a5b4383805efe9cf2a6b5ef/stacks/vpn_interface_07d4f1fc-5142-4fae-b115-627fc009e222/d74ec7b4-930f-422a-a306-1695cb268680 |
| notification_topics   | []                                                                                                                                                                                          |
| outputs               | [                                                                                                                                                                                           |
|                       |   {                                                                                                                                                                                         |
|                       |     "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/3bdb3c86-ac6d-4ff2-aa55-4b2989971614",                                                        |
|                       |     "description": "Monitoring Process Link",                                                                                                                                               |
|                       |     "output_key": "secondary_interface_monitoring_link"                                                                                                                                     |
|                       |   },                                                                                                                                                                                        |
|                       |   {                                                                                                                                                                                         |
|                       |     "output_value": "34b9de21-40c0-46f1-afa5-787220cc5ed2",                                                                                                                                 |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                  |
|                       |     "output_key": "monitoring_target_id"                                                                                                                                                    |
|                       |   },                                                                                                                                                                                        |
|                       |   {                                                                                                                                                                                         |
|                       |     "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/d7885526-613f-4565-a3df-de89ed911e3b",                                                        |
|                       |     "description": "Monitoring Process Link",                                                                                                                                               |
|                       |     "output_key": "primary_interface_monitoring_link"                                                                                                                                       |
|                       |   },                                                                                                                                                                                        |
|                       |   {                                                                                                                                                                                         |
|                       |     "output_value": "d7885526-613f-4565-a3df-de89ed911e3b",                                                                                                                                 |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                  |
|                       |     "output_key": "primary_interface_monitoring_target_id"                                                                                                                                  |
|                       |   },                                                                                                                                                                                        |
|                       |   {                                                                                                                                                                                         |
|                       |     "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/34b9de21-40c0-46f1-afa5-787220cc5ed2",                                                        |
|                       |     "description": "Monitoring Process Link",                                                                                                                                               |
|                       |     "output_key": "monitoring_link"                                                                                                                                                         |
|                       |   },                                                                                                                                                                                        |
|                       |   {                                                                                                                                                                                         |
|                       |     "output_value": "3bdb3c86-ac6d-4ff2-aa55-4b2989971614",                                                                                                                                 |
|                       |     "description": "Monitoring Target ID",                                                                                                                                                  |
|                       |     "output_key": "secondary_interface_monitoring_target_id"                                                                                                                                |
|                       |   }                                                                                                                                                                                         |
|                       | ]                                                                                                                                                                                           |
| parameters            | {                                                                                                                                                                                           |
|                       |   "secondary_router_id": "192.168.8.6",                                                                                                                                                     |
|                       |   "secondary_device_physical_interface": "ge-0/0/1",                                                                                                                                        |
|                       |   "primary_peer_ip": "192.168.8.1",                                                                                                                                                         |
|                       |   "primary_device_logical_interface": "ge-0/0/1.122",                                                                                                                                       |
|                       |   "primary_device_password": "******",                                                                                                                                                      |
|                       |   "gohan_id": "07d4f1fc-5142-4fae-b115-627fc009e222",                                                                                                                                       |
|                       |   "bgp_group_name": "CloudGW1",                                                                                                                                                             |
|                       |   "remote_as": "9598",                                                                                                                                                                      |
|                       |   "primary_device_ip": "10.79.5.185",                                                                                                                                                       |
|                       |   "secondary_ebgp_config_group": "VPNGW2-RI-EBGP",                                                                                                                                          |
|                       |   "version": "1",                                                                                                                                                                           |
|                       |   "secondary_device_username": "esi",                                                                                                                                                       |
|                       |   "secondary_device_logical_interface": "ge-0/0/1.122",                                                                                                                                     |
|                       |   "OS::stack_name": "vpn_interface_07d4f1fc-5142-4fae-b115-627fc009e222",                                                                                                                   |
|                       |   "local_as": "65101",                                                                                                                                                                      |
|                       |   "primary_device_physical_interface": "ge-0/0/1",                                                                                                                                          |
|                       |   "uplink_vlan": "122",                                                                                                                                                                     |
|                       |   "md5": "test",                                                                                                                                                                            |
|                       |   "secondary_peer_ip": "192.168.8.5",                                                                                                                                                       |
|                       |   "primary_router_id": "192.168.8.2",                                                                                                                                                       |
|                       |   "OS::stack_id": "d74ec7b4-930f-422a-a306-1695cb268680",                                                                                                                                   |
|                       |   "primary_ebgp_config_group": "VPNGW1-RI-EBGP",                                                                                                                                            |
|                       |   "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",                                                                                                                                          |
|                       |   "secondary_device_port": "830",                                                                                                                                                           |
|                       |   "secondary_device_password": "******",                                                                                                                                                    |
|                       |   "vrf_name": "vrf_gw_sample-ha-router-downlink_1025",                                                                                                                                      |
|                       |   "primary_device_username": "esi",                                                                                                                                                         |
|                       |   "primary_device_port": "830",                                                                                                                                                             |
|                       |   "secondary_device_ip": "10.79.5.184"                                                                                                                                                      |
|                       | }                                                                                                                                                                                           |
| parent                | None                                                                                                                                                                                        |
| stack_name            | vpn_interface_07d4f1fc-5142-4fae-b115-627fc009e222                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                       |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                             |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                         |
| stack_user_project_id | b3e3095c0a5b4383805efe9cf2a6b5ef                                                                                                                                                            |
| template_description  | Inet Address                                                                                                                                                                                |
| timeout_mins          | 60                                                                                                                                                                                          |
| updated_time          | None                                                                                                                                                                                        |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "vpn_interface" via heatclient.
```
$ heat template-show vpn_interface_07d4f1fc-5142-4fae-b115-627fc009e222
description: 'Inet Address

  '
heat_template_version: '2013-05-23'
outputs:
  monitoring_link:
    description: Monitoring Process Link
    value:
      get_attr: [bgp_monitor, link]
  monitoring_target_id:
    description: Monitoring Target ID
    value: {get_resource: bgp_monitor}
  primary_interface_monitoring_link:
    description: Monitoring Process Link
    value:
      get_attr: [primary_interface_metric_monitor, link]
  primary_interface_monitoring_target_id:
    description: Monitoring Target ID
    value: {get_resource: primary_interface_metric_monitor}
  secondary_interface_monitoring_link:
    description: Monitoring Process Link
    value:
      get_attr: [secondary_interface_metric_monitor, link]
  secondary_interface_monitoring_target_id:
    description: Monitoring Target ID
    value: {get_resource: secondary_interface_metric_monitor}
parameters:
  bgp_group_name: {description: Name of eBGP group, label: eBGP group name, type: string}
  gohan_id: {description: UUID of the VPN Interface, label: Gohan resource ID, type: string}
  local_as: {label: Local AS Number, type: number}
  md5: {description: eBGP authentication key, label: eBGP authentication key, type: string}
  primary_device_ip: {description: Ip address that will be used to establish ssh connection
      to the Primary Device., label: Ip address of the device., type: string}
  primary_device_logical_interface: {description: Name of the created logical uplink
      interface on the Primary device, label: Logical Interface name, type: string}
  primary_device_password: {description: Password of the user which will be used to
      log onto the Primary Device., hidden: true, label: Users password., type: string}
  primary_device_physical_interface: {description: MX physical port on which logical
      interface will be created, label: Underlying physical interface, type: string}
  primary_device_port: {description: Port that will be used to establish ssh connection
      to the Primary Device., label: Port of the ssh connection., type: number}
  primary_device_username: {description: Name of the user which will be used to log
      onto the Primary Device., label: User name to log on to device., type: string}
  primary_ebgp_config_group: {description: Name of MX config group for eBGP config,
    label: eBGP config group, type: string}
  primary_peer_ip: {description: IP address of primary router eBGP neighbour, label: Primary
      device BGP peer, type: string}
  primary_router_id: {description: Primary router VRF router id, label: Primary router
      id, type: string}
  remote_as: {description: eBGP remote autonomous system, label: Remote AS, type: string}
  secondary_device_ip: {description: Ip address that will be used to establish ssh
      connection to the Secondary Device., label: Ip address of the device., type: string}
  secondary_device_logical_interface: {description: Name of the created logical uplink
      interface on the Secondary device, label: Logical Interface name, type: string}
  secondary_device_password: {description: Password of the user which will be used
      to log onto the Secondary Device., hidden: true, label: Users password., type: string}
  secondary_device_physical_interface: {description: MX physical port on which logical
      interface will be created, label: Underlying physical interface, type: string}
  secondary_device_port: {description: Port that will be used to establish ssh connection
      to the Secondary Device., label: Port of the ssh connection., type: number}
  secondary_device_username: {description: Name of the user which will be used to
      log onto the Secondary Device., label: User name to log on to device., type: string}
  secondary_ebgp_config_group: {description: Name of MX config group for eBGP config,
    label: eBGP config group, type: string}
  secondary_peer_ip: {description: IP address of secondary router eBGP neighbour,
    label: Secondary device BGP peer, type: string}
  secondary_router_id: {description: Secondary router VRF router id, label: Secondary
      router id, type: string}
  tenant_id: {label: Tenant ID, type: string}
  uplink_vlan: {description: VLAN ID used on uplink interfaces (same for both primary
      and secondary device), label: Uplink VLAN ID, type: string}
  version: {label: Config version, type: number}
  vrf_name: {description: Name of VRF (routing-instance) in MX config, label: VRF
      Name, type: string}
resources:
  bgp_monitor:
    depends_on: netconf_configure_secondary
    properties:
      field_name: status
      properties:
        instance: {get_param: vrf_name}
        primary:
          host: {get_param: primary_device_ip}
          login: {get_param: primary_device_username}
          password: {get_param: primary_device_password}
          peer_address: {get_param: primary_peer_ip}
          port: {get_param: primary_device_port}
        secondary:
          host: {get_param: secondary_device_ip}
          login: {get_param: secondary_device_username}
          password: {get_param: secondary_device_password}
          peer_address: {get_param: secondary_peer_ip}
          port: {get_param: secondary_device_port}
      resource_id: {get_param: gohan_id}
      resource_type: vpn_interfaces
      syncer_properties:
        etcd:
          status: {key: status}
      tenant_id: {get_param: tenant_id}
      type: bgp_pool
      version: {get_param: version}
    type: ESI::Monitoring::MonitoringTarget
  netconf_configure_primary:
    properties:
      configs:
      - config: ''
        path:
        - {config_type: tag, tag: interfaces, xml_type: tag}
        - config_type: name
          name: {get_param: primary_device_physical_interface}
          tag: interface
          xml_type: named_tag
        - config_type: named_tag
          name: {get_param: uplink_vlan}
          tag: unit
          xml_type: named_tag
        - {config_type: tag, tag: family, xml_type: tag}
        - {config_type: tag, tag: inet, xml_type: tag}
        - {config_type: named_tag, name: 192.168.8.2/30, tag: address, xml_type: named_tag}
      - config:
          str_replace:
            params:
              $APPLY_GROUP: {get_param: primary_ebgp_config_group}
              $KEY: {get_param: md5}
              $NEIGHBOR_IP: {get_param: primary_peer_ip}
              $REMOTE_AS: {get_param: remote_as}
            template: 'apply-groups $APPLY_GROUP;

              local-address  192.168.8.2 ;

              peer-as $REMOTE_AS;

              neighbor $NEIGHBOR_IP authentication-key $KEY;

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
      - config:
          str_replace:
            params:
              $LOCAL_AS: {get_param: local_as}
              $ROUTER_ID: {get_param: primary_router_id}
            template: 'router-id $ROUTER_ID;

              autonomous-system $LOCAL_AS;

              '
        path:
        - {config_type: tag, tag: routing-instances, xml_type: tag}
        - config_type: name
          name: {get_param: vrf_name}
          tag: instance
          xml_type: named_tag
        - {config_type: tag, tag: routing-options, xml_type: tag}
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
      - config: ''
        path:
        - {config_type: tag, tag: interfaces, xml_type: tag}
        - config_type: name
          name: {get_param: secondary_device_physical_interface}
          tag: interface
          xml_type: named_tag
        - config_type: named_tag
          name: {get_param: uplink_vlan}
          tag: unit
          xml_type: named_tag
        - {config_type: tag, tag: family, xml_type: tag}
        - {config_type: tag, tag: inet, xml_type: tag}
        - {config_type: named_tag, name: 192.168.8.6/30, tag: address, xml_type: named_tag}
      - config:
          str_replace:
            params:
              $APPLY_GROUP: {get_param: secondary_ebgp_config_group}
              $KEY: {get_param: md5}
              $NEIGHBOR_IP: {get_param: secondary_peer_ip}
              $REMOTE_AS: {get_param: remote_as}
            template: 'apply-groups $APPLY_GROUP;

              local-address  192.168.8.6 ;

              peer-as $REMOTE_AS;

              neighbor $NEIGHBOR_IP authentication-key $KEY;

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
      - config:
          str_replace:
            params:
              $LOCAL_AS: {get_param: local_as}
              $ROUTER_ID: {get_param: secondary_router_id}
            template: 'router-id $ROUTER_ID;

              autonomous-system $LOCAL_AS;

              '
        path:
        - {config_type: tag, tag: routing-instances, xml_type: tag}
        - config_type: name
          name: {get_param: vrf_name}
          tag: instance
          xml_type: named_tag
        - {config_type: tag, tag: routing-options, xml_type: tag}
      device_ip: {get_param: secondary_device_ip}
      lock_timeout: 3000
      password: {get_param: secondary_device_password}
      port: {get_param: secondary_device_port}
      username: {get_param: secondary_device_username}
    type: OS::Contrail::NetconfNamedConfigs
  primary_interface_metric_monitor:
    depends_on: bgp_monitor
    properties:
      field_name: primary_router
      properties:
        community_name: EDGE_ROUTER_COMMUNITY
        device_ip: {get_param: primary_device_ip}
        if_name: {get_param: primary_device_logical_interface}
      resource_id: {get_param: gohan_id}
      resource_type: vpn_interfaces
      syncer_properties:
        tsdb:
          traffic.in:
            metric: traffic.bytes
            tags:
              device_index: primary
              direction: in
              resource_id: {get_param: gohan_id}
          traffic.out:
            metric: traffic.bytes
            tags:
              device_index: primary
              direction: out
              resource_id: {get_param: gohan_id}
      tenant_id: {get_param: tenant_id}
      type: snmp_ports_metric
      version: {get_param: version}
    type: ESI::Monitoring::MonitoringTarget
  secondary_interface_metric_monitor:
    depends_on: bgp_monitor
    properties:
      field_name: secondary_router
      properties:
        community_name: EDGE_ROUTER_COMMUNITY
        device_ip: {get_param: secondary_device_ip}
        if_name: {get_param: secondary_device_logical_interface}
      resource_id: {get_param: gohan_id}
      resource_type: vpn_interfaces
      syncer_properties:
        tsdb:
          traffic.in:
            metric: traffic.bytes
            tags:
              device_index: secondary
              direction: in
              resource_id: {get_param: gohan_id}
          traffic.out:
            metric: traffic.bytes
            tags:
              device_index: secondary
              direction: out
              resource_id: {get_param: gohan_id}
      tenant_id: {get_param: tenant_id}
      type: snmp_ports_metric
      version: {get_param: version}
    type: ESI::Monitoring::MonitoringTarget
```
