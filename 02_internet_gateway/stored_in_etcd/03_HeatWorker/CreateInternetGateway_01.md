# Stored data in etcd: Create Internet Gateway

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/internet_gateways/f6e8c695-c4c1-4a93-9b7e-1663aee6dec9
{
    "stack_id": "internet_gateway_f6e8c695-c4c1-4a93-9b7e-1663aee6dec9", 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "ca354a39-f48c-4698-9cdd-9e106e2a5bf4", 
            "description": "Monitoring Target ID", 
            "output_key": "primary_monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/e4609dae-5c88-494a-bdb5-19187026ccfc", 
            "description": "Monitoring Process Link", 
            "output_key": "secondary_monitoring_link"
        }, 
        {
            "output_value": "e4609dae-5c88-494a-bdb5-19187026ccfc", 
            "description": "Monitoring Target ID", 
            "output_key": "secondary_monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/ca354a39-f48c-4698-9cdd-9e106e2a5bf4", 
            "description": "Monitoring Process Link", 
            "output_key": "primary_monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "internet_gateway:f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/internet_gateways/f6e8c695-c4c1-4a93-9b7e-1663aee6dec9
{
    "heat_outputs": [
        {
            "output_value": "ca354a39-f48c-4698-9cdd-9e106e2a5bf4", 
            "description": "Monitoring Target ID", 
            "output_key": "primary_monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/e4609dae-5c88-494a-bdb5-19187026ccfc", 
            "description": "Monitoring Process Link", 
            "output_key": "secondary_monitoring_link"
        }, 
        {
            "output_value": "e4609dae-5c88-494a-bdb5-19187026ccfc", 
            "description": "Monitoring Target ID", 
            "output_key": "secondary_monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/ca354a39-f48c-4698-9cdd-9e106e2a5bf4", 
            "description": "Monitoring Process Link", 
            "output_key": "primary_monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/internet_gateways/f6e8c695-c4c1-4a93-9b7e-1663aee6dec9
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"ca354a39-f48c-4698-9cdd-9e106e2a5bf4\", \"description\": \"Monitoring Target ID\", \"output_key\": \"primary_monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/e4609dae-5c88-494a-bdb5-19187026ccfc\", \"description\": \"Monitoring Process Link\", \"output_key\": \"secondary_monitoring_link\"}, {\"output_value\": \"e4609dae-5c88-494a-bdb5-19187026ccfc\", \"description\": \"Monitoring Target ID\", \"output_key\": \"secondary_monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/ca354a39-f48c-4698-9cdd-9e106e2a5bf4\", \"description\": \"Monitoring Process Link\", \"output_key\": \"primary_monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
