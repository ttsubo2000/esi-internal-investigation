# Stored data in etcd: Update Firewall Interface

These are stored data for "heat_templates" in etcd.

* port

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ports/dea87c7b-b43f-4936-8e32-8995b038b3f8
{
    "body": {
        "ese_logical_port_id": null, 
        "allowed_address_pairs": [], 
        "device_owner": "compute:nova", 
        "fake_delete": false, 
        "fixed_ips": [
            {
                "subnet_id": "1244d619-cc55-4bb7-b181-606776ba5e88", 
                "ip_address": "10.121.232.3"
            }
        ], 
        "id": "dea87c7b-b43f-4936-8e32-8995b038b3f8", 
        "security_groups": [], 
        "binding:vif_type": "vrouter", 
        "mac_address": "fa:16:3e:99:1e:37", 
        "status": "PENDING_DELETE", 
        "description": "", 
        "tags": {}, 
        "segmentation_id": 0, 
        "device_id": "2e555b09-e0d7-4cce-8854-c481a2363917", 
        "name": "firewall-user-port", 
        "admin_state_up": false, 
        "network_id": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
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
/jobs/all/logical_delete:heat_worker:port:dea87c7b-b43f-4936-8e32-8995b038b3f8:4:iq8l6
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "dea87c7b-b43f-4936-8e32-8995b038b3f8", 
        "handler": "heat_worker", 
        "job_name": "port:dea87c7b-b43f-4936-8e32-8995b038b3f8:4", 
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
                        "resource_id": "73b2c401-a1f3-49fb-8612-8c755b37a28d"
                    }, 
                    {
                        "resource_type": "network", 
                        "resource_id": "73b2c401-a1f3-49fb-8612-8c755b37a28d"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "73b2c401-a1f3-49fb-8612-8c755b37a28d"
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
                "value": "dea87c7b-b43f-4936-8e32-8995b038b3f8", 
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
                "value": "fa:16:3e:99:1e:37", 
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
                        "subnet_id": "1244d619-cc55-4bb7-b181-606776ba5e88", 
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
                        "resource_id": "1244d619-cc55-4bb7-b181-606776ba5e88"
                    }, 
                    {
                        "resource_type": "subnet", 
                        "resource_id": "1244d619-cc55-4bb7-b181-606776ba5e88"
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
                            "resource_id": "1244d619-cc55-4bb7-b181-606776ba5e88"
                        }, 
                        "resources": []
                    }
                ], 
                "param": "jinja_subnets"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "dea87c7b-b43f-4936-8e32-8995b038b3f8", 
                "param": "uuid"
            }
        ], 
        "resource_type": "port", 
        "action": "logical_delete", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "logical_delete:heat_worker:port:dea87c7b-b43f-4936-8e32-8995b038b3f8:4:iq8l6", 
        "resource_input": {
            "ese_logical_port_id": null, 
            "allowed_address_pairs": [], 
            "device_owner": "compute:nova", 
            "fake_delete": false, 
            "fixed_ips": [
                {
                    "subnet_id": "1244d619-cc55-4bb7-b181-606776ba5e88", 
                    "ip_address": "10.121.232.3"
                }
            ], 
            "id": "dea87c7b-b43f-4936-8e32-8995b038b3f8", 
            "security_groups": [], 
            "binding:vif_type": "vrouter", 
            "mac_address": "fa:16:3e:99:1e:37", 
            "status": "PENDING_DELETE", 
            "description": "", 
            "tags": {}, 
            "segmentation_id": 0, 
            "device_id": "2e555b09-e0d7-4cce-8854-c481a2363917", 
            "name": "firewall-user-port", 
            "managed_by_service": false, 
            "network_id": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
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
/esi-worker/heat_stacks/v2.0/ports/dea87c7b-b43f-4936-8e32-8995b038b3f8
{
    "stack_id": "", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "stack_status": "DELETE_COMPLETE", 
    "output": [], 
    "status_reason": "", 
    "id": "port:dea87c7b-b43f-4936-8e32-8995b038b3f8"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/ports/dea87c7b-b43f-4936-8e32-8995b038b3f8
{
    "heat_outputs": [], 
    "orchestration_state": "DELETE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/ports/dea87c7b-b43f-4936-8e32-8995b038b3f8
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
