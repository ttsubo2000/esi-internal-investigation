# Stored data in etcd: Create Er Physical Interface

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/er_physical_interfaces/c8e2d558-02ee-4bf3-ba5b-958821a21043
{
    "stack_id": "er_physical_interface_c8e2d558-02ee-4bf3-ba5b-958821a21043", 
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "81b1e3e1-1182-4431-9c0f-9e430ec29a09", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/81b1e3e1-1182-4431-9c0f-9e430ec29a09", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "er_physical_interface:c8e2d558-02ee-4bf3-ba5b-958821a21043"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/er_physical_interfaces/c8e2d558-02ee-4bf3-ba5b-958821a21043
{
    "heat_outputs": [
        {
            "output_value": "81b1e3e1-1182-4431-9c0f-9e430ec29a09", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/81b1e3e1-1182-4431-9c0f-9e430ec29a09", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/er_physical_interfaces/c8e2d558-02ee-4bf3-ba5b-958821a21043
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"81b1e3e1-1182-4431-9c0f-9e430ec29a09\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/81b1e3e1-1182-4431-9c0f-9e430ec29a09\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
