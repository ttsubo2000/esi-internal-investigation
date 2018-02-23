# Stored data in etcd: Create Edge Router

These are stored data for "heat_templates" in etcd.

* edge_router_monitoring

![scope](../../images/esi_interface.010.png)

These are stored data for "Create Edge Router" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/edge_routers/198b93f2-006e-45b6-96d3-e7ef6f759501
{
    "body": {
        "status": "PENDING_CREATE", 
        "name": "vMX-router-01", 
        "ssh_port": 830, 
        "ip": "10.79.5.184", 
        "autonomous_system": "65101", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "login": "esi", 
        "password": "esiesi0000", 
        "id": "198b93f2-006e-45b6-96d3-e7ef6f759501", 
        "description": "MX80 #1"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:edge_router:198b93f2-006e-45b6-96d3-e7ef6f759501:1:wngsi
[
    "monitoring_worker", 
    {
        "is_first": true, 
        "resource_id": "198b93f2-006e-45b6-96d3-e7ef6f759501", 
        "handler": "monitoring_worker", 
        "job_name": "edge_router:198b93f2-006e-45b6-96d3-e7ef6f759501:1", 
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
                "value": "10.79.5.184", 
                "param": "device_ip"
            }
        ], 
        "resource_type": "edge_router", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:edge_router:198b93f2-006e-45b6-96d3-e7ef6f759501:1:wngsi", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "vMX-router-01", 
            "ssh_port": 830, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "id": "198b93f2-006e-45b6-96d3-e7ef6f759501", 
            "ip": "10.79.5.184", 
            "login": "esi", 
            "password": "esiesi0000", 
            "autonomous_system": "65101", 
            "description": "MX80 #1"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/job_state/v2.0/edge_routers/198b93f2-006e-45b6-96d3-e7ef6f759501
{
    "state_monitoring": {
        "router": "ACTIVE"
    }
}
```

### Checking stored data at the point of (4) in etcd

```
/state/v2.0/edge_routers/198b93f2-006e-45b6-96d3-e7ef6f759501
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
/monitoring/v2.0/edge_routers/198b93f2-006e-45b6-96d3-e7ef6f759501
{
    "router": "UP", 
    "version": 1
}
```
