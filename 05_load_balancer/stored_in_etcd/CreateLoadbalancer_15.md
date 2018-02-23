# Stored data in etcd: Create Loadbalancer

These are stored data for "heat_templates" in etcd.

* port

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ports/ddc14be4-3480-4e97-a978-817b18f9904c
{
    "body": {
        "ese_logical_port_id": null, 
        "allowed_address_pairs": [], 
        "device_owner": "compute:nova", 
        "fake_delete": true, 
        "fixed_ips": [
            {
                "subnet_id": "707847d0-89d9-4b98-93a2-8b376709c5f3", 
                "ip_address": "100.64.193.3"
            }
        ], 
        "id": "ddc14be4-3480-4e97-a978-817b18f9904c", 
        "security_groups": [], 
        "binding:vif_type": "vrouter", 
        "mac_address": "fa:16:3e:cf:b0:c4", 
        "status": "PENDING_UPDATE", 
        "description": "", 
        "tags": {}, 
        "segmentation_id": 0, 
        "device_id": "47531b14-72e9-439d-8949-fd941457ecde", 
        "name": "load_balancer-management-port", 
        "admin_state_up": true, 
        "network_id": "168c1535-9001-49c7-bb05-21844570a83c", 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
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
/jobs/all/modify:heat_worker:port:ddc14be4-3480-4e97-a978-817b18f9904c:3:28byp
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "ddc14be4-3480-4e97-a978-817b18f9904c", 
        "handler": "heat_worker", 
        "job_name": "port:ddc14be4-3480-4e97-a978-817b18f9904c:3", 
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
                        "resource_id": "168c1535-9001-49c7-bb05-21844570a83c"
                    }, 
                    {
                        "resource_type": "network", 
                        "resource_id": "168c1535-9001-49c7-bb05-21844570a83c"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "168c1535-9001-49c7-bb05-21844570a83c"
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
                "value": "ddc14be4-3480-4e97-a978-817b18f9904c", 
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
                "value": "fa:16:3e:cf:b0:c4", 
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
                        "subnet_id": "707847d0-89d9-4b98-93a2-8b376709c5f3", 
                        "ip_address": "100.64.193.3"
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
                        "resource_id": "707847d0-89d9-4b98-93a2-8b376709c5f3"
                    }, 
                    {
                        "resource_type": "subnet", 
                        "resource_id": "707847d0-89d9-4b98-93a2-8b376709c5f3"
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
                            "resource_id": "707847d0-89d9-4b98-93a2-8b376709c5f3"
                        }, 
                        "resources": []
                    }
                ], 
                "param": "jinja_subnets"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "ddc14be4-3480-4e97-a978-817b18f9904c", 
                "param": "uuid"
            }
        ], 
        "resource_type": "port", 
        "action": "modify", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "modify:heat_worker:port:ddc14be4-3480-4e97-a978-817b18f9904c:3:28byp", 
        "resource_input": {
            "ese_logical_port_id": null, 
            "allowed_address_pairs": [], 
            "device_owner": "compute:nova", 
            "fake_delete": true, 
            "fixed_ips": [
                {
                    "subnet_id": "707847d0-89d9-4b98-93a2-8b376709c5f3", 
                    "ip_address": "100.64.193.3"
                }
            ], 
            "id": "ddc14be4-3480-4e97-a978-817b18f9904c", 
            "security_groups": [], 
            "binding:vif_type": "vrouter", 
            "mac_address": "fa:16:3e:cf:b0:c4", 
            "status": "PENDING_UPDATE", 
            "description": "", 
            "tags": {}, 
            "segmentation_id": 0, 
            "device_id": "47531b14-72e9-439d-8949-fd941457ecde", 
            "name": "load_balancer-management-port", 
            "managed_by_service": false, 
            "network_id": "168c1535-9001-49c7-bb05-21844570a83c", 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
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

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/ports/ddc14be4-3480-4e97-a978-817b18f9904c
{
    "stack_id": "port_ddc14be4-3480-4e97-a978-817b18f9904c", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
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
            "output_value": "cc987cdf-428c-446c-a390-540c5af4449d", 
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
            "output_value": "http://collector-agents-se:7070/targets/cc987cdf-428c-446c-a390-540c5af4449d", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack successfully updated", 
    "id": "port:ddc14be4-3480-4e97-a978-817b18f9904c"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/ports/ddc14be4-3480-4e97-a978-817b18f9904c
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
            "output_value": "cc987cdf-428c-446c-a390-540c5af4449d", 
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
            "output_value": "http://collector-agents-se:7070/targets/cc987cdf-428c-446c-a390-540c5af4449d", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "UPDATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/ports/ddc14be4-3480-4e97-a978-817b18f9904c
{
    "state": {
        "worker_state": "MODIFY_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7\", \"description\": \"Fully Qualified Name of the VMI\", \"output_key\": \"fq_name\"}, {\"output_value\": {\"allowed_address_pair\": []}, \"description\": \"Virtual machine allowed address pairs.\", \"output_key\": \"allowed_address_pairs\"}, {\"output_value\": \"cc987cdf-428c-446c-a390-540c5af4449d\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": [\"fa:16:3e:f7:60:7f\"], \"description\": \"Virtual machine interface mac address.\", \"output_key\": \"mac_address\"}, {\"output_value\": [[\"default-domain\", \"admin\", \"b62eefe0-0872-478d-adfe-1a606320f0e7\"]], \"description\": \"Virtual network.\", \"output_key\": \"virtual_network\"}, {\"output_value\": \"f68d0924-ef20-4c1b-ac45-0e6b879af5e7\", \"description\": \"A unique id for the virtual machine interface.\", \"output_key\": \"id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/cc987cdf-428c-446c-a390-540c5af4449d\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "UPDATE_COMPLETE"
    }, 
    "version": 3, 
    "error": ""
}
```

### Checking stored data at the point of (6) in etcd

```
/monitoring/v2.0/ports/ddc14be4-3480-4e97-a978-817b18f9904c
{
    "version": 3, 
    "vmi": "UP"
}
```
and then ...
```
/monitoring/v2.0/ports/ddc14be4-3480-4e97-a978-817b18f9904c
{
    "version": 3, 
    "vmi": "FAIL"
}
```
