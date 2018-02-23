# HTTP Methods for creating heat-stack: Subnet

Checking heat-stack of "subnet" via heatclient.
```
$ heat stack-show subnet_b4f0c956-2fe0-4634-b7c8-22bfd8095aaf
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Value                                                                                                                                                   |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| capabilities          | []                                                                                                                                                      |
| creation_time         | 2017-05-11T05:02:03Z                                                                                                                                    |
| description           | Subnet template                                                                                                                                         |
| disable_rollback      | True                                                                                                                                                    |
| id                    | ae4327f2-0f4c-460e-a370-2965a731cf8d                                                                                                                    |
| links                 | http://heat-api:8004/v1/0b576f6f4cbf414f829cd12f008bf08f/stacks/subnet_b4f0c956-2fe0-4634-b7c8-22bfd8095aaf/ae4327f2-0f4c-460e-a370-2965a731cf8d (self) |
| notification_topics   | []                                                                                                                                                      |
| outputs               | [                                                                                                                                                       |
|                       |   {                                                                                                                                                     |
|                       |     "output_value": "172.16.101.0/24",                                                                                                                  |
|                       |     "description": "IP prefix of local subnet.",                                                                                                        |
|                       |     "output_key": "ip_prefix"                                                                                                                           |
|                       |   },                                                                                                                                                    |
|                       |   {                                                                                                                                                     |
|                       |     "output_value": "b4f0c956-2fe0-4634-b7c8-22bfd8095aaf",                                                                                             |
|                       |     "description": "The name of the local subnet.",                                                                                                     |
|                       |     "output_key": "name"                                                                                                                                |
|                       |   },                                                                                                                                                    |
|                       |   {                                                                                                                                                     |
|                       |     "output_value": "172.16.101.1",                                                                                                                     |
|                       |     "description": "Default gateway of local subnet.",                                                                                                  |
|                       |     "output_key": "default_gateway"                                                                                                                     |
|                       |   },                                                                                                                                                    |
|                       |   {                                                                                                                                                     |
|                       |     "output_value": "bb69041d-c654-4e9f-a763-afd4333275bc",                                                                                             |
|                       |     "description": "A unique id for the network.",                                                                                                      |
|                       |     "output_key": "network_id"                                                                                                                          |
|                       |   },                                                                                                                                                    |
|                       |   {                                                                                                                                                     |
|                       |     "output_value": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",                                                                                             |
|                       |     "description": "IPAM this local subnet uses.",                                                                                                      |
|                       |     "output_key": "ipam"                                                                                                                                |
|                       |   },                                                                                                                                                    |
|                       |   {                                                                                                                                                     |
|                       |     "output_value": "8f9e2ede-c3b4-438e-888d-55e326ec29a9",                                                                                             |
|                       |     "description": "A unique id for the local subnet.",                                                                                                 |
|                       |     "output_key": "id"                                                                                                                                  |
|                       |   }                                                                                                                                                     |
|                       | ]                                                                                                                                                       |
| parameters            | {                                                                                                                                                       |
|                       |   "OS::stack_name": "subnet_b4f0c956-2fe0-4634-b7c8-22bfd8095aaf",                                                                                      |
|                       |   "enable_dhcp": "True",                                                                                                                                |
|                       |   "network_id": "bb69041d-c654-4e9f-a763-afd4333275bc",                                                                                                 |
|                       |   "ipam": "default-domain:default-project:default-network-ipam",                                                                                        |
|                       |   "dns_nameservers": "",                                                                                                                                |
|                       |   "dhcp_server_address": "172.16.101.2",                                                                                                                |
|                       |   "OS::stack_id": "ae4327f2-0f4c-460e-a370-2965a731cf8d",                                                                                               |
|                       |   "ntp_servers": "",                                                                                                                                    |
|                       |   "allocation_pools": "[{u'start': u'172.16.101.2', u'end': u'172.16.101.254'}]",                                                                       |
|                       |   "gateway_ip": "172.16.101.1",                                                                                                                         |
|                       |   "host_routes": "[]",                                                                                                                                  |
|                       |   "cidr": "172.16.101.0/24",                                                                                                                            |
|                       |   "name": "b4f0c956-2fe0-4634-b7c8-22bfd8095aaf"                                                                                                        |
|                       | }                                                                                                                                                       |
| parent                | None                                                                                                                                                    |
| stack_name            | subnet_b4f0c956-2fe0-4634-b7c8-22bfd8095aaf                                                                                                             |
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
$ heat template-show subnet_b4f0c956-2fe0-4634-b7c8-22bfd8095aaf
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
