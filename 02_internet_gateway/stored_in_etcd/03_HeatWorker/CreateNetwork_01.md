# Stored data in etcd: Create Network

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/networks/6e557507-1c2a-49b1-ba90-5f616a1f1f3e
{
    "stack_id": "network_6e557507-1c2a-49b1-ba90-5f616a1f1f3e", 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:6e557507-1c2a-49b1-ba90-5f616a1f1f3e", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "network:6e557507-1c2a-49b1-ba90-5f616a1f1f3e"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/networks/6e557507-1c2a-49b1-ba90-5f616a1f1f3e
{
    "heat_outputs": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:6e557507-1c2a-49b1-ba90-5f616a1f1f3e", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/networks/6e557507-1c2a-49b1-ba90-5f616a1f1f3e
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": [], \"description\": \"The name of the virtual network.\", \"output_key\": \"route_targets\"}, {\"output_value\": \"default-domain:usertenant:6e557507-1c2a-49b1-ba90-5f616a1f1f3e\", \"description\": \"The FQ name of the virtual network.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"6e557507-1c2a-49b1-ba90-5f616a1f1f3e\", \"description\": \"A unique id for the virtual network.\", \"output_key\": \"id\"}, {\"output_value\": \"6e557507-1c2a-49b1-ba90-5f616a1f1f3e\", \"description\": \"The name of the virtual network.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
