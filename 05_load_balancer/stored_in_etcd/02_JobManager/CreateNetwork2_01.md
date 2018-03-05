# Stored data in etcd: Create Network (admin-net)

```
/jobs/all/create:heat_worker:network:168c1535-9001-49c7-bb05-21844570a83c:1:0jhpg
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "168c1535-9001-49c7-bb05-21844570a83c", 
        "handler": "heat_worker", 
        "job_name": "network:168c1535-9001-49c7-bb05-21844570a83c:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "168c1535-9001-49c7-bb05-21844570a83c", 
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
                "value": "168c1535-9001-49c7-bb05-21844570a83c", 
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
        "id": "create:heat_worker:network:168c1535-9001-49c7-bb05-21844570a83c:1:0jhpg", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "subnets": [], 
            "description": "adminpod network", 
            "tags": {}, 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "admin_state_up": true, 
            "plane": "data", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "shared": false, 
            "id": "168c1535-9001-49c7-bb05-21844570a83c", 
            "name": "adminpod-net"
        }
    }, 
    0
]
```
