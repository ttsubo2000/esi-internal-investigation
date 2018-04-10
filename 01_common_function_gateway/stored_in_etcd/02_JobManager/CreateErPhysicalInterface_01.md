# Stored data in etcd: Create Er Physical Interface

```
/jobs/all/create:heat_worker:er_physical_interface:c2576120-00b0-461e-a2ae-f7bbff9465d0:1:i19ds
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "c2576120-00b0-461e-a2ae-f7bbff9465d0", 
        "handler": "heat_worker", 
        "job_name": "er_physical_interface:c2576120-00b0-461e-a2ae-f7bbff9465d0:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "c583ce78843344adbe5fd20f13620274", 
                "param": "tenant_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "f4f54175-93fe-406b-ae66-dbca4df99e03"
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
                "value": "c2576120-00b0-461e-a2ae-f7bbff9465d0", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "er_physical_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:er_physical_interface:c2576120-00b0-461e-a2ae-f7bbff9465d0:1:i19ds", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "connected_ese_port_id": "9451c9ca-289d-42ba-846d-359c448e910c", 
            "description": "", 
            "name": "ae0", 
            "tenant_id": "c583ce78843344adbe5fd20f13620274", 
            "operational_state": "NO_STATE", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "id": "c2576120-00b0-461e-a2ae-f7bbff9465d0", 
            "device_id": "f4f54175-93fe-406b-ae66-dbca4df99e03"
        }
    }, 
    0
]
```
