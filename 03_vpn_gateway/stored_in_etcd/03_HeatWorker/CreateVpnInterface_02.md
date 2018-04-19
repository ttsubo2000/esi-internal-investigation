# Stored data in etcd: Create Vpn Interface

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/vpn_gateways/b1da850c-3344-4de2-aa18-d96a30b54f69
{
    "stack_id": "vpn_gateway_b1da850c-3344-4de2-aa18-d96a30b54f69", 
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
    "stack_status": "UPDATE_COMPLETE", 
    "output": [], 
    "status_reason": "Stack successfully updated", 
    "id": "vpn_gateway:b1da850c-3344-4de2-aa18-d96a30b54f69"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/vpn_gateways/b1da850c-3344-4de2-aa18-d96a30b54f69
{
    "heat_outputs": [], 
    "orchestration_state": "UPDATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/vpn_gateways/b1da850c-3344-4de2-aa18-d96a30b54f69
{
    "state": {
        "worker_state": "MODIFY_COMPLETED", 
        "heat_outputs": "[]", 
        "orchestration_state": "UPDATE_COMPLETE"
    }, 
    "version": 2, 
    "error": ""
}
```
