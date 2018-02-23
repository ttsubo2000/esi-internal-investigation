# Stored data in etcd: Create Common Function

No stored data for "heat_templates" in etcd.

![scope](../../images/esi_interface.011.png)

These are stored data for "Create Common Function" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/common_function_pools/cca32fd7-2430-4acc-87e9-a7b527e9918d
{
    "body": {
        "dnat_pool_group_name": "DNAT-POOL", 
        "description": "sample common function pool", 
        "common_function_pool_state": "gAD//w==", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "link_local_netmask": 17, 
        "vrrp_group_name": "IF-USER-VRRP-ACT", 
        "vrrp_config": [
            {
                "vrid": 41, 
                "primary_ip": "169.254.1.251", 
                "secondary_ip": "169.254.1.252"
            }, 
            {
                "vrid": 42, 
                "primary_ip": "169.254.1.253", 
                "secondary_ip": "169.254.1.254"
            }
        ], 
        "snapt_group_name": "SNAPT-RULE", 
        "snapt_pool_group_name": "SNAPT-POOL", 
        "downlink_interfaces": [
            "372ed357-e622-41fb-a613-076d332838e2"
        ], 
        "dnat_group_name": "DNAT-RULE", 
        "service_vrf_name": "SHARED-RESOURCE", 
        "logical_tunnel_interface_name": "lt-0/0/0", 
        "link_local_cidr": "169.254.0.0/17", 
        "service_interface_name": "ms-0/2/0", 
        "id": "cca32fd7-2430-4acc-87e9-a7b527e9918d", 
        "name": "common_function_pool"
    }, 
    "version": 2, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/state/v2.0/common_function_pools/cca32fd7-2430-4acc-87e9-a7b527e9918d
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 2, 
    "error": ""
}
```
