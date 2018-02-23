# Stored data in etcd: Create Edge Router

These are stored data for "heat_templates" in etcd.

* edge_router_monitoring

![scope](../../images/esi_interface.010.png)

These are stored data for "Create Edge Router" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/edge_routers/9b82b55a-551e-4069-ae77-c972e30ab0cc
{
    "body": {
        "status": "PENDING_CREATE", 
        "name": "vMX-router-02", 
        "ssh_port": 830, 
        "ip": "10.79.5.185", 
        "autonomous_system": "65101", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "login": "esi", 
        "password": "esiesi0000", 
        "id": "9b82b55a-551e-4069-ae77-c972e30ab0cc", 
        "description": "MX80 #2"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:edge_router:9b82b55a-551e-4069-ae77-c972e30ab0cc:1:iybq9
[
    "monitoring_worker", 
    {
        "is_first": true, 
        "resource_id": "9b82b55a-551e-4069-ae77-c972e30ab0cc", 
        "handler": "monitoring_worker", 
        "job_name": "edge_router:9b82b55a-551e-4069-ae77-c972e30ab0cc:1", 
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
                "resources": [], 
                "type": "value", 
                "value": "10.79.5.185", 
                "param": "device_ip"
            }
        ], 
        "resource_type": "edge_router", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:edge_router:9b82b55a-551e-4069-ae77-c972e30ab0cc:1:iybq9", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "vMX-router-02", 
            "ssh_port": 830, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "id": "9b82b55a-551e-4069-ae77-c972e30ab0cc", 
            "ip": "10.79.5.185", 
            "login": "esi", 
            "password": "esiesi0000", 
            "autonomous_system": "65101", 
            "description": "MX80 #2"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/job_state/v2.0/edge_routers/9b82b55a-551e-4069-ae77-c972e30ab0cc
{
    "state_monitoring": {
        "router": "ACTIVE"
    }
}
```

### Checking stored data at the point of (4) in etcd

```
/state/v2.0/edge_routers/9b82b55a-551e-4069-ae77-c972e30ab0cc
{
    "state": {
        "state_monitoring": "{\"router\": \"ACTIVE\"}", 
        "worker_state": "CREATE_COMPLETED"
    }, 
    "version": 1, 
    "error": ""
}
```

### Checking stored data at the point of (5) in etcd

```
/monitoring/v2.0/edge_routers/9b82b55a-551e-4069-ae77-c972e30ab0cc
{
    "router": "UP", 
    "version": 1
}
```
