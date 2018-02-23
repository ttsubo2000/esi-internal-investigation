# Stored data in etcd: Create Common Function Gateway

These are stored data for "heat_templates" in etcd.

* network
* network_monitoring

![scope](../../images/esi_interface.008.png)

These are stored data for "Create Common Function Gateway" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/networks/f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57
{
    "body": {
        "status": "PENDING_CREATE", 
        "subnets": [], 
        "description": "", 
        "admin_state_up": true, 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "tags": {}, 
        "plane": "data", 
        "shared": false, 
        "id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
        "name": "common_function_gw_access_5c241c51-2003-407a-a239-689fabd19022"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:network:f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57:1:7vfno
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
        "handler": "heat_worker", 
        "job_name": "network:f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
                "param": "uuid"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
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
        "is_last": false, 
        "on_failure": "fail", 
        "id": "create:heat_worker:network:f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57:1:7vfno", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "subnets": [], 
            "description": "", 
            "tags": {}, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "admin_state_up": true, 
            "plane": "data", 
            "shared": false, 
            "id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
            "name": "common_function_gw_access_5c241c51-2003-407a-a239-689fabd19022"
        }
    }, 
    0
]
```

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:network:f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57:1:3v9r9
[
    "monitoring_worker", 
    {
        "is_first": false, 
        "resource_id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
        "handler": "monitoring_worker", 
        "job_name": "network:f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57:1", 
        "dependency": [
            "create:heat_worker:network:f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57:1:7vfno"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "output_key", 
                "value": {
                    "output_key": "fq_name", 
                    "resource_type": "network", 
                    "resource_id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57"
                }, 
                "param": "fq_name"
            }, 
            {
                "resources": [], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57"
                }, 
                "param": "uuid"
            }
        ], 
        "resource_type": "network", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:network:f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57:1:3v9r9", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "subnets": [], 
            "description": "", 
            "tags": {}, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "admin_state_up": true, 
            "plane": "data", 
            "shared": false, 
            "id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
            "name": "common_function_gw_access_5c241c51-2003-407a-a239-689fabd19022"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/networks/f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57
{
    "stack_id": "network_f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "[]", 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:admin:f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "network:f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/networks/f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57
{
    "heat_outputs": [
        {
            "output_value": "[]", 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:admin:f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ]
}
```

### Checking stored data at the point of (5) in etcd

```
/esi-worker/job_state/v2.0/networks/f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57
{
    "state_monitoring": {
        "network": "ACTIVE"
    }, 
    "heat_outputs": [
        {
            "output_value": "[]", 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:admin:f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ]
}
```

### Checking stored data at the point of (6) in etcd

```
/state/v2.0/networks/f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57
{
    "state": {
        "state_monitoring": "{\"network\": \"ACTIVE\"}", 
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"[]\", \"description\": \"The name of the virtual network.\", \"output_key\": \"route_targets\"}, {\"output_value\": \"default-domain:admin:f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57\", \"description\": \"The FQ name of the virtual network.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57\", \"description\": \"A unique id for the virtual network.\", \"output_key\": \"id\"}, {\"output_value\": \"f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57\", \"description\": \"The name of the virtual network.\", \"output_key\": \"name\"}]"
    }, 
    "version": 1, 
    "error": ""
}
```

### Checking stored data at the point of (7) in etcd

```
/monitoring/v2.0/networks/f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57
{
    "version": 1, 
    "network": "UP"
}
```
