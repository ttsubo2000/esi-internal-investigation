# Stored data in etcd: Create Ese Device

```
/jobs/all/create:heat_worker:ese_device:4d8371c0-1b91-4818-a6e7-26425178e5d4:1:6ud1f
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "4d8371c0-1b91-4818-a6e7-26425178e5d4", 
        "handler": "heat_worker", 
        "job_name": "ese_device:4d8371c0-1b91-4818-a6e7-26425178e5d4:1", 
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
                "value": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
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
                "value": "4d8371c0-1b91-4818-a6e7-26425178e5d4", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "ese_device", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:ese_device:4d8371c0-1b91-4818-a6e7-26425178e5d4:1:6ud1f", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "username": "esi", 
            "description": "", 
            "name": "QFX-NW02", 
            "tags": {}, 
            "existing": "existing", 
            "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
            "hostname": "QFX-NW02", 
            "operational_state": "NO_STATE", 
            "management_ip_address": "10.161.0.34", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "password": "password", 
            "type": "tor", 
            "id": "4d8371c0-1b91-4818-a6e7-26425178e5d4", 
            "public_ip_address": "10.161.0.34"
        }
    }, 
    0
]
```
