# Stored data in etcd: Create Vpn Interface

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/vpn_interfaces/07d4f1fc-5142-4fae-b115-627fc009e222
{
    "stack_id": "vpn_interface_07d4f1fc-5142-4fae-b115-627fc009e222", 
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/3bdb3c86-ac6d-4ff2-aa55-4b2989971614", 
            "description": "Monitoring Process Link", 
            "output_key": "secondary_interface_monitoring_link"
        }, 
        {
            "output_value": "34b9de21-40c0-46f1-afa5-787220cc5ed2", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/d7885526-613f-4565-a3df-de89ed911e3b", 
            "description": "Monitoring Process Link", 
            "output_key": "primary_interface_monitoring_link"
        }, 
        {
            "output_value": "d7885526-613f-4565-a3df-de89ed911e3b", 
            "description": "Monitoring Target ID", 
            "output_key": "primary_interface_monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/34b9de21-40c0-46f1-afa5-787220cc5ed2", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }, 
        {
            "output_value": "3bdb3c86-ac6d-4ff2-aa55-4b2989971614", 
            "description": "Monitoring Target ID", 
            "output_key": "secondary_interface_monitoring_target_id"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "vpn_interface:07d4f1fc-5142-4fae-b115-627fc009e222"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/vpn_interfaces/07d4f1fc-5142-4fae-b115-627fc009e222
{
    "heat_outputs": [
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/3bdb3c86-ac6d-4ff2-aa55-4b2989971614", 
            "description": "Monitoring Process Link", 
            "output_key": "secondary_interface_monitoring_link"
        }, 
        {
            "output_value": "34b9de21-40c0-46f1-afa5-787220cc5ed2", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/d7885526-613f-4565-a3df-de89ed911e3b", 
            "description": "Monitoring Process Link", 
            "output_key": "primary_interface_monitoring_link"
        }, 
        {
            "output_value": "d7885526-613f-4565-a3df-de89ed911e3b", 
            "description": "Monitoring Target ID", 
            "output_key": "primary_interface_monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/34b9de21-40c0-46f1-afa5-787220cc5ed2", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }, 
        {
            "output_value": "3bdb3c86-ac6d-4ff2-aa55-4b2989971614", 
            "description": "Monitoring Target ID", 
            "output_key": "secondary_interface_monitoring_target_id"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/vpn_interfaces/07d4f1fc-5142-4fae-b115-627fc009e222
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/3bdb3c86-ac6d-4ff2-aa55-4b2989971614\", \"description\": \"Monitoring Process Link\", \"output_key\": \"secondary_interface_monitoring_link\"}, {\"output_value\": \"34b9de21-40c0-46f1-afa5-787220cc5ed2\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/d7885526-613f-4565-a3df-de89ed911e3b\", \"description\": \"Monitoring Process Link\", \"output_key\": \"primary_interface_monitoring_link\"}, {\"output_value\": \"d7885526-613f-4565-a3df-de89ed911e3b\", \"description\": \"Monitoring Target ID\", \"output_key\": \"primary_interface_monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/34b9de21-40c0-46f1-afa5-787220cc5ed2\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}, {\"output_value\": \"3bdb3c86-ac6d-4ff2-aa55-4b2989971614\", \"description\": \"Monitoring Target ID\", \"output_key\": \"secondary_interface_monitoring_target_id\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
