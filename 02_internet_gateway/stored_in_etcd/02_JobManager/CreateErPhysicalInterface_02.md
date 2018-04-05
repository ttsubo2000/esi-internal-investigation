# Stored data in etcd: Create Er Physical Interface

```
/jobs/all/create:heat_worker:er_physical_interface:d108a472-81ab-43a0-8c49-e0d1a46e6128:1:jo3rt
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "d108a472-81ab-43a0-8c49-e0d1a46e6128", 
        "handler": "heat_worker", 
        "job_name": "er_physical_interface:d108a472-81ab-43a0-8c49-e0d1a46e6128:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "06d6b792b31c40daa546fb0f4e35980d", 
                "param": "tenant_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "ca43aedb-bc30-4355-a931-7bb1d9040659"
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
                "value": "d108a472-81ab-43a0-8c49-e0d1a46e6128", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "er_physical_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:er_physical_interface:d108a472-81ab-43a0-8c49-e0d1a46e6128:1:jo3rt", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "connected_ese_port_id": "6b29894f-8694-4865-92c1-2e78360e65a6", 
            "description": "", 
            "name": "ae0", 
            "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
            "operational_state": "NO_STATE", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "id": "d108a472-81ab-43a0-8c49-e0d1a46e6128", 
            "device_id": "ca43aedb-bc30-4355-a931-7bb1d9040659"
        }
    }, 
    0
]
```
