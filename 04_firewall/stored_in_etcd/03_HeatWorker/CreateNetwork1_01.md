# Stored data in etcd: Create Network (dummy-net)

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/networks/73b2c401-a1f3-49fb-8612-8c755b37a28d
{
    "stack_id": "network_73b2c401-a1f3-49fb-8612-8c755b37a28d", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:73b2c401-a1f3-49fb-8612-8c755b37a28d", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "network:73b2c401-a1f3-49fb-8612-8c755b37a28d"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/networks/73b2c401-a1f3-49fb-8612-8c755b37a28d
{
    "heat_outputs": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:73b2c401-a1f3-49fb-8612-8c755b37a28d", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/networks/73b2c401-a1f3-49fb-8612-8c755b37a28d
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": [], \"description\": \"The name of the virtual network.\", \"output_key\": \"route_targets\"}, {\"output_value\": \"default-domain:usertenant:73b2c401-a1f3-49fb-8612-8c755b37a28d\", \"description\": \"The FQ name of the virtual network.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"73b2c401-a1f3-49fb-8612-8c755b37a28d\", \"description\": \"A unique id for the virtual network.\", \"output_key\": \"id\"}, {\"output_value\": \"73b2c401-a1f3-49fb-8612-8c755b37a28d\", \"description\": \"The name of the virtual network.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
