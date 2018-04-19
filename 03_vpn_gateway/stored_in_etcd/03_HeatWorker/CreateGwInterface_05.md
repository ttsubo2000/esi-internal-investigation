# Stored data in etcd: Create Gw Interface

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/ese_logical_ports/257d0a9f-d5ae-4a93-9af4-81ad611e1b0d
{
    "stack_id": "ese_logical_port_257d0a9f-d5ae-4a93-9af4-81ad611e1b0d", 
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "5e4c28ad-c5f2-43fc-97e8-1b5e99642b87", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "46b0cd68-d0fb-4d72-9def-830164f9e215", 
            "description": "A unique id for the logical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/5e4c28ad-c5f2-43fc-97e8-1b5e99642b87", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }, 
        {
            "output_value": "xe-0/0/38.0", 
            "description": "The name of the logical interface.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "ese_logical_port:257d0a9f-d5ae-4a93-9af4-81ad611e1b0d"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/ese_logical_ports/257d0a9f-d5ae-4a93-9af4-81ad611e1b0d
{
    "heat_outputs": [
        {
            "output_value": "5e4c28ad-c5f2-43fc-97e8-1b5e99642b87", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "46b0cd68-d0fb-4d72-9def-830164f9e215", 
            "description": "A unique id for the logical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/5e4c28ad-c5f2-43fc-97e8-1b5e99642b87", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }, 
        {
            "output_value": "xe-0/0/38.0", 
            "description": "The name of the logical interface.", 
            "output_key": "name"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/ese_logical_ports/257d0a9f-d5ae-4a93-9af4-81ad611e1b0d
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"5e4c28ad-c5f2-43fc-97e8-1b5e99642b87\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"46b0cd68-d0fb-4d72-9def-830164f9e215\", \"description\": \"A unique id for the logical interface\", \"output_key\": \"id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/5e4c28ad-c5f2-43fc-97e8-1b5e99642b87\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}, {\"output_value\": \"xe-0/0/38.0\", \"description\": \"The name of the logical interface.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
