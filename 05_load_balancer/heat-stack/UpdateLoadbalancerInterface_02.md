# HTTP Methods for updating heat-stack: Load Balancer Configuration

Checking heat-stack of "load_balancer_conf" via heatclient.
```
$ heat stack-show load_balancer_conf_1d2023e1-0cf4-48a1-af42-ab32466b2acb
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                                                                                                  |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                                                                                                     |
| creation_time         | 2018-02-19T05:21:56Z                                                                                                                                                                                                                                                   |
| description           | Load Balancer Configuration                                                                                                                                                                                                                                            |
| disable_rollback      | True                                                                                                                                                                                                                                                                   |
| id                    | eea47c50-62b0-4ac3-9ee6-7ac3978fbdaa                                                                                                                                                                                                                                   |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/fe3a4a1a72c04479bb6c19c2c0ccba4c/stacks/load_balancer_conf_1d2023e1-0cf4-48a1-af42-ab32466b2acb/eea47c50-62b0-4ac3-9ee6-7ac3978fbdaa                                                                       |
| notification_topics   | []                                                                                                                                                                                                                                                                     |
| outputs               | []                                                                                                                                                                                                                                                                     |
| parameters            | {                                                                                                                                                                                                                                                                      |
|                       |   "model": "{u'edition': u'Standard', u'size': u'10'}",                                                                                                                                                                                                                |
|                       |   "server_id": "47531b14-72e9-439d-8949-fd941457ecde",                                                                                                                                                                                                                 |
|                       |   "OS::stack_id": "eea47c50-62b0-4ac3-9ee6-7ac3978fbdaa",                                                                                                                                                                                                              |
|                       |   "OS::stack_name": "load_balancer_conf_1d2023e1-0cf4-48a1-af42-ab32466b2acb",                                                                                                                                                                                         |
|                       |   "license_code": "LA-0001969526-49522",                                                                                                                                                                                                                               |
|                       |   "user_password": "******",                                                                                                                                                                                                                                           |
|                       |   "other_username": "",                                                                                                                                                                                                                                                |
|                       |   "init_config": "{}",                                                                                                                                                                                                                                                 |
|                       |   "admin_username": "user-admin",                                                                                                                                                                                                                                      |
|                       |   "networks": "[{u'ip_address': u'100.64.193.3', u'cidr': u'100.64.193.0/24', u'type': u'user'}, {u'ip_address': u'10.225.225.3', u'cidr': u'10.225.225.0/24', u'type': u'user'}, {u'ip_address': u'10.121.232.4', u'cidr': u'10.121.232.0/24', u'type': u'dummy'}]",  |
|                       |   "user_username": "user-read",                                                                                                                                                                                                                                        |
|                       |   "management_ip": "100.64.193.3",                                                                                                                                                                                                                                     |
|                       |   "other_password": "******",                                                                                                                                                                                                                                          |
|                       |   "admin_password": "******",                                                                                                                                                                                                                                          |
|                       |   "credentials": "{u'username': u'vlbadmin', u'password': u'password'}",                                                                                                                                                                                               |
|                       |   "default_gateway": "",                                                                                                                                                                                                                                               |
|                       |   "management_gateway": "100.64.193.1",                                                                                                                                                                                                                                |
|                       |   "internet_port": "{u'ip_address': u'100.64.193.4', u'mask': u'255.255.255.0'}"                                                                                                                                                                                       |
|                       | }                                                                                                                                                                                                                                                                      |
| parent                | None                                                                                                                                                                                                                                                                   |
| stack_name            | load_balancer_conf_1d2023e1-0cf4-48a1-af42-ab32466b2acb                                                                                                                                                                                                                |
| stack_owner           | admin                                                                                                                                                                                                                                                                  |
| stack_status          | UPDATE_COMPLETE                                                                                                                                                                                                                                                        |
| stack_status_reason   | Stack successfully updated                                                                                                                                                                                                                                             |
| stack_user_project_id | fe3a4a1a72c04479bb6c19c2c0ccba4c                                                                                                                                                                                                                                       |
| template_description  | Load Balancer Configuration                                                                                                                                                                                                                                            |
| timeout_mins          | 10                                                                                                                                                                                                                                                                     |
| updated_time          | 2018-02-19T05:26:14Z                                                                                                                                                                                                                                                   |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "load_balancer_conf" via heatclient.
```
$ heat template-show load_balancer_conf_1d2023e1-0cf4-48a1-af42-ab32466b2acb
description: Load Balancer Configuration
heat_template_version: '2013-05-23'
parameters:
  admin_password: {hidden: true, type: string}
  admin_username: {type: string}
  credentials: {type: string}
  default_gateway: {default: '', type: string}
  init_config: {type: string}
  internet_port: {type: string}
  license_code: {type: string}
  management_gateway: {type: string}
  management_ip: {type: string}
  model: {type: string}
  networks: {type: string}
  other_password: {hidden: true, type: string}
  other_username: {type: string}
  server_id: {type: string}
  user_password: {hidden: true, type: string}
  user_username: {type: string}
resources:
  netscaler_configuration:
    properties:
      admin_password: {get_param: admin_password}
      admin_username: {get_param: admin_username}
      credentials: {get_param: credentials}
      default_gateway: {get_param: default_gateway}
      init_config: {get_param: init_config}
      internet_port: {get_param: internet_port}
      license_code: {get_param: license_code}
      management_gateway: {get_param: management_gateway}
      management_ip: {get_param: management_ip}
      model: {get_param: model}
      networks: {get_param: networks}
      other_password: {get_param: other_password}
      other_username: {get_param: other_username}
      server_id: {get_param: server_id}
      user_password: {get_param: user_password}
      user_username: {get_param: user_username}
    type: ESI::VNF::NetscalerConfig
```
