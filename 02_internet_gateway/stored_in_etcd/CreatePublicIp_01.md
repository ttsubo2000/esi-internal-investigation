# Stored data in etcd: Create Public Ip

No stored data for "heat_templates" in etcd.

![scope](../../images/esi_interface.011.png)

These are stored data for "Create Public Ip" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/public_ip_pools/5cd14f90-cf3c-4aeb-b30a-227b3c936761
{
    "body": {
        "pool_state": "UQEAAQAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==", 
        "addresses_available": 496, 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "internet_service_id": "848e04de-733d-4f98-8971-bdb3b83e0296", 
        "ip_version": 4, 
        "ha_router_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17", 
        "submask_length": 23, 
        "subnet_ip": "203.0.112.0", 
        "id": "5cd14f90-cf3c-4aeb-b30a-227b3c936761"
    }, 
    "version": 2, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/state/v2.0/public_ip_pools/5cd14f90-cf3c-4aeb-b30a-227b3c936761
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 2, 
    "error": ""
}
```
