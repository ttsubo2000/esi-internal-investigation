# Stored data in etcd: Create Er Physical Interface

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/er_physical_interfaces/c2576120-00b0-461e-a2ae-f7bbff9465d0
{
    "stack_id": "er_physical_interface_c2576120-00b0-461e-a2ae-f7bbff9465d0", 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "23d9d390-e1e3-41c7-b926-479d6909aeeb", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/23d9d390-e1e3-41c7-b926-479d6909aeeb", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "er_physical_interface:c2576120-00b0-461e-a2ae-f7bbff9465d0"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/er_physical_interfaces/c2576120-00b0-461e-a2ae-f7bbff9465d0
{
    "heat_outputs": [
        {
            "output_value": "23d9d390-e1e3-41c7-b926-479d6909aeeb", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/23d9d390-e1e3-41c7-b926-479d6909aeeb", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/er_physical_interfaces/c2576120-00b0-461e-a2ae-f7bbff9465d0
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"23d9d390-e1e3-41c7-b926-479d6909aeeb\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/23d9d390-e1e3-41c7-b926-479d6909aeeb\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
