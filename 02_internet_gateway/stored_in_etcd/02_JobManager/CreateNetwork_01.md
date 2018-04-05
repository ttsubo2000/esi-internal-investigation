# Stored data in etcd: Create Network

```
/jobs/all/create:heat_worker:network:6e557507-1c2a-49b1-ba90-5f616a1f1f3e:1:tlbso
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e", 
        "handler": "heat_worker", 
        "job_name": "network:6e557507-1c2a-49b1-ba90-5f616a1f1f3e:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e", 
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
                "value": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e", 
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
        "id": "create:heat_worker:network:6e557507-1c2a-49b1-ba90-5f616a1f1f3e:1:tlbso", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "subnets": [], 
            "description": "Sample Network", 
            "tags": {}, 
            "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
            "admin_state_up": true, 
            "plane": "data", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "shared": false, 
            "id": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e", 
            "name": "sample-network"
        }
    }, 
    0
]
```
