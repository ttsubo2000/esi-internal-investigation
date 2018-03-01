# Stored data in etcd: Create Port

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/ese_logical_ports/ced1435d-6dfa-4dab-bb7c-19da4d8e48b7
{
    "stack_id": "ese_logical_port_ced1435d-6dfa-4dab-bb7c-19da4d8e48b7", 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "9dcbbbbc-e9ea-4276-ba65-68ce8737e568", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "46b0cd68-d0fb-4d72-9def-830164f9e215", 
            "description": "A unique id for the logical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/9dcbbbbc-e9ea-4276-ba65-68ce8737e568", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }, 
        {
            "output_value": "xe-0/0/38.0", 
            "description": "The name of the logical interface.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "ese_logical_port:ced1435d-6dfa-4dab-bb7c-19da4d8e48b7"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/ese_logical_ports/ced1435d-6dfa-4dab-bb7c-19da4d8e48b7
{
    "heat_outputs": [
        {
            "output_value": "9dcbbbbc-e9ea-4276-ba65-68ce8737e568", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "46b0cd68-d0fb-4d72-9def-830164f9e215", 
            "description": "A unique id for the logical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/9dcbbbbc-e9ea-4276-ba65-68ce8737e568", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }, 
        {
            "output_value": "xe-0/0/38.0", 
            "description": "The name of the logical interface.", 
            "output_key": "name"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/ese_logical_ports/ced1435d-6dfa-4dab-bb7c-19da4d8e48b7
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"9dcbbbbc-e9ea-4276-ba65-68ce8737e568\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"46b0cd68-d0fb-4d72-9def-830164f9e215\", \"description\": \"A unique id for the logical interface\", \"output_key\": \"id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/9dcbbbbc-e9ea-4276-ba65-68ce8737e568\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}, {\"output_value\": \"xe-0/0/38.0\", \"description\": \"The name of the logical interface.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
