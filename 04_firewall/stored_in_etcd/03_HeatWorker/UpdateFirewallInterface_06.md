# Stored data in etcd: Update Firewall Interface

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/ports/dea87c7b-b43f-4936-8e32-8995b038b3f8
{
    "stack_id": "", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "stack_status": "DELETE_COMPLETE", 
    "output": [], 
    "status_reason": "", 
    "id": "port:dea87c7b-b43f-4936-8e32-8995b038b3f8"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/ports/dea87c7b-b43f-4936-8e32-8995b038b3f8
{
    "heat_outputs": [], 
    "orchestration_state": "DELETE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/ports/dea87c7b-b43f-4936-8e32-8995b038b3f8
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
