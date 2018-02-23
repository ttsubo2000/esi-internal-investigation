# Stored data in etcd: Create Nat Ip Pool

No stored data for "heat_templates" in etcd.

![scope](../../images/esi_interface.011.png)

These are stored data for "Create Nat Ip Pool" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/nat_ip_pools/75733e12-47f7-49ea-9939-2819df6c8253
{
    "body": {
        "description": "", 
        "ip_allocation_state": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB/8=", 
        "ip_ranges": [
            {
                "start": "100.64.0.10", 
                "end": "100.64.0.254"
            }
        ], 
        "common_function_pool_id": "cca32fd7-2430-4acc-87e9-a7b527e9918d", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "ha_router_id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258", 
        "id": "75733e12-47f7-49ea-9939-2819df6c8253", 
        "name": "sample-nat-ip-pool"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/state/v2.0/nat_ip_pools/75733e12-47f7-49ea-9939-2819df6c8253
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
