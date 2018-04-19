# Stored data in etcd: Create Edge Router

```
/jobs/all/create:heat_worker:edge_router:b7e6d8ad-5377-4380-bbb4-1a62566cbd6d:1:zyp5y
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "b7e6d8ad-5377-4380-bbb4-1a62566cbd6d", 
        "handler": "heat_worker", 
        "job_name": "edge_router:b7e6d8ad-5377-4380-bbb4-1a62566cbd6d:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "b7e6d8ad-5377-4380-bbb4-1a62566cbd6d", 
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
                "value": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
                "param": "tenant_id"
            }
        ], 
        "resource_type": "edge_router", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:edge_router:b7e6d8ad-5377-4380-bbb4-1a62566cbd6d:1:zyp5y", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "vMX-router-01", 
            "ssh_port": 830, 
            "ip": "10.79.5.184", 
            "operational_state": "NO_STATE", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
            "id": "b7e6d8ad-5377-4380-bbb4-1a62566cbd6d", 
            "login": "esi", 
            "password": "esiesi0000", 
            "autonomous_system": "65101", 
            "description": "MX80 #1"
        }
    }, 
    0
]
```
