# Stored data in etcd: Create Er Physical Interface

These are stored data for "heat_templates" in etcd.

* er_physical_interface_monitoring

![scope](../../images/esi_interface.010.png)

These are stored data for "Create Er Physical Interface" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/er_physical_interfaces/96c3629b-9bfb-4d54-adc1-750d024c2858
{
    "body": {
        "status": "PENDING_CREATE", 
        "connected_ese_port_id": "5b2dee2e-7420-4cd4-b270-5081eb9eb371", 
        "description": "", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "device_id": "769b5e3b-3320-41ec-9be0-4567b50f1aab", 
        "id": "96c3629b-9bfb-4d54-adc1-750d024c2858", 
        "name": "ae0"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:er_physical_interface:96c3629b-9bfb-4d54-adc1-750d024c2858:1:fcdeb
[
    "monitoring_worker", 
    {
        "is_first": true, 
        "resource_id": "96c3629b-9bfb-4d54-adc1-750d024c2858", 
        "handler": "monitoring_worker", 
        "job_name": "er_physical_interface:96c3629b-9bfb-4d54-adc1-750d024c2858:1", 
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
                        "resource_id": "769b5e3b-3320-41ec-9be0-4567b50f1aab"
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
        "id": "create:monitoring_worker:er_physical_interface:96c3629b-9bfb-4d54-adc1-750d024c2858:1:fcdeb", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "connected_ese_port_id": "5b2dee2e-7420-4cd4-b270-5081eb9eb371", 
            "description": "", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "name": "ae0", 
            "id": "96c3629b-9bfb-4d54-adc1-750d024c2858", 
            "device_id": "769b5e3b-3320-41ec-9be0-4567b50f1aab"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/job_state/v2.0/er_physical_interfaces/96c3629b-9bfb-4d54-adc1-750d024c2858
{
    "state_monitoring": {
        "interface": "ACTIVE"
    }
}
```

### Checking stored data at the point of (4) in etcd

```
/state/v2.0/er_physical_interfaces/96c3629b-9bfb-4d54-adc1-750d024c2858
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
/monitoring/v2.0/er_physical_interfaces/96c3629b-9bfb-4d54-adc1-750d024c2858
{
    "interface": "UP", 
    "version": 1
}
```
