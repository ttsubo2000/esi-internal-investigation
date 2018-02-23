# Stored data in etcd: Update Loadbalancer Interface

These are stored data for "heat_templates" in etcd.

* port

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ports/db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc
{
    "body": {
        "ese_logical_port_id": null, 
        "allowed_address_pairs": [], 
        "device_owner": "compute:nova", 
        "fake_delete": false, 
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
        "status": "PENDING_DELETE", 
        "description": "", 
        "tags": {}, 
        "segmentation_id": 0, 
        "device_id": "47531b14-72e9-439d-8949-fd941457ecde", 
        "name": "load_balancer-user-port", 
        "admin_state_up": false, 
        "network_id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
        "managed_by_service": false, 
        "attached": true, 
        "operational_state": "INIT", 
        "orchestration_state": "DELETE_IN_PROGRESS", 
        "segmentation_type": "flat"
    }, 
    "version": 4, 
    "marked_for_deletion": true
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/logical_delete:heat_worker:port:db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc:4:ajjld
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc", 
        "handler": "heat_worker", 
        "job_name": "port:db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc:4", 
        "dependency": [], 
        "version": 4, 
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
                "value": 4, 
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
        "action": "logical_delete", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "logical_delete:heat_worker:port:db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc:4:ajjld", 
        "resource_input": {
            "ese_logical_port_id": null, 
            "allowed_address_pairs": [], 
            "device_owner": "compute:nova", 
            "fake_delete": false, 
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
            "status": "PENDING_DELETE", 
            "description": "", 
            "tags": {}, 
            "segmentation_id": 0, 
            "device_id": "47531b14-72e9-439d-8949-fd941457ecde", 
            "name": "load_balancer-user-port", 
            "managed_by_service": false, 
            "network_id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "admin_state_up": false, 
            "attached": true, 
            "operational_state": "INIT", 
            "orchestration_state": "DELETE_IN_PROGRESS", 
            "segmentation_type": "flat"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/ports/db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc
{
    "stack_id": "", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "DELETE_COMPLETE", 
    "output": [], 
    "status_reason": "", 
    "id": "port:db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/ports/db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc
{
    "heat_outputs": [], 
    "orchestration_state": "DELETE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/ports/db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc
{
    "state": {
        "worker_state": "DELETE_COMPLETED", 
        "heat_outputs": "[]", 
        "orchestration_state": "DELETE_COMPLETE"
    }, 
    "version": 4, 
    "error": ""
}
```
