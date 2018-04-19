# Stored data in etcd: Create Er Physical Interface

```
/jobs/all/create:heat_worker:er_physical_interface:2bc8e40d-ab01-4738-a4aa-e69d8fd30688:1:qb54n
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "2bc8e40d-ab01-4738-a4aa-e69d8fd30688", 
        "handler": "heat_worker", 
        "job_name": "er_physical_interface:2bc8e40d-ab01-4738-a4aa-e69d8fd30688:1", 
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
                "value": "2bc8e40d-ab01-4738-a4aa-e69d8fd30688", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "er_physical_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:er_physical_interface:2bc8e40d-ab01-4738-a4aa-e69d8fd30688:1:qb54n", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "", 
            "name": "ge-0/0/1", 
            "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
            "operational_state": "NO_STATE", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "id": "2bc8e40d-ab01-4738-a4aa-e69d8fd30688", 
            "device_id": "b7e6d8ad-5377-4380-bbb4-1a62566cbd6d"
        }
    }, 
    0
]
```
