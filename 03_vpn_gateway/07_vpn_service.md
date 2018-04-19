[Return to Previous Page](00_vpn_gateway.md)

# 7. Clarification of interface in Sequence Diagram "Create Vpn Service"
You can see the relations of "Vpn Service" as following.

![Vpn Service](resource/gohan_investigate_for_vpngw.008.png)


## 7.1. Gohan

![scope](../images/ESI_Sequence_diagram.002.png)

### Outline
First of all, Gohan has received JSON data for "Create Vpn Service" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/vpn_services
```
```
{
    "vpn_service": {
        "be_forwarding_class": "FC-VPN-BE",
        "default_static_routes_per_gateway": 32,
        "downlink_interfaces": [
            "66bdfe91-b9e6-42f2-8942-bb4d4a67d5ba"
        ],
        "ga_forwarding_class": "FC-VPN-GA",
        "name": "sample-vpn-service",
        "neighbour_prefix": "BGP-VIRTUAL-ROUTER-PEERS",
        "primary_downlink_vrrp_config_group": "VPNGW1-VRRP",
        "primary_ebgp_config_group": "VPNGW1-RI-EBGP",
        "primary_ibgp_config_group": "VPNGW1-RI-IBGP",
        "secondary_downlink_vrrp_config_group": "VPNGW2-VRRP",
        "secondary_ebgp_config_group": "VPNGW2-RI-EBGP",
        "secondary_ibgp_config_group": "VPNGW2-RI-IBGP",
        "uplink_interfaces": [
            "c50006de-8afe-48fc-b7b8-37dc7617764a"
        ],
        "zone": "jp1-zone1",
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef"
    }
}
```
After processing, Gohan has stored data for "Create Vpn Service" in etcd

* [Checking stored data for creating "vpn_service"](stored_in_etcd/01_Gohan/CreateVpnService_01.md)


## 7.2. ResourceReader
When ResourceReader has started, it gets all of schemas from Gohan.
After that, these schemas are converted as a template_mappings.
And then, ResourceReader keeps storing template_mappings for following processing.

### Reference
* [Checking schemas in ResourceReader](../memo/schemas.txt)
* [Checking template_mappings in ResourceReader](../memo/template_mappings.md)

![scope](../images/ESI_Sequence_diagram.003.png)

### Outline
After fetching resource_data for "Create Vpn Service" in etcd, ResourceReader has not fetched heat_templates in etcd because of non_workable_resource.
And then, ResourceReader has stored data as finishing resource

* [Checking stored data for creating "vpn_service"](stored_in_etcd/00_ResourceReader/CreateVpnService_01.md)


## 7.3. Stored resource in gohan
As a result, checking resources regarding of "Vpn Service" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client vpn_service show --output-format json c8d57f7e-b439-475e-a6fb-ee2594390177
{
    "vpn_service": {
        "be_forwarding_class": "FC-VPN-BE",
        "default_static_routes_per_gateway": 32,
        "description": "",
        "downlink_interfaces": [
            "66bdfe91-b9e6-42f2-8942-bb4d4a67d5ba"
        ],
        "ga_forwarding_class": "FC-VPN-GA",
        "id": "c8d57f7e-b439-475e-a6fb-ee2594390177",
        "name": "sample-vpn-service",
        "neighbour_prefix": "BGP-VIRTUAL-ROUTER-PEERS",
        "primary_downlink_vrrp_config_group": "VPNGW1-VRRP",
        "primary_ebgp_config_group": "VPNGW1-RI-EBGP",
        "primary_ibgp_config_group": "VPNGW1-RI-IBGP",
        "secondary_downlink_vrrp_config_group": "VPNGW2-VRRP",
        "secondary_ebgp_config_group": "VPNGW2-RI-EBGP",
        "secondary_ibgp_config_group": "VPNGW2-RI-IBGP",
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
        "uplink_interfaces": [
            "c50006de-8afe-48fc-b7b8-37dc7617764a"
        ],
        "vrf_config": null,
        "zone": "jp1-zone1"
    }
}
```

[Return to Previous Page](00_vpn_gateway.md)
