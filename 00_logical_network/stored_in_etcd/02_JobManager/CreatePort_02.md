# Stored data in etcd: Create Port

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
