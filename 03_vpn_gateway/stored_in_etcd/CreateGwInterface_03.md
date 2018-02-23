# Stored data in etcd: Create Gw Interface

These are stored data for "heat_templates" in etcd.

* ese_logical_port
* ese_logical_port_monitoring

![scope](../../images/esi_interface.008.png)

These are stored data for "Create Gw Interface" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ese_logical_ports/ef450536-01c9-4380-a34d-a1ae56e0447e
{
    "body": {
        "status": "PENDING_CREATE", 
        "name": "xe-0/0/3.1025", 
        "tags": {}, 
        "network_id": "bb69041d-c654-4e9f-a763-afd4333275bc", 
        "gw_interface_id": "fbd7d07e-9e84-4ad7-ab85-36d46adb9435", 
        "port_ids": [
            "33907bcb-8689-425d-a700-fe8acfd94aed"
        ], 
        "ese_physical_port_id": "eec156b0-7317-48dd-b76c-019c0758e99d", 
        "connected_resource": "gw_interface", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "type": "L2", 
        "id": "ef450536-01c9-4380-a34d-a1ae56e0447e", 
        "vlan_id": 1025, 
        "description": "ESE Logical port for Port 33907bcb-8689-425d-a700-fe8acfd94aed"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:ese_logical_port:ef450536-01c9-4380-a34d-a1ae56e0447e:1:c21em
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "ef450536-01c9-4380-a34d-a1ae56e0447e", 
        "handler": "heat_worker", 
        "job_name": "ese_logical_port:ef450536-01c9-4380-a34d-a1ae56e0447e:1", 
        "dependency": [
            "create:heat_worker:port:33907bcb-8689-425d-a700-fe8acfd94aed:1:6n77u"
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
                        "resource_id": "33907bcb-8689-425d-a700-fe8acfd94aed"
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
                            "resource_id": "33907bcb-8689-425d-a700-fe8acfd94aed"
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
                        "resource_id": "eec156b0-7317-48dd-b76c-019c0758e99d"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "ese_physical_port", 
                    "resource_id": "eec156b0-7317-48dd-b76c-019c0758e99d"
                }, 
                "param": "physical_port_id"
            }
        ], 
        "resource_type": "ese_logical_port", 
        "action": "create", 
        "is_last": false, 
        "on_failure": "fail", 
        "id": "create:heat_worker:ese_logical_port:ef450536-01c9-4380-a34d-a1ae56e0447e:1:c21em", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "xe-0/0/3.1025", 
            "tags": {}, 
            "network_id": "bb69041d-c654-4e9f-a763-afd4333275bc", 
            "gw_interface_id": "fbd7d07e-9e84-4ad7-ab85-36d46adb9435", 
            "port_ids": [
                "33907bcb-8689-425d-a700-fe8acfd94aed"
            ], 
            "ese_physical_port_id": "eec156b0-7317-48dd-b76c-019c0758e99d", 
            "connected_resource": "gw_interface", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "type": "L2", 
            "id": "ef450536-01c9-4380-a34d-a1ae56e0447e", 
            "vlan_id": 1025, 
            "description": "ESE Logical port for Port 33907bcb-8689-425d-a700-fe8acfd94aed"
        }
    }, 
    0
]
```

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:ese_logical_port:ef450536-01c9-4380-a34d-a1ae56e0447e:1:tv0o3
[
    "monitoring_worker", 
    {
        "is_first": false, 
        "resource_id": "ef450536-01c9-4380-a34d-a1ae56e0447e", 
        "handler": "monitoring_worker", 
        "job_name": "ese_logical_port:ef450536-01c9-4380-a34d-a1ae56e0447e:1", 
        "dependency": [
            "create:heat_worker:ese_logical_port:ef450536-01c9-4380-a34d-a1ae56e0447e:1:c21em"
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
                    "33907bcb-8689-425d-a700-fe8acfd94aed"
                ], 
                "param": "port_ids"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_physical_port", 
                        "resource_id": "eec156b0-7317-48dd-b76c-019c0758e99d"
                    }, 
                    {
                        "resource_type": "ese_device", 
                        "resource_id": "5314fffc-6c86-4410-a64b-5386286ac629"
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
                    "resource_id": "ef450536-01c9-4380-a34d-a1ae56e0447e"
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
                "value": "ef450536-01c9-4380-a34d-a1ae56e0447e", 
                "param": "id"
            }
        ], 
        "resource_type": "ese_logical_port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:ese_logical_port:ef450536-01c9-4380-a34d-a1ae56e0447e:1:tv0o3", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "xe-0/0/3.1025", 
            "tags": {}, 
            "network_id": "bb69041d-c654-4e9f-a763-afd4333275bc", 
            "gw_interface_id": "fbd7d07e-9e84-4ad7-ab85-36d46adb9435", 
            "port_ids": [
                "33907bcb-8689-425d-a700-fe8acfd94aed"
            ], 
            "ese_physical_port_id": "eec156b0-7317-48dd-b76c-019c0758e99d", 
            "connected_resource": "gw_interface", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "type": "L2", 
            "id": "ef450536-01c9-4380-a34d-a1ae56e0447e", 
            "vlan_id": 1025, 
            "description": "ESE Logical port for Port 33907bcb-8689-425d-a700-fe8acfd94aed"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/ese_logical_ports/ef450536-01c9-4380-a34d-a1ae56e0447e
{
    "stack_id": "ese_logical_port_ef450536-01c9-4380-a34d-a1ae56e0447e", 
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
    "id": "ese_logical_port:ef450536-01c9-4380-a34d-a1ae56e0447e"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/ese_logical_ports/ef450536-01c9-4380-a34d-a1ae56e0447e
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
/esi-worker/job_state/v2.0/ese_logical_ports/ebee8782-4803-4dd6-a4bd-82e27758707d
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
/state/v2.0/ese_logical_ports/ef450536-01c9-4380-a34d-a1ae56e0447e
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
