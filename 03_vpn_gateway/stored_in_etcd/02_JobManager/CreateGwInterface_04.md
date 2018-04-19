# Stored data in etcd: Create Gw Interface

```
/jobs/all/create:heat_worker:port:53eeb091-3297-4b9b-a200-b6568567e387:1:o685k
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "53eeb091-3297-4b9b-a200-b6568567e387", 
        "handler": "heat_worker", 
        "job_name": "port:53eeb091-3297-4b9b-a200-b6568567e387:1", 
        "dependency": [
            "create:heat_worker:gw_interface:3dbcfce5-bca5-4182-991a-c23de685fcf1:1:2qwyd"
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
                        "resource_id": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2"
                }, 
                "param": "virtual_network"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "3dbcfce5-bca5-4182-991a-c23de685fcf1", 
                "param": "virtual_machine"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "53eeb091-3297-4b9b-a200-b6568567e387", 
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
                "value": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
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
                "value": "fa:16:3e:7b:6f:90", 
                "param": "virtual_machine_interface_mac_address"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "network:gw_interface", 
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
                "resources": [
                    {
                        "resource_type": "gw_interface", 
                        "resource_id": "3dbcfce5-bca5-4182-991a-c23de685fcf1"
                    }
                ], 
                "type": "value", 
                "value": "3dbcfce5-bca5-4182-991a-c23de685fcf1", 
                "param": "jinja_force_dependency_gw_interface"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [
                    {
                        "subnet_id": "e825f4e4-ba44-4d9e-9578-a31ad45bedda", 
                        "ip_address": "172.16.101.153"
                    }
                ], 
                "param": "jinja_fixed_ips"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": null, 
                "param": "jinja_force_dependency_cfg"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "network:gw_interface", 
                "param": "jinja_device_owner"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "subnet", 
                        "resource_id": "e825f4e4-ba44-4d9e-9578-a31ad45bedda"
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
                            "resource_id": "e825f4e4-ba44-4d9e-9578-a31ad45bedda"
                        }, 
                        "resources": []
                    }
                ], 
                "param": "jinja_subnets"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "53eeb091-3297-4b9b-a200-b6568567e387", 
                "param": "uuid"
            }
        ], 
        "resource_type": "port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:port:53eeb091-3297-4b9b-a200-b6568567e387:1:o685k", 
        "resource_input": {
            "allowed_address_pairs": [], 
            "device_owner": "network:gw_interface", 
            "fake_delete": false, 
            "fixed_ips": [
                {
                    "subnet_id": "e825f4e4-ba44-4d9e-9578-a31ad45bedda", 
                    "ip_address": "172.16.101.153"
                }
            ], 
            "id": "53eeb091-3297-4b9b-a200-b6568567e387", 
            "security_groups": [], 
            "binding:vif_type": "vrouter", 
            "mac_address": "fa:16:3e:7b:6f:90", 
            "status": "PENDING_CREATE", 
            "description": "", 
            "tags": {}, 
            "segmentation_id": 1025, 
            "device_id": "3dbcfce5-bca5-4182-991a-c23de685fcf1", 
            "name": "Port for : a6e70af1-386b-4d79-943f-6f44e87f95b3", 
            "managed_by_service": true, 
            "network_id": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2", 
            "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
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
