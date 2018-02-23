# HTTP Methods for creating heat-stack: QoS Option

Checking heat-stack of "qos_option" via heatclient.
```
$ heat stack-show qos_option_eb82e824-a043-41cd-bf7e-caed6a2f9711
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                               |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                                  |
| creation_time         | 2017-01-08T08:00:39Z                                                                                                                                                                                |
| description           | QoS Option                                                                                                                                                                                          |
| disable_rollback      | True                                                                                                                                                                                                |
| id                    | 8ab165f6-f530-4f93-9034-41b09e3a9461                                                                                                                                                                |
| links                 | http://heat-api:8004/v1/0b576f6f4cbf414f829cd12f008bf08f/stacks/qos_option_eb82e824-a043-41cd-bf7e-caed6a2f9711/8ab165f6-f530-4f93-9034-41b09e3a9461 (self)                                         |
| notification_topics   | []                                                                                                                                                                                                  |
| outputs               | []                                                                                                                                                                                                  |
| parameters            | {                                                                                                                                                                                                   |
|                       |   "primary_device_ip": "172.23.16.66",                                                                                                                                                              |
|                       |   "OS::stack_id": "8ab165f6-f530-4f93-9034-41b09e3a9461",                                                                                                                                           |
|                       |   "OS::stack_name": "qos_option_eb82e824-a043-41cd-bf7e-caed6a2f9711",                                                                                                                              |
|                       |   "incoming_policer_name": "1G-GA-UP-VPN",                                                                                                                                                          |
|                       |   "secondary_device_port": "830",                                                                                                                                                                   |
|                       |   "secondary_device_password": "esiesi0000",                                                                                                                                                        |
|                       |   "primary_device_password": "esiesi0000",                                                                                                                                                          |
|                       |   "outgoing_policer_config": "if-exceeding { bandwidth-limit 1g; burst-size-limit 187500000; } then discard;",                                                                                      |
|                       |   "primary_device_username": "esi",                                                                                                                                                                 |
|                       |   "outgoing_policer_name": "1G-GA-DOWN-VPN",                                                                                                                                                        |
|                       |   "neighbour_prefix": "BGP-VIRTUAL-ROUTER-PEERS",                                                                                                                                                   |
|                       |   "secondary_device_username": "esi",                                                                                                                                                               |
|                       |   "primary_device_port": "830",                                                                                                                                                                     |
|                       |   "secondary_device_ip": "172.23.16.65",                                                                                                                                                            |
|                       |   "incoming_policer_config": "action { loss-priority high then discard; } single-rate { color-blind; committed-information-rate 1g; committed-burst-size 187500000; excess-burst-size 187500000; }" |
|                       | }                                                                                                                                                                                                   |
| parent                | None                                                                                                                                                                                                |
| stack_name            | qos_option_eb82e824-a043-41cd-bf7e-caed6a2f9711                                                                                                                                                     |
| stack_owner           | admin                                                                                                                                                                                               |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                                     |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                                 |
| stack_user_project_id | 0b576f6f4cbf414f829cd12f008bf08f                                                                                                                                                                    |
| template_description  | QoS Option                                                                                                                                                                                          |
| timeout_mins          | 60                                                                                                                                                                                                  |
| updated_time          | None                                                                                                                                                                                                |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "qos_option" via heatclient.
```
$ heat template-show qos_option_eb82e824-a043-41cd-bf7e-caed6a2f9711
description: 'QoS Option

  '
heat_template_version: '2013-05-23'
parameters:
  incoming_policer_config: {description: Configuration of incoming policer, label: Incoming
      policer config, type: string}
  incoming_policer_name: {description: Name of created incoming policer, label: Incoming
      policer name, type: string}
  neighbour_prefix: {description: Name of prefix list used to specify traffic source/destination,
    label: Neighbour prefix, type: string}
  outgoing_policer_config: {description: Configuration of outgoing policer, label: Outgoing
      policer config, type: string}
  outgoing_policer_name: {description: Name of created outgoing policer, label: Outgoing
      policer name, type: string}
  primary_device_ip: {description: Ip address that will be used to establish ssh connection
      to the Primary Device., label: Ip address of the device., type: string}
  primary_device_password: {description: Password of the user which will be used to
      log onto the Primary Device., label: Users password., type: string}
  primary_device_port: {description: Port that will be used to establish ssh connection
      to the Primary Device., label: Port of the ssh connection., type: number}
  primary_device_username: {description: Name of the user which will be used to log
      onto the Primary Device., label: User name to log on to device., type: string}
  secondary_device_ip: {description: Ip address that will be used to establish ssh
      connection to the Secondary Device., label: Ip address of the device., type: string}
  secondary_device_password: {description: Password of the user which will be used
      to log onto the Secondary Device., label: Users password., type: string}
  secondary_device_port: {description: Port that will be used to establish ssh connection
      to the Secondary Device., label: Port of the ssh connection., type: number}
  secondary_device_username: {description: Name of the user which will be used to
      log onto the Secondary Device., label: User name to log on to device., type: string}
resources:
  netconf_configure_primary:
    properties:
      configs:
      - config: {get_param: incoming_policer_config}
        path:
        - {config_type: tag, tag: firewall, xml_type: tag}
        - config_type: named_tag
          name: {get_param: incoming_policer_name}
          tag: three-color-policer
          xml_type: named_tag
      - config: {get_param: outgoing_policer_config}
        path:
        - {config_type: tag, tag: firewall, xml_type: tag}
        - config_type: named_tag
          name: {get_param: outgoing_policer_name}
          tag: policer
          xml_type: named_tag
      - config:
          str_replace:
            params:
              $CLASS: FC-VPN-GA
              $POLICER_NAME: {get_param: incoming_policer_name}
              $PREFIX: {get_param: neighbour_prefix}
            template: "term bgp-accept {\n    from {\n        source-prefix-list {\n\
              \            $PREFIX;\n        }\n        protocol tcp;\n        port\
              \ bgp;\n    }\n    then accept;\n}\nterm vrrp-accept {\n    from {\n\
              \        source-prefix-list {\n            $PREFIX;\n        }\n   \
              \     protocol vrrp;\n    }\n    then accept;\n}\nterm qos {\n    then\
              \ {\n        three-color-policer {\n            single-rate $POLICER_NAME;\n\
              \        }\n        forwarding-class $CLASS;\n        accept;\n    }\n\
              }\n"
        path:
        - {config_type: tag, tag: firewall, xml_type: tag}
        - config_type: named_tag
          name:
            str_replace:
              params:
                $NAME: {get_param: incoming_policer_name}
              template: 'FILTER_$NAME

                '
          tag: filter
          xml_type: named_tag
      - config:
          str_replace:
            params:
              $POLICER_NAME: {get_param: outgoing_policer_name}
              $PREFIX: {get_param: neighbour_prefix}
            template: "term bgp-accept {\n    from {\n        destination-prefix-list\
              \ {\n            $PREFIX;\n        }\n        protocol tcp;\n      \
              \  port bgp;\n    }\n    then accept;\n}\nterm vrrp-accept {\n    from\
              \ {\n        protocol vrrp;\n    }\n    then accept;\n}\nterm policer\
              \ {\n    then {\n        policer $POLICER_NAME;\n        accept;\n \
              \   }\n}\n"
        path:
        - {config_type: tag, tag: firewall, xml_type: tag}
        - config_type: named_tag
          name:
            str_replace:
              params:
                $NAME: {get_param: outgoing_policer_name}
              template: 'FILTER_$NAME

                '
          tag: filter
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
      - config: {get_param: incoming_policer_config}
        path:
        - {config_type: tag, tag: firewall, xml_type: tag}
        - config_type: named_tag
          name: {get_param: incoming_policer_name}
          tag: three-color-policer
          xml_type: named_tag
      - config: {get_param: outgoing_policer_config}
        path:
        - {config_type: tag, tag: firewall, xml_type: tag}
        - config_type: named_tag
          name: {get_param: outgoing_policer_name}
          tag: policer
          xml_type: named_tag
      - config:
          str_replace:
            params:
              $CLASS: FC-VPN-GA
              $POLICER_NAME: {get_param: incoming_policer_name}
              $PREFIX: {get_param: neighbour_prefix}
            template: "term bgp-accept {\n    from {\n        source-prefix-list {\n\
              \            $PREFIX;\n        }\n        protocol tcp;\n        port\
              \ bgp;\n    }\n    then accept;\n}\nterm vrrp-accept {\n    from {\n\
              \        source-prefix-list {\n            $PREFIX;\n        }\n   \
              \     protocol vrrp;\n    }\n    then accept;\n}\nterm qos {\n    then\
              \ {\n        three-color-policer {\n            single-rate $POLICER_NAME;\n\
              \        }\n        forwarding-class $CLASS;\n        accept;\n    }\n\
              }\n"
        path:
        - {config_type: tag, tag: firewall, xml_type: tag}
        - config_type: named_tag
          name:
            str_replace:
              params:
                $NAME: {get_param: incoming_policer_name}
              template: 'FILTER_$NAME

                '
          tag: filter
          xml_type: named_tag
      - config:
          str_replace:
            params:
              $POLICER_NAME: {get_param: outgoing_policer_name}
              $PREFIX: {get_param: neighbour_prefix}
            template: "term bgp-accept {\n    from {\n        destination-prefix-list\
              \ {\n            $PREFIX;\n        }\n        protocol tcp;\n      \
              \  port bgp;\n    }\n    then accept;\n}\nterm vrrp-accept {\n    from\
              \ {\n        protocol vrrp;\n    }\n    then accept;\n}\nterm policer\
              \ {\n    then {\n        policer $POLICER_NAME;\n        accept;\n \
              \   }\n}\n"
        path:
        - {config_type: tag, tag: firewall, xml_type: tag}
        - config_type: named_tag
          name:
            str_replace:
              params:
                $NAME: {get_param: outgoing_policer_name}
              template: 'FILTER_$NAME

                '
          tag: filter
          xml_type: named_tag
      device_ip: {get_param: secondary_device_ip}
      lock_timeout: 3000
      password: {get_param: secondary_device_password}
      port: {get_param: secondary_device_port}
      username: {get_param: secondary_device_username}
    type: OS::Contrail::NetconfNamedConfigs
```
