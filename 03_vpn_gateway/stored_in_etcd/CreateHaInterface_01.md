# Stored data in etcd: Create Ha Interface

These are stored data for "heat_templates" in etcd.

* ha_interface_monitoring

![scope](../../images/esi_interface.010.png)

These are stored data for "Create Ha Interface" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ha_interfaces/5e552b8f-cd5a-454c-a224-33f7da0afa24
{
    "body": {
        "status": "PENDING_CREATE", 
        "secondary_interface_id": "f87c6efe-f590-4c29-8fc9-2f914e1eb362", 
        "gateway_instances_count": 0, 
        "description": "", 
        "vlan_ids_available": 4093, 
        "admin_state_up": true, 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "available_be_bandwidth": 0, 
        "vlan_pool_state": "gAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE=", 
        "maximum_be_bandwidth": 0, 
        "restricted_vlans": "", 
        "available_ga_bandwidth": 0, 
        "ha_router_id": "f01ed0a6-7094-4e54-b14b-94657fff1efb", 
        "primary_interface_id": "6e8f473f-47ec-4b54-8f0f-d459d440393b", 
        "maximum_ga_bandwidth": 0, 
        "id": "5e552b8f-cd5a-454c-a224-33f7da0afa24", 
        "link_type": "uplink", 
        "name": "sample-ha-router-uplink"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:ha_interface:5e552b8f-cd5a-454c-a224-33f7da0afa24:1:pfty9
[
    "monitoring_worker", 
    {
        "is_first": true, 
        "resource_id": "5e552b8f-cd5a-454c-a224-33f7da0afa24", 
        "handler": "monitoring_worker", 
        "job_name": "ha_interface:5e552b8f-cd5a-454c-a224-33f7da0afa24:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "6e8f473f-47ec-4b54-8f0f-d459d440393b"
                    }
                ], 
                "type": "value", 
                "value": "6e8f473f-47ec-4b54-8f0f-d459d440393b", 
                "param": "primary_interface_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "f87c6efe-f590-4c29-8fc9-2f914e1eb362"
                    }
                ], 
                "type": "value", 
                "value": "f87c6efe-f590-4c29-8fc9-2f914e1eb362", 
                "param": "secondary_interface_id"
            }
        ], 
        "resource_type": "ha_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:ha_interface:5e552b8f-cd5a-454c-a224-33f7da0afa24:1:pfty9", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "gateway_instances_count": 0, 
            "description": "", 
            "admin_state_up": true, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "available_be_bandwidth": 0, 
            "id": "5e552b8f-cd5a-454c-a224-33f7da0afa24", 
            "vlan_pool_state": "gAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE=", 
            "secondary_interface_id": "f87c6efe-f590-4c29-8fc9-2f914e1eb362", 
            "available_ga_bandwidth": 0, 
            "ha_router_id": "f01ed0a6-7094-4e54-b14b-94657fff1efb", 
            "maximum_be_bandwidth": 0, 
            "restricted_vlans": "", 
            "vlan_ids_available": 4093, 
            "maximum_ga_bandwidth": 0, 
            "primary_interface_id": "6e8f473f-47ec-4b54-8f0f-d459d440393b", 
            "link_type": "uplink", 
            "name": "sample-ha-router-uplink"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/job_state/v2.0/ha_interfaces/5e552b8f-cd5a-454c-a224-33f7da0afa24
{
    "state_monitoring": {
        "primary": "ACTIVE", 
        "secondary": "ACTIVE"
    }
}
```

### Checking stored data at the point of (4) in etcd

```
/state/v2.0/ha_interfaces/5e552b8f-cd5a-454c-a224-33f7da0afa24
{
    "state": {
        "state_monitoring": "{\"primary\": \"ACTIVE\", \"secondary\": \"ACTIVE\"}", 
        "worker_state": "CREATE_COMPLETED"
    }, 
    "version": 1, 
    "error": ""
}
```
