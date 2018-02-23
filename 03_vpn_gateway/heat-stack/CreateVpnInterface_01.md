# HTTP Methods for creating heat-stack: Inet Address

Checking heat-stack of "vpn_interface" via heatclient.
```
$ heat stack-show vpn_interface_0bea303d-b6eb-4edc-83ef-e32f915d3047
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                          |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                             |
| creation_time         | 2017-05-11T05:00:42Z                                                                                                                                           |
| description           | Inet Address                                                                                                                                                   |
| disable_rollback      | True                                                                                                                                                           |
| id                    | 8d6c9985-ee1d-4fe5-9b4f-963a5758a76a                                                                                                                           |
| links                 | http://heat-api:8004/v1/0b576f6f4cbf414f829cd12f008bf08f/stacks/vpn_interface_0bea303d-b6eb-4edc-83ef-e32f915d3047/8d6c9985-ee1d-4fe5-9b4f-963a5758a76a (self) |
| notification_topics   | []                                                                                                                                                             |
| outputs               | []                                                                                                                                                             |
| parameters            | {                                                                                                                                                              |
|                       |   "secondary_router_id": "192.168.8.6",                                                                                                                        |
|                       |   "secondary_device_physical_interface": "ge-0/0/1",                                                                                                           |
|                       |   "primary_peer_ip": "192.168.8.1",                                                                                                                            |
|                       |   "primary_device_password": "esiesi0000",                                                                                                                     |
|                       |   "bgp_group_name": "CloudGW1",                                                                                                                                |
|                       |   "remote_as": "9598",                                                                                                                                         |
|                       |   "primary_device_ip": "10.79.5.185",                                                                                                                          |
|                       |   "secondary_ebgp_config_group": "VPNGW2-RI-EBGP",                                                                                                             |
|                       |   "secondary_device_username": "esi",                                                                                                                          |
|                       |   "OS::stack_name": "vpn_interface_0bea303d-b6eb-4edc-83ef-e32f915d3047",                                                                                      |
|                       |   "local_as": "65101",                                                                                                                                         |
|                       |   "primary_device_physical_interface": "ge-0/0/1",                                                                                                             |
|                       |   "uplink_vlan": "122",                                                                                                                                        |
|                       |   "md5": "test",                                                                                                                                               |
|                       |   "secondary_peer_ip": "192.168.8.5",                                                                                                                          |
|                       |   "primary_router_id": "192.168.8.2",                                                                                                                          |
|                       |   "OS::stack_id": "8d6c9985-ee1d-4fe5-9b4f-963a5758a76a",                                                                                                      |
|                       |   "primary_ebgp_config_group": "VPNGW1-RI-EBGP",                                                                                                               |
|                       |   "secondary_device_port": "830",                                                                                                                              |
|                       |   "secondary_device_password": "esiesi0000",                                                                                                                   |
|                       |   "vrf_name": "vrf_gw_sample-ha-router-downlink_1025",                                                                                                         |
|                       |   "primary_device_username": "esi",                                                                                                                            |
|                       |   "primary_device_port": "830",                                                                                                                                |
|                       |   "secondary_device_ip": "10.79.5.184"                                                                                                                         |
|                       | }                                                                                                                                                              |
| parent                | None                                                                                                                                                           |
| stack_name            | vpn_interface_0bea303d-b6eb-4edc-83ef-e32f915d3047                                                                                                             |
| stack_owner           | admin                                                                                                                                                          |
| stack_status          | CREATE_COMPLETE                                                                                                                                                |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                            |
| stack_user_project_id | 0b576f6f4cbf414f829cd12f008bf08f                                                                                                                               |
| template_description  | Inet Address                                                                                                                                                   |
| timeout_mins          | 60                                                                                                                                                             |
| updated_time          | None                                                                                                                                                           |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "vpn_interface" via heatclient.
```
$ heat template-show vpn_interface_0bea303d-b6eb-4edc-83ef-e32f915d3047
description: 'Inet Address

  '
heat_template_version: '2013-05-23'
parameters:
  bgp_group_name: {description: Name of eBGP group, label: eBGP group name, type: string}
  local_as: {label: Local AS Number, type: number}
  md5: {description: eBGP authentication key, label: eBGP authentication key, type: string}
  primary_device_ip: {description: Ip address that will be used to establish ssh connection
      to the Primary Device., label: Ip address of the device., type: string}
  primary_device_password: {description: Password of the user which will be used to
      log onto the Primary Device., label: Users password., type: string}
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
  secondary_device_password: {description: Password of the user which will be used
      to log onto the Secondary Device., label: Users password., type: string}
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
  uplink_vlan: {description: VLAN ID used on uplink interfaces (same for both primary
      and secondary device), label: Uplink VLAN ID, type: string}
  vrf_name: {description: Name of VRF (routing-instance) in MX config, label: VRF
      Name, type: string}
resources:
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
```
