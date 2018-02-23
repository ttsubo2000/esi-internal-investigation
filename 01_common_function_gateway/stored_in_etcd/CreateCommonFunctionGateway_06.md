# Stored data in etcd: Create Common Function Gateway

These are stored data for "heat_templates" in etcd.

* ese_logical_port
* ese_logical_port_monitoring

![scope](../../images/esi_interface.008.png)

These are stored data for "Create Common Function Gateway" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ese_logical_ports/b04853c4-6ebf-441f-9093-ea4b844c4bc7
{
    "body": {
        "status": "PENDING_CREATE", 
        "name": "xe-0/0/3.1025", 
        "tags": {}, 
        "network_id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "port_ids": [
            "327f59b7-df38-4d8f-97db-d320defcab76"
        ], 
        "common_function_gateway_id": "5c241c51-2003-407a-a239-689fabd19022", 
        "ese_physical_port_id": "976156ef-05b4-47f4-9497-a36531563a08", 
        "connected_resource": "common_function_gateway", 
        "type": "L2", 
        "id": "b04853c4-6ebf-441f-9093-ea4b844c4bc7", 
        "vlan_id": 1025, 
        "description": "ESE Logical port for Port 327f59b7-df38-4d8f-97db-d320defcab76"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:ese_logical_port:b04853c4-6ebf-441f-9093-ea4b844c4bc7:1:kgv13
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "b04853c4-6ebf-441f-9093-ea4b844c4bc7", 
        "handler": "heat_worker", 
        "job_name": "ese_logical_port:b04853c4-6ebf-441f-9093-ea4b844c4bc7:1", 
        "dependency": [
            "create:heat_worker:port:327f59b7-df38-4d8f-97db-d320defcab76:1:jog8i"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "xe-0/0/3.1025", 
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
                        "resource_id": "327f59b7-df38-4d8f-97db-d320defcab76"
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
                            "resource_id": "327f59b7-df38-4d8f-97db-d320defcab76"
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
                        "resource_id": "976156ef-05b4-47f4-9497-a36531563a08"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "ese_physical_port", 
                    "resource_id": "976156ef-05b4-47f4-9497-a36531563a08"
                }, 
                "param": "physical_port_id"
            }
        ], 
        "resource_type": "ese_logical_port", 
        "action": "create", 
        "is_last": false, 
        "on_failure": "fail", 
        "id": "create:heat_worker:ese_logical_port:b04853c4-6ebf-441f-9093-ea4b844c4bc7:1:kgv13", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "xe-0/0/3.1025", 
            "tags": {}, 
            "network_id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "port_ids": [
                "327f59b7-df38-4d8f-97db-d320defcab76"
            ], 
            "common_function_gateway_id": "5c241c51-2003-407a-a239-689fabd19022", 
            "ese_physical_port_id": "976156ef-05b4-47f4-9497-a36531563a08", 
            "connected_resource": "common_function_gateway", 
            "type": "L2", 
            "id": "b04853c4-6ebf-441f-9093-ea4b844c4bc7", 
            "vlan_id": 1025, 
            "description": "ESE Logical port for Port 327f59b7-df38-4d8f-97db-d320defcab76"
        }
    }, 
    0
]
```

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:ese_logical_port:b04853c4-6ebf-441f-9093-ea4b844c4bc7:1:w8773
[
    "monitoring_worker", 
    {
        "is_first": false, 
        "resource_id": "b04853c4-6ebf-441f-9093-ea4b844c4bc7", 
        "handler": "monitoring_worker", 
        "job_name": "ese_logical_port:b04853c4-6ebf-441f-9093-ea4b844c4bc7:1", 
        "dependency": [
            "create:heat_worker:ese_logical_port:b04853c4-6ebf-441f-9093-ea4b844c4bc7:1:kgv13"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "xe-0/0/3.1025", 
                "param": "name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [
                    "327f59b7-df38-4d8f-97db-d320defcab76"
                ], 
                "param": "port_ids"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_physical_port", 
                        "resource_id": "976156ef-05b4-47f4-9497-a36531563a08"
                    }, 
                    {
                        "resource_type": "ese_device", 
                        "resource_id": "9f05b260-26ca-46f7-98c3-ad88e411a989"
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
                    "resource_id": "b04853c4-6ebf-441f-9093-ea4b844c4bc7"
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
                "value": "b04853c4-6ebf-441f-9093-ea4b844c4bc7", 
                "param": "id"
            }
        ], 
        "resource_type": "ese_logical_port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:ese_logical_port:b04853c4-6ebf-441f-9093-ea4b844c4bc7:1:w8773", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "xe-0/0/3.1025", 
            "tags": {}, 
            "network_id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "port_ids": [
                "327f59b7-df38-4d8f-97db-d320defcab76"
            ], 
            "common_function_gateway_id": "5c241c51-2003-407a-a239-689fabd19022", 
            "ese_physical_port_id": "976156ef-05b4-47f4-9497-a36531563a08", 
            "connected_resource": "common_function_gateway", 
            "type": "L2", 
            "id": "b04853c4-6ebf-441f-9093-ea4b844c4bc7", 
            "vlan_id": 1025, 
            "description": "ESE Logical port for Port 327f59b7-df38-4d8f-97db-d320defcab76"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/ese_logical_ports/b04853c4-6ebf-441f-9093-ea4b844c4bc7
{
    "stack_id": "ese_logical_port_b04853c4-6ebf-441f-9093-ea4b844c4bc7", 
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
    "id": "ese_logical_port:b04853c4-6ebf-441f-9093-ea4b844c4bc7"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/ese_logical_ports/b04853c4-6ebf-441f-9093-ea4b844c4bc7
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
/esi-worker/job_state/v2.0/ese_logical_ports/b04853c4-6ebf-441f-9093-ea4b844c4bc7
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
/state/v2.0/ese_logical_ports/b04853c4-6ebf-441f-9093-ea4b844c4bc7
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
/monitoring/v2.0/ese_logical_ports/b04853c4-6ebf-441f-9093-ea4b844c4bc7
{
    "logical_port": "UP", 
    "version": 1
}
```
