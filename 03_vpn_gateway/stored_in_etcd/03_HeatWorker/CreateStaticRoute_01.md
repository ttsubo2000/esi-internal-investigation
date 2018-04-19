# Stored data in etcd: Create Static Route

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/static_routes/31980341-9bef-4f05-8df7-674dea343884
{
    "stack_id": "static_route_31980341-9bef-4f05-8df7-674dea343884", 
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "static_route:31980341-9bef-4f05-8df7-674dea343884"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/static_routes/31980341-9bef-4f05-8df7-674dea343884
{
    "heat_outputs": [], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/static_routes/31980341-9bef-4f05-8df7-674dea343884
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
