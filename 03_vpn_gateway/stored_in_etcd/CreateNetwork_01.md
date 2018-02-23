# Stored data in etcd: Create Network

These are stored data for "heat_templates" in etcd.

* network
* network_monitoring

![scope](../../images/esi_interface.008.png)

These are stored data for "Create Network" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/networks/bb69041d-c654-4e9f-a763-afd4333275bc
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
        "id": "bb69041d-c654-4e9f-a763-afd4333275bc", 
        "name": "sample-network"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:network:bb69041d-c654-4e9f-a763-afd4333275bc:1:gxz4g
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "bb69041d-c654-4e9f-a763-afd4333275bc", 
        "handler": "heat_worker", 
        "job_name": "network:bb69041d-c654-4e9f-a763-afd4333275bc:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "bb69041d-c654-4e9f-a763-afd4333275bc", 
                "param": "uuid"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "bb69041d-c654-4e9f-a763-afd4333275bc", 
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
        "id": "create:heat_worker:network:bb69041d-c654-4e9f-a763-afd4333275bc:1:gxz4g", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "subnets": [], 
            "description": "Sample Network", 
            "tags": {}, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "admin_state_up": true, 
            "plane": "data", 
            "shared": false, 
            "id": "bb69041d-c654-4e9f-a763-afd4333275bc", 
            "name": "sample-network"
        }
    }, 
    0
]
```

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:network:bb69041d-c654-4e9f-a763-afd4333275bc:1:iqi5y
[
    "monitoring_worker", 
    {
        "is_first": false, 
        "resource_id": "bb69041d-c654-4e9f-a763-afd4333275bc", 
        "handler": "monitoring_worker", 
        "job_name": "network:bb69041d-c654-4e9f-a763-afd4333275bc:1", 
        "dependency": [
            "create:heat_worker:network:bb69041d-c654-4e9f-a763-afd4333275bc:1:gxz4g"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "output_key", 
                "value": {
                    "output_key": "fq_name", 
                    "resource_type": "network", 
                    "resource_id": "bb69041d-c654-4e9f-a763-afd4333275bc"
                }, 
                "param": "fq_name"
            }, 
            {
                "resources": [], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "bb69041d-c654-4e9f-a763-afd4333275bc"
                }, 
                "param": "uuid"
            }
        ], 
        "resource_type": "network", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:network:bb69041d-c654-4e9f-a763-afd4333275bc:1:iqi5y", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "subnets": [], 
            "description": "Sample Network", 
            "tags": {}, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "admin_state_up": true, 
            "plane": "data", 
            "shared": false, 
            "id": "bb69041d-c654-4e9f-a763-afd4333275bc", 
            "name": "sample-network"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/networks/bb69041d-c654-4e9f-a763-afd4333275bc
{
    "stack_id": "network_bb69041d-c654-4e9f-a763-afd4333275bc", 
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "[]", 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:admin:bb69041d-c654-4e9f-a763-afd4333275bc", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "bb69041d-c654-4e9f-a763-afd4333275bc", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "bb69041d-c654-4e9f-a763-afd4333275bc", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "network:bb69041d-c654-4e9f-a763-afd4333275bc"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/networks/bb69041d-c654-4e9f-a763-afd4333275bc
{
    "heat_outputs": [
        {
            "output_value": "[]", 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:admin:bb69041d-c654-4e9f-a763-afd4333275bc", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "bb69041d-c654-4e9f-a763-afd4333275bc", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "bb69041d-c654-4e9f-a763-afd4333275bc", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ]
}
```

### Checking stored data at the point of (5) in etcd

```
/esi-worker/job_state/v2.0/networks/bb69041d-c654-4e9f-a763-afd4333275bc
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
            "output_value": "default-domain:admin:bb69041d-c654-4e9f-a763-afd4333275bc", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "bb69041d-c654-4e9f-a763-afd4333275bc", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "bb69041d-c654-4e9f-a763-afd4333275bc", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ]
}
```

### Checking stored data at the point of (6) in etcd

```
/state/v2.0/networks/bb69041d-c654-4e9f-a763-afd4333275bc
{
    "state": {
        "state_monitoring": "{\"network\": \"ACTIVE\"}", 
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"[]\", \"description\": \"The name of the virtual network.\", \"output_key\": \"route_targets\"}, {\"output_value\": \"default-domain:admin:bb69041d-c654-4e9f-a763-afd4333275bc\", \"description\": \"The FQ name of the virtual network.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"bb69041d-c654-4e9f-a763-afd4333275bc\", \"description\": \"A unique id for the virtual network.\", \"output_key\": \"id\"}, {\"output_value\": \"bb69041d-c654-4e9f-a763-afd4333275bc\", \"description\": \"The name of the virtual network.\", \"output_key\": \"name\"}]"
    }, 
    "version": 1, 
    "error": ""
}
```

### Checking stored data at the point of (7) in etcd

```
/monitoring/v2.0/networks/bb69041d-c654-4e9f-a763-afd4333275bc
{
    "version": 1, 
    "network": "UP"
}
```
