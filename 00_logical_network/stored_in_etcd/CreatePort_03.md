# Stored data in etcd: Create Port

These are stored data for "heat_templates" in etcd.

* port

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ports/fde61b02-9615-4e75-aac0-30a333657c1b
{
    "body": {
        "ese_logical_port_id": "ced1435d-6dfa-4dab-bb7c-19da4d8e48b7", 
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
        "admin_state_up": true, 
        "network_id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
        "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
        "managed_by_service": false, 
        "attached": true, 
        "operational_state": "NO_STATE", 
        "orchestration_state": "UPDATE_IN_PROGRESS", 
        "segmentation_type": "vlan"
    }, 
    "version": 2, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/modify:heat_worker:port:fde61b02-9615-4e75-aac0-30a333657c1b:2:frkcu
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "fde61b02-9615-4e75-aac0-30a333657c1b", 
        "handler": "heat_worker", 
        "job_name": "port:fde61b02-9615-4e75-aac0-30a333657c1b:2", 
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
                        "resource_id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263"
                    }, 
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
                    }, 
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
        "action": "modify", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "modify:heat_worker:port:fde61b02-9615-4e75-aac0-30a333657c1b:2:frkcu", 
        "resource_input": {
            "ese_logical_port_id": "ced1435d-6dfa-4dab-bb7c-19da4d8e48b7", 
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
            "attached": true, 
            "operational_state": "NO_STATE", 
            "orchestration_state": "UPDATE_IN_PROGRESS", 
            "segmentation_type": "vlan"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/ports/fde61b02-9615-4e75-aac0-30a333657c1b
{
    "stack_id": "port_fde61b02-9615-4e75-aac0-30a333657c1b", 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
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
            "output_value": "31ac332f-d172-4a39-8fa5-976ada238eff", 
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
            "output_value": "http://collector-agents-se:7070/targets/31ac332f-d172-4a39-8fa5-976ada238eff", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack successfully updated", 
    "id": "port:fde61b02-9615-4e75-aac0-30a333657c1b"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/ports/fde61b02-9615-4e75-aac0-30a333657c1b
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
            "output_value": "31ac332f-d172-4a39-8fa5-976ada238eff", 
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
            "output_value": "http://collector-agents-se:7070/targets/31ac332f-d172-4a39-8fa5-976ada238eff", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "UPDATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/ports/fde61b02-9615-4e75-aac0-30a333657c1b
{
    "state": {
        "worker_state": "MODIFY_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7\", \"description\": \"Fully Qualified Name of the VMI\", \"output_key\": \"fq_name\"}, {\"output_value\": {\"allowed_address_pair\": []}, \"description\": \"Virtual machine allowed address pairs.\", \"output_key\": \"allowed_address_pairs\"}, {\"output_value\": \"31ac332f-d172-4a39-8fa5-976ada238eff\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": [\"fa:16:3e:f7:60:7f\"], \"description\": \"Virtual machine interface mac address.\", \"output_key\": \"mac_address\"}, {\"output_value\": [[\"default-domain\", \"admin\", \"b62eefe0-0872-478d-adfe-1a606320f0e7\"]], \"description\": \"Virtual network.\", \"output_key\": \"virtual_network\"}, {\"output_value\": \"f68d0924-ef20-4c1b-ac45-0e6b879af5e7\", \"description\": \"A unique id for the virtual machine interface.\", \"output_key\": \"id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/31ac332f-d172-4a39-8fa5-976ada238eff\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "UPDATE_COMPLETE"
    }, 
    "version": 2, 
    "error": ""
}
```

### Checking stored data at the point of (6) in etcd

```
/monitoring/v2.0/ports/fde61b02-9615-4e75-aac0-30a333657c1b
{
    "version": 2, 
    "vmi": "UP"
}
```
