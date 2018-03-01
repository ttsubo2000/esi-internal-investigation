# Stored data in etcd: Create Ese Device

```
/jobs/all/create:heat_worker:ese_device:718148aa-4483-47d5-bbd1-a0e0738dc018:1:91uyh
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "718148aa-4483-47d5-bbd1-a0e0738dc018", 
        "handler": "heat_worker", 
        "job_name": "ese_device:718148aa-4483-47d5-bbd1-a0e0738dc018:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "QFX-NW01", 
                "param": "hostname"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "QFX-NW01", 
                "param": "name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "ae69b52f46ba480bb9636f62736436f4", 
                "param": "tenant_id"
            }, 
            {
                "resources": [], 
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
                "value": "718148aa-4483-47d5-bbd1-a0e0738dc018", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "ese_device", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:ese_device:718148aa-4483-47d5-bbd1-a0e0738dc018:1:91uyh", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "username": "esi", 
            "description": "", 
            "name": "QFX-NW01", 
            "tags": {}, 
            "existing": "existing", 
            "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
            "hostname": "QFX-NW01", 
            "operational_state": "NO_STATE", 
            "management_ip_address": "10.161.0.33", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "password": "password", 
            "type": "tor", 
            "id": "718148aa-4483-47d5-bbd1-a0e0738dc018", 
            "public_ip_address": "10.161.0.33"
        }
    }, 
    0
]
```
