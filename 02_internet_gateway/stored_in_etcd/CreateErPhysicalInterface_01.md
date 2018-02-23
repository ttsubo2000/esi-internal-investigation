# Stored data in etcd: Create Er Physical Interface

These are stored data for "heat_templates" in etcd.

* er_physical_interface_monitoring

![scope](../../images/esi_interface.010.png)

These are stored data for "Create Er Physical Interface" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/er_physical_interfaces/1fda2a88-f7e9-4982-9ce2-d65c9611aae7
{
    "body": {
        "status": "PENDING_CREATE", 
        "connected_ese_port_id": "97fcdf3a-81a4-41a5-8ae6-52c431fc5a5c", 
        "description": "", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "device_id": "9b82b55a-551e-4069-ae77-c972e30ab0cc", 
        "id": "1fda2a88-f7e9-4982-9ce2-d65c9611aae7", 
        "name": "ae0"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:er_physical_interface:1fda2a88-f7e9-4982-9ce2-d65c9611aae7:1:hi5em
[
    "monitoring_worker", 
    {
        "is_first": true, 
        "resource_id": "1fda2a88-f7e9-4982-9ce2-d65c9611aae7", 
        "handler": "monitoring_worker", 
        "job_name": "er_physical_interface:1fda2a88-f7e9-4982-9ce2-d65c9611aae7:1", 
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
                        "resource_id": "9b82b55a-551e-4069-ae77-c972e30ab0cc"
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
        "id": "create:monitoring_worker:er_physical_interface:1fda2a88-f7e9-4982-9ce2-d65c9611aae7:1:hi5em", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "connected_ese_port_id": "97fcdf3a-81a4-41a5-8ae6-52c431fc5a5c", 
            "description": "", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "name": "ae0", 
            "id": "1fda2a88-f7e9-4982-9ce2-d65c9611aae7", 
            "device_id": "9b82b55a-551e-4069-ae77-c972e30ab0cc"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/job_state/v2.0/er_physical_interfaces/1fda2a88-f7e9-4982-9ce2-d65c9611aae7
{
    "state_monitoring": {
        "interface": "ACTIVE"
    }
}
```

### Checking stored data at the point of (4) in etcd

```
/state/v2.0/er_physical_interfaces/1fda2a88-f7e9-4982-9ce2-d65c9611aae7
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
/monitoring/v2.0/er_physical_interfaces/1fda2a88-f7e9-4982-9ce2-d65c9611aae7
{
    "interface": "UP", 
    "version": 1
}
```
