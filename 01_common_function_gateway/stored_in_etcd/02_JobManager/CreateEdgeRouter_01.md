# Stored data in etcd: Create Edge Router

```
/jobs/all/create:heat_worker:edge_router:f4f54175-93fe-406b-ae66-dbca4df99e03:1:iprr1
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "f4f54175-93fe-406b-ae66-dbca4df99e03", 
        "handler": "heat_worker", 
        "job_name": "edge_router:f4f54175-93fe-406b-ae66-dbca4df99e03:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "f4f54175-93fe-406b-ae66-dbca4df99e03", 
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
                "value": "c583ce78843344adbe5fd20f13620274", 
                "param": "tenant_id"
            }
        ], 
        "resource_type": "edge_router", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:edge_router:f4f54175-93fe-406b-ae66-dbca4df99e03:1:iprr1", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "vMX-router-02", 
            "ssh_port": 830, 
            "ip": "10.79.5.185", 
            "operational_state": "NO_STATE", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "tenant_id": "c583ce78843344adbe5fd20f13620274", 
            "id": "f4f54175-93fe-406b-ae66-dbca4df99e03", 
            "login": "esi", 
            "password": "esiesi0000", 
            "autonomous_system": "65101", 
            "description": "MX80 #2"
        }
    }, 
    0
]
```
