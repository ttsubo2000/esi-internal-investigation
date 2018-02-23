# Stored data in etcd: Create Network (dummy-net)

These are stored data for "heat_templates" in etcd.

* network

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/networks/73b2c401-a1f3-49fb-8612-8c755b37a28d
{
    "body": {
        "status": "PENDING_CREATE", 
        "subnets": [], 
        "description": "dummy network for firewall", 
        "admin_state_up": true, 
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
        "tags": {}, 
        "plane": "data", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "shared": false, 
        "id": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
        "name": "dummy-net"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/create:heat_worker:network:73b2c401-a1f3-49fb-8612-8c755b37a28d:1:cp3xh
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
        "handler": "heat_worker", 
        "job_name": "network:73b2c401-a1f3-49fb-8612-8c755b37a28d:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
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
                "value": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
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
        "id": "create:heat_worker:network:73b2c401-a1f3-49fb-8612-8c755b37a28d:1:cp3xh", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "subnets": [], 
            "description": "dummy network for firewall", 
            "tags": {}, 
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
            "admin_state_up": true, 
            "plane": "data", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "shared": false, 
            "id": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
            "name": "dummy-net"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/networks/73b2c401-a1f3-49fb-8612-8c755b37a28d
{
    "stack_id": "network_73b2c401-a1f3-49fb-8612-8c755b37a28d", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:73b2c401-a1f3-49fb-8612-8c755b37a28d", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "network:73b2c401-a1f3-49fb-8612-8c755b37a28d"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/networks/73b2c401-a1f3-49fb-8612-8c755b37a28d
{
    "heat_outputs": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:73b2c401-a1f3-49fb-8612-8c755b37a28d", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/networks/73b2c401-a1f3-49fb-8612-8c755b37a28d
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": [], \"description\": \"The name of the virtual network.\", \"output_key\": \"route_targets\"}, {\"output_value\": \"default-domain:usertenant:73b2c401-a1f3-49fb-8612-8c755b37a28d\", \"description\": \"The FQ name of the virtual network.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"73b2c401-a1f3-49fb-8612-8c755b37a28d\", \"description\": \"A unique id for the virtual network.\", \"output_key\": \"id\"}, {\"output_value\": \"73b2c401-a1f3-49fb-8612-8c755b37a28d\", \"description\": \"The name of the virtual network.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
