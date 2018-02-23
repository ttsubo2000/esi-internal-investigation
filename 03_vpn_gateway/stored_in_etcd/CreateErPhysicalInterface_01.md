# Stored data in etcd: Create Er Physical Interface

These are stored data for "heat_templates" in etcd.

* er_physical_interface_monitoring

![scope](../../images/esi_interface.010.png)

These are stored data for "Create Er Physical Interface" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/er_physical_interfaces/6e8f473f-47ec-4b54-8f0f-d459d440393b
{
    "body": {
        "status": "PENDING_CREATE", 
        "description": "", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "device_id": "792c7a6d-19b5-4d6f-b9f6-1e5b1eb45198", 
        "id": "6e8f473f-47ec-4b54-8f0f-d459d440393b", 
        "name": "ge-0/0/1"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:er_physical_interface:6e8f473f-47ec-4b54-8f0f-d459d440393b:1:tcsfl
[
    "monitoring_worker", 
    {
        "is_first": true, 
        "resource_id": "6e8f473f-47ec-4b54-8f0f-d459d440393b", 
        "handler": "monitoring_worker", 
        "job_name": "er_physical_interface:6e8f473f-47ec-4b54-8f0f-d459d440393b:1", 
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
                        "resource_id": "792c7a6d-19b5-4d6f-b9f6-1e5b1eb45198"
                    }
                ], 
                "type": "value", 
                "value": "10.79.5.185", 
                "param": "device_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "ge-0/0/1", 
                "param": "name"
            }
        ], 
        "resource_type": "er_physical_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:er_physical_interface:6e8f473f-47ec-4b54-8f0f-d459d440393b:1:tcsfl", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "device_id": "792c7a6d-19b5-4d6f-b9f6-1e5b1eb45198", 
            "id": "6e8f473f-47ec-4b54-8f0f-d459d440393b", 
            "name": "ge-0/0/1"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/job_state/v2.0/er_physical_interfaces/6e8f473f-47ec-4b54-8f0f-d459d440393b
{
    "state_monitoring": {
        "interface": "ACTIVE"
    }
}
```

### Checking stored data at the point of (4) in etcd

```
/state/v2.0/er_physical_interfaces/6e8f473f-47ec-4b54-8f0f-d459d440393b
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
/monitoring/v2.0/er_physical_interfaces/6e8f473f-47ec-4b54-8f0f-d459d440393b
{
    "interface": "UP", 
    "version": 1
}
```
