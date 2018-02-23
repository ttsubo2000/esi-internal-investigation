# Stored data in etcd: Create Gw Interface

These are stored data for "heat_templates" in etcd.

* port
* port_monitoring

![scope](../../images/esi_interface.008.png)

These are stored data for "Create Gw Interface" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ports/67d9f139-b5be-4082-a090-3a1a9cbf1df8
{
    "body": {
        "ese_logical_port_id": "ecb4c4ac-3ebc-4045-a27c-52fecc93bac5", 
        "status": "PENDING_CREATE", 
        "description": "", 
        "allowed_address_pairs": [], 
        "admin_state_up": true, 
        "network_id": "bb69041d-c654-4e9f-a763-afd4333275bc", 
        "segmentation_id": 1025, 
        "managed_by_service": true, 
        "attached": true, 
        "segmentation_type": "vlan", 
        "name": "Port for : 176ec475-e9e8-4605-8b41-802fbc6220c1", 
        "binding:vif_type": "vrouter", 
        "device_owner": "network:gw_interface", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "fake_delete": false, 
        "mac_address": "fa:16:3e:62:dd:f5", 
        "fixed_ips": [
            {
                "subnet_id": "b4f0c956-2fe0-4634-b7c8-22bfd8095aaf", 
                "ip_address": "172.16.101.153"
            }
        ], 
        "id": "67d9f139-b5be-4082-a090-3a1a9cbf1df8", 
        "tags": {}, 
        "device_id": "fbd7d07e-9e84-4ad7-ab85-36d46adb9435"
    }, 
    "version": 2, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for monitoring_worker
```
/jobs/all/delete:monitoring_worker:port:67d9f139-b5be-4082-a090-3a1a9cbf1df8:2:1d1eh
[
    "monitoring_worker", 
    {
        "is_first": true, 
        "resource_id": "67d9f139-b5be-4082-a090-3a1a9cbf1df8", 
        "handler": "monitoring_worker", 
        "job_name": "port:67d9f139-b5be-4082-a090-3a1a9cbf1df8:2", 
        "dependency": [], 
        "version": 2, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "network:gw_interface", 
                "param": "device_owner"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": false, 
                "param": "attached"
            }, 
            {
                "resources": [], 
                "type": "output_key", 
                "value": {
                    "output_key": "fq_name", 
                    "resource_type": "port", 
                    "resource_id": "67d9f139-b5be-4082-a090-3a1a9cbf1df8"
                }, 
                "param": "vmi_fq_name"
            }, 
            {
                "resources": [], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "port", 
                    "resource_id": "67d9f139-b5be-4082-a090-3a1a9cbf1df8"
                }, 
                "param": "vmi_uuid"
            }
        ], 
        "resource_type": "port", 
        "action": "delete", 
        "is_last": false, 
        "on_failure": "ignore", 
        "id": "delete:monitoring_worker:port:67d9f139-b5be-4082-a090-3a1a9cbf1df8:2:1d1eh", 
        "resource_input": {
            "ese_logical_port_id": "ecb4c4ac-3ebc-4045-a27c-52fecc93bac5", 
            "status": "PENDING_CREATE", 
            "description": "", 
            "allowed_address_pairs": [], 
            "admin_state_up": true, 
            "network_id": "bb69041d-c654-4e9f-a763-afd4333275bc", 
            "segmentation_id": 1025, 
            "fixed_ips": [
                {
                    "subnet_id": "b4f0c956-2fe0-4634-b7c8-22bfd8095aaf", 
                    "ip_address": "172.16.101.153"
                }
            ], 
            "managed_by_service": true, 
            "attached": true, 
            "id": "67d9f139-b5be-4082-a090-3a1a9cbf1df8", 
            "binding:vif_type": "vrouter", 
            "device_owner": "network:gw_interface", 
            "fake_delete": false, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "device_id": "fbd7d07e-9e84-4ad7-ab85-36d46adb9435", 
            "segmentation_type": "vlan", 
            "mac_address": "fa:16:3e:62:dd:f5", 
            "tags": {}, 
            "name": "Port for : 176ec475-e9e8-4605-8b41-802fbc6220c1"
        }
    }, 
    0
]
```

* Jobs for heat_worker
```
/jobs/all/modify:heat_worker:port:67d9f139-b5be-4082-a090-3a1a9cbf1df8:2:to984
[
    "heat_worker", 
    {
        "is_first": false, 
        "resource_id": "67d9f139-b5be-4082-a090-3a1a9cbf1df8", 
        "handler": "heat_worker", 
        "job_name": "port:67d9f139-b5be-4082-a090-3a1a9cbf1df8:2", 
        "dependency": [
            "delete:monitoring_worker:port:67d9f139-b5be-4082-a090-3a1a9cbf1df8:2:1d1eh"
        ], 
        "version": 2, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "network", 
                        "resource_id": "bb69041d-c654-4e9f-a763-afd4333275bc"
                    }, 
                    {
                        "resource_type": "network", 
                        "resource_id": "bb69041d-c654-4e9f-a763-afd4333275bc"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "bb69041d-c654-4e9f-a763-afd4333275bc"
                }, 
                "param": "virtual_network"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "fbd7d07e-9e84-4ad7-ab85-36d46adb9435", 
                "param": "virtual_machine"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "67d9f139-b5be-4082-a090-3a1a9cbf1df8", 
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
                "value": [], 
                "param": "virtual_machine_interface_allowed_address_pairs"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "fa:16:3e:62:dd:f5", 
                "param": "virtual_machine_interface_mac_address"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "network:gw_interface", 
                "param": "device_owner"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "gw_interface", 
                        "resource_id": "fbd7d07e-9e84-4ad7-ab85-36d46adb9435"
                    }, 
                    {
                        "resource_type": "gw_interface", 
                        "resource_id": "fbd7d07e-9e84-4ad7-ab85-36d46adb9435"
                    }
                ], 
                "type": "value", 
                "value": "fbd7d07e-9e84-4ad7-ab85-36d46adb9435", 
                "param": "jinja_force_dependency_gw_interface"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [
                    {
                        "subnet_id": "b4f0c956-2fe0-4634-b7c8-22bfd8095aaf", 
                        "ip_address": "172.16.101.153"
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
                "resources": [
                    {
                        "resource_type": "subnet", 
                        "resource_id": "b4f0c956-2fe0-4634-b7c8-22bfd8095aaf"
                    }, 
                    {
                        "resource_type": "subnet", 
                        "resource_id": "b4f0c956-2fe0-4634-b7c8-22bfd8095aaf"
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
                            "resource_id": "b4f0c956-2fe0-4634-b7c8-22bfd8095aaf"
                        }, 
                        "resources": []
                    }
                ], 
                "param": "jinja_subnets"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "67d9f139-b5be-4082-a090-3a1a9cbf1df8", 
                "param": "uuid"
            }
        ], 
        "resource_type": "port", 
        "action": "modify", 
        "is_last": false, 
        "on_failure": "fail", 
        "id": "modify:heat_worker:port:67d9f139-b5be-4082-a090-3a1a9cbf1df8:2:to984", 
        "resource_input": {
            "ese_logical_port_id": "ecb4c4ac-3ebc-4045-a27c-52fecc93bac5", 
            "status": "PENDING_CREATE", 
            "description": "", 
            "allowed_address_pairs": [], 
            "admin_state_up": true, 
            "network_id": "bb69041d-c654-4e9f-a763-afd4333275bc", 
            "segmentation_id": 1025, 
            "fixed_ips": [
                {
                    "subnet_id": "b4f0c956-2fe0-4634-b7c8-22bfd8095aaf", 
                    "ip_address": "172.16.101.153"
                }
            ], 
            "managed_by_service": true, 
            "attached": true, 
            "id": "67d9f139-b5be-4082-a090-3a1a9cbf1df8", 
            "binding:vif_type": "vrouter", 
            "device_owner": "network:gw_interface", 
            "fake_delete": false, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "device_id": "fbd7d07e-9e84-4ad7-ab85-36d46adb9435", 
            "segmentation_type": "vlan", 
            "mac_address": "fa:16:3e:62:dd:f5", 
            "tags": {}, 
            "name": "Port for : 176ec475-e9e8-4605-8b41-802fbc6220c1"
        }
    }, 
    0
]
```

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:port:67d9f139-b5be-4082-a090-3a1a9cbf1df8:2:t549r
[
    "monitoring_worker", 
    {
        "is_first": false, 
        "resource_id": "67d9f139-b5be-4082-a090-3a1a9cbf1df8", 
        "handler": "monitoring_worker", 
        "job_name": "port:67d9f139-b5be-4082-a090-3a1a9cbf1df8:2", 
        "dependency": [
            "modify:heat_worker:port:67d9f139-b5be-4082-a090-3a1a9cbf1df8:2:to984", 
            "delete:monitoring_worker:port:67d9f139-b5be-4082-a090-3a1a9cbf1df8:2:1d1eh"
        ], 
        "version": 2, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "network:gw_interface", 
                "param": "device_owner"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": true, 
                "param": "attached"
            }, 
            {
                "resources": [], 
                "type": "output_key", 
                "value": {
                    "output_key": "fq_name", 
                    "resource_type": "port", 
                    "resource_id": "67d9f139-b5be-4082-a090-3a1a9cbf1df8"
                }, 
                "param": "vmi_fq_name"
            }, 
            {
                "resources": [], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "port", 
                    "resource_id": "67d9f139-b5be-4082-a090-3a1a9cbf1df8"
                }, 
                "param": "vmi_uuid"
            }
        ], 
        "resource_type": "port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:port:67d9f139-b5be-4082-a090-3a1a9cbf1df8:2:t549r", 
        "resource_input": {
            "ese_logical_port_id": "ecb4c4ac-3ebc-4045-a27c-52fecc93bac5", 
            "status": "PENDING_CREATE", 
            "description": "", 
            "allowed_address_pairs": [], 
            "admin_state_up": true, 
            "network_id": "bb69041d-c654-4e9f-a763-afd4333275bc", 
            "segmentation_id": 1025, 
            "fixed_ips": [
                {
                    "subnet_id": "b4f0c956-2fe0-4634-b7c8-22bfd8095aaf", 
                    "ip_address": "172.16.101.153"
                }
            ], 
            "managed_by_service": true, 
            "attached": true, 
            "id": "67d9f139-b5be-4082-a090-3a1a9cbf1df8", 
            "binding:vif_type": "vrouter", 
            "device_owner": "network:gw_interface", 
            "fake_delete": false, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "device_id": "fbd7d07e-9e84-4ad7-ab85-36d46adb9435", 
            "segmentation_type": "vlan", 
            "mac_address": "fa:16:3e:62:dd:f5", 
            "tags": {}, 
            "name": "Port for : 176ec475-e9e8-4605-8b41-802fbc6220c1"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/ports/67d9f139-b5be-4082-a090-3a1a9cbf1df8
{
    "stack_id": "port_67d9f139-b5be-4082-a090-3a1a9cbf1df8", 
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
    "stack_status": "UPDATE_COMPLETE", 
    "output": [
        {
            "output_value": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb", 
            "description": "Virtual network.", 
            "output_key": "virtual_network"
        }, 
        {
            "output_value": "default-domain:admin:67d9f139-b5be-4082-a090-3a1a9cbf1df8", 
            "description": "Fully Qualified Name of the VMI", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "67d9f139-b5be-4082-a090-3a1a9cbf1df8", 
            "description": "A unique id for the virtual machine interface.", 
            "output_key": "id"
        }, 
        {
            "output_value": "null", 
            "description": "Virtual machine allowed address pairs.", 
            "output_key": "allowed_address_pairs"
        }, 
        {
            "output_value": "xx:xx:xx:xx:xx:xx", 
            "description": "Virtual machine interface mac address.", 
            "output_key": "mac_address"
        }
    ], 
    "status_reason": "Stack successfully updated", 
    "id": "port:67d9f139-b5be-4082-a090-3a1a9cbf1df8"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/ports/67d9f139-b5be-4082-a090-3a1a9cbf1df8
{
    "heat_outputs": [
        {
            "output_value": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb", 
            "description": "Virtual network.", 
            "output_key": "virtual_network"
        }, 
        {
            "output_value": "default-domain:admin:67d9f139-b5be-4082-a090-3a1a9cbf1df8", 
            "description": "Fully Qualified Name of the VMI", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "67d9f139-b5be-4082-a090-3a1a9cbf1df8", 
            "description": "A unique id for the virtual machine interface.", 
            "output_key": "id"
        }, 
        {
            "output_value": "null", 
            "description": "Virtual machine allowed address pairs.", 
            "output_key": "allowed_address_pairs"
        }, 
        {
            "output_value": "xx:xx:xx:xx:xx:xx", 
            "description": "Virtual machine interface mac address.", 
            "output_key": "mac_address"
        }
    ]
}
```

### Checking stored data at the point of (5) in etcd

```
/esi-worker/job_state/v2.0/ports/67d9f139-b5be-4082-a090-3a1a9cbf1df8
{
    "state_monitoring": {
        "vmi": "ACTIVE"
    }, 
    "heat_outputs": [
        {
            "output_value": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb", 
            "description": "Virtual network.", 
            "output_key": "virtual_network"
        }, 
        {
            "output_value": "default-domain:admin:67d9f139-b5be-4082-a090-3a1a9cbf1df8", 
            "description": "Fully Qualified Name of the VMI", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "67d9f139-b5be-4082-a090-3a1a9cbf1df8", 
            "description": "A unique id for the virtual machine interface.", 
            "output_key": "id"
        }, 
        {
            "output_value": "null", 
            "description": "Virtual machine allowed address pairs.", 
            "output_key": "allowed_address_pairs"
        }, 
        {
            "output_value": "xx:xx:xx:xx:xx:xx", 
            "description": "Virtual machine interface mac address.", 
            "output_key": "mac_address"
        }
    ]
}
```

### Checking stored data at the point of (6) in etcd

```
/state/v2.0/ports/67d9f139-b5be-4082-a090-3a1a9cbf1df8
{
    "state": {
        "state_monitoring": "{\"vmi\": \"ACTIVE\"}", 
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb\", \"description\": \"Virtual network.\", \"output_key\": \"virtual_network\"}, {\"output_value\": \"default-domain:admin:67d9f139-b5be-4082-a090-3a1a9cbf1df8\", \"description\": \"Fully Qualified Name of the VMI\", \"output_key\": \"fq_name\"}, {\"output_value\": \"67d9f139-b5be-4082-a090-3a1a9cbf1df8\", \"description\": \"A unique id for the virtual machine interface.\", \"output_key\": \"id\"}, {\"output_value\": \"null\", \"description\": \"Virtual machine allowed address pairs.\", \"output_key\": \"allowed_address_pairs\"}, {\"output_value\": \"xx:xx:xx:xx:xx:xx\", \"description\": \"Virtual machine interface mac address.\", \"output_key\": \"mac_address\"}]"
    }, 
    "version": 2, 
    "error": ""
}
```

### Checking stored data at the point of (7) in etcd

```
/monitoring/v2.0/ports/67d9f139-b5be-4082-a090-3a1a9cbf1df8
{
    "version": 2, 
    "vmi": "UP"
}
```
