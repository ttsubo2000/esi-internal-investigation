# Stored data in etcd: Create Network (admin-net)

These are stored data for "heat_templates" in etcd.

* network

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/networks/168c1535-9001-49c7-bb05-21844570a83c
{
    "body": {
        "status": "PENDING_CREATE", 
        "subnets": [], 
        "description": "adminpod network", 
        "admin_state_up": true, 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
        "tags": {}, 
        "plane": "data", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "shared": false, 
        "id": "168c1535-9001-49c7-bb05-21844570a83c", 
        "name": "adminpod-net"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/create:heat_worker:network:168c1535-9001-49c7-bb05-21844570a83c:1:0jhpg
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "168c1535-9001-49c7-bb05-21844570a83c", 
        "handler": "heat_worker", 
        "job_name": "network:168c1535-9001-49c7-bb05-21844570a83c:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "168c1535-9001-49c7-bb05-21844570a83c", 
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
                "value": "168c1535-9001-49c7-bb05-21844570a83c", 
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
        "id": "create:heat_worker:network:168c1535-9001-49c7-bb05-21844570a83c:1:0jhpg", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "subnets": [], 
            "description": "adminpod network", 
            "tags": {}, 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "admin_state_up": true, 
            "plane": "data", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "shared": false, 
            "id": "168c1535-9001-49c7-bb05-21844570a83c", 
            "name": "adminpod-net"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/networks/168c1535-9001-49c7-bb05-21844570a83c
{
    "stack_id": "network_168c1535-9001-49c7-bb05-21844570a83c", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:168c1535-9001-49c7-bb05-21844570a83c", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "168c1535-9001-49c7-bb05-21844570a83c", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "168c1535-9001-49c7-bb05-21844570a83c", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "network:168c1535-9001-49c7-bb05-21844570a83c"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/networks/168c1535-9001-49c7-bb05-21844570a83c
{
    "heat_outputs": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:168c1535-9001-49c7-bb05-21844570a83c", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "168c1535-9001-49c7-bb05-21844570a83c", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "168c1535-9001-49c7-bb05-21844570a83c", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/networks/168c1535-9001-49c7-bb05-21844570a83c
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": [], \"description\": \"The name of the virtual network.\", \"output_key\": \"route_targets\"}, {\"output_value\": \"default-domain:usertenant:168c1535-9001-49c7-bb05-21844570a83c\", \"description\": \"The FQ name of the virtual network.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"168c1535-9001-49c7-bb05-21844570a83c\", \"description\": \"A unique id for the virtual network.\", \"output_key\": \"id\"}, {\"output_value\": \"168c1535-9001-49c7-bb05-21844570a83c\", \"description\": \"The name of the virtual network.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
