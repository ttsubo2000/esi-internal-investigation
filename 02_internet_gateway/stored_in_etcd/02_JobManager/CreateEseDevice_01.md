# Stored data in etcd: Create Ese Device

```
/jobs/all/create:heat_worker:ese_device:3fb53223-b614-46b6-92e8-25c3bcbed214:1:sb69v
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "3fb53223-b614-46b6-92e8-25c3bcbed214", 
        "handler": "heat_worker", 
        "job_name": "ese_device:3fb53223-b614-46b6-92e8-25c3bcbed214:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "QFX-NW02", 
                "param": "hostname"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "QFX-NW02", 
                "param": "name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "06d6b792b31c40daa546fb0f4e35980d", 
                "param": "tenant_id"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "10.161.0.34", 
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
                "value": "3fb53223-b614-46b6-92e8-25c3bcbed214", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "ese_device", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:ese_device:3fb53223-b614-46b6-92e8-25c3bcbed214:1:sb69v", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "username": "esi", 
            "description": "", 
            "name": "QFX-NW02", 
            "tags": {}, 
            "existing": "existing", 
            "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
            "hostname": "QFX-NW02", 
            "operational_state": "NO_STATE", 
            "management_ip_address": "10.161.0.34", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "password": "password", 
            "type": "tor", 
            "id": "3fb53223-b614-46b6-92e8-25c3bcbed214", 
            "public_ip_address": "10.161.0.34"
        }
    }, 
    0
]
```
