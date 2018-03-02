# Stored data in etcd: Create Network (admin-net)

```
/jobs/all/create:heat_worker:network:75c2c3ec-7fe7-494c-a35c-db3f94d3a554:1:s0u5y
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
        "handler": "heat_worker", 
        "job_name": "network:75c2c3ec-7fe7-494c-a35c-db3f94d3a554:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
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
                "value": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
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
        "id": "create:heat_worker:network:75c2c3ec-7fe7-494c-a35c-db3f94d3a554:1:s0u5y", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "subnets": [], 
            "description": "adminpod network", 
            "tags": {}, 
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
            "admin_state_up": true, 
            "plane": "data", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "shared": false, 
            "id": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
            "name": "adminpod-net"
        }
    }, 
    0
]
```
