# HTTP Methods for creating heat-stack: Subnet

Checking heat-stack of "subnet" via heatclient.
```
$ heat stack-show subnet_e1353d56-b05a-43a9-b924-383ab0d64d7b
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                   |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                      |
| creation_time         | 2017-05-11T03:05:34Z                                                                                                                                    |
| description           | Subnet template                                                                                                                                         |
| disable_rollback      | True                                                                                                                                                    |
| id                    | ad399461-7f17-4d5c-a825-67c298f59bd8                                                                                                                    |
| links                 | http://heat-api:8004/v1/0b576f6f4cbf414f829cd12f008bf08f/stacks/subnet_e1353d56-b05a-43a9-b924-383ab0d64d7b/ad399461-7f17-4d5c-a825-67c298f59bd8 (self) |
| notification_topics   | []                                                                                                                                                      |
| outputs               | [                                                                                                                                                       |
|                       |   {                                                                                                                                                     |
|                       |     "output_value": "169.254.0.0/17",                                                                                                                   |
|                       |     "description": "IP prefix of local subnet.",                                                                                                        |
|                       |     "output_key": "ip_prefix"                                                                                                                           |
|                       |   },                                                                                                                                                    |
|                       |   {                                                                                                                                                     |
|                       |     "output_value": "e1353d56-b05a-43a9-b924-383ab0d64d7b",                                                                                             |
|                       |     "description": "The name of the local subnet.",                                                                                                     |
|                       |     "output_key": "name"                                                                                                                                |
|                       |   },                                                                                                                                                    |
|                       |   {                                                                                                                                                     |
|                       |     "output_value": "0.0.0.0",                                                                                                                          |
|                       |     "description": "Default gateway of local subnet.",                                                                                                  |
|                       |     "output_key": "default_gateway"                                                                                                                     |
|                       |   },                                                                                                                                                    |
|                       |   {                                                                                                                                                     |
|                       |     "output_value": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57",                                                                                             |
|                       |     "description": "A unique id for the network.",                                                                                                      |
|                       |     "output_key": "network_id"                                                                                                                          |
|                       |   },                                                                                                                                                    |
|                       |   {                                                                                                                                                     |
|                       |     "output_value": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",                                                                                             |
|                       |     "description": "IPAM this local subnet uses.",                                                                                                      |
|                       |     "output_key": "ipam"                                                                                                                                |
|                       |   },                                                                                                                                                    |
|                       |   {                                                                                                                                                     |
|                       |     "output_value": "9e61b626-a866-4ba5-b1c7-01935fdac3f4",                                                                                             |
|                       |     "description": "A unique id for the local subnet.",                                                                                                 |
|                       |     "output_key": "id"                                                                                                                                  |
|                       |   }                                                                                                                                                     |
|                       | ]                                                                                                                                                       |
| parameters            | {                                                                                                                                                       |
|                       |   "OS::stack_name": "subnet_e1353d56-b05a-43a9-b924-383ab0d64d7b",                                                                                      |
|                       |   "enable_dhcp": "True",                                                                                                                                |
|                       |   "network_id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57",                                                                                                 |
|                       |   "ipam": "default-domain:default-project:default-network-ipam",                                                                                        |
|                       |   "dns_nameservers": "",                                                                                                                                |
|                       |   "dhcp_server_address": "169.254.0.2",                                                                                                                 |
|                       |   "OS::stack_id": "ad399461-7f17-4d5c-a825-67c298f59bd8",                                                                                               |
|                       |   "ntp_servers": "",                                                                                                                                    |
|                       |   "allocation_pools": "[{u'start': u'169.254.0.2', u'end': u'169.254.127.254'}]",                                                                       |
|                       |   "gateway_ip": "0.0.0.0",                                                                                                                              |
|                       |   "host_routes": "[]",                                                                                                                                  |
|                       |   "cidr": "169.254.0.0/17",                                                                                                                             |
|                       |   "name": "e1353d56-b05a-43a9-b924-383ab0d64d7b"                                                                                                        |
|                       | }                                                                                                                                                       |
| parent                | None                                                                                                                                                    |
| stack_name            | subnet_e1353d56-b05a-43a9-b924-383ab0d64d7b                                                                                                             |
| stack_owner           | admin                                                                                                                                                   |
| stack_status          | CREATE_COMPLETE                                                                                                                                         |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                     |
| stack_user_project_id | 0b576f6f4cbf414f829cd12f008bf08f                                                                                                                        |
| template_description  | Subnet template                                                                                                                                         |
| timeout_mins          | 10                                                                                                                                                      |
| updated_time          | None                                                                                                                                                    |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
```
Checking heat-template of "subnet" via heatclient.
```
$ heat template-show subnet_e1353d56-b05a-43a9-b924-383ab0d64d7b
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
