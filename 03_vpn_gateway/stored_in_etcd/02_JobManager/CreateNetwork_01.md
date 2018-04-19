# Stored data in etcd: Create Network

```
/jobs/all/create:heat_worker:network:afa0d9d6-84dc-4755-9c6e-db2f23f9dde2:1:vodtl
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2", 
        "handler": "heat_worker", 
        "job_name": "network:afa0d9d6-84dc-4755-9c6e-db2f23f9dde2:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2", 
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
                "value": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2", 
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
        "id": "create:heat_worker:network:afa0d9d6-84dc-4755-9c6e-db2f23f9dde2:1:vodtl", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "subnets": [], 
            "description": "Sample Network", 
            "tags": {}, 
            "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
            "admin_state_up": true, 
            "plane": "data", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "shared": false, 
            "id": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2", 
            "name": "sample-network"
        }
    }, 
    0
]
```
