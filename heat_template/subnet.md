# heat_template: subnet
This is heat_template of "subnet" which is provided by gohan via etcd

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/subnet
{
    "body": {
        "handler": "heat_worker",
        "watch": [],
        "id": "subnet",
        "template_file": "heat_template_version: 2013-05-23\n\ndescription: >\n  Subnet template\n\nparameters:\n  name:\n    type: string\n    label: Local Subnet Name\n    description: Name of the local subnet that will be created.\n  network_id:\n    type: string\n    label: Network ID\n    description: ID of the network for which subnet will be created.\n  cidr:\n    type: string\n    label: Local Subnet IP prefix\n    description: IP prefix of the local subnet that will be created.\n  gateway_ip:\n    default: \"0.0.0.0\"\n    type: string\n    label: Default Gateway\n    description: Default gateway for the local subnet that will be created.\n  ipam:\n    type: string\n    label: IP Address Management\n    description: IPAM for the local subnet that will be created.\n    default: ''\n  enable_dhcp:\n    type: boolean\n    label: Enable DHCP\n    description: Enable DHCP\n    default: true\n  dhcp_server_address:\n    type: string\n    label: DHCP Server address\n    description: DHCP Server address\n    default: \"0.0.0.0\"\n  allocation_pools:\n    type: string\n    label: Allocation Pools\n    description: Allocation Pools\n    default: []\n  dns_nameservers:\n    type: comma_delimited_list\n    label: DNS Nameservers List\n    description: DNS Nameservers List\n    default: []\n  ntp_servers:\n    type: comma_delimited_list\n    label: NTP Nameservers List\n    description: NTP Nameservers List\n    default: []\n  host_routes:\n    type: json\n    label: Host Routes\n    description: Host Routes\n    default: []\n\nresources:\n  subnet:\n    type: OS::Contrail::VnSubnet\n    properties:\n      name: { get_param: name }\n      network_id: { get_param: network_id }\n      ip_prefix: { get_param: cidr }\n      default_gateway: { get_param: gateway_ip }\n      ipam: { get_param: ipam }\n      enable_dhcp: { get_param: enable_dhcp }\n      dns_server_address: { get_param: dhcp_server_address }\n      dns_nameservers: { get_param: dns_nameservers }\n      ntp_servers: { get_param: ntp_servers }\n      host_routes: { get_param: host_routes }\n      allocation_pools: { get_param: allocation_pools }\n      gateway_is_vrouter: false\n\noutputs:\n  id:\n    description: A unique id for the local subnet.\n    value: { get_resource: subnet }\n  name:\n    description: The name of the local subnet.\n    value: { get_attr: [subnet, name] }\n  network_id:\n    description: A unique id for the network.\n    value: { get_attr: [subnet, network_id] }\n  ip_prefix:\n    description: IP prefix of local subnet.\n    value: { get_attr: [subnet, ip_prefix] }\n  default_gateway:\n    description: Default gateway of local subnet.\n    value: { get_attr: [subnet, default_gateway] }\n  ipam:\n    description: IPAM this local subnet uses.\n    value: { get_attr: [subnet, ipam] }\n",
        "parameter_mappings": {
            "name": "Pid",
            "enable_dhcp": "Penable_dhcp",
            "network_id": "Mnetwork:network_id:id",
            "ipam": "Cdefault-domain:default-project:default-network-ipam",
            "dns_nameservers": "Pdns_nameservers",
            "heat_timeout": "C3",
            "dhcp_server_address": "Pdhcp_server_address",
            "ntp_servers": "Pntp_servers",
            "allocation_pools": "Pallocation_pools",
            "gateway_ip": "Pgateway_ip",
            "host_routes": "Phost_routes",
            "cidr": "Pcidr"
        }
    },
    "version": 1,
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* OS::Contrail::VnSubnet

```
heat_template_version: 2013-05-23

description: >
  Subnet template

parameters:
  name:
    type: string
    label: Local Subnet Name
    description: Name of the local subnet that will be created.
  network_id:
    type: string
    label: Network ID
    description: ID of the network for which subnet will be created.
  cidr:
    type: string
    label: Local Subnet IP prefix
    description: IP prefix of the local subnet that will be created.
  gateway_ip:
    default: "0.0.0.0"
    type: string
    label: Default Gateway
    description: Default gateway for the local subnet that will be created.
  ipam:
    type: string
    label: IP Address Management
    description: IPAM for the local subnet that will be created.
    default: ''
  enable_dhcp:
    type: boolean
    label: Enable DHCP
    description: Enable DHCP
    default: true
  dhcp_server_address:
    type: string
    label: DHCP Server address
    description: DHCP Server address
    default: "0.0.0.0"
  allocation_pools:
    type: string
    label: Allocation Pools
    description: Allocation Pools
    default: []
  dns_nameservers:
    type: comma_delimited_list
    label: DNS Nameservers List
    description: DNS Nameservers List
    default: []
  ntp_servers:
    type: comma_delimited_list
    label: NTP Nameservers List
    description: NTP Nameservers List
    default: []
  host_routes:
    type: json
    label: Host Routes
    description: Host Routes
    default: []

resources:
  subnet:
    type: OS::Contrail::VnSubnet
    properties:
      name: { get_param: name }
      network_id: { get_param: network_id }
      ip_prefix: { get_param: cidr }
      default_gateway: { get_param: gateway_ip }
      ipam: { get_param: ipam }
      enable_dhcp: { get_param: enable_dhcp }
      dns_server_address: { get_param: dhcp_server_address }
      dns_nameservers: { get_param: dns_nameservers }
      ntp_servers: { get_param: ntp_servers }
      host_routes: { get_param: host_routes }
      allocation_pools: { get_param: allocation_pools }
      gateway_is_vrouter: false

outputs:
  id:
    description: A unique id for the local subnet.
    value: { get_resource: subnet }
  name:
    description: The name of the local subnet.
    value: { get_attr: [subnet, name] }
  network_id:
    description: A unique id for the network.
    value: { get_attr: [subnet, network_id] }
  ip_prefix:
    description: IP prefix of local subnet.
    value: { get_attr: [subnet, ip_prefix] }
  default_gateway:
    description: Default gateway of local subnet.
    value: { get_attr: [subnet, default_gateway] }
  ipam:
    description: IPAM this local subnet uses.
    value: { get_attr: [subnet, ipam] }
```
