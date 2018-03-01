# Stored data in etcd: Create Ese Physical Port

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/ese_physical_ports/24dd42cf-b343-47a9-966a-8f7486378c46
{
    "stack_id": "ese_physical_port_24dd42cf-b343-47a9-966a-8f7486378c46", 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "a481c2c4-e9cd-41f3-8e27-3a4184119abf", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "A unique id for the physical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/a481c2c4-e9cd-41f3-8e27-3a4184119abf", 
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
    "id": "ese_physical_port:24dd42cf-b343-47a9-966a-8f7486378c46"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/ese_physical_ports/24dd42cf-b343-47a9-966a-8f7486378c46
{
    "heat_outputs": [
        {
            "output_value": "a481c2c4-e9cd-41f3-8e27-3a4184119abf", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "A unique id for the physical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/a481c2c4-e9cd-41f3-8e27-3a4184119abf", 
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
/state/v2.0/ese_physical_ports/24dd42cf-b343-47a9-966a-8f7486378c46
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"a481c2c4-e9cd-41f3-8e27-3a4184119abf\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"5a79909b-2bf3-4e26-8a9c-0bf6bb175457\", \"description\": \"A unique id for the physical interface\", \"output_key\": \"id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/a481c2c4-e9cd-41f3-8e27-3a4184119abf\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}, {\"output_value\": \"xe-0/0/38\", \"description\": \"The name of the physical interface.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
