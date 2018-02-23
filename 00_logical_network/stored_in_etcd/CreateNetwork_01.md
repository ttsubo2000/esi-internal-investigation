# Stored data in etcd: Create Network

These are stored data for "heat_templates" in etcd.

* network

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/networks/35bc496f-3c0e-46b4-a5c0-33810e8e7263
{
    "body": {
        "status": "PENDING_CREATE", 
        "subnets": [], 
        "description": "sample network", 
        "admin_state_up": true, 
        "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
        "tags": {}, 
        "plane": "data", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "shared": false, 
        "id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
        "name": "sample-network"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/create:heat_worker:network:35bc496f-3c0e-46b4-a5c0-33810e8e7263:1:pp459
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
        "handler": "heat_worker", 
        "job_name": "network:35bc496f-3c0e-46b4-a5c0-33810e8e7263:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
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
                "value": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
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
        "id": "create:heat_worker:network:35bc496f-3c0e-46b4-a5c0-33810e8e7263:1:pp459", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "subnets": [], 
            "description": "sample network", 
            "tags": {}, 
            "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
            "admin_state_up": true, 
            "plane": "data", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "shared": false, 
            "id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
            "name": "sample-network"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/networks/35bc496f-3c0e-46b4-a5c0-33810e8e7263
{
    "stack_id": "network_35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "network:35bc496f-3c0e-46b4-a5c0-33810e8e7263"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/networks/35bc496f-3c0e-46b4-a5c0-33810e8e7263
{
    "heat_outputs": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/networks/35bc496f-3c0e-46b4-a5c0-33810e8e7263
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": [], \"description\": \"The name of the virtual network.\", \"output_key\": \"route_targets\"}, {\"output_value\": \"default-domain:usertenant:35bc496f-3c0e-46b4-a5c0-33810e8e7263\", \"description\": \"The FQ name of the virtual network.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"35bc496f-3c0e-46b4-a5c0-33810e8e7263\", \"description\": \"A unique id for the virtual network.\", \"output_key\": \"id\"}, {\"output_value\": \"35bc496f-3c0e-46b4-a5c0-33810e8e7263\", \"description\": \"The name of the virtual network.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
