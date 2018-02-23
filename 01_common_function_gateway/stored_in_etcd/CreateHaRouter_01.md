# Stored data in etcd: Create Ha Router

These are stored data for "heat_templates" in etcd.

* ha_router_monitoring

![scope](../../images/esi_interface.010.png)

These are stored data for "Create Ha Router" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ha_routers/3a3d7a43-d749-44e8-90bc-de7b37d1d258
{
    "body": {
        "maximum_gateways": 500, 
        "status": "PENDING_CREATE", 
        "primary_router_id": "8aba84f9-4675-4d22-a231-e9eabde80818", 
        "secondary_router_id": "769b5e3b-3320-41ec-9be0-4567b50f1aab", 
        "description": "sample_ha_router", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "available_gateways": 500, 
        "id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258", 
        "name": "sample-ha-router"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:ha_router:3a3d7a43-d749-44e8-90bc-de7b37d1d258:1:qt83z
[
    "monitoring_worker", 
    {
        "is_first": true, 
        "resource_id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258", 
        "handler": "monitoring_worker", 
        "job_name": "ha_router:3a3d7a43-d749-44e8-90bc-de7b37d1d258:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "769b5e3b-3320-41ec-9be0-4567b50f1aab"
                    }
                ], 
                "type": "value", 
                "value": "769b5e3b-3320-41ec-9be0-4567b50f1aab", 
                "param": "secondary_device_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "8aba84f9-4675-4d22-a231-e9eabde80818"
                    }
                ], 
                "type": "value", 
                "value": "8aba84f9-4675-4d22-a231-e9eabde80818", 
                "param": "primary_device_id"
            }
        ], 
        "resource_type": "ha_router", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:ha_router:3a3d7a43-d749-44e8-90bc-de7b37d1d258:1:qt83z", 
        "resource_input": {
            "maximum_gateways": 500, 
            "status": "PENDING_CREATE", 
            "primary_router_id": "8aba84f9-4675-4d22-a231-e9eabde80818", 
            "secondary_router_id": "769b5e3b-3320-41ec-9be0-4567b50f1aab", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "name": "sample-ha-router", 
            "available_gateways": 500, 
            "id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258", 
            "description": "sample_ha_router"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/job_state/v2.0/ha_routers/3a3d7a43-d749-44e8-90bc-de7b37d1d258
{
    "state_monitoring": {
        "primary": "ACTIVE", 
        "secondary": "ACTIVE"
    }
}
```

### Checking stored data at the point of (4) in etcd

```
/state/v2.0/ha_routers/3a3d7a43-d749-44e8-90bc-de7b37d1d258
{
    "state": {
        "state_monitoring": "{\"primary\": \"ACTIVE\", \"secondary\": \"ACTIVE\"}", 
        "worker_state": "CREATE_COMPLETED"
    }, 
    "version": 1, 
    "error": ""
}
```
