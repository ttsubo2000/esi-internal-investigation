# Stored data in etcd: Create Ese Physical Port

These are stored data for "heat_templates" in etcd.

* ese_physical_port_existing

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ese_physical_ports/24dd42cf-b343-47a9-966a-8f7486378c46
{
    "body": {
        "status": "PENDING_CREATE", 
        "connected_port_owner": "physical_port", 
        "name": "xe-0/0/1", 
        "tags": {}, 
        "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
        "existing": "existing", 
        "connected_port_id": "7ff183de-0188-46bf-b7d0-68d08ad2b54f", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "ese_device_id": "718148aa-4483-47d5-bbd1-a0e0738dc018", 
        "operational_state": "NO_STATE", 
        "id": "24dd42cf-b343-47a9-966a-8f7486378c46", 
        "description": ""
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/create:heat_worker:ese_physical_port:24dd42cf-b343-47a9-966a-8f7486378c46:1:paaak
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "24dd42cf-b343-47a9-966a-8f7486378c46", 
        "handler": "heat_worker", 
        "job_name": "ese_physical_port:24dd42cf-b343-47a9-966a-8f7486378c46:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "xe-0/0/1", 
                "param": "physical_port_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_device", 
                        "resource_id": "718148aa-4483-47d5-bbd1-a0e0738dc018"
                    }
                ], 
                "type": "value", 
                "value": "QFX-NW01", 
                "param": "physical_device_hostname"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "ae69b52f46ba480bb9636f62736436f4", 
                "param": "tenant_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_device", 
                        "resource_id": "718148aa-4483-47d5-bbd1-a0e0738dc018"
                    }
                ], 
                "type": "value", 
                "value": "10.161.0.33", 
                "param": "device_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "6", 
                "param": "heat_timeout"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": 1, 
                "param": "version"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "24dd42cf-b343-47a9-966a-8f7486378c46", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "ese_physical_port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:ese_physical_port:24dd42cf-b343-47a9-966a-8f7486378c46:1:paaak", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "connected_port_owner": "physical_port", 
            "tags": {}, 
            "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
            "description": "", 
            "existing": "existing", 
            "connected_port_id": "7ff183de-0188-46bf-b7d0-68d08ad2b54f", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "ese_device_id": "718148aa-4483-47d5-bbd1-a0e0738dc018", 
            "operational_state": "NO_STATE", 
            "id": "24dd42cf-b343-47a9-966a-8f7486378c46", 
            "name": "xe-0/0/1"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

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

### Checking stored data at the point of (4) in etcd

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

### Checking stored data at the point of (5) in etcd

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

### Checking stored data at the point of (6) in etcd

```
/monitoring/v2.0/ese_physical_ports/24dd42cf-b343-47a9-966a-8f7486378c46
{
    "version": 1, 
    "port": "UP"
}
```
