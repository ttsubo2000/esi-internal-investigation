# Stored data in etcd: Create Ese Physical Port

```
/jobs/all/create:heat_worker:ese_physical_port:a6e70af1-386b-4d79-943f-6f44e87f95b3:1:dug4j
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "a6e70af1-386b-4d79-943f-6f44e87f95b3", 
        "handler": "heat_worker", 
        "job_name": "ese_physical_port:a6e70af1-386b-4d79-943f-6f44e87f95b3:1", 
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
                "value": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
                "param": "tenant_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_device", 
                        "resource_id": "4d8371c0-1b91-4818-a6e7-26425178e5d4"
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
                        "resource_id": "4d8371c0-1b91-4818-a6e7-26425178e5d4"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "ese_device", 
                    "resource_id": "4d8371c0-1b91-4818-a6e7-26425178e5d4"
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
                "value": "a6e70af1-386b-4d79-943f-6f44e87f95b3", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "ese_physical_port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:ese_physical_port:a6e70af1-386b-4d79-943f-6f44e87f95b3:1:dug4j", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "connected_port_owner": "mx_downlink", 
            "tags": {}, 
            "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
            "description": "", 
            "existing": "new", 
            "connected_port_id": "", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "ese_device_id": "4d8371c0-1b91-4818-a6e7-26425178e5d4", 
            "operational_state": "NO_STATE", 
            "id": "a6e70af1-386b-4d79-943f-6f44e87f95b3", 
            "name": "xe-0/0/4"
        }
    }, 
    0
]
```
