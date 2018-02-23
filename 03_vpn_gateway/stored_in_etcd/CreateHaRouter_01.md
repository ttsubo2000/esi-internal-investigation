# Stored data in etcd: Create Ha Router

These are stored data for "heat_templates" in etcd.

* ha_router_monitoring

![scope](../../images/esi_interface.010.png)

These are stored data for "Create Ha Router" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ha_routers/f01ed0a6-7094-4e54-b14b-94657fff1efb
{
    "body": {
        "maximum_gateways": 500, 
        "status": "PENDING_CREATE", 
        "primary_router_id": "792c7a6d-19b5-4d6f-b9f6-1e5b1eb45198", 
        "secondary_router_id": "3ca3a59a-4f92-4a8a-9ec1-1c55a97c794e", 
        "description": "sample_ha_router", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "available_gateways": 500, 
        "id": "f01ed0a6-7094-4e54-b14b-94657fff1efb", 
        "name": "sample-ha-router"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:ha_router:f01ed0a6-7094-4e54-b14b-94657fff1efb:1:w4ig8
[
    "monitoring_worker", 
    {
        "is_first": true, 
        "resource_id": "f01ed0a6-7094-4e54-b14b-94657fff1efb", 
        "handler": "monitoring_worker", 
        "job_name": "ha_router:f01ed0a6-7094-4e54-b14b-94657fff1efb:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "3ca3a59a-4f92-4a8a-9ec1-1c55a97c794e"
                    }
                ], 
                "type": "value", 
                "value": "3ca3a59a-4f92-4a8a-9ec1-1c55a97c794e", 
                "param": "secondary_device_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "792c7a6d-19b5-4d6f-b9f6-1e5b1eb45198"
                    }
                ], 
                "type": "value", 
                "value": "792c7a6d-19b5-4d6f-b9f6-1e5b1eb45198", 
                "param": "primary_device_id"
            }
        ], 
        "resource_type": "ha_router", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:ha_router:f01ed0a6-7094-4e54-b14b-94657fff1efb:1:w4ig8", 
        "resource_input": {
            "maximum_gateways": 500, 
            "status": "PENDING_CREATE", 
            "primary_router_id": "792c7a6d-19b5-4d6f-b9f6-1e5b1eb45198", 
            "secondary_router_id": "3ca3a59a-4f92-4a8a-9ec1-1c55a97c794e", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "name": "sample-ha-router", 
            "available_gateways": 500, 
            "id": "f01ed0a6-7094-4e54-b14b-94657fff1efb", 
            "description": "sample_ha_router"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/job_state/v2.0/ha_routers/f01ed0a6-7094-4e54-b14b-94657fff1efb
{
    "state_monitoring": {
        "primary": "ACTIVE", 
        "secondary": "ACTIVE"
    }
}
```

### Checking stored data at the point of (4) in etcd

```
/state/v2.0/ha_routers/f01ed0a6-7094-4e54-b14b-94657fff1efb
{
    "state": {
        "state_monitoring": "{\"primary\": \"ACTIVE\", \"secondary\": \"ACTIVE\"}", 
        "worker_state": "CREATE_COMPLETED"
    }, 
    "version": 1, 
    "error": ""
}
```
