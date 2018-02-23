# Stored data in etcd: Create Network (admin-net)

These are stored data for "heat_templates" in etcd.

* network

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/networks/75c2c3ec-7fe7-494c-a35c-db3f94d3a554
{
    "body": {
        "status": "PENDING_CREATE", 
        "subnets": [], 
        "description": "adminpod network", 
        "admin_state_up": true, 
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
        "tags": {}, 
        "plane": "data", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "shared": false, 
        "id": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
        "name": "adminpod-net"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/create:heat_worker:network:75c2c3ec-7fe7-494c-a35c-db3f94d3a554:1:s0u5y
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
        "handler": "heat_worker", 
        "job_name": "network:75c2c3ec-7fe7-494c-a35c-db3f94d3a554:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
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
                "value": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
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
        "id": "create:heat_worker:network:75c2c3ec-7fe7-494c-a35c-db3f94d3a554:1:s0u5y", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "subnets": [], 
            "description": "adminpod network", 
            "tags": {}, 
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
            "admin_state_up": true, 
            "plane": "data", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "shared": false, 
            "id": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
            "name": "adminpod-net"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/networks/75c2c3ec-7fe7-494c-a35c-db3f94d3a554
{
    "stack_id": "network_75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "network:75c2c3ec-7fe7-494c-a35c-db3f94d3a554"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/networks/75c2c3ec-7fe7-494c-a35c-db3f94d3a554
{
    "heat_outputs": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/networks/75c2c3ec-7fe7-494c-a35c-db3f94d3a554
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": [], \"description\": \"The name of the virtual network.\", \"output_key\": \"route_targets\"}, {\"output_value\": \"default-domain:usertenant:75c2c3ec-7fe7-494c-a35c-db3f94d3a554\", \"description\": \"The FQ name of the virtual network.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"75c2c3ec-7fe7-494c-a35c-db3f94d3a554\", \"description\": \"A unique id for the virtual network.\", \"output_key\": \"id\"}, {\"output_value\": \"75c2c3ec-7fe7-494c-a35c-db3f94d3a554\", \"description\": \"The name of the virtual network.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
