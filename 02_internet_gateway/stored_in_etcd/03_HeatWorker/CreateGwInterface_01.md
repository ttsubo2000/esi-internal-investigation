# Stored data in etcd: Create Gw Interface

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/gw_interfaces/ce8831fd-d30c-41e3-95de-feaee0b95405
{
    "stack_id": "gw_interface_ce8831fd-d30c-41e3-95de-feaee0b95405", 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "921a9234-0ae4-44f5-89b0-2f68dcaaae5b", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/921a9234-0ae4-44f5-89b0-2f68dcaaae5b", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "gw_interface:ce8831fd-d30c-41e3-95de-feaee0b95405"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/gw_interfaces/ce8831fd-d30c-41e3-95de-feaee0b95405
{
    "heat_outputs": [
        {
            "output_value": "921a9234-0ae4-44f5-89b0-2f68dcaaae5b", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/921a9234-0ae4-44f5-89b0-2f68dcaaae5b", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/gw_interfaces/ce8831fd-d30c-41e3-95de-feaee0b95405
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"921a9234-0ae4-44f5-89b0-2f68dcaaae5b\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/921a9234-0ae4-44f5-89b0-2f68dcaaae5b\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
