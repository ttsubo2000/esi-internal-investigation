# Stored data in etcd: Create Common Function Gateway

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/ese_logical_ports/e8555ee6-529c-42d9-8bb1-bfbe217133b1
{
    "stack_id": "ese_logical_port_e8555ee6-529c-42d9-8bb1-bfbe217133b1", 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "7f066c44-1dc2-44b2-95f7-d59d70bd77fb", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "46b0cd68-d0fb-4d72-9def-830164f9e215", 
            "description": "A unique id for the logical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/7f066c44-1dc2-44b2-95f7-d59d70bd77fb", 
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
    "id": "ese_logical_port:e8555ee6-529c-42d9-8bb1-bfbe217133b1"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/ese_logical_ports/e8555ee6-529c-42d9-8bb1-bfbe217133b1
{
    "heat_outputs": [
        {
            "output_value": "7f066c44-1dc2-44b2-95f7-d59d70bd77fb", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "46b0cd68-d0fb-4d72-9def-830164f9e215", 
            "description": "A unique id for the logical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/7f066c44-1dc2-44b2-95f7-d59d70bd77fb", 
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
/state/v2.0/ese_logical_ports/e8555ee6-529c-42d9-8bb1-bfbe217133b1
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"7f066c44-1dc2-44b2-95f7-d59d70bd77fb\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"46b0cd68-d0fb-4d72-9def-830164f9e215\", \"description\": \"A unique id for the logical interface\", \"output_key\": \"id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/7f066c44-1dc2-44b2-95f7-d59d70bd77fb\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}, {\"output_value\": \"xe-0/0/38.0\", \"description\": \"The name of the logical interface.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
