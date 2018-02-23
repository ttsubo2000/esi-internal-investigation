## Sample of heat-stack of qos_option(aws)

* Checking heat-stack of qos_option in heat-engine
```
$ openstack stack show qos_option_b10db1d9-4ba8-48b0-8e63-36aa1d6e5cd1
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Field                 | Value                                                                                                                                  |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| id                    | 3e8b70b5-051c-42c5-a8ba-b415875c4e35                                                                                                   |
| stack_name            | qos_option_b10db1d9-4ba8-48b0-8e63-36aa1d6e5cd1                                                                                        |
| description           | QoS Option                                                                                                                             |
|                       |                                                                                                                                        |
| creation_time         | 2016-11-14T11:11:01Z                                                                                                                   |
| updated_time          | None                                                                                                                                   |
| stack_status          | CREATE_COMPLETE                                                                                                                        |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                    |
| parameters            | OS::stack_id: 3e8b70b5-051c-42c5-a8ba-b415875c4e35                                                                                     |
|                       | OS::stack_name: qos_option_b10db1d9-4ba8-48b0-8e63-36aa1d6e5cd1                                                                        |
|                       | incoming_policer_config: action { loss-priority high then discard; } two-rate { color-blind;                                           |
|                       |   committed-information-rate 1m; committed-burst-size 1500; peak-information-rate                                                      |
|                       |   100m; peak-burst-size 50k; }                                                                                                         |
|                       | incoming_policer_name: 100M-BE-UP-AWS                                                                                                  |
|                       | neighbour_prefix: BGP-VIRTUAL-ROUTER-PEERS                                                                                             |
|                       | outgoing_policer_config: if-exceeding { bandwidth-limit 100m; burst-size-limit 50k;                                                    |
|                       |   } then discard;                                                                                                                      |
|                       | outgoing_policer_name: 100M-BE-DOWN-AWS                                                                                                |
|                       | primary_device_ip: 172.23.16.41                                                                                                        |
|                       | primary_device_password: esiesi01                                                                                                      |
|                       | primary_device_port: '830'                                                                                                             |
|                       | primary_device_username: esi                                                                                                           |
|                       | secondary_device_ip: 172.23.16.42                                                                                                      |
|                       | secondary_device_password: esiesi01                                                                                                    |
|                       | secondary_device_port: '830'                                                                                                           |
|                       | secondary_device_username: esi                                                                                                         |
|                       |                                                                                                                                        |
| outputs               | []                                                                                                                                     |
|                       |                                                                                                                                        |
| links                 | - href: http://172.23.16.190:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/qos_option_b10db1d9-4ba8-48b0-8e63-36aa1d6e5cd1/3e8b70b5  |
|                       | -051c-42c5-a8ba-b415875c4e35                                                                                                           |
|                       |   rel: self                                                                                                                            |
|                       |                                                                                                                                        |
| parent                | None                                                                                                                                   |
| disable_rollback      | True                                                                                                                                   |
| stack_user_project_id | aee85dff980f4b0f94bed7861765acc7                                                                                                       |
| stack_owner           | sdp_esi_admin                                                                                                                          |
| capabilities          | []                                                                                                                                     |
| notification_topics   | []                                                                                                                                     |
| timeout_mins          | 60                                                                                                                                     |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------+
```

* Checking heat-template of qos_option in heat-engine
```
$ openstack stack template show qos_option_b10db1d9-4ba8-48b0-8e63-36aa1d6e5cd1
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
            template: "interface-specific;\nterm bgp-accept {\n    from {\n      \
              \  source-prefix-list {\n            $PREFIX;\n        }\n        protocol\
              \ tcp;\n        port bgp;\n    }\n    then accept;\n}\nterm vrrp-accept\
              \ {\n    from {\n        source-prefix-list {\n            $PREFIX;\n\
              \        }\n        protocol vrrp;\n    }\n    then policer 10K-RE;\n\
              \    then accept;\n}\nterm qos {\n    then {\n        three-color-policer\
              \ {\n            two-rate $POLICER_NAME;\n        }\n        forwarding-class\
              \ $CLASS;\n        accept;\n    }\n}\n"
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
            template: "interface-specific;\nterm bgp-accept {\n    from {\n      \
              \  destination-prefix-list {\n            $PREFIX;\n        }\n    \
              \    protocol tcp;\n        port bgp;\n    }\n    then accept;\n}\n\
              term vrrp-accept {\n    from {\n        protocol vrrp;\n    }\n    then\
              \ accept;\n}\nterm policer {\n    then {\n        policer $POLICER_NAME;\n\
              \        accept;\n    }\n}\n"
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
            template: "interface-specific;\nterm bgp-accept {\n    from {\n      \
              \  source-prefix-list {\n            $PREFIX;\n        }\n        protocol\
              \ tcp;\n        port bgp;\n    }\n    then accept;\n}\nterm vrrp-accept\
              \ {\n    from {\n        source-prefix-list {\n            $PREFIX;\n\
              \        }\n        protocol vrrp;\n    }\n    then policer 10K-RE;\n\
              \    then accept;\n}\nterm qos {\n    then {\n        three-color-policer\
              \ {\n            two-rate $POLICER_NAME;\n        }\n        forwarding-class\
              \ $CLASS;\n        accept;\n    }\n}\n"
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
            template: "interface-specific;\nterm bgp-accept {\n    from {\n      \
              \  destination-prefix-list {\n            $PREFIX;\n        }\n    \
              \    protocol tcp;\n        port bgp;\n    }\n    then accept;\n}\n\
              term vrrp-accept {\n    from {\n        protocol vrrp;\n    }\n    then\
              \ accept;\n}\nterm policer {\n    then {\n        policer $POLICER_NAME;\n\
              \        accept;\n    }\n}\n"
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
$ openstack stack resource list qos_option_b10db1d9-4ba8-48b0-8e63-36aa1d6e5cd1
+-----------------------------+--------------------------------------+-----------------------------------+-----------------+----------------------+
| resource_name               | physical_resource_id                 | resource_type                     | resource_status | updated_time         |
+-----------------------------+--------------------------------------+-----------------------------------+-----------------+----------------------+
| netconf_configure_primary   | 0a372567-24bf-41f8-8e47-1d0d6cb57ed9 | OS::Contrail::NetconfNamedConfigs | CREATE_COMPLETE | 2016-11-14T11:11:48Z |
| netconf_configure_secondary | 8b535c59-1b3c-4988-8a95-7753e8df5061 | OS::Contrail::NetconfNamedConfigs | CREATE_COMPLETE | 2016-11-14T11:11:01Z |
+-----------------------------+--------------------------------------+-----------------------------------+-----------------+----------------------+
```

* Checking resource-show of netconf_configure_primary in heat-engine
```
$ openstack stack resource show qos_option_b10db1d9-4ba8-48b0-8e63-36aa1d6e5cd1 netconf_configure_primary 
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Field                  | Value                                                                                                                                  |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| description            |                                                                                                                                        |
| links                  | [{u'href':                                                                                                                             |
|                        | u'http://172.23.16.190:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/qos_option_b10db1d9-4ba8-48b0-8e63-36aa1d6e5cd1/3e8b70b5-051c-  |
|                        | 42c5-a8ba-b415875c4e35/resources/netconf_configure_primary', u'rel': u'self'}, {u'href':                                               |
|                        | u'http://172.23.16.190:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/qos_option_b10db1d9-4ba8-48b0-8e63-36aa1d6e5cd1/3e8b70b5-051c-  |
|                        | 42c5-a8ba-b415875c4e35', u'rel': u'stack'}]                                                                                            |
| logical_resource_id    | netconf_configure_primary                                                                                                              |
| physical_resource_id   | 0a372567-24bf-41f8-8e47-1d0d6cb57ed9                                                                                                   |
| required_by            | []                                                                                                                                     |
| resource_name          | netconf_configure_primary                                                                                                              |
| resource_status        | CREATE_COMPLETE                                                                                                                        |
| resource_status_reason | state changed                                                                                                                          |
| resource_type          | OS::Contrail::NetconfNamedConfigs                                                                                                      |
| updated_time           | 2016-11-14T11:11:48Z                                                                                                                   |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
```

* Checking resource-show of netconf_configure_secondary in heat-engine
```
$ openstack stack resource show qos_option_b10db1d9-4ba8-48b0-8e63-36aa1d6e5cd1 netconf_configure_secondary
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Field                  | Value                                                                                                                                  |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| description            |                                                                                                                                        |
| links                  | [{u'href':                                                                                                                             |
|                        | u'http://172.23.16.190:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/qos_option_b10db1d9-4ba8-48b0-8e63-36aa1d6e5cd1/3e8b70b5-051c-  |
|                        | 42c5-a8ba-b415875c4e35/resources/netconf_configure_secondary', u'rel': u'self'}, {u'href':                                             |
|                        | u'http://172.23.16.190:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/qos_option_b10db1d9-4ba8-48b0-8e63-36aa1d6e5cd1/3e8b70b5-051c-  |
|                        | 42c5-a8ba-b415875c4e35', u'rel': u'stack'}]                                                                                            |
| logical_resource_id    | netconf_configure_secondary                                                                                                            |
| physical_resource_id   | 8b535c59-1b3c-4988-8a95-7753e8df5061                                                                                                   |
| required_by            | []                                                                                                                                     |
| resource_name          | netconf_configure_secondary                                                                                                            |
| resource_status        | CREATE_COMPLETE                                                                                                                        |
| resource_status_reason | state changed                                                                                                                          |
| resource_type          | OS::Contrail::NetconfNamedConfigs                                                                                                      |
| updated_time           | 2016-11-14T11:11:01Z                                                                                                                   |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
```
