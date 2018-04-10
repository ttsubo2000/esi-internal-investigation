# Stored data in etcd: Create Ese Physical Port

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/ese_physical_ports/9451c9ca-289d-42ba-846d-359c448e910c
{
    "stack_id": "ese_physical_port_9451c9ca-289d-42ba-846d-359c448e910c", 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "78d717f0-66d9-4f82-afe6-833c5e8f38f5", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "06bfe521-07f0-4931-9f8c-318c3ad8114e", 
            "description": "A unique id for the physical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/78d717f0-66d9-4f82-afe6-833c5e8f38f5", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }, 
        {
            "output_value": "xe-0/0/38", 
            "description": "The name of the physical interface.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "ese_physical_port:9451c9ca-289d-42ba-846d-359c448e910c"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/ese_physical_ports/9451c9ca-289d-42ba-846d-359c448e910c
{
    "heat_outputs": [
        {
            "output_value": "78d717f0-66d9-4f82-afe6-833c5e8f38f5", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "06bfe521-07f0-4931-9f8c-318c3ad8114e", 
            "description": "A unique id for the physical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/78d717f0-66d9-4f82-afe6-833c5e8f38f5", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }, 
        {
            "output_value": "xe-0/0/38", 
            "description": "The name of the physical interface.", 
            "output_key": "name"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/ese_physical_ports/9451c9ca-289d-42ba-846d-359c448e910c
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"78d717f0-66d9-4f82-afe6-833c5e8f38f5\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"06bfe521-07f0-4931-9f8c-318c3ad8114e\", \"description\": \"A unique id for the physical interface\", \"output_key\": \"id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/78d717f0-66d9-4f82-afe6-833c5e8f38f5\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}, {\"output_value\": \"xe-0/0/38\", \"description\": \"The name of the physical interface.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
