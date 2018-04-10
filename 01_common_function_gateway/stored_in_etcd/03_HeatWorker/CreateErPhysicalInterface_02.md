# Stored data in etcd: Create Er Physical Interface

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/er_physical_interfaces/b9c7c1f4-1b90-4a7a-8161-34276bb2ed10
{
    "stack_id": "er_physical_interface_b9c7c1f4-1b90-4a7a-8161-34276bb2ed10", 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "17d442df-0ac4-4c5e-bbef-34fc7e4c4b06", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/17d442df-0ac4-4c5e-bbef-34fc7e4c4b06", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "er_physical_interface:b9c7c1f4-1b90-4a7a-8161-34276bb2ed10"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/er_physical_interfaces/b9c7c1f4-1b90-4a7a-8161-34276bb2ed10
{
    "heat_outputs": [
        {
            "output_value": "17d442df-0ac4-4c5e-bbef-34fc7e4c4b06", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/17d442df-0ac4-4c5e-bbef-34fc7e4c4b06", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/er_physical_interfaces/b9c7c1f4-1b90-4a7a-8161-34276bb2ed10
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"17d442df-0ac4-4c5e-bbef-34fc7e4c4b06\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/17d442df-0ac4-4c5e-bbef-34fc7e4c4b06\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
