# Stored data in etcd: Create Common Function Gateway

```
/jobs/all/create:heat_worker:port:f84496b5-dc56-4727-87b1-aa06e2471737:1:3xe01
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "f84496b5-dc56-4727-87b1-aa06e2471737", 
        "handler": "heat_worker", 
        "job_name": "port:f84496b5-dc56-4727-87b1-aa06e2471737:1", 
        "dependency": [
            "create:heat_worker:network:fc8814a7-eb1e-4f59-8422-7de500e72782:1:oodvi", 
            "create:heat_worker:subnet:cf9356ae-b4e1-4a91-8193-089fdc12173d:1:7kdu4"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": false, 
                "param": "jinja_attached"
            }, 
            {
                "resources": [
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
                "value": "f84496b5-dc56-4727-87b1-aa06e2471737", 
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
                "value": "fa:16:3e:82:e7:8b", 
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
                "value": 1, 
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
                        "ip_address": "169.254.0.3"
                    }
                ], 
                "param": "jinja_fixed_ips"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "", 
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
                "value": "f84496b5-dc56-4727-87b1-aa06e2471737", 
                "param": "uuid"
            }
        ], 
        "resource_type": "port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:port:f84496b5-dc56-4727-87b1-aa06e2471737:1:3xe01", 
        "resource_input": {
            "allowed_address_pairs": [], 
            "device_owner": "network:common_function_gateway", 
            "fake_delete": false, 
            "fixed_ips": [
                {
                    "subnet_id": "cf9356ae-b4e1-4a91-8193-089fdc12173d", 
                    "ip_address": "169.254.0.3"
                }
            ], 
            "id": "f84496b5-dc56-4727-87b1-aa06e2471737", 
            "security_groups": [], 
            "binding:vif_type": "vrouter", 
            "mac_address": "fa:16:3e:82:e7:8b", 
            "status": "PENDING_CREATE", 
            "description": "", 
            "tags": {}, 
            "segmentation_id": 1025, 
            "device_id": "f649736d-1920-41eb-96af-d4e4fe192d0e", 
            "name": "common_function_gw_f649736d-1920-41eb-96af-d4e4fe192d0e_primary_port:9451c9ca-289d-42ba-846d-359c448e910c", 
            "managed_by_service": true, 
            "network_id": "fc8814a7-eb1e-4f59-8422-7de500e72782", 
            "tenant_id": "c583ce78843344adbe5fd20f13620274", 
            "admin_state_up": true, 
            "attached": false, 
            "operational_state": "NO_STATE", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "segmentation_type": "vlan"
        }
    }, 
    0
]
```
