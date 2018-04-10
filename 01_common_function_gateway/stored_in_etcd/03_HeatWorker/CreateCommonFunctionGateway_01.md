# Stored data in etcd: Create Common Function Gateway

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/networks/fc8814a7-eb1e-4f59-8422-7de500e72782
{
    "stack_id": "network_fc8814a7-eb1e-4f59-8422-7de500e72782", 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:fc8814a7-eb1e-4f59-8422-7de500e72782", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "fc8814a7-eb1e-4f59-8422-7de500e72782", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "fc8814a7-eb1e-4f59-8422-7de500e72782", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "network:fc8814a7-eb1e-4f59-8422-7de500e72782"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/networks/fc8814a7-eb1e-4f59-8422-7de500e72782
{
    "heat_outputs": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:fc8814a7-eb1e-4f59-8422-7de500e72782", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "fc8814a7-eb1e-4f59-8422-7de500e72782", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "fc8814a7-eb1e-4f59-8422-7de500e72782", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/networks/fc8814a7-eb1e-4f59-8422-7de500e72782
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": [], \"description\": \"The name of the virtual network.\", \"output_key\": \"route_targets\"}, {\"output_value\": \"default-domain:usertenant:fc8814a7-eb1e-4f59-8422-7de500e72782\", \"description\": \"The FQ name of the virtual network.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"fc8814a7-eb1e-4f59-8422-7de500e72782\", \"description\": \"A unique id for the virtual network.\", \"output_key\": \"id\"}, {\"output_value\": \"fc8814a7-eb1e-4f59-8422-7de500e72782\", \"description\": \"The name of the virtual network.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
