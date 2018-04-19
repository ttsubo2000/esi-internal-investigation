# Stored data in etcd: Create Er Physical Interface

```
/jobs/all/create:heat_worker:er_physical_interface:c8e2d558-02ee-4bf3-ba5b-958821a21043:1:df5np
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "c8e2d558-02ee-4bf3-ba5b-958821a21043", 
        "handler": "heat_worker", 
        "job_name": "er_physical_interface:c8e2d558-02ee-4bf3-ba5b-958821a21043:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
                "param": "tenant_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "b7e6d8ad-5377-4380-bbb4-1a62566cbd6d"
                    }
                ], 
                "type": "value", 
                "value": "10.79.5.184", 
                "param": "device_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "ae0", 
                "param": "if_name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "3", 
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
                "value": "c8e2d558-02ee-4bf3-ba5b-958821a21043", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "er_physical_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:er_physical_interface:c8e2d558-02ee-4bf3-ba5b-958821a21043:1:df5np", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "connected_ese_port_id": "a6e70af1-386b-4d79-943f-6f44e87f95b3", 
            "description": "", 
            "name": "ae0", 
            "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
            "operational_state": "NO_STATE", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "id": "c8e2d558-02ee-4bf3-ba5b-958821a21043", 
            "device_id": "b7e6d8ad-5377-4380-bbb4-1a62566cbd6d"
        }
    }, 
    0
]
```
