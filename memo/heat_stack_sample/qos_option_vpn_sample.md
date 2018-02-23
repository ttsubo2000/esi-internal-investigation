## Sample of heat-stack of qos_option(vpn)

* Checking heat-stack of qos_option in heat-engine
```
$ openstack stack show qos_option_021a6fd0-d44e-41c6-9ebe-a98afd82d854
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                 | Value                                                                                                                                                            |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| id                    | 1f2951fe-ae97-403c-9186-e30dd8e95355                                                                                                                             |
| stack_name            | qos_option_021a6fd0-d44e-41c6-9ebe-a98afd82d854                                                                                                                  |
| description           | QoS Option                                                                                                                                                       |
|                       |                                                                                                                                                                  |
| creation_time         | 2016-11-07T10:17:16Z                                                                                                                                             |
| updated_time          | None                                                                                                                                                             |
| stack_status          | CREATE_COMPLETE                                                                                                                                                  |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                              |
| parameters            | OS::stack_id: 1f2951fe-ae97-403c-9186-e30dd8e95355                                                                                                               |
|                       | OS::stack_name: qos_option_021a6fd0-d44e-41c6-9ebe-a98afd82d854                                                                                                  |
|                       | incoming_policer_config: action { loss-priority high then discard; } two-rate { color-blind;                                                                     |
|                       |   committed-information-rate 500k; committed-burst-size 93750; peak-information-rate                                                                             |
|                       |   10m; peak-burst-size 1875000; }                                                                                                                                |
|                       | incoming_policer_name: 10M-BE-UP_VPN-F13                                                                                                                         |
|                       | neighbour_prefix: BGP-VIRTUAL-ROUTER-PEERS                                                                                                                       |
|                       | outgoing_policer_config: if-exceeding { bandwidth-limit 10m; burst-size-limit 1875000;                                                                           |
|                       |   } then discard;                                                                                                                                                |
|                       | outgoing_policer_name: 10M-BE-DOWN_VPN-F13                                                                                                                       |
|                       | primary_device_ip: 172.23.16.41                                                                                                                                  |
|                       | primary_device_password: esiesi01                                                                                                                                |
|                       | primary_device_port: '830'                                                                                                                                       |
|                       | primary_device_username: esi                                                                                                                                     |
|                       | secondary_device_ip: 172.23.16.42                                                                                                                                |
|                       | secondary_device_password: esiesi01                                                                                                                              |
|                       | secondary_device_port: '830'                                                                                                                                     |
|                       | secondary_device_username: esi                                                                                                                                   |
|                       |                                                                                                                                                                  |
| outputs               | []                                                                                                                                                               |
|                       |                                                                                                                                                                  |
| links                 | - href: http://172.23.16.51:8004/v1/a367ed245222497db761a6c0becacab0/stacks/qos_option_021a6fd0-d44e-41c6-9ebe-a98afd82d854/1f2951fe-ae97-403c-9186-e30dd8e95355 |
|                       |   rel: self                                                                                                                                                      |
|                       |                                                                                                                                                                  |
| parent                | None                                                                                                                                                             |
| disable_rollback      | True                                                                                                                                                             |
| stack_user_project_id | a367ed245222497db761a6c0becacab0                                                                                                                                 |
| stack_owner           | sdp_esi_admin                                                                                                                                                    |
| capabilities          | []                                                                                                                                                               |
| notification_topics   | []                                                                                                                                                               |
| timeout_mins          | 60                                                                                                                                                               |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

* Checking heat-template of qos_option in heat-engine
```
$ openstack stack template show qos_option_021a6fd0-d44e-41c6-9ebe-a98afd82d854
description: 'QoS Option

  '
heat_template_version: '2013-05-23'
parameters:
  incoming_policer_config:
    description: Configuration of incoming policer
    label: Incoming policer config
    type: string
  incoming_policer_name:
    description: Name of created incoming policer
    label: Incoming policer name
    type: string
  neighbour_prefix:
    description: Name of prefix list used to specify traffic source/destination
    label: Neighbour prefix
    type: string
  outgoing_policer_config:
    description: Configuration of outgoing policer
    label: Outgoing policer config
    type: string
  outgoing_policer_name:
    description: Name of created outgoing policer
    label: Outgoing policer name
    type: string
  primary_device_ip:
    description: Ip address that will be used to establish ssh connection to the Primary
      Device.
    label: Ip address of the device.
    type: string
  primary_device_password:
    description: Password of the user which will be used to log onto the Primary Device.
    label: Users password.
    type: string
  primary_device_port:
    description: Port that will be used to establish ssh connection to the Primary
      Device.
    label: Port of the ssh connection.
    type: number
  primary_device_username:
    description: Name of the user which will be used to log onto the Primary Device.
    label: User name to log on to device.
    type: string
  secondary_device_ip:
    description: Ip address that will be used to establish ssh connection to the Secondary
      Device.
    label: Ip address of the device.
    type: string
  secondary_device_password:
    description: Password of the user which will be used to log onto the Secondary
      Device.
    label: Users password.
    type: string
  secondary_device_port:
    description: Port that will be used to establish ssh connection to the Secondary
      Device.
    label: Port of the ssh connection.
    type: number
  secondary_device_username:
    description: Name of the user which will be used to log onto the Secondary Device.
    label: User name to log on to device.
    type: string
resources:
  netconf_configure_primary:
    properties:
      configs:
      - config:
          get_param: incoming_policer_config
        path:
        - config_type: tag
          tag: firewall
          xml_type: tag
        - config_type: named_tag
          name:
            get_param: incoming_policer_name
          tag: three-color-policer
          xml_type: named_tag
      - config:
          get_param: outgoing_policer_config
        path:
        - config_type: tag
          tag: firewall
          xml_type: tag
        - config_type: named_tag
          name:
            get_param: outgoing_policer_name
          tag: policer
          xml_type: named_tag
      - config:
          str_replace:
            params:
              $CLASS: FC-VPN-BE
              $POLICER_NAME:
                get_param: incoming_policer_name
              $PREFIX:
                get_param: neighbour_prefix
            template: "term bgp-accept {\n    from {\n        source-prefix-list {\n\
              \            $PREFIX;\n        }\n        protocol tcp;\n        port\
              \ bgp;\n    }\n    then accept;\n}\nterm vrrp-accept {\n    from {\n\
              \        source-prefix-list {\n            $PREFIX;\n        }\n   \
              \     protocol vrrp;\n    }\n    then accept;\n}\nterm qos {\n    then\
              \ {\n        three-color-policer {\n            two-rate $POLICER_NAME;\n\
              \        }\n        forwarding-class $CLASS;\n        accept;\n    }\n\
              }\n"
        path:
        - config_type: tag
          tag: firewall
          xml_type: tag
        - config_type: named_tag
          name:
            str_replace:
              params:
                $NAME:
                  get_param: incoming_policer_name
              template: 'FILTER_$NAME

                '
          tag: filter
          xml_type: named_tag
      - config:
          str_replace:
            params:
              $POLICER_NAME:
                get_param: outgoing_policer_name
              $PREFIX:
                get_param: neighbour_prefix
            template: "term bgp-accept {\n    from {\n        destination-prefix-list\
              \ {\n            $PREFIX;\n        }\n        protocol tcp;\n      \
              \  port bgp;\n    }\n    then accept;\n}\nterm vrrp-accept {\n    from\
              \ {\n        protocol vrrp;\n    }\n    then accept;\n}\nterm policer\
              \ {\n    then {\n        policer $POLICER_NAME;\n        accept;\n \
              \   }\n}\n"
        path:
        - config_type: tag
          tag: firewall
          xml_type: tag
        - config_type: named_tag
          name:
            str_replace:
              params:
                $NAME:
                  get_param: outgoing_policer_name
              template: 'FILTER_$NAME

                '
          tag: filter
          xml_type: named_tag
      device_ip:
        get_param: primary_device_ip
      lock_timeout: 3000
      password:
        get_param: primary_device_password
      port:
        get_param: primary_device_port
      username:
        get_param: primary_device_username
    type: OS::Contrail::NetconfNamedConfigs
  netconf_configure_secondary:
    properties:
      configs:
      - config:
          get_param: incoming_policer_config
        path:
        - config_type: tag
          tag: firewall
          xml_type: tag
        - config_type: named_tag
          name:
            get_param: incoming_policer_name
          tag: three-color-policer
          xml_type: named_tag
      - config:
          get_param: outgoing_policer_config
        path:
        - config_type: tag
          tag: firewall
          xml_type: tag
        - config_type: named_tag
          name:
            get_param: outgoing_policer_name
          tag: policer
          xml_type: named_tag
      - config:
          str_replace:
            params:
              $CLASS: FC-VPN-BE
              $POLICER_NAME:
                get_param: incoming_policer_name
              $PREFIX:
                get_param: neighbour_prefix
            template: "term bgp-accept {\n    from {\n        source-prefix-list {\n\
              \            $PREFIX;\n        }\n        protocol tcp;\n        port\
              \ bgp;\n    }\n    then accept;\n}\nterm vrrp-accept {\n    from {\n\
              \        source-prefix-list {\n            $PREFIX;\n        }\n   \
              \     protocol vrrp;\n    }\n    then accept;\n}\nterm qos {\n    then\
              \ {\n        three-color-policer {\n            two-rate $POLICER_NAME;\n\
              \        }\n        forwarding-class $CLASS;\n        accept;\n    }\n\
              }\n"
        path:
        - config_type: tag
          tag: firewall
          xml_type: tag
        - config_type: named_tag
          name:
            str_replace:
              params:
                $NAME:
                  get_param: incoming_policer_name
              template: 'FILTER_$NAME

                '
          tag: filter
          xml_type: named_tag
      - config:
          str_replace:
            params:
              $POLICER_NAME:
                get_param: outgoing_policer_name
              $PREFIX:
                get_param: neighbour_prefix
            template: "term bgp-accept {\n    from {\n        destination-prefix-list\
              \ {\n            $PREFIX;\n        }\n        protocol tcp;\n      \
              \  port bgp;\n    }\n    then accept;\n}\nterm vrrp-accept {\n    from\
              \ {\n        protocol vrrp;\n    }\n    then accept;\n}\nterm policer\
              \ {\n    then {\n        policer $POLICER_NAME;\n        accept;\n \
              \   }\n}\n"
        path:
        - config_type: tag
          tag: firewall
          xml_type: tag
        - config_type: named_tag
          name:
            str_replace:
              params:
                $NAME:
                  get_param: outgoing_policer_name
              template: 'FILTER_$NAME

                '
          tag: filter
          xml_type: named_tag
      device_ip:
        get_param: secondary_device_ip
      lock_timeout: 3000
      password:
        get_param: secondary_device_password
      port:
        get_param: secondary_device_port
      username:
        get_param: secondary_device_username
    type: OS::Contrail::NetconfNamedConfigs
```

* Checking resource-list of qos_option in heat-engine
```
$ openstack stack resource list qos_option_021a6fd0-d44e-41c6-9ebe-a98afd82d854
+-----------------------------+--------------------------------------+-----------------------------------+-----------------+----------------------+
| resource_name               | physical_resource_id                 | resource_type                     | resource_status | updated_time         |
+-----------------------------+--------------------------------------+-----------------------------------+-----------------+----------------------+
| netconf_configure_primary   | 0de6b60b-9d32-4c69-8cec-945a5cf1cdd0 | OS::Contrail::NetconfNamedConfigs | CREATE_COMPLETE | 2016-11-07T10:17:16Z |
| netconf_configure_secondary | 2e160183-4247-46cf-b59c-c24178f31c09 | OS::Contrail::NetconfNamedConfigs | CREATE_COMPLETE | 2016-11-07T10:17:45Z |
+-----------------------------+--------------------------------------+-----------------------------------+-----------------+----------------------+
```

* Checking resource-show of netconf_configure_primary in heat-engine
```
$ openstack stack resource show qos_option_021a6fd0-d44e-41c6-9ebe-a98afd82d854 netconf_configure_primary 
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                  | Value                                                                                                                                                           |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| description            |                                                                                                                                                                 |
| links                  | [{u'href': u'http://172.23.16.51:8004/v1/a367ed245222497db761a6c0becacab0/stacks/qos_option_021a6fd0-d44e-41c6-9ebe-a98afd82d854/1f2951fe-                      |
|                        | ae97-403c-9186-e30dd8e95355/resources/netconf_configure_primary', u'rel': u'self'}, {u'href':                                                                   |
|                        | u'http://172.23.16.51:8004/v1/a367ed245222497db761a6c0becacab0/stacks/qos_option_021a6fd0-d44e-41c6-9ebe-a98afd82d854/1f2951fe-ae97-403c-9186-e30dd8e95355',    |
|                        | u'rel': u'stack'}]                                                                                                                                              |
| logical_resource_id    | netconf_configure_primary                                                                                                                                       |
| physical_resource_id   | 0de6b60b-9d32-4c69-8cec-945a5cf1cdd0                                                                                                                            |
| required_by            | []                                                                                                                                                              |
| resource_name          | netconf_configure_primary                                                                                                                                       |
| resource_status        | CREATE_COMPLETE                                                                                                                                                 |
| resource_status_reason | state changed                                                                                                                                                   |
| resource_type          | OS::Contrail::NetconfNamedConfigs                                                                                                                               |
| updated_time           | 2016-11-07T10:17:16Z                                                                                                                                            |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

* Checking resource-show of netconf_configure_secondary in heat-engine
```
$ openstack stack resource show qos_option_021a6fd0-d44e-41c6-9ebe-a98afd82d854 netconf_configure_secondary
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                  | Value                                                                                                                                                           |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| description            |                                                                                                                                                                 |
| links                  | [{u'href': u'http://172.23.16.51:8004/v1/a367ed245222497db761a6c0becacab0/stacks/qos_option_021a6fd0-d44e-41c6-9ebe-a98afd82d854/1f2951fe-                      |
|                        | ae97-403c-9186-e30dd8e95355/resources/netconf_configure_secondary', u'rel': u'self'}, {u'href':                                                                 |
|                        | u'http://172.23.16.51:8004/v1/a367ed245222497db761a6c0becacab0/stacks/qos_option_021a6fd0-d44e-41c6-9ebe-a98afd82d854/1f2951fe-ae97-403c-9186-e30dd8e95355',    |
|                        | u'rel': u'stack'}]                                                                                                                                              |
| logical_resource_id    | netconf_configure_secondary                                                                                                                                     |
| physical_resource_id   | 2e160183-4247-46cf-b59c-c24178f31c09                                                                                                                            |
| required_by            | []                                                                                                                                                              |
| resource_name          | netconf_configure_secondary                                                                                                                                     |
| resource_status        | CREATE_COMPLETE                                                                                                                                                 |
| resource_status_reason | state changed                                                                                                                                                   |
| resource_type          | OS::Contrail::NetconfNamedConfigs                                                                                                                               |
| updated_time           | 2016-11-07T10:17:45Z                                                                                                                                            |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
