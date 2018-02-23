# Stored data in etcd: Create Gw Interface

These are stored data for "heat_templates" in etcd.

* ese_logical_port
* ese_logical_port_monitoring

![scope](../../images/esi_interface.008.png)

These are stored data for "Create Gw Interface" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ese_logical_ports/ecb4c4ac-3ebc-4045-a27c-52fecc93bac5
{
    "body": {
        "status": "PENDING_CREATE", 
        "name": "xe-0/0/4.1025", 
        "tags": {}, 
        "network_id": "bb69041d-c654-4e9f-a763-afd4333275bc", 
        "gw_interface_id": "fbd7d07e-9e84-4ad7-ab85-36d46adb9435", 
        "port_ids": [
            "67d9f139-b5be-4082-a090-3a1a9cbf1df8"
        ], 
        "ese_physical_port_id": "176ec475-e9e8-4605-8b41-802fbc6220c1", 
        "connected_resource": "gw_interface", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "type": "L2", 
        "id": "ecb4c4ac-3ebc-4045-a27c-52fecc93bac5", 
        "vlan_id": 1025, 
        "description": "ESE Logical port for Port 67d9f139-b5be-4082-a090-3a1a9cbf1df8"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:ese_logical_port:ecb4c4ac-3ebc-4045-a27c-52fecc93bac5:1:vxorv
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "ecb4c4ac-3ebc-4045-a27c-52fecc93bac5", 
        "handler": "heat_worker", 
        "job_name": "ese_logical_port:ecb4c4ac-3ebc-4045-a27c-52fecc93bac5:1", 
        "dependency": [
            "create:heat_worker:port:67d9f139-b5be-4082-a090-3a1a9cbf1df8:1:qzqhf"
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
                        "resource_id": "67d9f139-b5be-4082-a090-3a1a9cbf1df8"
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
                            "resource_id": "67d9f139-b5be-4082-a090-3a1a9cbf1df8"
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
                        "resource_id": "176ec475-e9e8-4605-8b41-802fbc6220c1"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "ese_physical_port", 
                    "resource_id": "176ec475-e9e8-4605-8b41-802fbc6220c1"
                }, 
                "param": "physical_port_id"
            }
        ], 
        "resource_type": "ese_logical_port", 
        "action": "create", 
        "is_last": false, 
        "on_failure": "fail", 
        "id": "create:heat_worker:ese_logical_port:ecb4c4ac-3ebc-4045-a27c-52fecc93bac5:1:vxorv", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "xe-0/0/4.1025", 
            "tags": {}, 
            "network_id": "bb69041d-c654-4e9f-a763-afd4333275bc", 
            "gw_interface_id": "fbd7d07e-9e84-4ad7-ab85-36d46adb9435", 
            "port_ids": [
                "67d9f139-b5be-4082-a090-3a1a9cbf1df8"
            ], 
            "ese_physical_port_id": "176ec475-e9e8-4605-8b41-802fbc6220c1", 
            "connected_resource": "gw_interface", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "type": "L2", 
            "id": "ecb4c4ac-3ebc-4045-a27c-52fecc93bac5", 
            "vlan_id": 1025, 
            "description": "ESE Logical port for Port 67d9f139-b5be-4082-a090-3a1a9cbf1df8"
        }
    }, 
    0
]
```

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:ese_logical_port:ecb4c4ac-3ebc-4045-a27c-52fecc93bac5:1:1dtrn
[
    "monitoring_worker", 
    {
        "is_first": false, 
        "resource_id": "ecb4c4ac-3ebc-4045-a27c-52fecc93bac5", 
        "handler": "monitoring_worker", 
        "job_name": "ese_logical_port:ecb4c4ac-3ebc-4045-a27c-52fecc93bac5:1", 
        "dependency": [
            "create:heat_worker:ese_logical_port:ecb4c4ac-3ebc-4045-a27c-52fecc93bac5:1:vxorv"
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
                    "67d9f139-b5be-4082-a090-3a1a9cbf1df8"
                ], 
                "param": "port_ids"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_physical_port", 
                        "resource_id": "176ec475-e9e8-4605-8b41-802fbc6220c1"
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
                    "resource_id": "ecb4c4ac-3ebc-4045-a27c-52fecc93bac5"
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
                "value": "ecb4c4ac-3ebc-4045-a27c-52fecc93bac5", 
                "param": "id"
            }
        ], 
        "resource_type": "ese_logical_port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:ese_logical_port:ecb4c4ac-3ebc-4045-a27c-52fecc93bac5:1:1dtrn", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "xe-0/0/4.1025", 
            "tags": {}, 
            "network_id": "bb69041d-c654-4e9f-a763-afd4333275bc", 
            "gw_interface_id": "fbd7d07e-9e84-4ad7-ab85-36d46adb9435", 
            "port_ids": [
                "67d9f139-b5be-4082-a090-3a1a9cbf1df8"
            ], 
            "ese_physical_port_id": "176ec475-e9e8-4605-8b41-802fbc6220c1", 
            "connected_resource": "gw_interface", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "type": "L2", 
            "id": "ecb4c4ac-3ebc-4045-a27c-52fecc93bac5", 
            "vlan_id": 1025, 
            "description": "ESE Logical port for Port 67d9f139-b5be-4082-a090-3a1a9cbf1df8"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/ese_logical_ports/ecb4c4ac-3ebc-4045-a27c-52fecc93bac5
{
    "stack_id": "ese_logical_port_ecb4c4ac-3ebc-4045-a27c-52fecc93bac5", 
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
    "id": "ese_logical_port:ecb4c4ac-3ebc-4045-a27c-52fecc93bac5"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/ese_logical_ports/ecb4c4ac-3ebc-4045-a27c-52fecc93bac5
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
/esi-worker/job_state/v2.0/ese_logical_ports/ecb4c4ac-3ebc-4045-a27c-52fecc93bac5
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
/state/v2.0/ese_logical_ports/ecb4c4ac-3ebc-4045-a27c-52fecc93bac5
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
