# Stored data in etcd: Create Network (admin-net)

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/networks/168c1535-9001-49c7-bb05-21844570a83c
{
    "stack_id": "network_168c1535-9001-49c7-bb05-21844570a83c", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:168c1535-9001-49c7-bb05-21844570a83c", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "168c1535-9001-49c7-bb05-21844570a83c", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "168c1535-9001-49c7-bb05-21844570a83c", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "network:168c1535-9001-49c7-bb05-21844570a83c"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/networks/168c1535-9001-49c7-bb05-21844570a83c
{
    "heat_outputs": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:168c1535-9001-49c7-bb05-21844570a83c", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "168c1535-9001-49c7-bb05-21844570a83c", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "168c1535-9001-49c7-bb05-21844570a83c", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/networks/168c1535-9001-49c7-bb05-21844570a83c
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": [], \"description\": \"The name of the virtual network.\", \"output_key\": \"route_targets\"}, {\"output_value\": \"default-domain:usertenant:168c1535-9001-49c7-bb05-21844570a83c\", \"description\": \"The FQ name of the virtual network.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"168c1535-9001-49c7-bb05-21844570a83c\", \"description\": \"A unique id for the virtual network.\", \"output_key\": \"id\"}, {\"output_value\": \"168c1535-9001-49c7-bb05-21844570a83c\", \"description\": \"The name of the virtual network.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
