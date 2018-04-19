# Stored data in etcd: Create Gw Interface

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/ese_logical_ports/e30fdd19-2f48-422e-9c68-7c59a0e2fae8
{
    "stack_id": "ese_logical_port_e30fdd19-2f48-422e-9c68-7c59a0e2fae8", 
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "fc210c75-e57f-4657-8114-a528d3b3aac5", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "46b0cd68-d0fb-4d72-9def-830164f9e215", 
            "description": "A unique id for the logical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/fc210c75-e57f-4657-8114-a528d3b3aac5", 
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
    "id": "ese_logical_port:e30fdd19-2f48-422e-9c68-7c59a0e2fae8"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/ese_logical_ports/e30fdd19-2f48-422e-9c68-7c59a0e2fae8
{
    "heat_outputs": [
        {
            "output_value": "fc210c75-e57f-4657-8114-a528d3b3aac5", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "46b0cd68-d0fb-4d72-9def-830164f9e215", 
            "description": "A unique id for the logical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/fc210c75-e57f-4657-8114-a528d3b3aac5", 
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
/state/v2.0/ese_logical_ports/e30fdd19-2f48-422e-9c68-7c59a0e2fae8
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"fc210c75-e57f-4657-8114-a528d3b3aac5\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"46b0cd68-d0fb-4d72-9def-830164f9e215\", \"description\": \"A unique id for the logical interface\", \"output_key\": \"id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/fc210c75-e57f-4657-8114-a528d3b3aac5\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}, {\"output_value\": \"xe-0/0/38.0\", \"description\": \"The name of the logical interface.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
