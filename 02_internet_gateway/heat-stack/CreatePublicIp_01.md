# HTTP Methods for creating heat-stack: QoS Option

Checking heat-stack of "public_ip" via heatclient.
```
$ heat stack-show public_ip_d5622781-f06a-4fad-b800-b577a05ad8b2
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                   |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                      |
| creation_time         | 2018-04-04T05:01:04Z                                                                                                                                                                    |
| description           | QoS Option                                                                                                                                                                              |
| disable_rollback      | True                                                                                                                                                                                    |
| id                    | 96d6707c-565e-4175-9690-40dfd081cf0e                                                                                                                                                    |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/06d6b792b31c40daa546fb0f4e35980d/stacks/public_ip_d5622781-f06a-4fad-b800-b577a05ad8b2/96d6707c-565e-4175-9690-40dfd081cf0e |
| notification_topics   | []                                                                                                                                                                                      |
| outputs               | []                                                                                                                                                                                      |
| parameters            | {                                                                                                                                                                                       |
|                       |   "primary_device_ip": "10.79.5.185",                                                                                                                                                   |
|                       |   "OS::stack_id": "96d6707c-565e-4175-9690-40dfd081cf0e",                                                                                                                               |
|                       |   "OS::stack_name": "public_ip_d5622781-f06a-4fad-b800-b577a05ad8b2",                                                                                                                   |
|                       |   "secondary_device_port": "830",                                                                                                                                                       |
|                       |   "secondary_device_password": "******",                                                                                                                                                |
|                       |   "ip_mask": "28",                                                                                                                                                                      |
|                       |   "primary_device_password": "******",                                                                                                                                                  |
|                       |   "ip_cidr": "203.0.112.0",                                                                                                                                                             |
|                       |   "primary_device_username": "esi",                                                                                                                                                     |
|                       |   "secondary_device_username": "esi",                                                                                                                                                   |
|                       |   "primary_device_port": "830",                                                                                                                                                         |
|                       |   "secondary_device_ip": "10.79.5.184",                                                                                                                                                 |
|                       |   "prefix_list_name": "vrf_gw_sample-ha-router-downlink_1025_prefix"                                                                                                                    |
|                       | }                                                                                                                                                                                       |
| parent                | None                                                                                                                                                                                    |
| stack_name            | public_ip_d5622781-f06a-4fad-b800-b577a05ad8b2                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                   |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                         |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                     |
| stack_user_project_id | 06d6b792b31c40daa546fb0f4e35980d                                                                                                                                                        |
| template_description  | QoS Option                                                                                                                                                                              |
| timeout_mins          | 60                                                                                                                                                                                      |
| updated_time          | None                                                                                                                                                                                    |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "public_ip" via heatclient.
```
$ heat template-show public_ip_d5622781-f06a-4fad-b800-b577a05ad8b2
description: 'QoS Option

  '
heat_template_version: '2013-05-23'
parameters:
  ip_cidr: {label: Public IP CIDR, type: string}
  ip_mask: {label: Public IP CIDR, type: string}
  prefix_list_name: {label: Prefix List name., type: string}
  primary_device_ip: {description: Ip address that will be used to establish ssh connection
      to the Primary Device., label: Ip address of the device., type: string}
  primary_device_password: {description: Password of the user which will be used to
      log onto the Primary Device., hidden: true, label: Users password., type: string}
  primary_device_port: {description: Port that will be used to establish ssh connection
      to the Primary Device., label: Port of the ssh connection., type: number}
  primary_device_username: {description: Name of the user which will be used to log
      onto the Primary Device., label: User name to log on to device., type: string}
  secondary_device_ip: {description: Ip address that will be used to establish ssh
      connection to the Secondary Device., label: Ip address of the device., type: string}
  secondary_device_password: {description: Password of the user which will be used
      to log onto the Secondary Device., hidden: true, label: Users password., type: string}
  secondary_device_port: {description: Port that will be used to establish ssh connection
      to the Secondary Device., label: Port of the ssh connection., type: number}
  secondary_device_username: {description: Name of the user which will be used to
      log onto the Secondary Device., label: User name to log on to device., type: string}
resources:
  netconf_configure_primary:
    properties:
      configs:
      - config: ''
        path:
        - {config_type: tag, tag: policy-options, xml_type: tag}
        - config_type: named_tag
          name: {get_param: prefix_list_name}
          tag: prefix-list
          xml_type: named_tag
        - config_type: name
          name:
            str_replace:
              params:
                $CIDR: {get_param: ip_cidr}
                $MASK: {get_param: ip_mask}
              template: '$CIDR/$MASK

                '
          tag: prefix-list-item
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
      - config: ''
        path:
        - {config_type: tag, tag: policy-options, xml_type: tag}
        - config_type: named_tag
          name: {get_param: prefix_list_name}
          tag: prefix-list
          xml_type: named_tag
        - config_type: name
          name:
            str_replace:
              params:
                $CIDR: {get_param: ip_cidr}
                $MASK: {get_param: ip_mask}
              template: '$CIDR/$MASK

                '
          tag: prefix-list-item
          xml_type: named_tag
      device_ip: {get_param: secondary_device_ip}
      lock_timeout: 3000
      password: {get_param: secondary_device_password}
      port: {get_param: secondary_device_port}
      username: {get_param: secondary_device_username}
    type: OS::Contrail::NetconfNamedConfigs
```
