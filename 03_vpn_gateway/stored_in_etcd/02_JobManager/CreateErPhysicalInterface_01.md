# Stored data in etcd: Create Er Physical Interface

```
/jobs/all/create:heat_worker:er_physical_interface:f3ecf585-5c3b-445a-97a7-d8e124c99e16:1:13pri
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "f3ecf585-5c3b-445a-97a7-d8e124c99e16", 
        "handler": "heat_worker", 
        "job_name": "er_physical_interface:f3ecf585-5c3b-445a-97a7-d8e124c99e16:1", 
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
                "value": "ge-0/0/1", 
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
                "value": "f3ecf585-5c3b-445a-97a7-d8e124c99e16", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "er_physical_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:er_physical_interface:f3ecf585-5c3b-445a-97a7-d8e124c99e16:1:13pri", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "", 
            "name": "ge-0/0/1", 
            "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
            "operational_state": "NO_STATE", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "id": "f3ecf585-5c3b-445a-97a7-d8e124c99e16", 
            "device_id": "7a35974a-a19f-49e2-b907-ad7fd8692975"
        }
    }, 
    0
]
```
