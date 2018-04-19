# Stored data in etcd: Create Vpn Gateway

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/vpn_gateways/b1da850c-3344-4de2-aa18-d96a30b54f69
{
    "stack_id": "vpn_gateway_b1da850c-3344-4de2-aa18-d96a30b54f69", 
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "vpn_gateway:b1da850c-3344-4de2-aa18-d96a30b54f69"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/vpn_gateways/b1da850c-3344-4de2-aa18-d96a30b54f69
{
    "heat_outputs": [], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/vpn_gateways/b1da850c-3344-4de2-aa18-d96a30b54f69
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
