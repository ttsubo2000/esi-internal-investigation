# Stored data in etcd: Create Edge Router

```
/jobs/all/create:heat_worker:edge_router:7a35974a-a19f-49e2-b907-ad7fd8692975:1:nkfox
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "7a35974a-a19f-49e2-b907-ad7fd8692975", 
        "handler": "heat_worker", 
        "job_name": "edge_router:7a35974a-a19f-49e2-b907-ad7fd8692975:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "7a35974a-a19f-49e2-b907-ad7fd8692975", 
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
                "value": "10.79.5.185", 
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
                "value": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
                "param": "tenant_id"
            }
        ], 
        "resource_type": "edge_router", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:edge_router:7a35974a-a19f-49e2-b907-ad7fd8692975:1:nkfox", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "vMX-router-02", 
            "ssh_port": 830, 
            "ip": "10.79.5.185", 
            "operational_state": "NO_STATE", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
            "id": "7a35974a-a19f-49e2-b907-ad7fd8692975", 
            "login": "esi", 
            "password": "esiesi0000", 
            "autonomous_system": "65101", 
            "description": "MX80 #2"
        }
    }, 
    0
]
```
