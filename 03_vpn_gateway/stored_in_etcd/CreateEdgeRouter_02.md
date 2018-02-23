# Stored data in etcd: Create Edge Router

These are stored data for "heat_templates" in etcd.

* edge_router_monitoring

![scope](../../images/esi_interface.010.png)

These are stored data for "Create Edge Router" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/edge_routers/3ca3a59a-4f92-4a8a-9ec1-1c55a97c794e
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
        "id": "3ca3a59a-4f92-4a8a-9ec1-1c55a97c794e", 
        "description": "MX80 #1"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:edge_router:3ca3a59a-4f92-4a8a-9ec1-1c55a97c794e:1:ktgx2
[
    "monitoring_worker", 
    {
        "is_first": true, 
        "resource_id": "3ca3a59a-4f92-4a8a-9ec1-1c55a97c794e", 
        "handler": "monitoring_worker", 
        "job_name": "edge_router:3ca3a59a-4f92-4a8a-9ec1-1c55a97c794e:1", 
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
        "id": "create:monitoring_worker:edge_router:3ca3a59a-4f92-4a8a-9ec1-1c55a97c794e:1:ktgx2", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "vMX-router-01", 
            "ssh_port": 830, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "id": "3ca3a59a-4f92-4a8a-9ec1-1c55a97c794e", 
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
/esi-worker/job_state/v2.0/edge_routers/3ca3a59a-4f92-4a8a-9ec1-1c55a97c794e
{
    "state_monitoring": {
        "router": "ACTIVE"
    }
}
```

### Checking stored data at the point of (4) in etcd

```
/state/v2.0/edge_routers/3ca3a59a-4f92-4a8a-9ec1-1c55a97c794e
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
/monitoring/v2.0/edge_routers/3ca3a59a-4f92-4a8a-9ec1-1c55a97c794e
{
    "router": "UP", 
    "version": 1
}
```
