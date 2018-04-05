# Stored data in etcd: Create Edge Router

```
/jobs/all/create:heat_worker:edge_router:ca43aedb-bc30-4355-a931-7bb1d9040659:1:t7my3
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "ca43aedb-bc30-4355-a931-7bb1d9040659", 
        "handler": "heat_worker", 
        "job_name": "edge_router:ca43aedb-bc30-4355-a931-7bb1d9040659:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "ca43aedb-bc30-4355-a931-7bb1d9040659", 
                "param": "gohan_id"
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
                "value": "10.79.5.184", 
                "param": "device_ip"
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
                "value": "06d6b792b31c40daa546fb0f4e35980d", 
                "param": "tenant_id"
            }
        ], 
        "resource_type": "edge_router", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:edge_router:ca43aedb-bc30-4355-a931-7bb1d9040659:1:t7my3", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "vMX-router-01", 
            "ssh_port": 830, 
            "ip": "10.79.5.184", 
            "operational_state": "NO_STATE", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
            "id": "ca43aedb-bc30-4355-a931-7bb1d9040659", 
            "login": "esi", 
            "password": "esiesi0000", 
            "autonomous_system": "65101", 
            "description": "MX80 #1"
        }
    }, 
    0
]
```
