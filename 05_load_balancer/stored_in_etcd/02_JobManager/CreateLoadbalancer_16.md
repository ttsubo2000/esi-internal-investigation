# Stored data in etcd: Create Loadbalancer

```
/jobs/all/modify:heat_worker:port:db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc:2:m0jnd
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc", 
        "handler": "heat_worker", 
        "job_name": "port:db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc:2", 
        "dependency": [], 
        "version": 2, 
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
                        "resource_id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f"
                    }, 
                    {
                        "resource_type": "network", 
                        "resource_id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f"
                }, 
                "param": "virtual_network"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "47531b14-72e9-439d-8949-fd941457ecde", 
                "param": "virtual_machine"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc", 
                "param": "name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": false, 
                "param": "admin_state_up"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
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
                "value": "fa:16:3e:90:8a:94", 
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
                        "subnet_id": "6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a", 
                        "ip_address": "10.121.232.3"
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
                        "resource_id": "6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a"
                    }, 
                    {
                        "resource_type": "subnet", 
                        "resource_id": "6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a"
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
                            "resource_id": "6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a"
                        }, 
                        "resources": []
                    }
                ], 
                "param": "jinja_subnets"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc", 
                "param": "uuid"
            }
        ], 
        "resource_type": "port", 
        "action": "modify", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "modify:heat_worker:port:db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc:2:m0jnd", 
        "resource_input": {
            "ese_logical_port_id": null, 
            "allowed_address_pairs": [], 
            "device_owner": "compute:nova", 
            "fake_delete": true, 
            "fixed_ips": [
                {
                    "subnet_id": "6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a", 
                    "ip_address": "10.121.232.3"
                }
            ], 
            "id": "db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc", 
            "security_groups": [], 
            "binding:vif_type": "vrouter", 
            "mac_address": "fa:16:3e:90:8a:94", 
            "status": "PENDING_UPDATE", 
            "description": "", 
            "tags": {}, 
            "segmentation_id": 0, 
            "device_id": "47531b14-72e9-439d-8949-fd941457ecde", 
            "name": "load_balancer-user-port", 
            "managed_by_service": false, 
            "network_id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "admin_state_up": false, 
            "attached": false, 
            "operational_state": "NO_STATE", 
            "orchestration_state": "UPDATE_IN_PROGRESS", 
            "segmentation_type": "flat"
        }
    }, 
    0
]
```
