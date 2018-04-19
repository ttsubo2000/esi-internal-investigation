# Stored data in etcd: Create Network

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/networks/afa0d9d6-84dc-4755-9c6e-db2f23f9dde2
{
    "stack_id": "network_afa0d9d6-84dc-4755-9c6e-db2f23f9dde2", 
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:afa0d9d6-84dc-4755-9c6e-db2f23f9dde2", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "network:afa0d9d6-84dc-4755-9c6e-db2f23f9dde2"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/networks/afa0d9d6-84dc-4755-9c6e-db2f23f9dde2
{
    "heat_outputs": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:afa0d9d6-84dc-4755-9c6e-db2f23f9dde2", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/networks/afa0d9d6-84dc-4755-9c6e-db2f23f9dde2
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": [], \"description\": \"The name of the virtual network.\", \"output_key\": \"route_targets\"}, {\"output_value\": \"default-domain:usertenant:afa0d9d6-84dc-4755-9c6e-db2f23f9dde2\", \"description\": \"The FQ name of the virtual network.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"afa0d9d6-84dc-4755-9c6e-db2f23f9dde2\", \"description\": \"A unique id for the virtual network.\", \"output_key\": \"id\"}, {\"output_value\": \"afa0d9d6-84dc-4755-9c6e-db2f23f9dde2\", \"description\": \"The name of the virtual network.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
