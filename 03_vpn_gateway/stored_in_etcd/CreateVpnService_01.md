# Stored data in etcd: Create Vpn Service

No stored data for "heat_templates" in etcd.

![scope](../../images/esi_interface.011.png)

These are stored data for "Create Vpn Service" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/vpn_services/72b05fe5-88c6-4888-a6fb-feb793fffae8
{
    "body": {
        "uplink_interfaces": [
            "5e552b8f-cd5a-454c-a224-33f7da0afa24"
        ], 
        "description": "", 
        "zone": "jp1-zone1", 
        "default_static_routes_per_gateway": 32, 
        "ga_forwarding_class": "FC-VPN-GA", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "primary_ebgp_config_group": "VPNGW1-RI-EBGP", 
        "secondary_ibgp_config_group": "VPNGW2-RI-IBGP", 
        "primary_downlink_vrrp_config_group": "VPNGW1-VRRP", 
        "secondary_ebgp_config_group": "VPNGW2-RI-EBGP", 
        "downlink_interfaces": [
            "a3a62a37-5657-4822-98e0-991ab63f0e96"
        ], 
        "be_forwarding_class": "FC-VPN-BE", 
        "secondary_downlink_vrrp_config_group": "VPNGW2-VRRP", 
        "neighbour_prefix": "BGP-VIRTUAL-ROUTER-PEERS", 
        "primary_ibgp_config_group": "VPNGW1-RI-IBGP", 
        "id": "72b05fe5-88c6-4888-a6fb-feb793fffae8", 
        "name": "sample-vpn-service"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/state/v2.0/vpn_services/72b05fe5-88c6-4888-a6fb-feb793fffae8
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
