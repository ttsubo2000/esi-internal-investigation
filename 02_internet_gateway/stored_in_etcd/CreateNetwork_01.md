# Stored data in etcd: Create Network

These are stored data for "heat_templates" in etcd.

* network
* network_monitoring

![scope](../../images/esi_interface.008.png)

These are stored data for "Create Network" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/networks/52d7bef8-aa17-45c3-b63e-6a0e504603f0
{
    "body": {
        "status": "PENDING_CREATE", 
        "subnets": [], 
        "description": "Sample Network", 
        "admin_state_up": true, 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "tags": {}, 
        "plane": "data", 
        "shared": false, 
        "id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
        "name": "sample-network"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:network:52d7bef8-aa17-45c3-b63e-6a0e504603f0:1:v1aq0
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
        "handler": "heat_worker", 
        "job_name": "network:52d7bef8-aa17-45c3-b63e-6a0e504603f0:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
                "param": "uuid"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
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
        "id": "create:heat_worker:network:52d7bef8-aa17-45c3-b63e-6a0e504603f0:1:v1aq0", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "subnets": [], 
            "description": "Sample Network", 
            "tags": {}, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "admin_state_up": true, 
            "plane": "data", 
            "shared": false, 
            "id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
            "name": "sample-network"
        }
    }, 
    0
]
```

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:network:52d7bef8-aa17-45c3-b63e-6a0e504603f0:1:2f10n
[
    "monitoring_worker", 
    {
        "is_first": false, 
        "resource_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
        "handler": "monitoring_worker", 
        "job_name": "network:52d7bef8-aa17-45c3-b63e-6a0e504603f0:1", 
        "dependency": [
            "create:heat_worker:network:52d7bef8-aa17-45c3-b63e-6a0e504603f0:1:v1aq0"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "output_key", 
                "value": {
                    "output_key": "fq_name", 
                    "resource_type": "network", 
                    "resource_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0"
                }, 
                "param": "fq_name"
            }, 
            {
                "resources": [], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0"
                }, 
                "param": "uuid"
            }
        ], 
        "resource_type": "network", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:network:52d7bef8-aa17-45c3-b63e-6a0e504603f0:1:2f10n", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "subnets": [], 
            "description": "Sample Network", 
            "tags": {}, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "admin_state_up": true, 
            "plane": "data", 
            "shared": false, 
            "id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
            "name": "sample-network"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/networks/52d7bef8-aa17-45c3-b63e-6a0e504603f0
{
    "stack_id": "network_52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "[]", 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:admin:52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "network:52d7bef8-aa17-45c3-b63e-6a0e504603f0"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/networks/52d7bef8-aa17-45c3-b63e-6a0e504603f0
{
    "heat_outputs": [
        {
            "output_value": "[]", 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:admin:52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ]
}
```

### Checking stored data at the point of (5) in etcd

```
/esi-worker/job_state/v2.0/networks/52d7bef8-aa17-45c3-b63e-6a0e504603f0
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
            "output_value": "default-domain:admin:52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ]
}
```

### Checking stored data at the point of (6) in etcd

```
/state/v2.0/networks/52d7bef8-aa17-45c3-b63e-6a0e504603f0
{
    "state": {
        "state_monitoring": "{\"network\": \"ACTIVE\"}", 
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"[]\", \"description\": \"The name of the virtual network.\", \"output_key\": \"route_targets\"}, {\"output_value\": \"default-domain:admin:52d7bef8-aa17-45c3-b63e-6a0e504603f0\", \"description\": \"The FQ name of the virtual network.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"52d7bef8-aa17-45c3-b63e-6a0e504603f0\", \"description\": \"A unique id for the virtual network.\", \"output_key\": \"id\"}, {\"output_value\": \"52d7bef8-aa17-45c3-b63e-6a0e504603f0\", \"description\": \"The name of the virtual network.\", \"output_key\": \"name\"}]"
    }, 
    "version": 1, 
    "error": ""
}
```

### Checking stored data at the point of (7) in etcd

```
/monitoring/v2.0/networks/52d7bef8-aa17-45c3-b63e-6a0e504603f0
{
    "version": 1, 
    "network": "UP"
}
```
