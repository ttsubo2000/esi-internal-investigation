# Stored data in etcd: Create Ha Interface

These are stored data for "heat_templates" in etcd.

* ha_interface_monitoring

![scope](../../images/esi_interface.010.png)

These are stored data for "Create Ha Interface" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ha_interfaces/372ed357-e622-41fb-a613-076d332838e2
{
    "body": {
        "status": "PENDING_CREATE", 
        "secondary_interface_id": "96c3629b-9bfb-4d54-adc1-750d024c2858", 
        "gateway_instances_count": 0, 
        "description": "", 
        "vlan_ids_available": 3069, 
        "admin_state_up": true, 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "available_be_bandwidth": 0, 
        "vlan_pool_state": "//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////+AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM=", 
        "maximum_be_bandwidth": 0, 
        "restricted_vlans": "0-1024,4094", 
        "available_ga_bandwidth": 0, 
        "ha_router_id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258", 
        "primary_interface_id": "a752c6c0-2075-4e7f-9040-5fcefcad0252", 
        "maximum_ga_bandwidth": 0, 
        "id": "372ed357-e622-41fb-a613-076d332838e2", 
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
/jobs/all/create:monitoring_worker:ha_interface:372ed357-e622-41fb-a613-076d332838e2:1:zv0bv
[
    "monitoring_worker", 
    {
        "is_first": true, 
        "resource_id": "372ed357-e622-41fb-a613-076d332838e2", 
        "handler": "monitoring_worker", 
        "job_name": "ha_interface:372ed357-e622-41fb-a613-076d332838e2:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "a752c6c0-2075-4e7f-9040-5fcefcad0252"
                    }
                ], 
                "type": "value", 
                "value": "a752c6c0-2075-4e7f-9040-5fcefcad0252", 
                "param": "primary_interface_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "96c3629b-9bfb-4d54-adc1-750d024c2858"
                    }
                ], 
                "type": "value", 
                "value": "96c3629b-9bfb-4d54-adc1-750d024c2858", 
                "param": "secondary_interface_id"
            }
        ], 
        "resource_type": "ha_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:ha_interface:372ed357-e622-41fb-a613-076d332838e2:1:zv0bv", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "gateway_instances_count": 0, 
            "description": "", 
            "admin_state_up": true, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "available_be_bandwidth": 0, 
            "id": "372ed357-e622-41fb-a613-076d332838e2", 
            "vlan_pool_state": "//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////+AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM=", 
            "secondary_interface_id": "96c3629b-9bfb-4d54-adc1-750d024c2858", 
            "available_ga_bandwidth": 0, 
            "ha_router_id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258", 
            "maximum_be_bandwidth": 0, 
            "restricted_vlans": "0-1024,4094", 
            "vlan_ids_available": 3069, 
            "maximum_ga_bandwidth": 0, 
            "primary_interface_id": "a752c6c0-2075-4e7f-9040-5fcefcad0252", 
            "link_type": "downlink", 
            "name": "sample-ha-router-downlink"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/job_state/v2.0/ha_interfaces/372ed357-e622-41fb-a613-076d332838e2
{
    "state_monitoring": {
        "primary": "ACTIVE", 
        "secondary": "ACTIVE"
    }
}
```

### Checking stored data at the point of (4) in etcd

```
/state/v2.0/ha_interfaces/372ed357-e622-41fb-a613-076d332838e2
{
    "state": {
        "state_monitoring": "{\"primary\": \"ACTIVE\", \"secondary\": \"ACTIVE\"}", 
        "worker_state": "CREATE_COMPLETED"
    }, 
    "version": 1, 
    "error": ""
}
```
