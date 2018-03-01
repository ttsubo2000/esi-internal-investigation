# Stored data in etcd: Create Network

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/networks/35bc496f-3c0e-46b4-a5c0-33810e8e7263
{
    "stack_id": "network_35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "network:35bc496f-3c0e-46b4-a5c0-33810e8e7263"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/networks/35bc496f-3c0e-46b4-a5c0-33810e8e7263
{
    "heat_outputs": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/networks/35bc496f-3c0e-46b4-a5c0-33810e8e7263
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": [], \"description\": \"The name of the virtual network.\", \"output_key\": \"route_targets\"}, {\"output_value\": \"default-domain:usertenant:35bc496f-3c0e-46b4-a5c0-33810e8e7263\", \"description\": \"The FQ name of the virtual network.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"35bc496f-3c0e-46b4-a5c0-33810e8e7263\", \"description\": \"A unique id for the virtual network.\", \"output_key\": \"id\"}, {\"output_value\": \"35bc496f-3c0e-46b4-a5c0-33810e8e7263\", \"description\": \"The name of the virtual network.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
