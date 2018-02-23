# Stored data in etcd: Create Common Function

These are stored data for "heat_templates" in etcd.

* common_function (no use)

![scope](../../images/esi_interface.009.png)

These are stored data for "Create Common Function" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/common_functions/18c64ec9-78c2-43ac-ae0d-48fa9b6c0858
{
    "body": {
        "link_local_ip_address": "169.254.1.227", 
        "status": "PENDING_CREATE", 
        "primary_vrrp_ip": "169.254.1.251", 
        "description": "", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "vrid": 41, 
        "secondary_vrrp_ip": "169.254.1.252", 
        "common_function_pool_id": "cca32fd7-2430-4acc-87e9-a7b527e9918d", 
        "shared_ip_address": "100.64.0.127", 
        "common_function_number": 1, 
        "ha_router_id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258", 
        "id": "18c64ec9-78c2-43ac-ae0d-48fa9b6c0858", 
        "name": "common_function1"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/state/v2.0/common_functions/18c64ec9-78c2-43ac-ae0d-48fa9b6c0858
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
