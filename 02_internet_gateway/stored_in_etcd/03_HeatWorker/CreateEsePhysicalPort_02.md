# Stored data in etcd: Create Ese Physical Port

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/ese_physical_ports/6b29894f-8694-4865-92c1-2e78360e65a6
{
    "stack_id": "ese_physical_port_6b29894f-8694-4865-92c1-2e78360e65a6", 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "02761d5d-f2ae-4806-bff6-df5851f514ed", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "06bfe521-07f0-4931-9f8c-318c3ad8114e", 
            "description": "A unique id for the physical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/02761d5d-f2ae-4806-bff6-df5851f514ed", 
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
    "id": "ese_physical_port:6b29894f-8694-4865-92c1-2e78360e65a6"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/ese_physical_ports/6b29894f-8694-4865-92c1-2e78360e65a6
{
    "heat_outputs": [
        {
            "output_value": "02761d5d-f2ae-4806-bff6-df5851f514ed", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "06bfe521-07f0-4931-9f8c-318c3ad8114e", 
            "description": "A unique id for the physical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/02761d5d-f2ae-4806-bff6-df5851f514ed", 
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
/state/v2.0/ese_physical_ports/6b29894f-8694-4865-92c1-2e78360e65a6
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"02761d5d-f2ae-4806-bff6-df5851f514ed\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"06bfe521-07f0-4931-9f8c-318c3ad8114e\", \"description\": \"A unique id for the physical interface\", \"output_key\": \"id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/02761d5d-f2ae-4806-bff6-df5851f514ed\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}, {\"output_value\": \"xe-0/0/38\", \"description\": \"The name of the physical interface.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
