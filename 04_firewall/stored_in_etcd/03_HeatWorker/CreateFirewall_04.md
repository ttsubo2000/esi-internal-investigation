# Stored data in etcd: Create Firewall

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/vnf_instances/44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb
{
    "stack_id": "vnf_instance_44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "2e555b09-e0d7-4cce-8854-c481a2363917", 
            "description": "A unique id for the nova server.", 
            "output_key": "server_id"
        }, 
        {
            "output_value": "4d5db024-8232-458d-bd72-7256fbceb446", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/4d5db024-8232-458d-bd72-7256fbceb446", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "vnf_instance:44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/vnf_instances/44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb
{
    "heat_outputs": [
        {
            "output_value": "2e555b09-e0d7-4cce-8854-c481a2363917", 
            "description": "A unique id for the nova server.", 
            "output_key": "server_id"
        }, 
        {
            "output_value": "4d5db024-8232-458d-bd72-7256fbceb446", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/4d5db024-8232-458d-bd72-7256fbceb446", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/vnf_instances/44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"2e555b09-e0d7-4cce-8854-c481a2363917\", \"description\": \"A unique id for the nova server.\", \"output_key\": \"server_id\"}, {\"output_value\": \"4d5db024-8232-458d-bd72-7256fbceb446\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/4d5db024-8232-458d-bd72-7256fbceb446\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
