# Stored data in etcd: Create Ese Physical Port

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/ese_physical_ports/a6e70af1-386b-4d79-943f-6f44e87f95b3
{
    "stack_id": "ese_physical_port_a6e70af1-386b-4d79-943f-6f44e87f95b3", 
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "07d5e8ed-4695-49b4-8560-897b586b1b71", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "06bfe521-07f0-4931-9f8c-318c3ad8114e", 
            "description": "A unique id for the physical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/07d5e8ed-4695-49b4-8560-897b586b1b71", 
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
    "id": "ese_physical_port:a6e70af1-386b-4d79-943f-6f44e87f95b3"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/ese_physical_ports/a6e70af1-386b-4d79-943f-6f44e87f95b3
{
    "heat_outputs": [
        {
            "output_value": "07d5e8ed-4695-49b4-8560-897b586b1b71", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "06bfe521-07f0-4931-9f8c-318c3ad8114e", 
            "description": "A unique id for the physical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/07d5e8ed-4695-49b4-8560-897b586b1b71", 
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
/state/v2.0/ese_physical_ports/a6e70af1-386b-4d79-943f-6f44e87f95b3
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"07d5e8ed-4695-49b4-8560-897b586b1b71\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"06bfe521-07f0-4931-9f8c-318c3ad8114e\", \"description\": \"A unique id for the physical interface\", \"output_key\": \"id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/07d5e8ed-4695-49b4-8560-897b586b1b71\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}, {\"output_value\": \"xe-0/0/38\", \"description\": \"The name of the physical interface.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
