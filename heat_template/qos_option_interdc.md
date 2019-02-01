# heat_template: qos_option_interdc
This is heat_template of "qos_option_interdc" which is provided by gohan via etcd

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/qos_option_interdc
{
    "body": {
        "handler": "heat_worker",
        "watch": [],
        "id": "qos_option_interdc",
        "template_file": "heat_template_version: 2013-05-23\n\ndescription: >\n  QoS Option\n\nparameters:\n  primary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Primary Device.\n    label: Ip address of the device.\n    type: string\n  primary_device_port:\n    description: Port that will be used to establish ssh connection to the Primary Device.\n    label: Port of the ssh connection.\n    type: number\n  primary_device_username:\n    description: Name of the user which will be used to log onto the Primary Device.\n    label: User name to log on to device.\n    type: string\n  primary_device_password:\n    description: Password of the user which will be used to log onto the Primary Device.\n    label: Users password.\n    type: string\n    hidden: true\n  secondary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Secondary Device.\n    label: Ip address of the device.\n    type: string\n  secondary_device_port:\n    description: Port that will be used to establish ssh connection to the Secondary Device.\n    label: Port of the ssh connection.\n    type: number\n  secondary_device_username:\n    description: Name of the user which will be used to log onto the Secondary Device.\n    label: User name to log on to device.\n    type: string\n  secondary_device_password:\n    description: Password of the user which will be used to log onto the Secondary Device.\n    label: Users password.\n    type: string\n    hidden: true\n  incoming_policer_name:\n    description: Name of created incoming policer\n    label: Incoming policer name\n    type: string\n  incoming_policer_config:\n    description: Configuration of incoming policer\n    label: Incoming policer config\n    type: string\n  outgoing_policer_name:\n    description: Name of created outgoing policer\n    label: Outgoing policer name\n    type: string\n  outgoing_policer_config:\n    description: Configuration of outgoing policer\n    label: Outgoing policer config\n    type: string\nresources:\n{% for device in [\"primary\", \"secondary\"] %}\n  netconf_configure_{{ device }}:\n    type: OS::Contrail::NetconfNamedConfigs\n    {% if device == \"secondary\" %}depends_on: netconf_configure_primary{% endif %}\n    properties:\n      lock_timeout: 3000\n      device_ip:\n        get_param: {{ device }}_device_ip\n      password:\n        get_param: {{ device }}_device_password\n      port:\n        get_param: {{ device }}_device_port\n      username:\n        get_param: {{ device }}_device_username\n      configs:\n      - config:\n          { get_param: incoming_policer_config }\n        path:\n        - config_type: tag\n          xml_type: tag\n          tag: firewall\n        - config_type: named_tag\n          xml_type: named_tag\n          tag: three-color-policer\n          name: { get_param: incoming_policer_name }\n      - config:\n          { get_param: outgoing_policer_config }\n        path:\n        - config_type: tag\n          xml_type: tag\n          tag: firewall\n        - config_type: named_tag\n          xml_type: named_tag\n          tag: policer\n          name: { get_param: outgoing_policer_name }\n      - config:\n          str_replace:\n            params:\n              $CLASS:\n              {% if jinja_type == \"besteffort\" %}\n                {{ jinja_be_forwarding_class }}\n              {% else %}\n                {{ jinja_ga_forwarding_class }}\n              {% endif %}\n              $POLICER_NAME:\n                get_param: incoming_policer_name\n            template: |\n              interface-specific;\n              term vrrp-accept {\n                from {\n                  protocol vrrp;\n                }\n                then policer 10K-RE;\n                then accept;\n              }\n              term qos {\n                then {\n                  three-color-policer {\n                    two-rate $POLICER_NAME;\n                  }\n                  forwarding-class $CLASS;\n                  accept;\n                }\n              }\n        path:\n        - config_type: tag\n          xml_type: tag\n          tag: firewall\n        - config_type: named_tag\n          xml_type: named_tag\n          tag: filter\n          name:\n            str_replace:\n              params:\n                $NAME:\n                  get_param: incoming_policer_name\n              template: |\n                FILTER_$NAME\n      - config:\n          str_replace:\n            params:\n              $POLICER_NAME:\n                get_param: outgoing_policer_name\n            template: |\n              interface-specific;\n              term vrrp-accept {\n                from {\n                  protocol vrrp;\n                }\n                then accept;\n              }\n              term policer {\n                then {\n                  policer $POLICER_NAME;\n                  accept;\n                }\n              }\n        path:\n        - config_type: tag\n          xml_type: tag\n          tag: firewall\n        - config_type: named_tag\n          xml_type: named_tag\n          tag: filter\n          name:\n            str_replace:\n              params:\n                $NAME:\n                  get_param: outgoing_policer_name\n              template: |\n                FILTER_$NAME\n{% endfor %}\n",
        "parameter_mappings": {
            "secondary_device_password": {
                "field": "password",
                "path": [
                    "ha_router_id",
                    "secondary_router_id"
                ]
            },
            "jinja_be_forwarding_class": {
                "field": "be_forwarding_class",
                "path": [
                    "interdc_service_id"
                ]
            },
            "primary_device_password": {
                "field": "password",
                "path": [
                    "ha_router_id",
                    "primary_router_id"
                ]
            },
            "jinja_ga_forwarding_class": {
                "field": "ga_forwarding_class",
                "path": [
                    "interdc_service_id"
                ]
            },
            "incoming_policer_name": {
                "field": "incoming_policer_name"
            },
            "jinja_type": {
                "field": "qos_type"
            },
            "secondary_device_port": {
                "field": "ssh_port",
                "path": [
                    "ha_router_id",
                    "secondary_router_id"
                ]
            },
            "primary_device_ip": {
                "field": "ip",
                "path": [
                    "ha_router_id",
                    "primary_router_id"
                ]
            },
            "heat_timeout": {
                "constant": 60
            },
            "outgoing_policer_config": {
                "field": "outgoing_policer_config"
            },
            "incoming_policer_config": {
                "field": "incoming_policer_config"
            },
            "outgoing_policer_name": {
                "field": "outgoing_policer_name"
            },
            "secondary_device_username": {
                "field": "login",
                "path": [
                    "ha_router_id",
                    "secondary_router_id"
                ]
            },
            "primary_device_port": {
                "field": "ssh_port",
                "path": [
                    "ha_router_id",
                    "primary_router_id"
                ]
            },
            "secondary_device_ip": {
                "field": "ip",
                "path": [
                    "ha_router_id",
                    "secondary_router_id"
                ]
            },
            "primary_device_username": {
                "field": "login",
                "path": [
                    "ha_router_id",
                    "primary_router_id"
                ]
            }
        }
    },
    "version": 1,
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

OS::Contrail::NetconfNamedConfigs

```
heat_template_version: 2013-05-23

description: >
  QoS Option

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
  incoming_policer_name:
    description: Name of created incoming policer
    label: Incoming policer name
    type: string
  incoming_policer_config:
    description: Configuration of incoming policer
    label: Incoming policer config
    type: string
  outgoing_policer_name:
    description: Name of created outgoing policer
    label: Outgoing policer name
    type: string
  outgoing_policer_config:
    description: Configuration of outgoing policer
    label: Outgoing policer config
    type: string
resources:
{% for device in ["primary", "secondary"] %}
  netconf_configure_{{ device }}:
    type: OS::Contrail::NetconfNamedConfigs
    {% if device == "secondary" %}depends_on: netconf_configure_primary{% endif %}
    properties:
      lock_timeout: 3000
      device_ip:
        get_param: {{ device }}_device_ip
      password:
        get_param: {{ device }}_device_password
      port:
        get_param: {{ device }}_device_port
      username:
        get_param: {{ device }}_device_username
      configs:
      - config:
          { get_param: incoming_policer_config }
        path:
        - config_type: tag
          xml_type: tag
          tag: firewall
        - config_type: named_tag
          xml_type: named_tag
          tag: three-color-policer
          name: { get_param: incoming_policer_name }
      - config:
          { get_param: outgoing_policer_config }
        path:
        - config_type: tag
          xml_type: tag
          tag: firewall
        - config_type: named_tag
          xml_type: named_tag
          tag: policer
          name: { get_param: outgoing_policer_name }
      - config:
          str_replace:
            params:
              $CLASS:
              {% if jinja_type == "besteffort" %}
                {{ jinja_be_forwarding_class }}
              {% else %}
                {{ jinja_ga_forwarding_class }}
              {% endif %}
              $POLICER_NAME:
                get_param: incoming_policer_name
            template: |
              interface-specific;
              term vrrp-accept {
                from {
                  protocol vrrp;
                }
                then policer 10K-RE;
                then accept;
              }
              term qos {
                then {
                  three-color-policer {
                    two-rate $POLICER_NAME;
                  }
                  forwarding-class $CLASS;
                  accept;
                }
              }
        path:
        - config_type: tag
          xml_type: tag
          tag: firewall
        - config_type: named_tag
          xml_type: named_tag
          tag: filter
          name:
            str_replace:
              params:
                $NAME:
                  get_param: incoming_policer_name
              template: |
                FILTER_$NAME
      - config:
          str_replace:
            params:
              $POLICER_NAME:
                get_param: outgoing_policer_name
            template: |
              interface-specific;
              term vrrp-accept {
                from {
                  protocol vrrp;
                }
                then accept;
              }
              term policer {
                then {
                  policer $POLICER_NAME;
                  accept;
                }
              }
        path:
        - config_type: tag
          xml_type: tag
          tag: firewall
        - config_type: named_tag
          xml_type: named_tag
          tag: filter
          name:
            str_replace:
              params:
                $NAME:
                  get_param: outgoing_policer_name
              template: |
                FILTER_$NAME
{% endfor %}
```
