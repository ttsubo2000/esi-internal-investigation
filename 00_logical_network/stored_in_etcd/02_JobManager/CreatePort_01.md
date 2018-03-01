# Stored data in etcd: Create Port

```
/jobs/all/create:heat_worker:port:fde61b02-9615-4e75-aac0-30a333657c1b:1:s23ew
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "fde61b02-9615-4e75-aac0-30a333657c1b", 
        "handler": "heat_worker", 
        "job_name": "port:fde61b02-9615-4e75-aac0-30a333657c1b:1", 
        "dependency": [], 
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
                        "resource_id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263"
                }, 
                "param": "virtual_network"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "7ff183de-0188-46bf-b7d0-68d08ad2b54f", 
                "param": "virtual_machine"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "fde61b02-9615-4e75-aac0-30a333657c1b", 
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
                "value": "ae69b52f46ba480bb9636f62736436f4", 
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
                "value": "fa:16:3e:67:26:46", 
                "param": "virtual_machine_interface_mac_address"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "physical_port", 
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
                        "subnet_id": "3cfa93ac-251a-4a60-9434-ff4c88bf3655", 
                        "ip_address": "192.168.200.101"
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
                "value": "physical_port", 
                "param": "jinja_device_owner"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "subnet", 
                        "resource_id": "3cfa93ac-251a-4a60-9434-ff4c88bf3655"
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
                            "resource_id": "3cfa93ac-251a-4a60-9434-ff4c88bf3655"
                        }, 
                        "resources": []
                    }
                ], 
                "param": "jinja_subnets"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "fde61b02-9615-4e75-aac0-30a333657c1b", 
                "param": "uuid"
            }
        ], 
        "resource_type": "port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:port:fde61b02-9615-4e75-aac0-30a333657c1b:1:s23ew", 
        "resource_input": {
            "allowed_address_pairs": [], 
            "device_owner": "physical_port", 
            "fake_delete": false, 
            "fixed_ips": [
                {
                    "subnet_id": "3cfa93ac-251a-4a60-9434-ff4c88bf3655", 
                    "ip_address": "192.168.200.101"
                }
            ], 
            "id": "fde61b02-9615-4e75-aac0-30a333657c1b", 
            "security_groups": [], 
            "binding:vif_type": "vrouter", 
            "mac_address": "fa:16:3e:67:26:46", 
            "status": "PENDING_CREATE", 
            "description": "", 
            "tags": {}, 
            "segmentation_id": 1003, 
            "device_id": "7ff183de-0188-46bf-b7d0-68d08ad2b54f", 
            "name": "sample-port", 
            "managed_by_service": false, 
            "network_id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
            "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
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
