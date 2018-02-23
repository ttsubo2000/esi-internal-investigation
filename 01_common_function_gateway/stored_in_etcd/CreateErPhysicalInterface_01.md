# Stored data in etcd: Create Er Physical Interface

These are stored data for "heat_templates" in etcd.

* er_physical_interface_monitoring

![scope](../../images/esi_interface.010.png)

These are stored data for "Create Er Physical Interface" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/er_physical_interfaces/a752c6c0-2075-4e7f-9040-5fcefcad0252
{
    "body": {
        "status": "PENDING_CREATE", 
        "connected_ese_port_id": "976156ef-05b4-47f4-9497-a36531563a08", 
        "description": "", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "device_id": "8aba84f9-4675-4d22-a231-e9eabde80818", 
        "id": "a752c6c0-2075-4e7f-9040-5fcefcad0252", 
        "name": "ae0"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:er_physical_interface:a752c6c0-2075-4e7f-9040-5fcefcad0252:1:di9ub
[
    "monitoring_worker", 
    {
        "is_first": true, 
        "resource_id": "a752c6c0-2075-4e7f-9040-5fcefcad0252", 
        "handler": "monitoring_worker", 
        "job_name": "er_physical_interface:a752c6c0-2075-4e7f-9040-5fcefcad0252:1", 
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
                        "resource_id": "8aba84f9-4675-4d22-a231-e9eabde80818"
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
                "param": "name"
            }
        ], 
        "resource_type": "er_physical_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:er_physical_interface:a752c6c0-2075-4e7f-9040-5fcefcad0252:1:di9ub", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "connected_ese_port_id": "976156ef-05b4-47f4-9497-a36531563a08", 
            "description": "", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "name": "ae0", 
            "id": "a752c6c0-2075-4e7f-9040-5fcefcad0252", 
            "device_id": "8aba84f9-4675-4d22-a231-e9eabde80818"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/job_state/v2.0/er_physical_interfaces/a752c6c0-2075-4e7f-9040-5fcefcad0252
{
    "state_monitoring": {
        "interface": "ACTIVE"
    }
}
```

### Checking stored data at the point of (4) in etcd

```
/state/v2.0/er_physical_interfaces/a752c6c0-2075-4e7f-9040-5fcefcad0252
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
/monitoring/v2.0/er_physical_interfaces/a752c6c0-2075-4e7f-9040-5fcefcad0252
{
    "interface": "UP", 
    "version": 1
}
```
