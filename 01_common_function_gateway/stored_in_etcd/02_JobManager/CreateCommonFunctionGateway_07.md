# Stored data in etcd: Create Common Function Gateway

```
/jobs/all/create:heat_worker:ese_logical_port:e8555ee6-529c-42d9-8bb1-bfbe217133b1:1:euyfe
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "e8555ee6-529c-42d9-8bb1-bfbe217133b1", 
        "handler": "heat_worker", 
        "job_name": "ese_logical_port:e8555ee6-529c-42d9-8bb1-bfbe217133b1:1", 
        "dependency": [
            "create:heat_worker:port:343b0257-512e-40e3-b063-8cc13a4b61f4:1:tsmd8"
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
                        "resource_id": "f4c3a1bf-3b61-48ba-a548-422036849465"
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
                    "343b0257-512e-40e3-b063-8cc13a4b61f4"
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
                        "resource_id": "343b0257-512e-40e3-b063-8cc13a4b61f4"
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
                            "resource_id": "343b0257-512e-40e3-b063-8cc13a4b61f4"
                        }, 
                        "resources": []
                    }
                ], 
                "param": "virtual_machine_interface_ids"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "xe-0/0/4.1025", 
                "param": "logical_port_name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "e8555ee6-529c-42d9-8bb1-bfbe217133b1", 
                "param": "gohan_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_physical_port", 
                        "resource_id": "f4c3a1bf-3b61-48ba-a548-422036849465"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "ese_physical_port", 
                    "resource_id": "f4c3a1bf-3b61-48ba-a548-422036849465"
                }, 
                "param": "physical_port_id"
            }
        ], 
        "resource_type": "ese_logical_port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:ese_logical_port:e8555ee6-529c-42d9-8bb1-bfbe217133b1:1:euyfe", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "xe-0/0/4.1025", 
            "tags": {}, 
            "network_id": "fc8814a7-eb1e-4f59-8422-7de500e72782", 
            "tenant_id": "c583ce78843344adbe5fd20f13620274", 
            "port_ids": [
                "343b0257-512e-40e3-b063-8cc13a4b61f4"
            ], 
            "operational_state": "NO_STATE", 
            "common_function_gateway_id": "f649736d-1920-41eb-96af-d4e4fe192d0e", 
            "ese_physical_port_id": "f4c3a1bf-3b61-48ba-a548-422036849465", 
            "connected_resource": "common_function_gateway", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "type": "L2", 
            "id": "e8555ee6-529c-42d9-8bb1-bfbe217133b1", 
            "vlan_id": 1025, 
            "description": "ESE Logical port for Port 343b0257-512e-40e3-b063-8cc13a4b61f4"
        }
    }, 
    0
]
```
