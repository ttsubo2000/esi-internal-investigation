# Stored data in etcd: Create Gw Interface

```
/jobs/all/create:heat_worker:ese_logical_port:e30fdd19-2f48-422e-9c68-7c59a0e2fae8:1:s3oth
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "e30fdd19-2f48-422e-9c68-7c59a0e2fae8", 
        "handler": "heat_worker", 
        "job_name": "ese_logical_port:e30fdd19-2f48-422e-9c68-7c59a0e2fae8:1", 
        "dependency": [
            "create:heat_worker:port:5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b:1:79pnn"
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
                "value": 1025, 
                "param": "logical_port_vlan_id"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
                "param": "tenant_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_physical_port", 
                        "resource_id": "0078808a-c28e-46e1-887d-8ec65f90c446"
                    }, 
                    {
                        "resource_type": "ese_device", 
                        "resource_id": "4d8371c0-1b91-4818-a6e7-26425178e5d4"
                    }
                ], 
                "type": "value", 
                "value": "10.161.0.34", 
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
                    "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b"
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
                        "resource_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b"
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
                            "resource_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b"
                        }, 
                        "resources": []
                    }
                ], 
                "param": "virtual_machine_interface_ids"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "xe-0/0/3.1025", 
                "param": "logical_port_name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "e30fdd19-2f48-422e-9c68-7c59a0e2fae8", 
                "param": "gohan_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_physical_port", 
                        "resource_id": "0078808a-c28e-46e1-887d-8ec65f90c446"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "ese_physical_port", 
                    "resource_id": "0078808a-c28e-46e1-887d-8ec65f90c446"
                }, 
                "param": "physical_port_id"
            }
        ], 
        "resource_type": "ese_logical_port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:ese_logical_port:e30fdd19-2f48-422e-9c68-7c59a0e2fae8:1:s3oth", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "xe-0/0/3.1025", 
            "tags": {}, 
            "network_id": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2", 
            "gw_interface_id": "3dbcfce5-bca5-4182-991a-c23de685fcf1", 
            "port_ids": [
                "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b"
            ], 
            "operational_state": "NO_STATE", 
            "vlan_id": 1025, 
            "ese_physical_port_id": "0078808a-c28e-46e1-887d-8ec65f90c446", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
            "type": "L2", 
            "id": "e30fdd19-2f48-422e-9c68-7c59a0e2fae8", 
            "connected_resource": "gw_interface", 
            "description": "ESE Logical port for Port 5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b"
        }
    }, 
    0
]
```
