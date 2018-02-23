# Stored data in etcd: Create Internet Service

No stored data for "heat_templates" in etcd.

![scope](../../images/esi_interface.011.png)

These are stored data for "Create Internet Service" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/internet_services/848e04de-733d-4f98-8971-bdb3b83e0296
{
    "body": {
        "vrf_export_policy": "INSTANCE-USER_OUT", 
        "primary_ibgp_config_group": "InetGW2-RI-IBGP", 
        "description": "", 
        "zone": "jp1-zone1", 
        "default_static_routes_per_gateway": 32, 
        "ga_forwarding_class": "FC-INET-GA", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "inet_out_filter": "INET_OUT", 
        "secondary_ibgp_config_group": "InetGW1-RI-IBGP", 
        "vrf_config": "", 
        "name": "sample-internet-service", 
        "secondary_vrrp_config_group": "InetGW2-VRRP", 
        "uplink_import_policy": "INSTANCE-MASTER_IN", 
        "primary_vrrp_config_group": "InetGW1-VRRP", 
        "downlink_interfaces": [
            "1205d3f2-7568-412a-a554-012340ab3172"
        ], 
        "be_forwarding_class": "FC-INET-BE", 
        "neighbour_prefix": "BGP-VIRTUAL-ROUTER-PEERS", 
        "inet_in_filter": "INET_IN", 
        "id": "848e04de-733d-4f98-8971-bdb3b83e0296", 
        "vrf_import_policy": "INSTANCE-USER_IN", 
        "minimal_submask_length": 26
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/state/v2.0/internet_services/848e04de-733d-4f98-8971-bdb3b83e0296
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
