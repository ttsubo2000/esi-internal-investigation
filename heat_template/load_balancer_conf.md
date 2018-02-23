# heat_template: load_balancer_conf
This is heat_template of "load_balancer_conf" which is provided by gohan via etcd

![scope](../images/esi_interface.002.png)

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/load_balancer_conf
{
    "body": {
        "handler": "heat_worker",
        "watch": [],
        "id": "load_balancer_conf",
        "template_file": "heat_template_version: 2013-05-23\ndescription: Load Balancer Configuration\nparameters:\n  management_ip:\n    type: string\n  management_gateway:\n    type: string\n  admin_username:\n    type: string\n  admin_password:\n    type: string\n    hidden: true\n  user_username:\n    type: string\n  user_password:\n    type: string\n    hidden: true\n  other_username:\n    type: string\n  other_password:\n    type: string\n    hidden: true\n  server_id:\n    type: string\n  license_code:\n    type: string\n  model:\n    type: string\n  init_config:\n    type: string\n  networks:\n    type: string\n  internet_port:\n    type: string\n  default_gateway:\n    type: string\n    default: \"\"\n  credentials:\n    type: string\nresources:\n  netscaler_configuration:\n    type: ESI::VNF::NetscalerConfig\n    properties:\n      management_ip: { get_param: management_ip }\n      management_gateway: { get_param: management_gateway }\n      admin_username: { get_param: admin_username }\n      admin_password: { get_param: admin_password }\n      user_username: { get_param: user_username }\n      user_password: { get_param: user_password }\n      other_username: { get_param: other_username }\n      other_password: { get_param: other_password }\n      server_id: { get_param: server_id }\n      license_code: { get_param: license_code }\n      model: { get_param: model }\n      init_config: { get_param: init_config }\n      networks: { get_param: networks }\n      internet_port: { get_param: internet_port }\n      default_gateway: { get_param: default_gateway }\n      credentials: { get_param: credentials }\n",
        "parameter_mappings": {
            "other_password": {
                "field": "other_password"
            },
            "other_username": {
                "field": "other_username"
            },
            "internet_port": {
                "field": "internet_port"
            },
            "default_gateway": {
                "field": "default_gateway"
            },
            "user_password": {
                "field": "user_password"
            },
            "license_code": {
                "field": "license_code",
                "path": [
                    "load_balancer_plan_id"
                ]
            },
            "init_config": {
                "field": "init_config",
                "path": [
                    "load_balancer_plan_id",
                    "vnf_template_id"
                ]
            },
            "management_ip": {
                "field": "management_ip",
                "path": [
                    "vnf_instance_id"
                ]
            },
            "admin_username": {
                "field": "admin_username"
            },
            "user_username": {
                "field": "user_username"
            },
            "heat_timeout": {
                "constant": 10
            },
            "management_gateway": {
                "field": "management_gateway"
            },
            "admin_password": {
                "field": "admin_password"
            },
            "credentials": {
                "field": "credentials",
                "path": [
                    "load_balancer_plan_id",
                    "vnf_template_id"
                ]
            },
            "model": {
                "field": "model",
                "path": [
                    "load_balancer_plan_id"
                ]
            },
            "server_id": {
                "path": [
                    "vnf_instance_id"
                ],
                "output_key": "server_id"
            },
            "networks": {
                "field": "networks"
            }
        }
    },
    "version": 1,
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* ESI::VNF::NetscalerConfig

```
heat_template_version: 2013-05-23
description: Load Balancer Configuration
parameters:
  management_ip:
    type: string
  management_gateway:
    type: string
  admin_username:
    type: string
  admin_password:
    type: string
    hidden: true
  user_username:
    type: string
  user_password:
    type: string
    hidden: true
  other_username:
    type: string
  other_password:
    type: string
    hidden: true
  server_id:
    type: string
  license_code:
    type: string
  model:
    type: string
  init_config:
    type: string
  networks:
    type: string
  internet_port:
    type: string
  default_gateway:
    type: string
    default: ""
  credentials:
    type: string
resources:
  netscaler_configuration:
    type: ESI::VNF::NetscalerConfig
    properties:
      management_ip: { get_param: management_ip }
      management_gateway: { get_param: management_gateway }
      admin_username: { get_param: admin_username }
      admin_password: { get_param: admin_password }
      user_username: { get_param: user_username }
      user_password: { get_param: user_password }
      other_username: { get_param: other_username }
      other_password: { get_param: other_password }
      server_id: { get_param: server_id }
      license_code: { get_param: license_code }
      model: { get_param: model }
      init_config: { get_param: init_config }
      networks: { get_param: networks }
      internet_port: { get_param: internet_port }
      default_gateway: { get_param: default_gateway }
      credentials: { get_param: credentials }
```
