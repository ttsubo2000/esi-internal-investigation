# Stored data in etcd: Create Network (user-net)

These are stored data for "heat_templates" in etcd.

* network

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/networks/774acf45-316f-4431-b31b-08770b76d761
{
    "body": {
        "status": "PENDING_CREATE", 
        "subnets": [], 
        "description": "load_balancer network", 
        "admin_state_up": true, 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
        "tags": {}, 
        "plane": "data", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "shared": false, 
        "id": "774acf45-316f-4431-b31b-08770b76d761", 
        "name": "sample-lb-net"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/create:heat_worker:network:774acf45-316f-4431-b31b-08770b76d761:1:do4lx
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "774acf45-316f-4431-b31b-08770b76d761", 
        "handler": "heat_worker", 
        "job_name": "network:774acf45-316f-4431-b31b-08770b76d761:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "774acf45-316f-4431-b31b-08770b76d761", 
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
                "value": "774acf45-316f-4431-b31b-08770b76d761", 
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
        "id": "create:heat_worker:network:774acf45-316f-4431-b31b-08770b76d761:1:do4lx", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "subnets": [], 
            "description": "load_balancer network", 
            "tags": {}, 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "admin_state_up": true, 
            "plane": "data", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "shared": false, 
            "id": "774acf45-316f-4431-b31b-08770b76d761", 
            "name": "sample-lb-net"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/networks/774acf45-316f-4431-b31b-08770b76d761
{
    "stack_id": "network_774acf45-316f-4431-b31b-08770b76d761", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:774acf45-316f-4431-b31b-08770b76d761", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "774acf45-316f-4431-b31b-08770b76d761", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "774acf45-316f-4431-b31b-08770b76d761", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "network:774acf45-316f-4431-b31b-08770b76d761"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/networks/774acf45-316f-4431-b31b-08770b76d761
{
    "heat_outputs": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:774acf45-316f-4431-b31b-08770b76d761", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "774acf45-316f-4431-b31b-08770b76d761", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "774acf45-316f-4431-b31b-08770b76d761", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/networks/774acf45-316f-4431-b31b-08770b76d761
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": [], \"description\": \"The name of the virtual network.\", \"output_key\": \"route_targets\"}, {\"output_value\": \"default-domain:usertenant:774acf45-316f-4431-b31b-08770b76d761\", \"description\": \"The FQ name of the virtual network.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"774acf45-316f-4431-b31b-08770b76d761\", \"description\": \"A unique id for the virtual network.\", \"output_key\": \"id\"}, {\"output_value\": \"774acf45-316f-4431-b31b-08770b76d761\", \"description\": \"The name of the virtual network.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
