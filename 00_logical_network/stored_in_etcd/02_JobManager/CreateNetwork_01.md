# Stored data in etcd: Create Network

```
/jobs/all/create:heat_worker:network:35bc496f-3c0e-46b4-a5c0-33810e8e7263:1:pp459
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
        "handler": "heat_worker", 
        "job_name": "network:35bc496f-3c0e-46b4-a5c0-33810e8e7263:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
                "param": "uuid"
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
                "value": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
                "param": "name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": true, 
                "param": "admin_state_up"
            }
        ], 
        "resource_type": "network", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:network:35bc496f-3c0e-46b4-a5c0-33810e8e7263:1:pp459", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "subnets": [], 
            "description": "sample network", 
            "tags": {}, 
            "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
            "admin_state_up": true, 
            "plane": "data", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "shared": false, 
            "id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
            "name": "sample-network"
        }
    }, 
    0
]
```
