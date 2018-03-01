# Stored data in etcd: Create Ese Physical Port

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
