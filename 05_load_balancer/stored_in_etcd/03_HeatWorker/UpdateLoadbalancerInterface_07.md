# Stored data in etcd: Update Loadbalancer Interface

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/ports/db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc
{
    "stack_id": "", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "DELETE_COMPLETE", 
    "output": [], 
    "status_reason": "", 
    "id": "port:db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/ports/db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc
{
    "heat_outputs": [], 
    "orchestration_state": "DELETE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/ports/db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc
{
    "state": {
        "worker_state": "DELETE_COMPLETED", 
        "heat_outputs": "[]", 
        "orchestration_state": "DELETE_COMPLETE"
    }, 
    "version": 4, 
    "error": ""
}
```
