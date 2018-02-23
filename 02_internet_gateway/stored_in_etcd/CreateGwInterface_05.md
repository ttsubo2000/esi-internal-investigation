# Stored data in etcd: Create Gw Interface

These are stored data for "heat_templates" in etcd.

* ese_logical_port
* ese_logical_port_monitoring

![scope](../../images/esi_interface.008.png)

These are stored data for "Create Gw Interface" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ese_logical_ports/3ce86e39-7a81-46f8-b0c4-62a4776746f1
{
    "body": {
        "status": "PENDING_CREATE", 
        "name": "xe-0/0/4.1025", 
        "tags": {}, 
        "network_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
        "gw_interface_id": "b9618566-14ea-4505-8eae-8fdb4b6a0ec1", 
        "port_ids": [
            "7abe783f-4837-417d-b76f-771ec4d38b97"
        ], 
        "ese_physical_port_id": "8a4bbfe0-5aae-42f5-8b94-c4c14b9e7306", 
        "connected_resource": "gw_interface", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "type": "L2", 
        "id": "3ce86e39-7a81-46f8-b0c4-62a4776746f1", 
        "vlan_id": 1025, 
        "description": "ESE Logical port for Port 7abe783f-4837-417d-b76f-771ec4d38b97"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:ese_logical_port:3ce86e39-7a81-46f8-b0c4-62a4776746f1:1:3l58a
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "3ce86e39-7a81-46f8-b0c4-62a4776746f1", 
        "handler": "heat_worker", 
        "job_name": "ese_logical_port:3ce86e39-7a81-46f8-b0c4-62a4776746f1:1", 
        "dependency": [
            "create:heat_worker:port:7abe783f-4837-417d-b76f-771ec4d38b97:1:3gezy"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "xe-0/0/4.1025", 
                "param": "logical_port_name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "L2", 
                "param": "logical_port_type"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "port", 
                        "resource_id": "7abe783f-4837-417d-b76f-771ec4d38b97"
                    }
                ], 
                "type": "list", 
                "value": [
                    {
                        "param": "virtual_machine_interface_ids", 
                        "type": "output_key", 
                        "value": {
                            "output_key": "id", 
                            "resource_type": "port", 
                            "resource_id": "7abe783f-4837-417d-b76f-771ec4d38b97"
                        }, 
                        "resources": []
                    }
                ], 
                "param": "virtual_machine_interface_ids"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": 1025, 
                "param": "logical_port_vlan_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_physical_port", 
                        "resource_id": "8a4bbfe0-5aae-42f5-8b94-c4c14b9e7306"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "ese_physical_port", 
                    "resource_id": "8a4bbfe0-5aae-42f5-8b94-c4c14b9e7306"
                }, 
                "param": "physical_port_id"
            }
        ], 
        "resource_type": "ese_logical_port", 
        "action": "create", 
        "is_last": false, 
        "on_failure": "fail", 
        "id": "create:heat_worker:ese_logical_port:3ce86e39-7a81-46f8-b0c4-62a4776746f1:1:3l58a", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "xe-0/0/4.1025", 
            "tags": {}, 
            "network_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
            "gw_interface_id": "b9618566-14ea-4505-8eae-8fdb4b6a0ec1", 
            "port_ids": [
                "7abe783f-4837-417d-b76f-771ec4d38b97"
            ], 
            "ese_physical_port_id": "8a4bbfe0-5aae-42f5-8b94-c4c14b9e7306", 
            "connected_resource": "gw_interface", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "type": "L2", 
            "id": "3ce86e39-7a81-46f8-b0c4-62a4776746f1", 
            "vlan_id": 1025, 
            "description": "ESE Logical port for Port 7abe783f-4837-417d-b76f-771ec4d38b97"
        }
    }, 
    0
]
```

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:ese_logical_port:3ce86e39-7a81-46f8-b0c4-62a4776746f1:1:pfhc1
[
    "monitoring_worker", 
    {
        "is_first": false, 
        "resource_id": "3ce86e39-7a81-46f8-b0c4-62a4776746f1", 
        "handler": "monitoring_worker", 
        "job_name": "ese_logical_port:3ce86e39-7a81-46f8-b0c4-62a4776746f1:1", 
        "dependency": [
            "create:heat_worker:ese_logical_port:3ce86e39-7a81-46f8-b0c4-62a4776746f1:1:3l58a"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "xe-0/0/4.1025", 
                "param": "name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [
                    "7abe783f-4837-417d-b76f-771ec4d38b97"
                ], 
                "param": "port_ids"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_physical_port", 
                        "resource_id": "8a4bbfe0-5aae-42f5-8b94-c4c14b9e7306"
                    }, 
                    {
                        "resource_type": "ese_device", 
                        "resource_id": "a1f745c1-e6b9-45ef-94db-f33b37709fb0"
                    }
                ], 
                "type": "value", 
                "value": "10.161.0.34", 
                "param": "device_ip"
            }, 
            {
                "resources": [], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "ese_logical_port", 
                    "resource_id": "3ce86e39-7a81-46f8-b0c4-62a4776746f1"
                }, 
                "param": "contarail_port_id"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "ESE_NODE_COMMUNITY", 
                "param": "community_name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "3ce86e39-7a81-46f8-b0c4-62a4776746f1", 
                "param": "id"
            }
        ], 
        "resource_type": "ese_logical_port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:ese_logical_port:3ce86e39-7a81-46f8-b0c4-62a4776746f1:1:pfhc1", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "xe-0/0/4.1025", 
            "tags": {}, 
            "network_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
            "gw_interface_id": "b9618566-14ea-4505-8eae-8fdb4b6a0ec1", 
            "port_ids": [
                "7abe783f-4837-417d-b76f-771ec4d38b97"
            ], 
            "ese_physical_port_id": "8a4bbfe0-5aae-42f5-8b94-c4c14b9e7306", 
            "connected_resource": "gw_interface", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "type": "L2", 
            "id": "3ce86e39-7a81-46f8-b0c4-62a4776746f1", 
            "vlan_id": 1025, 
            "description": "ESE Logical port for Port 7abe783f-4837-417d-b76f-771ec4d38b97"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/ese_logical_ports/3ce86e39-7a81-46f8-b0c4-62a4776746f1
{
    "stack_id": "ese_logical_port_3ce86e39-7a81-46f8-b0c4-62a4776746f1", 
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "cccccccc-cccc-cccc-cccc-cccccccccccc", 
            "description": "A unique id for the logical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": null, 
            "output_error": "'ContrailLogicalInterface' object has no attribute 'li_uuid'", 
            "description": "The name of the logical interface.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "ese_logical_port:3ce86e39-7a81-46f8-b0c4-62a4776746f1"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/ese_logical_ports/3ce86e39-7a81-46f8-b0c4-62a4776746f1
{
    "heat_outputs": [
        {
            "output_value": "cccccccc-cccc-cccc-cccc-cccccccccccc", 
            "description": "A unique id for the logical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": null, 
            "output_error": "'ContrailLogicalInterface' object has no attribute 'li_uuid'", 
            "description": "The name of the logical interface.", 
            "output_key": "name"
        }
    ]
}
```

### Checking stored data at the point of (5) in etcd

```
/esi-worker/job_state/v2.0/ese_logical_ports/3ce86e39-7a81-46f8-b0c4-62a4776746f1
{
    "state_monitoring": {
        "logical_port": "ACTIVE"
    }, 
    "heat_outputs": [
        {
            "output_value": "cccccccc-cccc-cccc-cccc-cccccccccccc", 
            "description": "A unique id for the logical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": null, 
            "output_error": "'ContrailLogicalInterface' object has no attribute 'li_uuid'", 
            "description": "The name of the logical interface.", 
            "output_key": "name"
        }
    ]
}
```

### Checking stored data at the point of (6) in etcd

```
/state/v2.0/ese_logical_ports/3ce86e39-7a81-46f8-b0c4-62a4776746f1
{
    "state": {
        "state_monitoring": "{\"logical_port\": \"ACTIVE\"}", 
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"cccccccc-cccc-cccc-cccc-cccccccccccc\", \"description\": \"A unique id for the logical interface\", \"output_key\": \"id\"}, {\"output_value\": null, \"output_error\": \"'ContrailLogicalInterface' object has no attribute 'li_uuid'\", \"description\": \"The name of the logical interface.\", \"output_key\": \"name\"}]"
    }, 
    "version": 1, 
    "error": ""
}
```

### Checking stored data at the point of (7) in etcd

```
/monitoring/v2.0/ese_logical_ports/3ce86e39-7a81-46f8-b0c4-62a4776746f1
{
    "logical_port": "UP", 
    "version": 1
}
```

