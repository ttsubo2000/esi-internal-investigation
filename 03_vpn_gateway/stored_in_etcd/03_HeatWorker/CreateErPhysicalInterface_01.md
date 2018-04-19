# Stored data in etcd: Create Er Physical Interface

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/er_physical_interfaces/f3ecf585-5c3b-445a-97a7-d8e124c99e16
{
    "stack_id": "er_physical_interface_f3ecf585-5c3b-445a-97a7-d8e124c99e16", 
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "03bc2bdc-e6b0-4ae6-acda-b76a5da84fb6", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/03bc2bdc-e6b0-4ae6-acda-b76a5da84fb6", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "er_physical_interface:f3ecf585-5c3b-445a-97a7-d8e124c99e16"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/er_physical_interfaces/f3ecf585-5c3b-445a-97a7-d8e124c99e16
{
    "heat_outputs": [
        {
            "output_value": "03bc2bdc-e6b0-4ae6-acda-b76a5da84fb6", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/03bc2bdc-e6b0-4ae6-acda-b76a5da84fb6", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/er_physical_interfaces/f3ecf585-5c3b-445a-97a7-d8e124c99e16
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"03bc2bdc-e6b0-4ae6-acda-b76a5da84fb6\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/03bc2bdc-e6b0-4ae6-acda-b76a5da84fb6\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
