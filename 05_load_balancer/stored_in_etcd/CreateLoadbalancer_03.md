# Stored data in etcd: Create Loadbalancer

These are stored data for "heat_templates" in etcd.

* port

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ports/a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f
{
    "body": {
        "allowed_address_pairs": [], 
        "device_owner": "", 
        "fake_delete": true, 
        "fixed_ips": [
            {
                "subnet_id": "6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a", 
                "ip_address": "10.121.232.4"
            }
        ], 
        "id": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f", 
        "security_groups": [], 
        "binding:vif_type": "vrouter", 
        "mac_address": "fa:16:3e:21:5b:14", 
        "status": "PENDING_CREATE", 
        "description": "", 
        "tags": {}, 
        "segmentation_id": 0, 
        "device_id": "", 
        "name": "load_balancer-user-port", 
        "admin_state_up": false, 
        "network_id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
        "managed_by_service": false, 
        "attached": false, 
        "operational_state": "NO_STATE", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "segmentation_type": "flat"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/create:heat_worker:port:a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f:1:kv4w8
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f", 
        "handler": "heat_worker", 
        "job_name": "port:a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f:1", 
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
                "value": "", 
                "param": "virtual_machine"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f", 
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
                "value": "fa:16:3e:21:5b:14", 
                "param": "virtual_machine_interface_mac_address"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "", 
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
                        "subnet_id": "6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a", 
                        "ip_address": "10.121.232.4"
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
                "value": "", 
                "param": "jinja_device_owner"
            }, 
            {
                "resources": [
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
                "value": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f", 
                "param": "uuid"
            }
        ], 
        "resource_type": "port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:port:a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f:1:kv4w8", 
        "resource_input": {
            "allowed_address_pairs": [], 
            "device_owner": "", 
            "fake_delete": true, 
            "fixed_ips": [
                {
                    "subnet_id": "6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a", 
                    "ip_address": "10.121.232.4"
                }
            ], 
            "id": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f", 
            "security_groups": [], 
            "binding:vif_type": "vrouter", 
            "mac_address": "fa:16:3e:21:5b:14", 
            "status": "PENDING_CREATE", 
            "description": "", 
            "tags": {}, 
            "segmentation_id": 0, 
            "device_id": "", 
            "name": "load_balancer-user-port", 
            "managed_by_service": false, 
            "network_id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "admin_state_up": false, 
            "attached": false, 
            "operational_state": "NO_STATE", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "segmentation_type": "flat"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/ports/a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f
{
    "stack_id": "port_a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
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
            "output_value": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7", 
            "description": "Fully Qualified Name of the VMI", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "f68d0924-ef20-4c1b-ac45-0e6b879af5e7", 
            "description": "A unique id for the virtual machine interface.", 
            "output_key": "id"
        }, 
        {
            "output_value": {
                "allowed_address_pair": []
            }, 
            "description": "Virtual machine allowed address pairs.", 
            "output_key": "allowed_address_pairs"
        }, 
        {
            "output_value": [
                "fa:16:3e:f7:60:7f"
            ], 
            "description": "Virtual machine interface mac address.", 
            "output_key": "mac_address"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "port:a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/ports/a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f
{
    "heat_outputs": [
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
            "output_value": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7", 
            "description": "Fully Qualified Name of the VMI", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "f68d0924-ef20-4c1b-ac45-0e6b879af5e7", 
            "description": "A unique id for the virtual machine interface.", 
            "output_key": "id"
        }, 
        {
            "output_value": {
                "allowed_address_pair": []
            }, 
            "description": "Virtual machine allowed address pairs.", 
            "output_key": "allowed_address_pairs"
        }, 
        {
            "output_value": [
                "fa:16:3e:f7:60:7f"
            ], 
            "description": "Virtual machine interface mac address.", 
            "output_key": "mac_address"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/ports/a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": [[\"default-domain\", \"admin\", \"b62eefe0-0872-478d-adfe-1a606320f0e7\"]], \"description\": \"Virtual network.\", \"output_key\": \"virtual_network\"}, {\"output_value\": \"default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7\", \"description\": \"Fully Qualified Name of the VMI\", \"output_key\": \"fq_name\"}, {\"output_value\": \"f68d0924-ef20-4c1b-ac45-0e6b879af5e7\", \"description\": \"A unique id for the virtual machine interface.\", \"output_key\": \"id\"}, {\"output_value\": {\"allowed_address_pair\": []}, \"description\": \"Virtual machine allowed address pairs.\", \"output_key\": \"allowed_address_pairs\"}, {\"output_value\": [\"fa:16:3e:f7:60:7f\"], \"description\": \"Virtual machine interface mac address.\", \"output_key\": \"mac_address\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```