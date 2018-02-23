# Stored data in etcd: Create Ha Interface

These are stored data for "heat_templates" in etcd.

* ha_interface_monitoring

![scope](../../images/esi_interface.010.png)

These are stored data for "Create Ha Interface" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ha_interfaces/a3a62a37-5657-4822-98e0-991ab63f0e96
{
    "body": {
        "status": "PENDING_CREATE", 
        "secondary_interface_id": "6b160a8d-fdad-4fe7-aaed-3ff5f729d6c8", 
        "gateway_instances_count": 0, 
        "description": "", 
        "vlan_ids_available": 3069, 
        "admin_state_up": true, 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "available_be_bandwidth": 500, 
        "vlan_pool_state": "//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////+AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM=", 
        "maximum_be_bandwidth": 500, 
        "restricted_vlans": "0-1024,4094", 
        "available_ga_bandwidth": 500, 
        "ha_router_id": "f01ed0a6-7094-4e54-b14b-94657fff1efb", 
        "primary_interface_id": "8ff57ce4-55f9-40d4-82ed-1f00c9051678", 
        "maximum_ga_bandwidth": 500, 
        "id": "a3a62a37-5657-4822-98e0-991ab63f0e96", 
        "link_type": "downlink", 
        "name": "sample-ha-router-downlink"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:ha_interface:a3a62a37-5657-4822-98e0-991ab63f0e96:1:k64ha
[
    "monitoring_worker", 
    {
        "is_first": true, 
        "resource_id": "a3a62a37-5657-4822-98e0-991ab63f0e96", 
        "handler": "monitoring_worker", 
        "job_name": "ha_interface:a3a62a37-5657-4822-98e0-991ab63f0e96:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "8ff57ce4-55f9-40d4-82ed-1f00c9051678"
                    }
                ], 
                "type": "value", 
                "value": "8ff57ce4-55f9-40d4-82ed-1f00c9051678", 
                "param": "primary_interface_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "6b160a8d-fdad-4fe7-aaed-3ff5f729d6c8"
                    }
                ], 
                "type": "value", 
                "value": "6b160a8d-fdad-4fe7-aaed-3ff5f729d6c8", 
                "param": "secondary_interface_id"
            }
        ], 
        "resource_type": "ha_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:ha_interface:a3a62a37-5657-4822-98e0-991ab63f0e96:1:k64ha", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "gateway_instances_count": 0, 
            "description": "", 
            "admin_state_up": true, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "available_be_bandwidth": 500, 
            "id": "a3a62a37-5657-4822-98e0-991ab63f0e96", 
            "vlan_pool_state": "//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////+AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM=", 
            "secondary_interface_id": "6b160a8d-fdad-4fe7-aaed-3ff5f729d6c8", 
            "available_ga_bandwidth": 500, 
            "ha_router_id": "f01ed0a6-7094-4e54-b14b-94657fff1efb", 
            "maximum_be_bandwidth": 500, 
            "restricted_vlans": "0-1024,4094", 
            "vlan_ids_available": 3069, 
            "maximum_ga_bandwidth": 500, 
            "primary_interface_id": "8ff57ce4-55f9-40d4-82ed-1f00c9051678", 
            "link_type": "downlink", 
            "name": "sample-ha-router-downlink"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/job_state/v2.0/ha_interfaces/a3a62a37-5657-4822-98e0-991ab63f0e96
{
    "state_monitoring": {
        "primary": "ACTIVE", 
        "secondary": "ACTIVE"
    }
}
```

### Checking stored data at the point of (4) in etcd

```
/state/v2.0/ha_interfaces/a3a62a37-5657-4822-98e0-991ab63f0e96
{
    "state": {
        "state_monitoring": "{\"primary\": \"ACTIVE\", \"secondary\": \"ACTIVE\"}", 
        "worker_state": "CREATE_COMPLETED"
    }, 
    "version": 1, 
    "error": ""
}
```
