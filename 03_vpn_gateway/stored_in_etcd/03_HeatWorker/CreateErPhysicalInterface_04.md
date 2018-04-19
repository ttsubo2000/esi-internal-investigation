# Stored data in etcd: Create Er Physical Interface

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/er_physical_interfaces/2bc8e40d-ab01-4738-a4aa-e69d8fd30688
{
    "stack_id": "er_physical_interface_2bc8e40d-ab01-4738-a4aa-e69d8fd30688", 
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "d80c91c1-a82c-4742-b571-03c17cbeff1c", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/d80c91c1-a82c-4742-b571-03c17cbeff1c", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "er_physical_interface:2bc8e40d-ab01-4738-a4aa-e69d8fd30688"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/er_physical_interfaces/2bc8e40d-ab01-4738-a4aa-e69d8fd30688
{
    "heat_outputs": [
        {
            "output_value": "d80c91c1-a82c-4742-b571-03c17cbeff1c", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/d80c91c1-a82c-4742-b571-03c17cbeff1c", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/er_physical_interfaces/2bc8e40d-ab01-4738-a4aa-e69d8fd30688
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"d80c91c1-a82c-4742-b571-03c17cbeff1c\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/d80c91c1-a82c-4742-b571-03c17cbeff1c\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
