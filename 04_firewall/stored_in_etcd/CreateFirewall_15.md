# Stored data in etcd: Create Firewall

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
        "fake_delete": true, 
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
        "status": "PENDING_UPDATE", 
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
        "operational_state": "NO_STATE", 
        "orchestration_state": "UPDATE_IN_PROGRESS", 
        "segmentation_type": "flat"
    }, 
    "version": 3, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/modify:heat_worker:port:dea87c7b-b43f-4936-8e32-8995b038b3f8:3:g8dg6
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "dea87c7b-b43f-4936-8e32-8995b038b3f8", 
        "handler": "heat_worker", 
        "job_name": "port:dea87c7b-b43f-4936-8e32-8995b038b3f8:3", 
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
        "action": "modify", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "modify:heat_worker:port:dea87c7b-b43f-4936-8e32-8995b038b3f8:3:g8dg6", 
        "resource_input": {
            "ese_logical_port_id": null, 
            "allowed_address_pairs": [], 
            "device_owner": "compute:nova", 
            "fake_delete": true, 
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
            "status": "PENDING_UPDATE", 
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
            "operational_state": "NO_STATE", 
            "orchestration_state": "UPDATE_IN_PROGRESS", 
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
    "stack_id": "port_dea87c7b-b43f-4936-8e32-8995b038b3f8", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "stack_status": "UPDATE_COMPLETE", 
    "output": [
        {
            "output_value": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7", 
            "description": "Fully Qualified Name of the VMI", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": {
                "allowed_address_pair": []
            }, 
            "description": "Virtual machine allowed address pairs.", 
            "output_key": "allowed_address_pairs"
        }, 
        {
            "output_value": "6eea0aa6-879f-4bec-a9de-97cb607b75bf", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": [
                "fa:16:3e:f7:60:7f"
            ], 
            "description": "Virtual machine interface mac address.", 
            "output_key": "mac_address"
        }, 
        {
            "output_value": [
                [
                    "default-domain", 
                    "admin", 
                    "b62eefe0-0872-478d-adfe-1a606320f0e7"
                ]
            ], 
            "description": "Virtual network.", 
            "output_key": "virtual_network"
        }, 
        {
            "output_value": "f68d0924-ef20-4c1b-ac45-0e6b879af5e7", 
            "description": "A unique id for the virtual machine interface.", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/6eea0aa6-879f-4bec-a9de-97cb607b75bf", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack successfully updated", 
    "id": "port:dea87c7b-b43f-4936-8e32-8995b038b3f8"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/ports/dea87c7b-b43f-4936-8e32-8995b038b3f8
{
    "heat_outputs": [
        {
            "output_value": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7", 
            "description": "Fully Qualified Name of the VMI", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": {
                "allowed_address_pair": []
            }, 
            "description": "Virtual machine allowed address pairs.", 
            "output_key": "allowed_address_pairs"
        }, 
        {
            "output_value": "6eea0aa6-879f-4bec-a9de-97cb607b75bf", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": [
                "fa:16:3e:f7:60:7f"
            ], 
            "description": "Virtual machine interface mac address.", 
            "output_key": "mac_address"
        }, 
        {
            "output_value": [
                [
                    "default-domain", 
                    "admin", 
                    "b62eefe0-0872-478d-adfe-1a606320f0e7"
                ]
            ], 
            "description": "Virtual network.", 
            "output_key": "virtual_network"
        }, 
        {
            "output_value": "f68d0924-ef20-4c1b-ac45-0e6b879af5e7", 
            "description": "A unique id for the virtual machine interface.", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/6eea0aa6-879f-4bec-a9de-97cb607b75bf", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "UPDATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/ports/dea87c7b-b43f-4936-8e32-8995b038b3f8
{
    "state": {
        "worker_state": "MODIFY_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7\", \"description\": \"Fully Qualified Name of the VMI\", \"output_key\": \"fq_name\"}, {\"output_value\": {\"allowed_address_pair\": []}, \"description\": \"Virtual machine allowed address pairs.\", \"output_key\": \"allowed_address_pairs\"}, {\"output_value\": \"6eea0aa6-879f-4bec-a9de-97cb607b75bf\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": [\"fa:16:3e:f7:60:7f\"], \"description\": \"Virtual machine interface mac address.\", \"output_key\": \"mac_address\"}, {\"output_value\": [[\"default-domain\", \"admin\", \"b62eefe0-0872-478d-adfe-1a606320f0e7\"]], \"description\": \"Virtual network.\", \"output_key\": \"virtual_network\"}, {\"output_value\": \"f68d0924-ef20-4c1b-ac45-0e6b879af5e7\", \"description\": \"A unique id for the virtual machine interface.\", \"output_key\": \"id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/6eea0aa6-879f-4bec-a9de-97cb607b75bf\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "UPDATE_COMPLETE"
    }, 
    "version": 3, 
    "error": ""
}
```

### Checking stored data at the point of (6) in etcd
```
/monitoring/v2.0/ports/dea87c7b-b43f-4936-8e32-8995b038b3f8
{
    "version": 3,
    "vmi": "FAIL"
}
``` 