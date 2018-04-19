# Stored data in etcd: Create Er Physical Interface

```
/jobs/all/create:heat_worker:er_physical_interface:3118d6be-b1cb-472a-805f-7e1ec46aa5e7:1:ozhuq
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "3118d6be-b1cb-472a-805f-7e1ec46aa5e7", 
        "handler": "heat_worker", 
        "job_name": "er_physical_interface:3118d6be-b1cb-472a-805f-7e1ec46aa5e7:1", 
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
                        "resource_id": "7a35974a-a19f-49e2-b907-ad7fd8692975"
                    }
                ], 
                "type": "value", 
                "value": "10.79.5.185", 
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
                "value": "3118d6be-b1cb-472a-805f-7e1ec46aa5e7", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "er_physical_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:er_physical_interface:3118d6be-b1cb-472a-805f-7e1ec46aa5e7:1:ozhuq", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "connected_ese_port_id": "0078808a-c28e-46e1-887d-8ec65f90c446", 
            "description": "", 
            "name": "ae0", 
            "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
            "operational_state": "NO_STATE", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "id": "3118d6be-b1cb-472a-805f-7e1ec46aa5e7", 
            "device_id": "7a35974a-a19f-49e2-b907-ad7fd8692975"
        }
    }, 
    0
]
```
