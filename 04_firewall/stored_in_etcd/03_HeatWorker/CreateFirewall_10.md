# Stored data in etcd: Create Firewall

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/firewall_interfaces/3543155d-0d9a-43a3-ae77-3479cf8a0e4a
{
    "stack_id": "firewall_interface_3543155d-0d9a-43a3-ae77-3479cf8a0e4a", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "d82baca9-9854-4da2-80c8-f823489be960", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/d82baca9-9854-4da2-80c8-f823489be960", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "firewall_interface:3543155d-0d9a-43a3-ae77-3479cf8a0e4a"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/firewall_interfaces/3543155d-0d9a-43a3-ae77-3479cf8a0e4a
{
    "heat_outputs": [
        {
            "output_value": "d82baca9-9854-4da2-80c8-f823489be960", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/d82baca9-9854-4da2-80c8-f823489be960", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd
```
/state/v2.0/firewall_interfaces/3543155d-0d9a-43a3-ae77-3479cf8a0e4a
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"d82baca9-9854-4da2-80c8-f823489be960\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/d82baca9-9854-4da2-80c8-f823489be960\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
