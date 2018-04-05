# Stored data in etcd: Create Gw Interface

```
/jobs/all/modify:heat_worker:port:f3867a99-de18-4512-8e94-f9aaa7b05c3a:2:37sxp
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a", 
        "handler": "heat_worker", 
        "job_name": "port:f3867a99-de18-4512-8e94-f9aaa7b05c3a:2", 
        "dependency": [], 
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
                        "resource_id": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e"
                    }, 
                    {
                        "resource_type": "network", 
                        "resource_id": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e"
                }, 
                "param": "virtual_network"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "ce8831fd-d30c-41e3-95de-feaee0b95405", 
                "param": "virtual_machine"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "f3867a99-de18-4512-8e94-f9aaa7b05c3a", 
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
                "value": "06d6b792b31c40daa546fb0f4e35980d", 
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
                "value": "fa:16:3e:c5:2b:92", 
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
                "resources": [
                    {
                        "resource_type": "gw_interface", 
                        "resource_id": "ce8831fd-d30c-41e3-95de-feaee0b95405"
                    }, 
                    {
                        "resource_type": "gw_interface", 
                        "resource_id": "ce8831fd-d30c-41e3-95de-feaee0b95405"
                    }
                ], 
                "type": "value", 
                "value": "ce8831fd-d30c-41e3-95de-feaee0b95405", 
                "param": "jinja_force_dependency_gw_interface"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [
                    {
                        "subnet_id": "67877f2d-0547-4cea-a6ce-2e3b937aa31b", 
                        "ip_address": "172.16.101.151"
                    }, 
                    {
                        "subnet_id": "67877f2d-0547-4cea-a6ce-2e3b937aa31b", 
                        "ip_address": "172.16.101.152"
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
                        "resource_id": "67877f2d-0547-4cea-a6ce-2e3b937aa31b"
                    }, 
                    {
                        "resource_type": "subnet", 
                        "resource_id": "67877f2d-0547-4cea-a6ce-2e3b937aa31b"
                    }, 
                    {
                        "resource_type": "subnet", 
                        "resource_id": "67877f2d-0547-4cea-a6ce-2e3b937aa31b"
                    }, 
                    {
                        "resource_type": "subnet", 
                        "resource_id": "67877f2d-0547-4cea-a6ce-2e3b937aa31b"
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
                            "resource_id": "67877f2d-0547-4cea-a6ce-2e3b937aa31b"
                        }, 
                        "resources": []
                    }, 
                    {
                        "param": "jinja_subnets", 
                        "type": "output_key", 
                        "value": {
                            "output_key": "id", 
                            "resource_type": "subnet", 
                            "resource_id": "67877f2d-0547-4cea-a6ce-2e3b937aa31b"
                        }, 
                        "resources": []
                    }
                ], 
                "param": "jinja_subnets"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "f3867a99-de18-4512-8e94-f9aaa7b05c3a", 
                "param": "uuid"
            }
        ], 
        "resource_type": "port", 
        "action": "modify", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "modify:heat_worker:port:f3867a99-de18-4512-8e94-f9aaa7b05c3a:2:37sxp", 
        "resource_input": {
            "ese_logical_port_id": "02112bb1-389c-4ff8-9354-94ab43459892", 
            "allowed_address_pairs": [], 
            "device_owner": "network:gw_interface", 
            "fake_delete": false, 
            "fixed_ips": [
                {
                    "subnet_id": "67877f2d-0547-4cea-a6ce-2e3b937aa31b", 
                    "ip_address": "172.16.101.151"
                }, 
                {
                    "subnet_id": "67877f2d-0547-4cea-a6ce-2e3b937aa31b", 
                    "ip_address": "172.16.101.152"
                }
            ], 
            "id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a", 
            "security_groups": [], 
            "binding:vif_type": "vrouter", 
            "mac_address": "fa:16:3e:c5:2b:92", 
            "status": "PENDING_CREATE", 
            "description": "", 
            "tags": {}, 
            "segmentation_id": 1025, 
            "device_id": "ce8831fd-d30c-41e3-95de-feaee0b95405", 
            "name": "Port for : 887fecdd-956b-47fa-a348-8940c53a5bf9", 
            "managed_by_service": true, 
            "network_id": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e", 
            "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
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
