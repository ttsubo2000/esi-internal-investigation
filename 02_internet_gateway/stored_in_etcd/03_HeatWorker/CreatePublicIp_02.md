# Stored data in etcd: Create Public Ip

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/public_ips/d5622781-f06a-4fad-b800-b577a05ad8b2
{
    "stack_id": "public_ip_d5622781-f06a-4fad-b800-b577a05ad8b2", 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "public_ip:d5622781-f06a-4fad-b800-b577a05ad8b2"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/public_ips/d5622781-f06a-4fad-b800-b577a05ad8b2
{
    "heat_outputs": [], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/public_ips/d5622781-f06a-4fad-b800-b577a05ad8b2
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
