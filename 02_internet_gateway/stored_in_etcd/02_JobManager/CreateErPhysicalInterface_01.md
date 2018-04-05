# Stored data in etcd: Create Er Physical Interface

```
/jobs/all/create:heat_worker:er_physical_interface:53712736-354c-4374-be82-6f07bea9d1bd:1:4i1bo
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "53712736-354c-4374-be82-6f07bea9d1bd", 
        "handler": "heat_worker", 
        "job_name": "er_physical_interface:53712736-354c-4374-be82-6f07bea9d1bd:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "06d6b792b31c40daa546fb0f4e35980d", 
                "param": "tenant_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78"
                    }
                ], 
                "type": "value", 
                "value": "10.79.5.185", 
                "param": "device_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "ae0", 
                "param": "if_name"
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
                "value": 1, 
                "param": "version"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "53712736-354c-4374-be82-6f07bea9d1bd", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "er_physical_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:er_physical_interface:53712736-354c-4374-be82-6f07bea9d1bd:1:4i1bo", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "connected_ese_port_id": "887fecdd-956b-47fa-a348-8940c53a5bf9", 
            "description": "", 
            "name": "ae0", 
            "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
            "operational_state": "NO_STATE", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "id": "53712736-354c-4374-be82-6f07bea9d1bd", 
            "device_id": "cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78"
        }
    }, 
    0
]
```
