# Stored data in etcd: Create Common Function Gateway

```
/jobs/all/create:heat_worker:ese_logical_port:be66c7e0-b222-4e76-bf81-af75e8cf1824:1:2u7dw
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "be66c7e0-b222-4e76-bf81-af75e8cf1824", 
        "handler": "heat_worker", 
        "job_name": "ese_logical_port:be66c7e0-b222-4e76-bf81-af75e8cf1824:1", 
        "dependency": [
            "create:heat_worker:port:f84496b5-dc56-4727-87b1-aa06e2471737:1:3xe01"
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
                "value": "c583ce78843344adbe5fd20f13620274", 
                "param": "tenant_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_physical_port", 
                        "resource_id": "9451c9ca-289d-42ba-846d-359c448e910c"
                    }, 
                    {
                        "resource_type": "ese_device", 
                        "resource_id": "cc214b6a-2f09-4094-b7cd-a9590f64b854"
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
                    "f84496b5-dc56-4727-87b1-aa06e2471737"
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
                        "resource_id": "f84496b5-dc56-4727-87b1-aa06e2471737"
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
                            "resource_id": "f84496b5-dc56-4727-87b1-aa06e2471737"
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
                "value": "be66c7e0-b222-4e76-bf81-af75e8cf1824", 
                "param": "gohan_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_physical_port", 
                        "resource_id": "9451c9ca-289d-42ba-846d-359c448e910c"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "ese_physical_port", 
                    "resource_id": "9451c9ca-289d-42ba-846d-359c448e910c"
                }, 
                "param": "physical_port_id"
            }
        ], 
        "resource_type": "ese_logical_port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:ese_logical_port:be66c7e0-b222-4e76-bf81-af75e8cf1824:1:2u7dw", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "xe-0/0/3.1025", 
            "tags": {}, 
            "network_id": "fc8814a7-eb1e-4f59-8422-7de500e72782", 
            "tenant_id": "c583ce78843344adbe5fd20f13620274", 
            "port_ids": [
                "f84496b5-dc56-4727-87b1-aa06e2471737"
            ], 
            "operational_state": "NO_STATE", 
            "common_function_gateway_id": "f649736d-1920-41eb-96af-d4e4fe192d0e", 
            "ese_physical_port_id": "9451c9ca-289d-42ba-846d-359c448e910c", 
            "connected_resource": "common_function_gateway", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "type": "L2", 
            "id": "be66c7e0-b222-4e76-bf81-af75e8cf1824", 
            "vlan_id": 1025, 
            "description": "ESE Logical port for Port f84496b5-dc56-4727-87b1-aa06e2471737"
        }
    }, 
    0
]
```
