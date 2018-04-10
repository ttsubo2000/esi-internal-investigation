# Stored data in etcd: Create Common Function

```
/config/v2.0/common_function_pools/2d4a700d-bf94-4217-9a3c-4217a16c951f
{
    "body": {
        "dnat_pool_group_name": "DNAT-POOL", 
        "description": "sample common function pool", 
        "common_function_pool_state": "wAD//w==", 
        "tenant_id": "c583ce78843344adbe5fd20f13620274", 
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
            "16f6433d-0864-4d24-809d-c1b8e878280c"
        ], 
        "dnat_group_name": "DNAT-RULE", 
        "service_vrf_name": "SHARED-RESOURCE", 
        "logical_tunnel_interface_name": "lt-0/0/0", 
        "link_local_cidr": "169.254.0.0/17", 
        "service_interface_name": "ms-0/2/0", 
        "id": "2d4a700d-bf94-4217-9a3c-4217a16c951f", 
        "name": "common_function_pool"
    }, 
    "version": 3, 
    "marked_for_deletion": false
}
```
