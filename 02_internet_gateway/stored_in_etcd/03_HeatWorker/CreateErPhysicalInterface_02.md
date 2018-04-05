# Stored data in etcd: Create Er Physical Interface

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/er_physical_interfaces/d108a472-81ab-43a0-8c49-e0d1a46e6128
{
    "stack_id": "er_physical_interface_d108a472-81ab-43a0-8c49-e0d1a46e6128", 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "79b7fc42-ebaf-4c34-adeb-20b43803a4fc", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/79b7fc42-ebaf-4c34-adeb-20b43803a4fc", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "er_physical_interface:d108a472-81ab-43a0-8c49-e0d1a46e6128"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/er_physical_interfaces/d108a472-81ab-43a0-8c49-e0d1a46e6128
{
    "heat_outputs": [
        {
            "output_value": "79b7fc42-ebaf-4c34-adeb-20b43803a4fc", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/79b7fc42-ebaf-4c34-adeb-20b43803a4fc", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/er_physical_interfaces/d108a472-81ab-43a0-8c49-e0d1a46e6128
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"79b7fc42-ebaf-4c34-adeb-20b43803a4fc\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/79b7fc42-ebaf-4c34-adeb-20b43803a4fc\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
