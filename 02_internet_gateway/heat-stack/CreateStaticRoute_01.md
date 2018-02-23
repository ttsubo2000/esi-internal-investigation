# HTTP Methods for creating heat-stack: Internet Gateway Static Route

Checking heat-stack of "static_route" via heatclient.
```
$ heat stack-show static_route_3ecf06a5-014e-48b0-841c-6ad812e69132
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                         |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                            |
| creation_time         | 2017-01-08T12:40:22Z                                                                                                                                          |
| description           | Internet Gateway Static Route                                                                                                                                 |
| disable_rollback      | True                                                                                                                                                          |
| id                    | 4bc09665-1557-41b3-a9ad-621d49276980                                                                                                                          |
| links                 | http://heat-api:8004/v1/0b576f6f4cbf414f829cd12f008bf08f/stacks/static_route_3ecf06a5-014e-48b0-841c-6ad812e69132/4bc09665-1557-41b3-a9ad-621d49276980 (self) |
| notification_topics   | []                                                                                                                                                            |
| outputs               | []                                                                                                                                                            |
| parameters            | {                                                                                                                                                             |
|                       |   "primary_device_ip": "172.23.16.66",                                                                                                                        |
|                       |   "OS::stack_id": "4bc09665-1557-41b3-a9ad-621d49276980",                                                                                                     |
|                       |   "OS::stack_name": "static_route_3ecf06a5-014e-48b0-841c-6ad812e69132",                                                                                      |
|                       |   "route": "203.0.112.0/28",                                                                                                                                  |
|                       |   "secondary_device_port": "830",                                                                                                                             |
|                       |   "secondary_device_password": "esiesi0000",                                                                                                                  |
|                       |   "primary_device_password": "esiesi0000",                                                                                                                    |
|                       |   "next_hop": "172.16.101.1",                                                                                                                                 |
|                       |   "vrf_name": "vrf_gw_sample-ha-router-downlink_1025",                                                                                                        |
|                       |   "primary_device_username": "esi",                                                                                                                           |
|                       |   "primary_device_port": "830",                                                                                                                               |
|                       |   "secondary_device_ip": "172.23.16.65",                                                                                                                      |
|                       |   "secondary_device_username": "esi"                                                                                                                          |
|                       | }                                                                                                                                                             |
| parent                | None                                                                                                                                                          |
| stack_name            | static_route_3ecf06a5-014e-48b0-841c-6ad812e69132                                                                                                             |
| stack_owner           | admin                                                                                                                                                         |
| stack_status          | CREATE_COMPLETE                                                                                                                                               |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                           |
| stack_user_project_id | 0b576f6f4cbf414f829cd12f008bf08f                                                                                                                              |
| template_description  | Internet Gateway Static Route                                                                                                                                 |
| timeout_mins          | 60                                                                                                                                                            |
| updated_time          | None                                                                                                                                                          |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "static_route" via heatclient.
```
$ heat template-show static_route_3ecf06a5-014e-48b0-841c-6ad812e69132
description: 'Internet Gateway Static Route

  '
heat_template_version: '2013-05-23'
parameters:
  next_hop: {description: Next hop for the static route, label: Next hop, type: string}
  primary_device_ip: {description: Ip address that will be used to establish ssh connection
      to the Primary Device., label: Ip address of the device., type: string}
  primary_device_password: {description: Password of the user which will be used to
      log onto the Primary Device., label: Users password., type: string}
  primary_device_port: {description: Port that will be used to establish ssh connection
      to the Primary Device., label: Port of the ssh connection., type: number}
  primary_device_username: {description: Name of the user which will be used to log
      onto the Primary Device., label: User name to log on to device., type: string}
  route: {description: Static Route definition, label: Route, type: string}
  secondary_device_ip: {description: Ip address that will be used to establish ssh
      connection to the Secondary Device., label: Ip address of the device., type: string}
  secondary_device_password: {description: Password of the user which will be used
      to log onto the Secondary Device., label: Users password., type: string}
  secondary_device_port: {description: Port that will be used to establish ssh connection
      to the Secondary Device., label: Port of the ssh connection., type: number}
  secondary_device_username: {description: Name of the user which will be used to
      log onto the Secondary Device., label: User name to log on to device., type: string}
  vrf_name: {description: Name of VRF to add this static route, label: VRF, type: string}
resources:
  netconf_configure_primary:
    properties:
      configs:
      - config:
          str_replace:
            params:
              $NEXT_HOP: {get_param: next_hop}
            template: 'next-hop $NEXT_HOP;

              '
        path:
        - {config_type: tag, tag: routing-instances, xml_type: tag}
        - config_type: name
          name: {get_param: vrf_name}
          tag: instance
          xml_type: named_tag
        - {config_type: tag, tag: routing-options, xml_type: tag}
        - {config_type: tag, tag: static, xml_type: tag}
        - config_type: named_tag
          name: {get_param: route}
          tag: route
          xml_type: named_tag
      device_ip: {get_param: primary_device_ip}
      lock_timeout: 3000
      password: {get_param: primary_device_password}
      port: {get_param: primary_device_port}
      username: {get_param: primary_device_username}
    type: OS::Contrail::NetconfNamedConfigs
  netconf_configure_secondary:
    properties:
      configs:
      - config:
          str_replace:
            params:
              $NEXT_HOP: {get_param: next_hop}
            template: 'next-hop $NEXT_HOP;

              '
        path:
        - {config_type: tag, tag: routing-instances, xml_type: tag}
        - config_type: name
          name: {get_param: vrf_name}
          tag: instance
          xml_type: named_tag
        - {config_type: tag, tag: routing-options, xml_type: tag}
        - {config_type: tag, tag: static, xml_type: tag}
        - config_type: named_tag
          name: {get_param: route}
          tag: route
          xml_type: named_tag
      device_ip: {get_param: secondary_device_ip}
      lock_timeout: 3000
      password: {get_param: secondary_device_password}
      port: {get_param: secondary_device_port}
      username: {get_param: secondary_device_username}
    type: OS::Contrail::NetconfNamedConfigs
```
