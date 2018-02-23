# Stored data in etcd: Create Er Physical Interface

These are stored data for "heat_templates" in etcd.

* er_physical_interface_monitoring

![scope](../../images/esi_interface.010.png)

These are stored data for "Create Er Physical Interface" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/er_physical_interfaces/469e4283-80e6-491c-830f-c483c1f7c695
{
    "body": {
        "status": "PENDING_CREATE", 
        "connected_ese_port_id": "8a4bbfe0-5aae-42f5-8b94-c4c14b9e7306", 
        "description": "", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "device_id": "198b93f2-006e-45b6-96d3-e7ef6f759501", 
        "id": "469e4283-80e6-491c-830f-c483c1f7c695", 
        "name": "ae0"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:er_physical_interface:469e4283-80e6-491c-830f-c483c1f7c695:1:js8ct
[
    "monitoring_worker", 
    {
        "is_first": true, 
        "resource_id": "469e4283-80e6-491c-830f-c483c1f7c695", 
        "handler": "monitoring_worker", 
        "job_name": "er_physical_interface:469e4283-80e6-491c-830f-c483c1f7c695:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "EDGE_ROUTER_COMMUNITY", 
                "param": "community_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "198b93f2-006e-45b6-96d3-e7ef6f759501"
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
                "param": "name"
            }
        ], 
        "resource_type": "er_physical_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:er_physical_interface:469e4283-80e6-491c-830f-c483c1f7c695:1:js8ct", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "connected_ese_port_id": "8a4bbfe0-5aae-42f5-8b94-c4c14b9e7306", 
            "description": "", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "name": "ae0", 
            "id": "469e4283-80e6-491c-830f-c483c1f7c695", 
            "device_id": "198b93f2-006e-45b6-96d3-e7ef6f759501"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/job_state/v2.0/er_physical_interfaces/469e4283-80e6-491c-830f-c483c1f7c695
{
    "state_monitoring": {
        "interface": "ACTIVE"
    }
}
```

### Checking stored data at the point of (4) in etcd

```
/state/v2.0/er_physical_interfaces/469e4283-80e6-491c-830f-c483c1f7c695
{
    "state": {
        "state_monitoring": "{\"interface\": \"ACTIVE\"}", 
        "worker_state": "CREATE_COMPLETED"
    }, 
    "version": 1, 
    "error": ""
}
```

### Checking stored data at the point of (5) in etcd

```
/monitoring/v2.0/er_physical_interfaces/469e4283-80e6-491c-830f-c483c1f7c695
{
    "interface": "UP", 
    "version": 1
}
```
