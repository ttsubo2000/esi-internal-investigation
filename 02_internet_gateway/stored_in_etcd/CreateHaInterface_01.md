# Stored data in etcd: Create Ha Interface

These are stored data for "heat_templates" in etcd.

* ha_interface_monitoring

![scope](../../images/esi_interface.010.png)

These are stored data for "Create Ha Interface" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ha_interfaces/1205d3f2-7568-412a-a554-012340ab3172
{
    "body": {
        "status": "PENDING_CREATE", 
        "secondary_interface_id": "469e4283-80e6-491c-830f-c483c1f7c695", 
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
        "ha_router_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17", 
        "primary_interface_id": "1fda2a88-f7e9-4982-9ce2-d65c9611aae7", 
        "maximum_ga_bandwidth": 500, 
        "id": "1205d3f2-7568-412a-a554-012340ab3172", 
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
/jobs/all/create:monitoring_worker:ha_interface:1205d3f2-7568-412a-a554-012340ab3172:1:r9e1w
[
    "monitoring_worker", 
    {
        "is_first": true, 
        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172", 
        "handler": "monitoring_worker", 
        "job_name": "ha_interface:1205d3f2-7568-412a-a554-012340ab3172:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "1fda2a88-f7e9-4982-9ce2-d65c9611aae7"
                    }
                ], 
                "type": "value", 
                "value": "1fda2a88-f7e9-4982-9ce2-d65c9611aae7", 
                "param": "primary_interface_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "469e4283-80e6-491c-830f-c483c1f7c695"
                    }
                ], 
                "type": "value", 
                "value": "469e4283-80e6-491c-830f-c483c1f7c695", 
                "param": "secondary_interface_id"
            }
        ], 
        "resource_type": "ha_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:ha_interface:1205d3f2-7568-412a-a554-012340ab3172:1:r9e1w", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "gateway_instances_count": 0, 
            "description": "", 
            "admin_state_up": true, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "available_be_bandwidth": 500, 
            "id": "1205d3f2-7568-412a-a554-012340ab3172", 
            "vlan_pool_state": "//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////+AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM=", 
            "secondary_interface_id": "469e4283-80e6-491c-830f-c483c1f7c695", 
            "available_ga_bandwidth": 500, 
            "ha_router_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17", 
            "maximum_be_bandwidth": 500, 
            "restricted_vlans": "0-1024,4094", 
            "vlan_ids_available": 3069, 
            "maximum_ga_bandwidth": 500, 
            "primary_interface_id": "1fda2a88-f7e9-4982-9ce2-d65c9611aae7", 
            "link_type": "downlink", 
            "name": "sample-ha-router-downlink"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/job_state/v2.0/ha_interfaces/1205d3f2-7568-412a-a554-012340ab3172
{
    "state_monitoring": {
        "primary": "ACTIVE", 
        "secondary": "ACTIVE"
    }
}
```

### Checking stored data at the point of (4) in etcd

```
/state/v2.0/ha_interfaces/1205d3f2-7568-412a-a554-012340ab3172
{
    "state": {
        "state_monitoring": "{\"primary\": \"ACTIVE\", \"secondary\": \"ACTIVE\"}", 
        "worker_state": "CREATE_COMPLETED"
    }, 
    "version": 1, 
    "error": ""
}
```
