# Stored data in etcd: Create Network (user-net)

```
/jobs/all/create:heat_worker:network:774acf45-316f-4431-b31b-08770b76d761:1:do4lx
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "774acf45-316f-4431-b31b-08770b76d761", 
        "handler": "heat_worker", 
        "job_name": "network:774acf45-316f-4431-b31b-08770b76d761:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "774acf45-316f-4431-b31b-08770b76d761", 
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
                "value": "774acf45-316f-4431-b31b-08770b76d761", 
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
        "id": "create:heat_worker:network:774acf45-316f-4431-b31b-08770b76d761:1:do4lx", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "subnets": [], 
            "description": "load_balancer network", 
            "tags": {}, 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "admin_state_up": true, 
            "plane": "data", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "shared": false, 
            "id": "774acf45-316f-4431-b31b-08770b76d761", 
            "name": "sample-lb-net"
        }
    }, 
    0
]
```
