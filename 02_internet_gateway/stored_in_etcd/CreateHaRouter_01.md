# Stored data in etcd: Create Ha Router

These are stored data for "heat_templates" in etcd.

* ha_router_monitoring

![scope](../../images/esi_interface.010.png)

These are stored data for "Create Ha Router" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ha_routers/d4286c1d-86e7-42d3-9d84-a4d9daa3ae17
{
    "body": {
        "maximum_gateways": 500, 
        "status": "PENDING_CREATE", 
        "primary_router_id": "9b82b55a-551e-4069-ae77-c972e30ab0cc", 
        "secondary_router_id": "198b93f2-006e-45b6-96d3-e7ef6f759501", 
        "description": "sample_ha_router", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "available_gateways": 500, 
        "id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17", 
        "name": "sample-ha-router"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:ha_router:d4286c1d-86e7-42d3-9d84-a4d9daa3ae17:1:r723b
[
    "monitoring_worker", 
    {
        "is_first": true, 
        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17", 
        "handler": "monitoring_worker", 
        "job_name": "ha_router:d4286c1d-86e7-42d3-9d84-a4d9daa3ae17:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "198b93f2-006e-45b6-96d3-e7ef6f759501"
                    }
                ], 
                "type": "value", 
                "value": "198b93f2-006e-45b6-96d3-e7ef6f759501", 
                "param": "secondary_device_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "9b82b55a-551e-4069-ae77-c972e30ab0cc"
                    }
                ], 
                "type": "value", 
                "value": "9b82b55a-551e-4069-ae77-c972e30ab0cc", 
                "param": "primary_device_id"
            }
        ], 
        "resource_type": "ha_router", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:ha_router:d4286c1d-86e7-42d3-9d84-a4d9daa3ae17:1:r723b", 
        "resource_input": {
            "maximum_gateways": 500, 
            "status": "PENDING_CREATE", 
            "primary_router_id": "9b82b55a-551e-4069-ae77-c972e30ab0cc", 
            "secondary_router_id": "198b93f2-006e-45b6-96d3-e7ef6f759501", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "name": "sample-ha-router", 
            "available_gateways": 500, 
            "id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17", 
            "description": "sample_ha_router"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/job_state/v2.0/ha_routers/d4286c1d-86e7-42d3-9d84-a4d9daa3ae17
{
    "state_monitoring": {
        "primary": "ACTIVE", 
        "secondary": "ACTIVE"
    }
}
```

### Checking stored data at the point of (4) in etcd

```
/state/v2.0/ha_routers/d4286c1d-86e7-42d3-9d84-a4d9daa3ae17
{
    "state": {
        "state_monitoring": "{\"primary\": \"ACTIVE\", \"secondary\": \"ACTIVE\"}", 
        "worker_state": "CREATE_COMPLETED"
    }, 
    "version": 1, 
    "error": ""
}
```
