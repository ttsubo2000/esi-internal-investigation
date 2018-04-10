# Stored data in etcd: Create Ese Physical Port

```
/jobs/all/create:heat_worker:ese_physical_port:f4c3a1bf-3b61-48ba-a548-422036849465:1:pymqx
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "f4c3a1bf-3b61-48ba-a548-422036849465", 
        "handler": "heat_worker", 
        "job_name": "ese_physical_port:f4c3a1bf-3b61-48ba-a548-422036849465:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "xe-0/0/4", 
                "param": "physical_port_name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "c583ce78843344adbe5fd20f13620274", 
                "param": "tenant_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_device", 
                        "resource_id": "cc214b6a-2f09-4094-b7cd-a9590f64b854"
                    }
                ], 
                "type": "value", 
                "value": "10.161.0.34", 
                "param": "device_ip"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_device", 
                        "resource_id": "cc214b6a-2f09-4094-b7cd-a9590f64b854"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "ese_device", 
                    "resource_id": "cc214b6a-2f09-4094-b7cd-a9590f64b854"
                }, 
                "param": "physical_device"
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
                "value": "f4c3a1bf-3b61-48ba-a548-422036849465", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "ese_physical_port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:ese_physical_port:f4c3a1bf-3b61-48ba-a548-422036849465:1:pymqx", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "connected_port_owner": "mx_downlink", 
            "tags": {}, 
            "tenant_id": "c583ce78843344adbe5fd20f13620274", 
            "description": "", 
            "existing": "new", 
            "connected_port_id": "", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "ese_device_id": "cc214b6a-2f09-4094-b7cd-a9590f64b854", 
            "operational_state": "NO_STATE", 
            "id": "f4c3a1bf-3b61-48ba-a548-422036849465", 
            "name": "xe-0/0/4"
        }
    }, 
    0
]
```
