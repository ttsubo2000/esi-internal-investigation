# HTTP Methods for creating heat-stack: Subnet

Checking heat-stack of "subnet" via heatclient.
```
$ heat stack-show subnet_e825f4e4-ba44-4d9e-9578-a31ad45bedda
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                   |
| creation_time         | 2018-04-16T00:12:11Z                                                                                                                                                                 |
| description           | Subnet template                                                                                                                                                                      |
| disable_rollback      | True                                                                                                                                                                                 |
| id                    | a88b397a-8099-4c6f-8063-26b1855ac113                                                                                                                                                 |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/b3e3095c0a5b4383805efe9cf2a6b5ef/stacks/subnet_e825f4e4-ba44-4d9e-9578-a31ad45bedda/a88b397a-8099-4c6f-8063-26b1855ac113 |
| notification_topics   | []                                                                                                                                                                                   |
| outputs               | [                                                                                                                                                                                    |
|                       |   {                                                                                                                                                                                  |
|                       |     "output_value": "172.16.101.0/24",                                                                                                                                               |
|                       |     "description": "IP prefix of local subnet.",                                                                                                                                     |
|                       |     "output_key": "ip_prefix"                                                                                                                                                        |
|                       |   },                                                                                                                                                                                 |
|                       |   {                                                                                                                                                                                  |
|                       |     "output_value": "e825f4e4-ba44-4d9e-9578-a31ad45bedda",                                                                                                                          |
|                       |     "description": "The name of the local subnet.",                                                                                                                                  |
|                       |     "output_key": "name"                                                                                                                                                             |
|                       |   },                                                                                                                                                                                 |
|                       |   {                                                                                                                                                                                  |
|                       |     "output_value": "172.16.101.1",                                                                                                                                                  |
|                       |     "description": "Default gateway of local subnet.",                                                                                                                               |
|                       |     "output_key": "default_gateway"                                                                                                                                                  |
|                       |   },                                                                                                                                                                                 |
|                       |   {                                                                                                                                                                                  |
|                       |     "output_value": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2",                                                                                                                          |
|                       |     "description": "A unique id for the network.",                                                                                                                                   |
|                       |     "output_key": "network_id"                                                                                                                                                       |
|                       |   },                                                                                                                                                                                 |
|                       |   {                                                                                                                                                                                  |
|                       |     "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457",                                                                                                                          |
|                       |     "description": "IPAM this local subnet uses.",                                                                                                                                   |
|                       |     "output_key": "ipam"                                                                                                                                                             |
|                       |   },                                                                                                                                                                                 |
|                       |   {                                                                                                                                                                                  |
|                       |     "output_value": "323017d2-b9fc-4407-b998-e4776b16aee8",                                                                                                                          |
|                       |     "description": "A unique id for the local subnet.",                                                                                                                              |
|                       |     "output_key": "id"                                                                                                                                                               |
|                       |   }                                                                                                                                                                                  |
|                       | ]                                                                                                                                                                                    |
| parameters            | {                                                                                                                                                                                    |
|                       |   "OS::stack_name": "subnet_e825f4e4-ba44-4d9e-9578-a31ad45bedda",                                                                                                                   |
|                       |   "enable_dhcp": "True",                                                                                                                                                             |
|                       |   "network_id": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2",                                                                                                                              |
|                       |   "ipam": "default-domain:default-project:default-network-ipam",                                                                                                                     |
|                       |   "dns_nameservers": "",                                                                                                                                                             |
|                       |   "dhcp_server_address": "172.16.101.2",                                                                                                                                             |
|                       |   "OS::stack_id": "a88b397a-8099-4c6f-8063-26b1855ac113",                                                                                                                            |
|                       |   "ntp_servers": "",                                                                                                                                                                 |
|                       |   "allocation_pools": "[{u'start': u'172.16.101.2', u'end': u'172.16.101.254'}]",                                                                                                    |
|                       |   "gateway_ip": "172.16.101.1",                                                                                                                                                      |
|                       |   "host_routes": "[]",                                                                                                                                                               |
|                       |   "cidr": "172.16.101.0/24",                                                                                                                                                         |
|                       |   "name": "e825f4e4-ba44-4d9e-9578-a31ad45bedda"                                                                                                                                     |
|                       | }                                                                                                                                                                                    |
| parent                | None                                                                                                                                                                                 |
| stack_name            | subnet_e825f4e4-ba44-4d9e-9578-a31ad45bedda                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                      |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                  |
| stack_user_project_id | b3e3095c0a5b4383805efe9cf2a6b5ef                                                                                                                                                     |
| template_description  | Subnet template                                                                                                                                                                      |
| timeout_mins          | 3                                                                                                                                                                                    |
| updated_time          | None                                                                                                                                                                                 |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "subnet" via heatclient.
```
$ heat template-show subnet_e825f4e4-ba44-4d9e-9578-a31ad45bedda
description: 'Subnet template

  '
heat_template_version: '2013-05-23'
outputs:
  default_gateway:
    description: Default gateway of local subnet.
    value:
      get_attr: [subnet, default_gateway]
  id:
    description: A unique id for the local subnet.
    value: {get_resource: subnet}
  ip_prefix:
    description: IP prefix of local subnet.
    value:
      get_attr: [subnet, ip_prefix]
  ipam:
    description: IPAM this local subnet uses.
    value:
      get_attr: [subnet, ipam]
  name:
    description: The name of the local subnet.
    value:
      get_attr: [subnet, name]
  network_id:
    description: A unique id for the network.
    value:
      get_attr: [subnet, network_id]
parameters:
  allocation_pools:
    default: []
    description: Allocation Pools
    label: Allocation Pools
    type: string
  cidr: {description: IP prefix of the local subnet that will be created., label: Local
      Subnet IP prefix, type: string}
  dhcp_server_address: {default: 0.0.0.0, description: DHCP Server address, label: DHCP
      Server address, type: string}
  dns_nameservers:
    default: []
    description: DNS Nameservers List
    label: DNS Nameservers List
    type: comma_delimited_list
  enable_dhcp: {default: true, description: Enable DHCP, label: Enable DHCP, type: boolean}
  gateway_ip: {default: 0.0.0.0, description: Default gateway for the local subnet
      that will be created., label: Default Gateway, type: string}
  host_routes:
    default: []
    description: Host Routes
    label: Host Routes
    type: json
  ipam: {default: '', description: IPAM for the local subnet that will be created.,
    label: IP Address Management, type: string}
  name: {description: Name of the local subnet that will be created., label: Local
      Subnet Name, type: string}
  network_id: {description: ID of the network for which subnet will be created., label: Network
      ID, type: string}
  ntp_servers:
    default: []
    description: NTP Nameservers List
    label: NTP Nameservers List
    type: comma_delimited_list
resources:
  subnet:
    properties:
      allocation_pools: {get_param: allocation_pools}
      default_gateway: {get_param: gateway_ip}
      dns_nameservers: {get_param: dns_nameservers}
      dns_server_address: {get_param: dhcp_server_address}
      enable_dhcp: {get_param: enable_dhcp}
      gateway_is_vrouter: false
      host_routes: {get_param: host_routes}
      ip_prefix: {get_param: cidr}
      ipam: {get_param: ipam}
      name: {get_param: name}
      network_id: {get_param: network_id}
      ntp_servers: {get_param: ntp_servers}
    type: OS::Contrail::VnSubnet
```
