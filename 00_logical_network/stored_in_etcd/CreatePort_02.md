# Stored data in etcd: Create Port

These are stored data for "heat_templates" in etcd.

* ese_logical_port

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ese_logical_ports/ced1435d-6dfa-4dab-bb7c-19da4d8e48b7
{
    "body": {
        "status": "PENDING_CREATE", 
        "name": "xe-0/0/1.1003", 
        "tags": {}, 
        "network_id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
        "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
        "port_ids": [
            "fde61b02-9615-4e75-aac0-30a333657c1b"
        ], 
        "operational_state": "NO_STATE", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "ese_physical_port_id": "24dd42cf-b343-47a9-966a-8f7486378c46", 
        "connected_resource": "port", 
        "type": "L2", 
        "id": "ced1435d-6dfa-4dab-bb7c-19da4d8e48b7", 
        "vlan_id": 1003, 
        "description": "ESE Logical port for Port fde61b02-9615-4e75-aac0-30a333657c1b"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/create:heat_worker:ese_logical_port:ced1435d-6dfa-4dab-bb7c-19da4d8e48b7:1:vcoy8
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "ced1435d-6dfa-4dab-bb7c-19da4d8e48b7", 
        "handler": "heat_worker", 
        "job_name": "ese_logical_port:ced1435d-6dfa-4dab-bb7c-19da4d8e48b7:1", 
        "dependency": [
            "create:heat_worker:port:fde61b02-9615-4e75-aac0-30a333657c1b:1:s23ew"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "L2", 
                "param": "logical_port_type"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": 1003, 
                "param": "logical_port_vlan_id"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "ae69b52f46ba480bb9636f62736436f4", 
                "param": "tenant_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_physical_port", 
                        "resource_id": "24dd42cf-b343-47a9-966a-8f7486378c46"
                    }, 
                    {
                        "resource_type": "ese_device", 
                        "resource_id": "718148aa-4483-47d5-bbd1-a0e0738dc018"
                    }
                ], 
                "type": "value", 
                "value": "10.161.0.33", 
                "param": "device_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "6", 
                "param": "heat_timeout"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [
                    "fde61b02-9615-4e75-aac0-30a333657c1b"
                ], 
                "param": "jinja_port_ids"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": 1, 
                "param": "version"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "port", 
                        "resource_id": "fde61b02-9615-4e75-aac0-30a333657c1b"
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
                            "resource_id": "fde61b02-9615-4e75-aac0-30a333657c1b"
                        }, 
                        "resources": []
                    }
                ], 
                "param": "virtual_machine_interface_ids"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "xe-0/0/1.1003", 
                "param": "logical_port_name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "ced1435d-6dfa-4dab-bb7c-19da4d8e48b7", 
                "param": "gohan_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_physical_port", 
                        "resource_id": "24dd42cf-b343-47a9-966a-8f7486378c46"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "ese_physical_port", 
                    "resource_id": "24dd42cf-b343-47a9-966a-8f7486378c46"
                }, 
                "param": "physical_port_id"
            }
        ], 
        "resource_type": "ese_logical_port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:ese_logical_port:ced1435d-6dfa-4dab-bb7c-19da4d8e48b7:1:vcoy8", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "xe-0/0/1.1003", 
            "tags": {}, 
            "network_id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
            "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
            "port_ids": [
                "fde61b02-9615-4e75-aac0-30a333657c1b"
            ], 
            "operational_state": "NO_STATE", 
            "vlan_id": 1003, 
            "ese_physical_port_id": "24dd42cf-b343-47a9-966a-8f7486378c46", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "type": "L2", 
            "id": "ced1435d-6dfa-4dab-bb7c-19da4d8e48b7", 
            "connected_resource": "port", 
            "description": "ESE Logical port for Port fde61b02-9615-4e75-aac0-30a333657c1b"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/ese_logical_ports/ced1435d-6dfa-4dab-bb7c-19da4d8e48b7
{
    "stack_id": "ese_logical_port_ced1435d-6dfa-4dab-bb7c-19da4d8e48b7", 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "9dcbbbbc-e9ea-4276-ba65-68ce8737e568", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "46b0cd68-d0fb-4d72-9def-830164f9e215", 
            "description": "A unique id for the logical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/9dcbbbbc-e9ea-4276-ba65-68ce8737e568", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }, 
        {
            "output_value": "xe-0/0/38.0", 
            "description": "The name of the logical interface.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "ese_logical_port:ced1435d-6dfa-4dab-bb7c-19da4d8e48b7"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/ese_logical_ports/ced1435d-6dfa-4dab-bb7c-19da4d8e48b7
{
    "heat_outputs": [
        {
            "output_value": "9dcbbbbc-e9ea-4276-ba65-68ce8737e568", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "46b0cd68-d0fb-4d72-9def-830164f9e215", 
            "description": "A unique id for the logical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/9dcbbbbc-e9ea-4276-ba65-68ce8737e568", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }, 
        {
            "output_value": "xe-0/0/38.0", 
            "description": "The name of the logical interface.", 
            "output_key": "name"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/ese_logical_ports/ced1435d-6dfa-4dab-bb7c-19da4d8e48b7
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"9dcbbbbc-e9ea-4276-ba65-68ce8737e568\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"46b0cd68-d0fb-4d72-9def-830164f9e215\", \"description\": \"A unique id for the logical interface\", \"output_key\": \"id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/9dcbbbbc-e9ea-4276-ba65-68ce8737e568\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}, {\"output_value\": \"xe-0/0/38.0\", \"description\": \"The name of the logical interface.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```

### Checking stored data at the point of (6) in etcd

```
/monitoring/v2.0/ese_logical_ports/ced1435d-6dfa-4dab-bb7c-19da4d8e48b7
{
    "logical_port": "UP", 
    "version": 1
}
```
