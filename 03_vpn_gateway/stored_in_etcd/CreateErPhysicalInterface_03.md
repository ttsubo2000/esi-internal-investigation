# Stored data in etcd: Create Er Physical Interface

These are stored data for "heat_templates" in etcd.

* er_physical_interface_monitoring

![scope](../../images/esi_interface.010.png)

These are stored data for "Create Er Physical Interface" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/er_physical_interfaces/6b160a8d-fdad-4fe7-aaed-3ff5f729d6c8
{
    "body": {
        "status": "PENDING_CREATE", 
        "connected_ese_port_id": "176ec475-e9e8-4605-8b41-802fbc6220c1", 
        "description": "", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "device_id": "3ca3a59a-4f92-4a8a-9ec1-1c55a97c794e", 
        "id": "6b160a8d-fdad-4fe7-aaed-3ff5f729d6c8", 
        "name": "ae0"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:er_physical_interface:6b160a8d-fdad-4fe7-aaed-3ff5f729d6c8:1:2gnc1
[
    "monitoring_worker", 
    {
        "is_first": true, 
        "resource_id": "6b160a8d-fdad-4fe7-aaed-3ff5f729d6c8", 
        "handler": "monitoring_worker", 
        "job_name": "er_physical_interface:6b160a8d-fdad-4fe7-aaed-3ff5f729d6c8:1", 
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
                        "resource_id": "3ca3a59a-4f92-4a8a-9ec1-1c55a97c794e"
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
        "id": "create:monitoring_worker:er_physical_interface:6b160a8d-fdad-4fe7-aaed-3ff5f729d6c8:1:2gnc1", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "connected_ese_port_id": "176ec475-e9e8-4605-8b41-802fbc6220c1", 
            "description": "", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "name": "ae0", 
            "id": "6b160a8d-fdad-4fe7-aaed-3ff5f729d6c8", 
            "device_id": "3ca3a59a-4f92-4a8a-9ec1-1c55a97c794e"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/job_state/v2.0/er_physical_interfaces/6b160a8d-fdad-4fe7-aaed-3ff5f729d6c8
{
    "state_monitoring": {
        "interface": "ACTIVE"
    }
}
```

### Checking stored data at the point of (4) in etcd

```
/state/v2.0/er_physical_interfaces/6b160a8d-fdad-4fe7-aaed-3ff5f729d6c8
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
/monitoring/v2.0/er_physical_interfaces/6b160a8d-fdad-4fe7-aaed-3ff5f729d6c8
{
    "interface": "UP", 
    "version": 1
}
```
