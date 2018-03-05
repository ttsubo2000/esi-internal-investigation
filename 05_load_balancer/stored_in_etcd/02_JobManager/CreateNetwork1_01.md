# Stored data in etcd: Create Network (dummy-net)

```
/jobs/all/create:heat_worker:network:ce9a7a92-d11a-4fc6-8ae7-18061b62c98f:1:4pxn8
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
        "handler": "heat_worker", 
        "job_name": "network:ce9a7a92-d11a-4fc6-8ae7-18061b62c98f:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
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
                "value": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
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
        "id": "create:heat_worker:network:ce9a7a92-d11a-4fc6-8ae7-18061b62c98f:1:4pxn8", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "subnets": [], 
            "description": "dummy network for load_balancer", 
            "tags": {}, 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "admin_state_up": true, 
            "plane": "data", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "shared": false, 
            "id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
            "name": "dummy-net"
        }
    }, 
    0
]
```
