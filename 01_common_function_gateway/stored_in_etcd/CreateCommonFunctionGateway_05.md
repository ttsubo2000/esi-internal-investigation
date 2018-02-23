# Stored data in etcd: Create Common Function Gateway

These are stored data for "heat_templates" in etcd.

* port
* port_monitoring

![scope](../../images/esi_interface.008.png)

These are stored data for "Create Common Function Gateway" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ports/327f59b7-df38-4d8f-97db-d320defcab76
{
    "body": {
        "status": "PENDING_CREATE", 
        "description": "", 
        "allowed_address_pairs": [], 
        "admin_state_up": true, 
        "network_id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
        "segmentation_id": 1025, 
        "managed_by_service": true, 
        "attached": false, 
        "segmentation_type": "vlan", 
        "name": "common_function_gw_5c241c51-2003-407a-a239-689fabd19022_primary_port:976156ef-05b4-47f4-9497-a36531563a08", 
        "binding:vif_type": "vrouter", 
        "device_owner": "network:common_function_gateway", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "fake_delete": false, 
        "mac_address": "fa:16:3e:e5:f6:39", 
        "fixed_ips": [
            {
                "subnet_id": "e1353d56-b05a-43a9-b924-383ab0d64d7b", 
                "ip_address": "169.254.0.3"
            }
        ], 
        "id": "327f59b7-df38-4d8f-97db-d320defcab76", 
        "tags": {}, 
        "device_id": "5c241c51-2003-407a-a239-689fabd19022"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:port:327f59b7-df38-4d8f-97db-d320defcab76:1:jog8i
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "327f59b7-df38-4d8f-97db-d320defcab76", 
        "handler": "heat_worker", 
        "job_name": "port:327f59b7-df38-4d8f-97db-d320defcab76:1", 
        "dependency": [
            "create:heat_worker:subnet:e1353d56-b05a-43a9-b924-383ab0d64d7b:1:junpn", 
            "create:heat_worker:network:f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57:1:7vfno"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "network", 
                        "resource_id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57"
                }, 
                "param": "virtual_network"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "5c241c51-2003-407a-a239-689fabd19022", 
                "param": "virtual_machine"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "327f59b7-df38-4d8f-97db-d320defcab76", 
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
                "value": "fa:16:3e:e5:f6:39", 
                "param": "virtual_machine_interface_mac_address"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "network:common_function_gateway", 
                "param": "device_owner"
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
                        "subnet_id": "e1353d56-b05a-43a9-b924-383ab0d64d7b", 
                        "ip_address": "169.254.0.3"
                    }
                ], 
                "param": "jinja_fixed_ips"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "", 
                "param": "jinja_force_dependency_cfg"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "subnet", 
                        "resource_id": "e1353d56-b05a-43a9-b924-383ab0d64d7b"
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
                            "resource_id": "e1353d56-b05a-43a9-b924-383ab0d64d7b"
                        }, 
                        "resources": []
                    }
                ], 
                "param": "jinja_subnets"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "327f59b7-df38-4d8f-97db-d320defcab76", 
                "param": "uuid"
            }
        ], 
        "resource_type": "port", 
        "action": "create", 
        "is_last": false, 
        "on_failure": "fail", 
        "id": "create:heat_worker:port:327f59b7-df38-4d8f-97db-d320defcab76:1:jog8i", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "", 
            "allowed_address_pairs": [], 
            "admin_state_up": true, 
            "network_id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
            "segmentation_id": 1025, 
            "fixed_ips": [
                {
                    "subnet_id": "e1353d56-b05a-43a9-b924-383ab0d64d7b", 
                    "ip_address": "169.254.0.3"
                }
            ], 
            "managed_by_service": true, 
            "attached": false, 
            "id": "327f59b7-df38-4d8f-97db-d320defcab76", 
            "binding:vif_type": "vrouter", 
            "device_owner": "network:common_function_gateway", 
            "fake_delete": false, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "device_id": "5c241c51-2003-407a-a239-689fabd19022", 
            "segmentation_type": "vlan", 
            "mac_address": "fa:16:3e:e5:f6:39", 
            "tags": {}, 
            "name": "common_function_gw_5c241c51-2003-407a-a239-689fabd19022_primary_port:976156ef-05b4-47f4-9497-a36531563a08"
        }
    }, 
    0
]
```

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:port:327f59b7-df38-4d8f-97db-d320defcab76:1:daz1w
[
    "monitoring_worker", 
    {
        "is_first": false, 
        "resource_id": "327f59b7-df38-4d8f-97db-d320defcab76", 
        "handler": "monitoring_worker", 
        "job_name": "port:327f59b7-df38-4d8f-97db-d320defcab76:1", 
        "dependency": [
            "create:heat_worker:port:327f59b7-df38-4d8f-97db-d320defcab76:1:jog8i"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "network:common_function_gateway", 
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
                    "resource_id": "327f59b7-df38-4d8f-97db-d320defcab76"
                }, 
                "param": "vmi_fq_name"
            }, 
            {
                "resources": [], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "port", 
                    "resource_id": "327f59b7-df38-4d8f-97db-d320defcab76"
                }, 
                "param": "vmi_uuid"
            }
        ], 
        "resource_type": "port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:port:327f59b7-df38-4d8f-97db-d320defcab76:1:daz1w", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "", 
            "allowed_address_pairs": [], 
            "admin_state_up": true, 
            "network_id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
            "segmentation_id": 1025, 
            "fixed_ips": [
                {
                    "subnet_id": "e1353d56-b05a-43a9-b924-383ab0d64d7b", 
                    "ip_address": "169.254.0.3"
                }
            ], 
            "managed_by_service": true, 
            "attached": false, 
            "id": "327f59b7-df38-4d8f-97db-d320defcab76", 
            "binding:vif_type": "vrouter", 
            "device_owner": "network:common_function_gateway", 
            "fake_delete": false, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "device_id": "5c241c51-2003-407a-a239-689fabd19022", 
            "segmentation_type": "vlan", 
            "mac_address": "fa:16:3e:e5:f6:39", 
            "tags": {}, 
            "name": "common_function_gw_5c241c51-2003-407a-a239-689fabd19022_primary_port:976156ef-05b4-47f4-9497-a36531563a08"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/ports/327f59b7-df38-4d8f-97db-d320defcab76
{
    "stack_id": "port_327f59b7-df38-4d8f-97db-d320defcab76", 
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb", 
            "description": "Virtual network.", 
            "output_key": "virtual_network"
        }, 
        {
            "output_value": "default-domain:admin:327f59b7-df38-4d8f-97db-d320defcab76", 
            "description": "Fully Qualified Name of the VMI", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "327f59b7-df38-4d8f-97db-d320defcab76", 
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
    "id": "port:327f59b7-df38-4d8f-97db-d320defcab76"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/ports/327f59b7-df38-4d8f-97db-d320defcab76
{
    "heat_outputs": [
        {
            "output_value": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb", 
            "description": "Virtual network.", 
            "output_key": "virtual_network"
        }, 
        {
            "output_value": "default-domain:admin:327f59b7-df38-4d8f-97db-d320defcab76", 
            "description": "Fully Qualified Name of the VMI", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "327f59b7-df38-4d8f-97db-d320defcab76", 
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
/esi-worker/job_state/v2.0/ports/327f59b7-df38-4d8f-97db-d320defcab76
{
    "state_monitoring": {}, 
    "heat_outputs": [
        {
            "output_value": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb", 
            "description": "Virtual network.", 
            "output_key": "virtual_network"
        }, 
        {
            "output_value": "default-domain:admin:327f59b7-df38-4d8f-97db-d320defcab76", 
            "description": "Fully Qualified Name of the VMI", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "327f59b7-df38-4d8f-97db-d320defcab76", 
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
/state/v2.0/ports/327f59b7-df38-4d8f-97db-d320defcab76
{
    "state": {
        "state_monitoring": "{}", 
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb\", \"description\": \"Virtual network.\", \"output_key\": \"virtual_network\"}, {\"output_value\": \"default-domain:admin:327f59b7-df38-4d8f-97db-d320defcab76\", \"description\": \"Fully Qualified Name of the VMI\", \"output_key\": \"fq_name\"}, {\"output_value\": \"327f59b7-df38-4d8f-97db-d320defcab76\", \"description\": \"A unique id for the virtual machine interface.\", \"output_key\": \"id\"}, {\"output_value\": \"null\", \"description\": \"Virtual machine allowed address pairs.\", \"output_key\": \"allowed_address_pairs\"}, {\"output_value\": \"xx:xx:xx:xx:xx:xx\", \"description\": \"Virtual machine interface mac address.\", \"output_key\": \"mac_address\"}]"
    }, 
    "version": 1, 
    "error": ""
}
```
