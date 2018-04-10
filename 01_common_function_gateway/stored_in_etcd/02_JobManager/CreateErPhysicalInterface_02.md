# Stored data in etcd: Create Er Physical Interface

```
/jobs/all/create:heat_worker:er_physical_interface:b9c7c1f4-1b90-4a7a-8161-34276bb2ed10:1:qsftf
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "b9c7c1f4-1b90-4a7a-8161-34276bb2ed10", 
        "handler": "heat_worker", 
        "job_name": "er_physical_interface:b9c7c1f4-1b90-4a7a-8161-34276bb2ed10:1", 
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
                        "resource_id": "2d056865-47a9-45cf-a890-ed10e3b5912a"
                    }
                ], 
                "type": "value", 
                "value": "10.79.5.184", 
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
                "value": "b9c7c1f4-1b90-4a7a-8161-34276bb2ed10", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "er_physical_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:er_physical_interface:b9c7c1f4-1b90-4a7a-8161-34276bb2ed10:1:qsftf", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "connected_ese_port_id": "f4c3a1bf-3b61-48ba-a548-422036849465", 
            "description": "", 
            "name": "ae0", 
            "tenant_id": "c583ce78843344adbe5fd20f13620274", 
            "operational_state": "NO_STATE", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "id": "b9c7c1f4-1b90-4a7a-8161-34276bb2ed10", 
            "device_id": "2d056865-47a9-45cf-a890-ed10e3b5912a"
        }
    }, 
    0
]
```
