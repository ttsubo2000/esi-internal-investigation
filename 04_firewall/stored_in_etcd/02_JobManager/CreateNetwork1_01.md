# Stored data in etcd: Create Network (dummy-net)

```
/jobs/all/create:heat_worker:network:73b2c401-a1f3-49fb-8612-8c755b37a28d:1:cp3xh
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
        "handler": "heat_worker", 
        "job_name": "network:73b2c401-a1f3-49fb-8612-8c755b37a28d:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
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
                "value": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
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
        "id": "create:heat_worker:network:73b2c401-a1f3-49fb-8612-8c755b37a28d:1:cp3xh", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "subnets": [], 
            "description": "dummy network for firewall", 
            "tags": {}, 
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
            "admin_state_up": true, 
            "plane": "data", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "shared": false, 
            "id": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
            "name": "dummy-net"
        }
    }, 
    0
]
```
