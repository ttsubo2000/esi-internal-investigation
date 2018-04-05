[Return to Previous Page](00_internet_gateway.md)

# 7. Clarification of interface in Sequence Diagram "Create Internet Service"
You can see the relations of "Internet Service" as following.

![Internet Service](resource/gohan_investigate_for_inetgw.008.png)


## 7.1. Gohan

![scope](../images/ESI_Sequence_diagram.002.png)

### Outline
First of all, Gohan has received JSON data for "Create Internet Service" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/internet_services
```
```
{
    "internet_service": {
        "be_forwarding_class": "FC-INET-BE",
        "default_static_routes_per_gateway": 32,
        "downlink_interfaces": [
            "2595e193-84a8-49dc-aa2e-7a68c60ea11e"
        ],
        "ga_forwarding_class": "FC-INET-GA",
        "inet_in_filter": "INET_IN",
        "inet_out_filter": "INET_OUT",
        "minimal_submask_length": 26,
        "name": "sample-internet-service",
        "neighbour_prefix": "BGP-VIRTUAL-ROUTER-PEERS",
        "primary_ibgp_config_group": "InetGW2-RI-IBGP",
        "primary_vrrp_config_group": "InetGW1-VRRP",
        "secondary_ibgp_config_group": "InetGW1-RI-IBGP",
        "secondary_vrrp_config_group": "InetGW2-VRRP",
        "uplink_import_policy": "INSTANCE-MASTER_IN",
        "vrf_export_policy": "INSTANCE-USER_OUT",
        "vrf_import_policy": "INSTANCE-USER_IN",
        "zone": "jp1-zone1",
        "tenant_id": "06d6b792b31c40daa546fb0f4e35980d"
    }
}
```
After processing, Gohan has stored data for "Create Internet Service" in etcd

* [Checking stored data for creating "internet_service"](stored_in_etcd/01_Gohan/CreateInternetService_01.md)


## 7.2. ResourceReader
When ResourceReader has started, it gets all of schemas from Gohan.
After that, these schemas are converted as a template_mappings.
And then, ResourceReader keeps storing template_mappings for following processing.

### Reference
* [Checking schemas in ResourceReader](../memo/schemas.txt)
* [Checking template_mappings in ResourceReader](../memo/template_mappings.md)

![scope](../images/ESI_Sequence_diagram.003.png)

### Outline
After fetching resource_data for "Create Internet Service" in etcd, ResourceReader has not fetched heat_templates in etcd because of non_workable_resource.
And then, ResourceReader has stored data as finishing resource

* [Checking stored data for creating "internet_service"](stored_in_etcd/00_ResourceReader/CreateInternetService_01.md)


## 7.3. Stored resource in gohan
As a result, checking resources regarding of "Internet Service" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client internet_service show --output-format json 986a140f-81da-4e5c-afc3-26f463a85786
{
    "internet_service": {
        "be_forwarding_class": "FC-INET-BE",
        "default_static_routes_per_gateway": 32,
        "description": "",
        "downlink_interfaces": [
            "2595e193-84a8-49dc-aa2e-7a68c60ea11e"
        ],
        "ga_forwarding_class": "FC-INET-GA",
        "id": "986a140f-81da-4e5c-afc3-26f463a85786",
        "inet_in_filter": "INET_IN",
        "inet_out_filter": "INET_OUT",
        "minimal_submask_length": 26,
        "name": "sample-internet-service",
        "neighbour_prefix": "BGP-VIRTUAL-ROUTER-PEERS",
        "primary_ibgp_config_group": "InetGW2-RI-IBGP",
        "primary_vrrp_config_group": "InetGW1-VRRP",
        "secondary_ibgp_config_group": "InetGW1-RI-IBGP",
        "secondary_vrrp_config_group": "InetGW2-VRRP",
        "tenant_id": "06d6b792b31c40daa546fb0f4e35980d",
        "uplink_import_policy": "INSTANCE-MASTER_IN",
        "vrf_config": "",
        "vrf_export_policy": "INSTANCE-USER_OUT",
        "vrf_import_policy": "INSTANCE-USER_IN",
        "zone": "jp1-zone1"
    }
}
```

[Return to Previous Page](00_internet_gateway.md)
