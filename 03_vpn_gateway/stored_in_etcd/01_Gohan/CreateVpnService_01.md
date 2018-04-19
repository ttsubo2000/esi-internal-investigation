# Stored data in etcd: Create Vpn Service

```
/config/v2.0/vpn_services/c8d57f7e-b439-475e-a6fb-ee2594390177
{
    "body": {
        "uplink_interfaces": [
            "c50006de-8afe-48fc-b7b8-37dc7617764a"
        ], 
        "description": "", 
        "zone": "jp1-zone1", 
        "default_static_routes_per_gateway": 32, 
        "ga_forwarding_class": "FC-VPN-GA", 
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
        "primary_ebgp_config_group": "VPNGW1-RI-EBGP", 
        "secondary_ibgp_config_group": "VPNGW2-RI-IBGP", 
        "primary_downlink_vrrp_config_group": "VPNGW1-VRRP", 
        "secondary_ebgp_config_group": "VPNGW2-RI-EBGP", 
        "downlink_interfaces": [
            "66bdfe91-b9e6-42f2-8942-bb4d4a67d5ba"
        ], 
        "be_forwarding_class": "FC-VPN-BE", 
        "secondary_downlink_vrrp_config_group": "VPNGW2-VRRP", 
        "neighbour_prefix": "BGP-VIRTUAL-ROUTER-PEERS", 
        "primary_ibgp_config_group": "VPNGW1-RI-IBGP", 
        "id": "c8d57f7e-b439-475e-a6fb-ee2594390177", 
        "name": "sample-vpn-service"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
