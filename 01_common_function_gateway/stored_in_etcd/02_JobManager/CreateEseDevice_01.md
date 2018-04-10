# Stored data in etcd: Create Ese Device

```
/jobs/all/create:heat_worker:ese_device:cc214b6a-2f09-4094-b7cd-a9590f64b854:1:1gsws
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "cc214b6a-2f09-4094-b7cd-a9590f64b854", 
        "handler": "heat_worker", 
        "job_name": "ese_device:cc214b6a-2f09-4094-b7cd-a9590f64b854:1", 
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
                "value": "c583ce78843344adbe5fd20f13620274", 
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
                "value": "cc214b6a-2f09-4094-b7cd-a9590f64b854", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "ese_device", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:ese_device:cc214b6a-2f09-4094-b7cd-a9590f64b854:1:1gsws", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "username": "esi", 
            "description": "", 
            "name": "QFX-NW02", 
            "tags": {}, 
            "existing": "existing", 
            "tenant_id": "c583ce78843344adbe5fd20f13620274", 
            "hostname": "QFX-NW02", 
            "operational_state": "NO_STATE", 
            "management_ip_address": "10.161.0.34", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "password": "password", 
            "type": "tor", 
            "id": "cc214b6a-2f09-4094-b7cd-a9590f64b854", 
            "public_ip_address": "10.161.0.34"
        }
    }, 
    0
]
```
