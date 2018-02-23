# Stored data in etcd: Create Network (dummy-net)

These are stored data for "heat_templates" in etcd.

* network

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/networks/ce9a7a92-d11a-4fc6-8ae7-18061b62c98f
{
    "body": {
        "status": "PENDING_CREATE", 
        "subnets": [], 
        "description": "dummy network for load_balancer", 
        "admin_state_up": true, 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
        "tags": {}, 
        "plane": "data", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "shared": false, 
        "id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
        "name": "dummy-net"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/create:heat_worker:network:ce9a7a92-d11a-4fc6-8ae7-18061b62c98f:1:4pxn8
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
        "handler": "heat_worker", 
        "job_name": "network:ce9a7a92-d11a-4fc6-8ae7-18061b62c98f:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
                "param": "uuid"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "3", 
                "param": "heat_timeout"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
                "param": "name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": true, 
                "param": "admin_state_up"
            }
        ], 
        "resource_type": "network", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:network:ce9a7a92-d11a-4fc6-8ae7-18061b62c98f:1:4pxn8", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "subnets": [], 
            "description": "dummy network for load_balancer", 
            "tags": {}, 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "admin_state_up": true, 
            "plane": "data", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "shared": false, 
            "id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
            "name": "dummy-net"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/networks/ce9a7a92-d11a-4fc6-8ae7-18061b62c98f
{
    "stack_id": "network_ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "network:ce9a7a92-d11a-4fc6-8ae7-18061b62c98f"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/networks/ce9a7a92-d11a-4fc6-8ae7-18061b62c98f
{
    "heat_outputs": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/networks/ce9a7a92-d11a-4fc6-8ae7-18061b62c98f
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": [], \"description\": \"The name of the virtual network.\", \"output_key\": \"route_targets\"}, {\"output_value\": \"default-domain:usertenant:ce9a7a92-d11a-4fc6-8ae7-18061b62c98f\", \"description\": \"The FQ name of the virtual network.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"ce9a7a92-d11a-4fc6-8ae7-18061b62c98f\", \"description\": \"A unique id for the virtual network.\", \"output_key\": \"id\"}, {\"output_value\": \"ce9a7a92-d11a-4fc6-8ae7-18061b62c98f\", \"description\": \"The name of the virtual network.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
