# Stored data in etcd: Create Common Function Gateway

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/common_function_gateways/f649736d-1920-41eb-96af-d4e4fe192d0e
{
    "stack_id": "common_function_gateway_f649736d-1920-41eb-96af-d4e4fe192d0e", 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "cfb54c6f-43cf-4e35-aff8-e2c2ec8adc7e", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/cfb54c6f-43cf-4e35-aff8-e2c2ec8adc7e", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "common_function_gateway:f649736d-1920-41eb-96af-d4e4fe192d0e"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/common_function_gateways/f649736d-1920-41eb-96af-d4e4fe192d0e
{
    "heat_outputs": [
        {
            "output_value": "cfb54c6f-43cf-4e35-aff8-e2c2ec8adc7e", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/cfb54c6f-43cf-4e35-aff8-e2c2ec8adc7e", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/common_function_gateways/f649736d-1920-41eb-96af-d4e4fe192d0e
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"cfb54c6f-43cf-4e35-aff8-e2c2ec8adc7e\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/cfb54c6f-43cf-4e35-aff8-e2c2ec8adc7e\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
