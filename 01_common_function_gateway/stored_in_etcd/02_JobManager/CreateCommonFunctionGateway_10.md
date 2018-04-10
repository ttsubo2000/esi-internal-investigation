# Stored data in etcd: Create Common Function Gateway

```
/jobs/all/modify:heat_worker:port:343b0257-512e-40e3-b063-8cc13a4b61f4:2:biikl
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "343b0257-512e-40e3-b063-8cc13a4b61f4", 
        "handler": "heat_worker", 
        "job_name": "port:343b0257-512e-40e3-b063-8cc13a4b61f4:2", 
        "dependency": [
            "create:heat_worker:common_function_gateway:f649736d-1920-41eb-96af-d4e4fe192d0e:1:2n65z"
        ], 
        "version": 2, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": true, 
                "param": "jinja_attached"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "network", 
                        "resource_id": "fc8814a7-eb1e-4f59-8422-7de500e72782"
                    }, 
                    {
                        "resource_type": "network", 
                        "resource_id": "fc8814a7-eb1e-4f59-8422-7de500e72782"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "fc8814a7-eb1e-4f59-8422-7de500e72782"
                }, 
                "param": "virtual_network"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "f649736d-1920-41eb-96af-d4e4fe192d0e", 
                "param": "virtual_machine"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "343b0257-512e-40e3-b063-8cc13a4b61f4", 
                "param": "name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": true, 
                "param": "admin_state_up"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "c583ce78843344adbe5fd20f13620274", 
                "param": "tenant_id"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "13", 
                "param": "heat_timeout"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [], 
                "param": "virtual_machine_interface_allowed_address_pairs"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "fa:16:3e:38:35:6a", 
                "param": "virtual_machine_interface_mac_address"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "network:common_function_gateway", 
                "param": "device_owner"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": 2, 
                "param": "version"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [], 
                "param": "security_groups"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": null, 
                "param": "jinja_force_dependency_gw_interface"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [
                    {
                        "subnet_id": "cf9356ae-b4e1-4a91-8193-089fdc12173d", 
                        "ip_address": "169.254.0.4"
                    }
                ], 
                "param": "jinja_fixed_ips"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "common_function_gateway", 
                        "resource_id": "f649736d-1920-41eb-96af-d4e4fe192d0e"
                    }, 
                    {
                        "resource_type": "common_function_gateway", 
                        "resource_id": "f649736d-1920-41eb-96af-d4e4fe192d0e"
                    }
                ], 
                "type": "value", 
                "value": "f649736d-1920-41eb-96af-d4e4fe192d0e", 
                "param": "jinja_force_dependency_cfg"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "network:common_function_gateway", 
                "param": "jinja_device_owner"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "subnet", 
                        "resource_id": "cf9356ae-b4e1-4a91-8193-089fdc12173d"
                    }, 
                    {
                        "resource_type": "subnet", 
                        "resource_id": "cf9356ae-b4e1-4a91-8193-089fdc12173d"
                    }
                ], 
                "type": "list", 
                "value": [
                    {
                        "param": "jinja_subnets", 
                        "type": "output_key", 
                        "value": {
                            "output_key": "id", 
                            "resource_type": "subnet", 
                            "resource_id": "cf9356ae-b4e1-4a91-8193-089fdc12173d"
                        }, 
                        "resources": []
                    }
                ], 
                "param": "jinja_subnets"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "343b0257-512e-40e3-b063-8cc13a4b61f4", 
                "param": "uuid"
            }
        ], 
        "resource_type": "port", 
        "action": "modify", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "modify:heat_worker:port:343b0257-512e-40e3-b063-8cc13a4b61f4:2:biikl", 
        "resource_input": {
            "ese_logical_port_id": "e8555ee6-529c-42d9-8bb1-bfbe217133b1", 
            "allowed_address_pairs": [], 
            "device_owner": "network:common_function_gateway", 
            "fake_delete": false, 
            "fixed_ips": [
                {
                    "subnet_id": "cf9356ae-b4e1-4a91-8193-089fdc12173d", 
                    "ip_address": "169.254.0.4"
                }
            ], 
            "id": "343b0257-512e-40e3-b063-8cc13a4b61f4", 
            "security_groups": [], 
            "binding:vif_type": "vrouter", 
            "mac_address": "fa:16:3e:38:35:6a", 
            "status": "PENDING_CREATE", 
            "description": "", 
            "tags": {}, 
            "segmentation_id": 1025, 
            "device_id": "f649736d-1920-41eb-96af-d4e4fe192d0e", 
            "name": "common_function_gw_f649736d-1920-41eb-96af-d4e4fe192d0e_secondary_port:f4c3a1bf-3b61-48ba-a548-422036849465", 
            "managed_by_service": true, 
            "network_id": "fc8814a7-eb1e-4f59-8422-7de500e72782", 
            "tenant_id": "c583ce78843344adbe5fd20f13620274", 
            "admin_state_up": true, 
            "attached": true, 
            "operational_state": "NO_STATE", 
            "orchestration_state": "UPDATE_IN_PROGRESS", 
            "segmentation_type": "vlan"
        }
    }, 
    0
]
```
