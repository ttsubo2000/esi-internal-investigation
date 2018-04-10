# Stored data in etcd: Create Common Function Gateway

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/ese_logical_ports/be66c7e0-b222-4e76-bf81-af75e8cf1824
{
    "stack_id": "ese_logical_port_be66c7e0-b222-4e76-bf81-af75e8cf1824", 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "bdc2f00e-073d-49d6-ac27-43782568b081", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "46b0cd68-d0fb-4d72-9def-830164f9e215", 
            "description": "A unique id for the logical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/bdc2f00e-073d-49d6-ac27-43782568b081", 
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
    "id": "ese_logical_port:be66c7e0-b222-4e76-bf81-af75e8cf1824"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/ese_logical_ports/be66c7e0-b222-4e76-bf81-af75e8cf1824
{
    "heat_outputs": [
        {
            "output_value": "bdc2f00e-073d-49d6-ac27-43782568b081", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "46b0cd68-d0fb-4d72-9def-830164f9e215", 
            "description": "A unique id for the logical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/bdc2f00e-073d-49d6-ac27-43782568b081", 
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
/state/v2.0/ese_logical_ports/be66c7e0-b222-4e76-bf81-af75e8cf1824
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"bdc2f00e-073d-49d6-ac27-43782568b081\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"46b0cd68-d0fb-4d72-9def-830164f9e215\", \"description\": \"A unique id for the logical interface\", \"output_key\": \"id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/bdc2f00e-073d-49d6-ac27-43782568b081\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}, {\"output_value\": \"xe-0/0/38.0\", \"description\": \"The name of the logical interface.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
