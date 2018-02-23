## Sample of heat-stack of subnet

* Checking heat-stack of subnet in heat-engine
```
$ openstack stack show subnet_ce0aeabc-a509-4834-a198-d25ed582092c
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                 | Value                                                                                                                                                        |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| id                    | 2f2dbe78-afec-4f64-a760-18a4623e323f                                                                                                                         |
| stack_name            | subnet_ce0aeabc-a509-4834-a198-d25ed582092c                                                                                                                  |
| description           | Subnet template                                                                                                                                              |
|                       |                                                                                                                                                              |
| creation_time         | 2016-11-07T06:17:34Z                                                                                                                                         |
| updated_time          | None                                                                                                                                                         |
| stack_status          | CREATE_COMPLETE                                                                                                                                              |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                                          |
| parameters            | OS::stack_id: 2f2dbe78-afec-4f64-a760-18a4623e323f                                                                                                           |
|                       | OS::stack_name: subnet_ce0aeabc-a509-4834-a198-d25ed582092c                                                                                                  |
|                       | allocation_pools: '[{u''start'': u''192.168.11.35'', u''end'': u''192.168.11.62''}]'                                                                         |
|                       | cidr: 192.168.11.32/27                                                                                                                                       |
|                       | dhcp_server_address: 192.168.11.35                                                                                                                           |
|                       | dns_nameservers: ''                                                                                                                                          |
|                       | enable_dhcp: 'True'                                                                                                                                          |
|                       | gateway_ip: 0.0.0.0                                                                                                                                          |
|                       | host_routes: '[{"nexthop": "192.168.11.36", "destination": "192.168.11.0/30"}, {"nexthop":                                                                   |
|                       |   "192.168.11.36", "destination": "172.23.16.0/24"}]'                                                                                                        |
|                       | ipam: default-domain:default-project:default-network-ipam                                                                                                    |
|                       | name: ce0aeabc-a509-4834-a198-d25ed582092c                                                                                                                   |
|                       | network_id: 23489ede-80ae-429f-a187-20586e8ba0f4                                                                                                             |
|                       | ntp_servers: ''                                                                                                                                              |
|                       |                                                                                                                                                              |
| outputs               | - description: IP prefix of local subnet.                                                                                                                    |
|                       |   output_key: ip_prefix                                                                                                                                      |
|                       |   output_value: 192.168.11.32/27                                                                                                                             |
|                       | - description: The name of the local subnet.                                                                                                                 |
|                       |   output_key: name                                                                                                                                           |
|                       |   output_value: ce0aeabc-a509-4834-a198-d25ed582092c                                                                                                         |
|                       | - description: Default gateway of local subnet.                                                                                                              |
|                       |   output_key: default_gateway                                                                                                                                |
|                       |   output_value: 0.0.0.0                                                                                                                                      |
|                       | - description: A unique id for the network.                                                                                                                  |
|                       |   output_key: network_id                                                                                                                                     |
|                       |   output_value: 23489ede-80ae-429f-a187-20586e8ba0f4                                                                                                         |
|                       | - description: IPAM this local subnet uses.                                                                                                                  |
|                       |   output_key: ipam                                                                                                                                           |
|                       |   output_value: 0b58462c-a502-4e7f-9cde-f3a0e49c8e29                                                                                                         |
|                       | - description: A unique id for the local subnet.                                                                                                             |
|                       |   output_key: id                                                                                                                                             |
|                       |   output_value: 498d2eb1-1eab-4a0a-bb58-8a979d5f5363                                                                                                         |
|                       |                                                                                                                                                              |
| links                 | - href: http://172.23.16.61:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/subnet_ce0aeabc-a509-4834-a198-d25ed582092c/2f2dbe78-afec-4f64-a760-18a4623e323f |
|                       |   rel: self                                                                                                                                                  |
|                       |                                                                                                                                                              |
| parent                | None                                                                                                                                                         |
| disable_rollback      | True                                                                                                                                                         |
| stack_user_project_id | aee85dff980f4b0f94bed7861765acc7                                                                                                                             |
| stack_owner           | sdp_esi_admin                                                                                                                                                |
| capabilities          | []                                                                                                                                                           |
| notification_topics   | []                                                                                                                                                           |
| timeout_mins          | 10                                                                                                                                                           |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

* Checking heat-template of subnet in heat-engine
```
$ openstack stack template show subnet_ce0aeabc-a509-4834-a198-d25ed582092c
description: 'Subnet template

  '
heat_template_version: '2013-05-23'
outputs:
  default_gateway:
    description: Default gateway of local subnet.
    value:
      get_attr:
      - subnet
      - default_gateway
  id:
    description: A unique id for the local subnet.
    value:
      get_resource: subnet
  ip_prefix:
    description: IP prefix of local subnet.
    value:
      get_attr:
      - subnet
      - ip_prefix
  ipam:
    description: IPAM this local subnet uses.
    value:
      get_attr:
      - subnet
      - ipam
  name:
    description: The name of the local subnet.
    value:
      get_attr:
      - subnet
      - name
  network_id:
    description: A unique id for the network.
    value:
      get_attr:
      - subnet
      - network_id
parameters:
  allocation_pools:
    default: []
    description: Allocation Pools
    label: Allocation Pools
    type: string
  cidr:
    description: IP prefix of the local subnet that will be created.
    label: Local Subnet IP prefix
    type: string
  dhcp_server_address:
    default: 0.0.0.0
    description: DHCP Server address
    label: DHCP Server address
    type: string
  dns_nameservers:
    default: []
    description: DNS Nameservers List
    label: DNS Nameservers List
    type: comma_delimited_list
  enable_dhcp:
    default: true
    description: Enable DHCP
    label: Enable DHCP
    type: boolean
  gateway_ip:
    default: 0.0.0.0
    description: Default gateway for the local subnet that will be created.
    label: Default Gateway
    type: string
  host_routes:
    default: []
    description: Host Routes
    label: Host Routes
    type: json
  ipam:
    default: ''
    description: IPAM for the local subnet that will be created.
    label: IP Address Management
    type: string
  name:
    description: Name of the local subnet that will be created.
    label: Local Subnet Name
    type: string
  network_id:
    description: ID of the network for which subnet will be created.
    label: Network ID
    type: string
  ntp_servers:
    default: []
    description: NTP Nameservers List
    label: NTP Nameservers List
    type: comma_delimited_list
resources:
  subnet:
    properties:
      allocation_pools:
        get_param: allocation_pools
      default_gateway:
        get_param: gateway_ip
      dns_nameservers:
        get_param: dns_nameservers
      dns_server_address:
        get_param: dhcp_server_address
      enable_dhcp:
        get_param: enable_dhcp
      gateway_is_vrouter: false
      host_routes:
        get_param: host_routes
      ip_prefix:
        get_param: cidr
      ipam:
        get_param: ipam
      name:
        get_param: name
      network_id:
        get_param: network_id
      ntp_servers:
        get_param: ntp_servers
    type: OS::Contrail::VnSubnet
```

* Checking resource-list of subnet in heat-engine
```
$ openstack stack resource list subnet_ce0aeabc-a509-4834-a198-d25ed582092c
+---------------+--------------------------------------+------------------------+-----------------+----------------------+
| resource_name | physical_resource_id                 | resource_type          | resource_status | updated_time         |
+---------------+--------------------------------------+------------------------+-----------------+----------------------+
| subnet        | 498d2eb1-1eab-4a0a-bb58-8a979d5f5363 | OS::Contrail::VnSubnet | CREATE_COMPLETE | 2016-11-07T06:17:34Z |
+---------------+--------------------------------------+------------------------+-----------------+----------------------+
```

* Checking resource-show of subnet in heat-engine
```
$ openstack stack resource show subnet_ce0aeabc-a509-4834-a198-d25ed582092c subnet
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                  | Value                                                                                                                                                           |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| description            |                                                                                                                                                                 |
| links                  | [{u'href': u'http://172.23.16.61:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/subnet_ce0aeabc-a509-4834-a198-d25ed582092c/2f2dbe78-afec-                     |
|                        | 4f64-a760-18a4623e323f/resources/subnet', u'rel': u'self'}, {u'href':                                                                                           |
|                        | u'http://172.23.16.61:8004/v1/aee85dff980f4b0f94bed7861765acc7/stacks/subnet_ce0aeabc-a509-4834-a198-d25ed582092c/2f2dbe78-afec-4f64-a760-18a4623e323f',        |
|                        | u'rel': u'stack'}]                                                                                                                                              |
| logical_resource_id    | subnet                                                                                                                                                          |
| physical_resource_id   | 498d2eb1-1eab-4a0a-bb58-8a979d5f5363                                                                                                                            |
| required_by            | []                                                                                                                                                              |
| resource_name          | subnet                                                                                                                                                          |
| resource_status        | CREATE_COMPLETE                                                                                                                                                 |
| resource_status_reason | state changed                                                                                                                                                   |
| resource_type          | OS::Contrail::VnSubnet                                                                                                                                          |
| updated_time           | 2016-11-07T06:17:34Z                                                                                                                                            |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
