# Stored data in etcd: Create Edge Router

```
/jobs/all/create:heat_worker:edge_router:cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78:1:a4a0e
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78", 
        "handler": "heat_worker", 
        "job_name": "edge_router:cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78", 
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
                "value": "06d6b792b31c40daa546fb0f4e35980d", 
                "param": "tenant_id"
            }
        ], 
        "resource_type": "edge_router", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:edge_router:cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78:1:a4a0e", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "vMX-router-02", 
            "ssh_port": 830, 
            "ip": "10.79.5.185", 
            "operational_state": "NO_STATE", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
            "id": "cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78", 
            "login": "esi", 
            "password": "esiesi0000", 
            "autonomous_system": "65101", 
            "description": "MX80 #2"
        }
    }, 
    0
]
```
