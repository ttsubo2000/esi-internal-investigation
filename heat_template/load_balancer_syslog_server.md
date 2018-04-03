# heat_template: load_balancer_syslog_server
This is heat_template of "load_balancer_syslog_server" which is provided by gohan via etcd

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/load_balancer_syslog_server
{
    "body": {
        "handler": "heat_worker",
        "watch": [],
        "id": "load_balancer_syslog_server",
        "template_file": "heat_template_version: 2013-05-23\ndescription: Syslog server\nparameters:\n  name:\n    type: string\n  ip_address:\n    type: string\n  port_number:\n    type: number\n  log_level:\n    type: string\n  log_facility:\n    type: string\n  tcp_logging:\n    type: string\n  acl_logging:\n    type: string\n  appflow_logging:\n    type: string\n  date_format:\n    type: string\n  time_zone:\n    type: string\n  user_configurable_log_messages:\n    type: string\n  transport_type:\n    type: string\n  priority:\n    type: number\n  vserver_ip_address:\n    type: string\n  comment:\n    type: string\n  management_ip:\n    type: string\n  credentials:\n    type: string\n  init_config:\n    type: string\nresources:\n  load_balancer_syslog_server:\n    type: ESI::VNF::NetscalerSyslogServer\n    properties:\n      name: { get_param: name }\n      ip_address: { get_param: ip_address }\n      port_number: { get_param: port_number }\n      log_level: { get_param: log_level }\n      log_facility: { get_param: log_facility }\n      tcp_logging: { get_param: tcp_logging }\n      acl_logging: { get_param: acl_logging }\n      appflow_logging: { get_param: appflow_logging }\n      date_format: { get_param: date_format }\n      time_zone: { get_param: time_zone }\n      user_configurable_log_messages: { get_param: user_configurable_log_messages }\n      transport_type: { get_param: transport_type }\n      priority: { get_param: priority }\n      vserver_ip_address: { get_param: vserver_ip_address }\n      comment: { get_param: comment }\n      management_ip: { get_param: management_ip }\n      credentials: { get_param: credentials }\n      init_config: { get_param: init_config }\n",
        "parameter_mappings": {
            "comment": {
                "field": "comment"
            },
            "date_format": {
                "field": "date_format"
            },
            "appflow_logging": {
                "field": "appflow_logging"
            },
            "name": {
                "field": "name"
            },
            "port_number": {
                "field": "port_number"
            },
            "tcp_logging": {
                "field": "tcp_logging"
            },
            "vserver_ip_address": {
                "field": "vserver_ip_address"
            },
            "log_level": {
                "field": "log_level"
            },
            "init_config": {
                "field": "init_config",
                "path": [
                    "load_balancer_id",
                    "load_balancer_plan_id",
                    "vnf_template_id"
                ]
            },
            "acl_logging": {
                "field": "acl_logging"
            },
            "time_zone": {
                "field": "time_zone"
            },
            "priority": {
                "field": "priority"
            },
            "transport_type": {
                "field": "transport_type"
            },
            "heat_timeout": {
                "constant": 10
            },
            "management_ip": {
                "field": "management_ip",
                "path": [
                    "load_balancer_id",
                    "vnf_instance_id"
                ]
            },
            "log_facility": {
                "field": "log_facility"
            },
            "credentials": {
                "field": "credentials",
                "path": [
                    "load_balancer_id",
                    "load_balancer_plan_id",
                    "vnf_template_id"
                ]
            },
            "ip_address": {
                "field": "ip_address"
            },
            "user_configurable_log_messages": {
                "field": "user_configurable_log_messages"
            }
        }
    },
    "version": 1,
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* ESI::VNF::NetscalerSyslogServer

```
heat_template_version: 2013-05-23
description: Syslog server
parameters:
  name:
    type: string
  ip_address:
    type: string
  port_number:
    type: number
  log_level:
    type: string
  log_facility:
    type: string
  tcp_logging:
    type: string
  acl_logging:
    type: string
  appflow_logging:
    type: string
  date_format:
    type: string
  time_zone:
    type: string
  user_configurable_log_messages:
    type: string
  transport_type:
    type: string
  priority:
    type: number
  vserver_ip_address:
    type: string
  comment:
    type: string
  management_ip:
    type: string
  credentials:
    type: string
  init_config:
    type: string
resources:
  load_balancer_syslog_server:
    type: ESI::VNF::NetscalerSyslogServer
    properties:
      name: { get_param: name }
      ip_address: { get_param: ip_address }
      port_number: { get_param: port_number }
      log_level: { get_param: log_level }
      log_facility: { get_param: log_facility }
      tcp_logging: { get_param: tcp_logging }
      acl_logging: { get_param: acl_logging }
      appflow_logging: { get_param: appflow_logging }
      date_format: { get_param: date_format }
      time_zone: { get_param: time_zone }
      user_configurable_log_messages: { get_param: user_configurable_log_messages }
      transport_type: { get_param: transport_type }
      priority: { get_param: priority }
      vserver_ip_address: { get_param: vserver_ip_address }
      comment: { get_param: comment }
      management_ip: { get_param: management_ip }
      credentials: { get_param: credentials }
      init_config: { get_param: init_config }
```
