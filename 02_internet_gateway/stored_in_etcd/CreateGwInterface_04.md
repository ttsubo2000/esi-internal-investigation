# Stored data in etcd: Create Gw Interface

These are stored data for "heat_templates" in etcd.

* port
* port_monitoring

![scope](../../images/esi_interface.008.png)

These are stored data for "Create Gw Interface" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ports/7abe783f-4837-417d-b76f-771ec4d38b97
{
    "body": {
        "status": "PENDING_CREATE", 
        "description": "", 
        "allowed_address_pairs": [], 
        "admin_state_up": true, 
        "network_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
        "segmentation_id": 1025, 
        "managed_by_service": true, 
        "attached": false, 
        "segmentation_type": "vlan", 
        "name": "Port for : 8a4bbfe0-5aae-42f5-8b94-c4c14b9e7306", 
        "binding:vif_type": "vrouter", 
        "device_owner": "network:gw_interface", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "fake_delete": false, 
        "mac_address": "fa:16:3e:f8:45:26", 
        "fixed_ips": [
            {
                "subnet_id": "a510f785-7758-4ce5-8fd4-c107d11b8e40", 
                "ip_address": "172.16.101.153"
            }
        ], 
        "id": "7abe783f-4837-417d-b76f-771ec4d38b97", 
        "tags": {}, 
        "device_id": "b9618566-14ea-4505-8eae-8fdb4b6a0ec1"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:port:7abe783f-4837-417d-b76f-771ec4d38b97:1:3gezy
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "7abe783f-4837-417d-b76f-771ec4d38b97", 
        "handler": "heat_worker", 
        "job_name": "port:7abe783f-4837-417d-b76f-771ec4d38b97:1", 
        "dependency": [
            "create:heat_worker:gw_interface:b9618566-14ea-4505-8eae-8fdb4b6a0ec1:1:ihknd"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "network", 
                        "resource_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0"
                }, 
                "param": "virtual_network"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "b9618566-14ea-4505-8eae-8fdb4b6a0ec1", 
                "param": "virtual_machine"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "7abe783f-4837-417d-b76f-771ec4d38b97", 
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
                "value": "fa:16:3e:f8:45:26", 
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
                        "resource_id": "b9618566-14ea-4505-8eae-8fdb4b6a0ec1"
                    }
                ], 
                "type": "value", 
                "value": "b9618566-14ea-4505-8eae-8fdb4b6a0ec1", 
                "param": "jinja_force_dependency_gw_interface"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [
                    {
                        "subnet_id": "a510f785-7758-4ce5-8fd4-c107d11b8e40", 
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
                        "resource_id": "a510f785-7758-4ce5-8fd4-c107d11b8e40"
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
                            "resource_id": "a510f785-7758-4ce5-8fd4-c107d11b8e40"
                        }, 
                        "resources": []
                    }
                ], 
                "param": "jinja_subnets"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "7abe783f-4837-417d-b76f-771ec4d38b97", 
                "param": "uuid"
            }
        ], 
        "resource_type": "port", 
        "action": "create", 
        "is_last": false, 
        "on_failure": "fail", 
        "id": "create:heat_worker:port:7abe783f-4837-417d-b76f-771ec4d38b97:1:3gezy", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "", 
            "allowed_address_pairs": [], 
            "admin_state_up": true, 
            "network_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
            "segmentation_id": 1025, 
            "fixed_ips": [
                {
                    "subnet_id": "a510f785-7758-4ce5-8fd4-c107d11b8e40", 
                    "ip_address": "172.16.101.153"
                }
            ], 
            "managed_by_service": true, 
            "attached": false, 
            "id": "7abe783f-4837-417d-b76f-771ec4d38b97", 
            "binding:vif_type": "vrouter", 
            "device_owner": "network:gw_interface", 
            "fake_delete": false, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "device_id": "b9618566-14ea-4505-8eae-8fdb4b6a0ec1", 
            "segmentation_type": "vlan", 
            "mac_address": "fa:16:3e:f8:45:26", 
            "tags": {}, 
            "name": "Port for : 8a4bbfe0-5aae-42f5-8b94-c4c14b9e7306"
        }
    }, 
    0
]
```

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:port:7abe783f-4837-417d-b76f-771ec4d38b97:1:ui963
[
    "monitoring_worker", 
    {
        "is_first": false, 
        "resource_id": "7abe783f-4837-417d-b76f-771ec4d38b97", 
        "handler": "monitoring_worker", 
        "job_name": "port:7abe783f-4837-417d-b76f-771ec4d38b97:1", 
        "dependency": [
            "create:heat_worker:port:7abe783f-4837-417d-b76f-771ec4d38b97:1:3gezy"
        ], 
        "version": 1, 
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
                    "resource_id": "7abe783f-4837-417d-b76f-771ec4d38b97"
                }, 
                "param": "vmi_fq_name"
            }, 
            {
                "resources": [], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "port", 
                    "resource_id": "7abe783f-4837-417d-b76f-771ec4d38b97"
                }, 
                "param": "vmi_uuid"
            }
        ], 
        "resource_type": "port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:port:7abe783f-4837-417d-b76f-771ec4d38b97:1:ui963", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "", 
            "allowed_address_pairs": [], 
            "admin_state_up": true, 
            "network_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
            "segmentation_id": 1025, 
            "fixed_ips": [
                {
                    "subnet_id": "a510f785-7758-4ce5-8fd4-c107d11b8e40", 
                    "ip_address": "172.16.101.153"
                }
            ], 
            "managed_by_service": true, 
            "attached": false, 
            "id": "7abe783f-4837-417d-b76f-771ec4d38b97", 
            "binding:vif_type": "vrouter", 
            "device_owner": "network:gw_interface", 
            "fake_delete": false, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "device_id": "b9618566-14ea-4505-8eae-8fdb4b6a0ec1", 
            "segmentation_type": "vlan", 
            "mac_address": "fa:16:3e:f8:45:26", 
            "tags": {}, 
            "name": "Port for : 8a4bbfe0-5aae-42f5-8b94-c4c14b9e7306"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/ports/7abe783f-4837-417d-b76f-771ec4d38b97
{
    "stack_id": "port_7abe783f-4837-417d-b76f-771ec4d38b97", 
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb", 
            "description": "Virtual network.", 
            "output_key": "virtual_network"
        }, 
        {
            "output_value": "default-domain:admin:7abe783f-4837-417d-b76f-771ec4d38b97", 
            "description": "Fully Qualified Name of the VMI", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "7abe783f-4837-417d-b76f-771ec4d38b97", 
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
    "status_reason": "Stack CREATE completed successfully", 
    "id": "port:7abe783f-4837-417d-b76f-771ec4d38b97"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/ports/7abe783f-4837-417d-b76f-771ec4d38b97
{
    "heat_outputs": [
        {
            "output_value": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb", 
            "description": "Virtual network.", 
            "output_key": "virtual_network"
        }, 
        {
            "output_value": "default-domain:admin:7abe783f-4837-417d-b76f-771ec4d38b97", 
            "description": "Fully Qualified Name of the VMI", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "7abe783f-4837-417d-b76f-771ec4d38b97", 
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
/esi-worker/job_state/v2.0/ports/7abe783f-4837-417d-b76f-771ec4d38b97
{
    "state_monitoring": {}, 
    "heat_outputs": [
        {
            "output_value": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb", 
            "description": "Virtual network.", 
            "output_key": "virtual_network"
        }, 
        {
            "output_value": "default-domain:admin:7abe783f-4837-417d-b76f-771ec4d38b97", 
            "description": "Fully Qualified Name of the VMI", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "7abe783f-4837-417d-b76f-771ec4d38b97", 
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
/state/v2.0/ports/7abe783f-4837-417d-b76f-771ec4d38b97
{
    "state": {
        "state_monitoring": "{}", 
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb\", \"description\": \"Virtual network.\", \"output_key\": \"virtual_network\"}, {\"output_value\": \"default-domain:admin:7abe783f-4837-417d-b76f-771ec4d38b97\", \"description\": \"Fully Qualified Name of the VMI\", \"output_key\": \"fq_name\"}, {\"output_value\": \"7abe783f-4837-417d-b76f-771ec4d38b97\", \"description\": \"A unique id for the virtual machine interface.\", \"output_key\": \"id\"}, {\"output_value\": \"null\", \"description\": \"Virtual machine allowed address pairs.\", \"output_key\": \"allowed_address_pairs\"}, {\"output_value\": \"xx:xx:xx:xx:xx:xx\", \"description\": \"Virtual machine interface mac address.\", \"output_key\": \"mac_address\"}]"
    }, 
    "version": 1, 
    "error": ""
}
```
