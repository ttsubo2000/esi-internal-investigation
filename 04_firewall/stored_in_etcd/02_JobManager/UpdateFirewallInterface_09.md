# Stored data in etcd: Update Firewall Interface

```
/jobs/all/modify:heat_worker:port:472879c4-4611-4762-a069-293e0081bcbf:3:tx85c
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "472879c4-4611-4762-a069-293e0081bcbf", 
        "handler": "heat_worker", 
        "job_name": "port:472879c4-4611-4762-a069-293e0081bcbf:3", 
        "dependency": [], 
        "version": 3, 
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
                        "resource_id": "82712b89-c35c-4276-83cb-818860d41f9e"
                    }, 
                    {
                        "resource_type": "network", 
                        "resource_id": "82712b89-c35c-4276-83cb-818860d41f9e"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "82712b89-c35c-4276-83cb-818860d41f9e"
                }, 
                "param": "virtual_network"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "2e555b09-e0d7-4cce-8854-c481a2363917", 
                "param": "virtual_machine"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "472879c4-4611-4762-a069-293e0081bcbf", 
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
                "value": "0f40dffa48614d9baa7eaac7e7532099", 
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
                "value": "fa:16:3e:f0:f2:72", 
                "param": "virtual_machine_interface_mac_address"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "compute:nova", 
                "param": "device_owner"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": 3, 
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
                        "subnet_id": "a11785e2-0c2b-4131-9144-349155f958f5", 
                        "ip_address": "10.98.76.3"
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
                "value": "compute:nova", 
                "param": "jinja_device_owner"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "subnet", 
                        "resource_id": "a11785e2-0c2b-4131-9144-349155f958f5"
                    }, 
                    {
                        "resource_type": "subnet", 
                        "resource_id": "a11785e2-0c2b-4131-9144-349155f958f5"
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
                            "resource_id": "a11785e2-0c2b-4131-9144-349155f958f5"
                        }, 
                        "resources": []
                    }
                ], 
                "param": "jinja_subnets"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "472879c4-4611-4762-a069-293e0081bcbf", 
                "param": "uuid"
            }
        ], 
        "resource_type": "port", 
        "action": "modify", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "modify:heat_worker:port:472879c4-4611-4762-a069-293e0081bcbf:3:tx85c", 
        "resource_input": {
            "ese_logical_port_id": null, 
            "allowed_address_pairs": [], 
            "device_owner": "compute:nova", 
            "fake_delete": true, 
            "fixed_ips": [
                {
                    "subnet_id": "a11785e2-0c2b-4131-9144-349155f958f5", 
                    "ip_address": "10.98.76.3"
                }
            ], 
            "id": "472879c4-4611-4762-a069-293e0081bcbf", 
            "security_groups": [], 
            "binding:vif_type": "vrouter", 
            "mac_address": "fa:16:3e:f0:f2:72", 
            "status": "PENDING_UPDATE", 
            "description": "", 
            "tags": {}, 
            "segmentation_id": 0, 
            "device_id": "2e555b09-e0d7-4cce-8854-c481a2363917", 
            "name": "firewall-user-port", 
            "managed_by_service": false, 
            "network_id": "82712b89-c35c-4276-83cb-818860d41f9e", 
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
            "admin_state_up": true, 
            "attached": true, 
            "operational_state": "NO_STATE", 
            "orchestration_state": "UPDATE_IN_PROGRESS", 
            "segmentation_type": "flat"
        }
    }, 
    0
]
```
