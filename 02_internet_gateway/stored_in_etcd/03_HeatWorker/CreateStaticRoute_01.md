# Stored data in etcd: Create Static Route

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/static_routes/d0aa20b1-9302-4b43-a3c1-9edce0811af8
{
    "stack_id": "static_route_d0aa20b1-9302-4b43-a3c1-9edce0811af8", 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "static_route:d0aa20b1-9302-4b43-a3c1-9edce0811af8"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/static_routes/d0aa20b1-9302-4b43-a3c1-9edce0811af8
{
    "heat_outputs": [], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/static_routes/d0aa20b1-9302-4b43-a3c1-9edce0811af8
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
