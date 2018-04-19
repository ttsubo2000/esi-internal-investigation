# Stored data in etcd: Create Er Physical Interface

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/er_physical_interfaces/3118d6be-b1cb-472a-805f-7e1ec46aa5e7
{
    "stack_id": "er_physical_interface_3118d6be-b1cb-472a-805f-7e1ec46aa5e7", 
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "e848bb97-1643-4167-9865-9a8b3b30b66f", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/e848bb97-1643-4167-9865-9a8b3b30b66f", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "er_physical_interface:3118d6be-b1cb-472a-805f-7e1ec46aa5e7"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/er_physical_interfaces/3118d6be-b1cb-472a-805f-7e1ec46aa5e7
{
    "heat_outputs": [
        {
            "output_value": "e848bb97-1643-4167-9865-9a8b3b30b66f", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/e848bb97-1643-4167-9865-9a8b3b30b66f", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/er_physical_interfaces/3118d6be-b1cb-472a-805f-7e1ec46aa5e7
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"e848bb97-1643-4167-9865-9a8b3b30b66f\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/e848bb97-1643-4167-9865-9a8b3b30b66f\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
