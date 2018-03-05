# Stored data in etcd: Create Network (dummy-net)

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/networks/ce9a7a92-d11a-4fc6-8ae7-18061b62c98f
{
    "stack_id": "network_ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "network:ce9a7a92-d11a-4fc6-8ae7-18061b62c98f"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/networks/ce9a7a92-d11a-4fc6-8ae7-18061b62c98f
{
    "heat_outputs": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/networks/ce9a7a92-d11a-4fc6-8ae7-18061b62c98f
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": [], \"description\": \"The name of the virtual network.\", \"output_key\": \"route_targets\"}, {\"output_value\": \"default-domain:usertenant:ce9a7a92-d11a-4fc6-8ae7-18061b62c98f\", \"description\": \"The FQ name of the virtual network.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"ce9a7a92-d11a-4fc6-8ae7-18061b62c98f\", \"description\": \"A unique id for the virtual network.\", \"output_key\": \"id\"}, {\"output_value\": \"ce9a7a92-d11a-4fc6-8ae7-18061b62c98f\", \"description\": \"The name of the virtual network.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
