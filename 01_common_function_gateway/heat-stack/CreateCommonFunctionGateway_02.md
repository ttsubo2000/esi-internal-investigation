# HTTP Methods for creating heat-stack: Subnet

Checking heat-stack of "subnet" via heatclient.
```
$ heat stack-show subnet_cf9356ae-b4e1-4a91-8193-089fdc12173d
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                                                |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                                                   |
| creation_time         | 2018-04-09T04:49:55Z                                                                                                                                                                 |
| description           | Subnet template                                                                                                                                                                      |
| disable_rollback      | True                                                                                                                                                                                 |
| id                    | 24114c92-7b42-4bad-8d3b-bc1d88ffdd3b                                                                                                                                                 |
| links                 | http://heat-server.monitoringrefactordocker_default:8004/v1/c583ce78843344adbe5fd20f13620274/stacks/subnet_cf9356ae-b4e1-4a91-8193-089fdc12173d/24114c92-7b42-4bad-8d3b-bc1d88ffdd3b |
| notification_topics   | []                                                                                                                                                                                   |
| outputs               | [                                                                                                                                                                                    |
|                       |   {                                                                                                                                                                                  |
|                       |     "output_value": "169.254.0.0/17",                                                                                                                                                |
|                       |     "description": "IP prefix of local subnet.",                                                                                                                                     |
|                       |     "output_key": "ip_prefix"                                                                                                                                                        |
|                       |   },                                                                                                                                                                                 |
|                       |   {                                                                                                                                                                                  |
|                       |     "output_value": "cf9356ae-b4e1-4a91-8193-089fdc12173d",                                                                                                                          |
|                       |     "description": "The name of the local subnet.",                                                                                                                                  |
|                       |     "output_key": "name"                                                                                                                                                             |
|                       |   },                                                                                                                                                                                 |
|                       |   {                                                                                                                                                                                  |
|                       |     "output_value": "0.0.0.0",                                                                                                                                                       |
|                       |     "description": "Default gateway of local subnet.",                                                                                                                               |
|                       |     "output_key": "default_gateway"                                                                                                                                                  |
|                       |   },                                                                                                                                                                                 |
|                       |   {                                                                                                                                                                                  |
|                       |     "output_value": "fc8814a7-eb1e-4f59-8422-7de500e72782",                                                                                                                          |
|                       |     "description": "A unique id for the network.",                                                                                                                                   |
|                       |     "output_key": "network_id"                                                                                                                                                       |
|                       |   },                                                                                                                                                                                 |
|                       |   {                                                                                                                                                                                  |
|                       |     "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457",                                                                                                                          |
|                       |     "description": "IPAM this local subnet uses.",                                                                                                                                   |
|                       |     "output_key": "ipam"                                                                                                                                                             |
|                       |   },                                                                                                                                                                                 |
|                       |   {                                                                                                                                                                                  |
|                       |     "output_value": "8f52422a-7115-4304-99cf-fc021562c352",                                                                                                                          |
|                       |     "description": "A unique id for the local subnet.",                                                                                                                              |
|                       |     "output_key": "id"                                                                                                                                                               |
|                       |   }                                                                                                                                                                                  |
|                       | ]                                                                                                                                                                                    |
| parameters            | {                                                                                                                                                                                    |
|                       |   "OS::stack_name": "subnet_cf9356ae-b4e1-4a91-8193-089fdc12173d",                                                                                                                   |
|                       |   "enable_dhcp": "True",                                                                                                                                                             |
|                       |   "network_id": "fc8814a7-eb1e-4f59-8422-7de500e72782",                                                                                                                              |
|                       |   "ipam": "default-domain:default-project:default-network-ipam",                                                                                                                     |
|                       |   "dns_nameservers": "",                                                                                                                                                             |
|                       |   "dhcp_server_address": "169.254.0.2",                                                                                                                                              |
|                       |   "OS::stack_id": "24114c92-7b42-4bad-8d3b-bc1d88ffdd3b",                                                                                                                            |
|                       |   "ntp_servers": "",                                                                                                                                                                 |
|                       |   "allocation_pools": "[{u'start': u'169.254.0.2', u'end': u'169.254.127.254'}]",                                                                                                    |
|                       |   "gateway_ip": "0.0.0.0",                                                                                                                                                           |
|                       |   "host_routes": "[]",                                                                                                                                                               |
|                       |   "cidr": "169.254.0.0/17",                                                                                                                                                          |
|                       |   "name": "cf9356ae-b4e1-4a91-8193-089fdc12173d"                                                                                                                                     |
|                       | }                                                                                                                                                                                    |
| parent                | None                                                                                                                                                                                 |
| stack_name            | subnet_cf9356ae-b4e1-4a91-8193-089fdc12173d                                                                                                                                          |
| stack_owner           | admin                                                                                                                                                                                |
| stack_status          | CREATE_COMPLETE                                                                                                                                                                      |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                                                  |
| stack_user_project_id | c583ce78843344adbe5fd20f13620274                                                                                                                                                     |
| template_description  | Subnet template                                                                                                                                                                      |
| timeout_mins          | 3                                                                                                                                                                                    |
| updated_time          | None                                                                                                                                                                                 |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "subnet" via heatclient.
```
$ heat template-show subnet_cf9356ae-b4e1-4a91-8193-089fdc12173d
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
