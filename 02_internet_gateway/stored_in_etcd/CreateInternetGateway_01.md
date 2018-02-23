# Stored data in etcd: Create Internet Gateway

These are stored data for "heat_templates" in etcd.

* internet_gateway
* internet_gateway_monitoring

![scope](../../images/esi_interface.008.png)

These are stored data for "Create Internet Gateway" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/internet_gateways/429e24b5-a2f0-4fb8-b467-e335857e9476
{
    "body": {
        "status": "PENDING_CREATE", 
        "secondary_logical_interface_name": "ae0.1025", 
        "name": "sample-internet-gateway", 
        "primary_logical_interface_name": "ae0.1025", 
        "downlink_interface_id": "1205d3f2-7568-412a-a554-012340ab3172", 
        "internet_service_id": "848e04de-733d-4f98-8971-bdb3b83e0296", 
        "qos_option_id": "e25f6309-c384-446e-bdc1-5241cb14890b", 
        "vrf_name": "vrf_gw_sample-ha-router-downlink_1025", 
        "maximum_static_routes": 32, 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "id": "429e24b5-a2f0-4fb8-b467-e335857e9476", 
        "vlan_id": "1025", 
        "description": "Sample Internet-gateway"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:internet_gateway:429e24b5-a2f0-4fb8-b467-e335857e9476:1:gt36x
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476", 
        "handler": "heat_worker", 
        "job_name": "internet_gateway:429e24b5-a2f0-4fb8-b467-e335857e9476:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "internet_service", 
                        "resource_id": "848e04de-733d-4f98-8971-bdb3b83e0296"
                    }
                ], 
                "type": "value", 
                "value": "INSTANCE-USER_OUT", 
                "param": "vrf_export_policy"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "469e4283-80e6-491c-830f-c483c1f7c695"
                    }
                ], 
                "type": "value", 
                "value": "ae0", 
                "param": "secondary_device_physical_interface"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "ae0.1025", 
                "param": "primary_device_logical_interface"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "9b82b55a-551e-4069-ae77-c972e30ab0cc"
                    }
                ], 
                "type": "value", 
                "value": "esiesi0000", 
                "param": "primary_device_password"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_service", 
                        "resource_id": "848e04de-733d-4f98-8971-bdb3b83e0296"
                    }
                ], 
                "type": "value", 
                "value": "INSTANCE-USER_IN", 
                "param": "vrf_import_policy"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "vrf_gw_sample-ha-router-downlink_1025_prefix", 
                "param": "prefix_list_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_service", 
                        "resource_id": "848e04de-733d-4f98-8971-bdb3b83e0296"
                    }
                ], 
                "type": "value", 
                "value": "", 
                "param": "jinja_vrf_config"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "qos_option", 
                        "resource_id": "e25f6309-c384-446e-bdc1-5241cb14890b"
                    }
                ], 
                "type": "value", 
                "value": "FILTER_10M-GA-DOWN-INET", 
                "param": "output_filter_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_service", 
                        "resource_id": "848e04de-733d-4f98-8971-bdb3b83e0296"
                    }
                ], 
                "type": "value", 
                "value": "InetGW2-VRRP", 
                "param": "secondary_vrrp_config_group"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "9b82b55a-551e-4069-ae77-c972e30ab0cc"
                    }
                ], 
                "type": "value", 
                "value": "10.79.5.185", 
                "param": "primary_device_ip"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_service", 
                        "resource_id": "848e04de-733d-4f98-8971-bdb3b83e0296"
                    }
                ], 
                "type": "value", 
                "value": "INET_IN", 
                "param": "inet_in_filter"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "9b82b55a-551e-4069-ae77-c972e30ab0cc"
                    }
                ], 
                "type": "value", 
                "value": "esi", 
                "param": "primary_device_username"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "ae0.1025", 
                "param": "secondary_device_logical_interface"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_service", 
                        "resource_id": "848e04de-733d-4f98-8971-bdb3b83e0296"
                    }
                ], 
                "type": "value", 
                "value": "INET_OUT", 
                "param": "inet_out_filter"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "1025", 
                "param": "vlan"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "1fda2a88-f7e9-4982-9ce2-d65c9611aae7"
                    }
                ], 
                "type": "value", 
                "value": "ae0", 
                "param": "primary_device_physical_interface"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_service", 
                        "resource_id": "848e04de-733d-4f98-8971-bdb3b83e0296"
                    }
                ], 
                "type": "value", 
                "value": "INSTANCE-MASTER_IN", 
                "param": "uplink_import_policy"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "qos_option", 
                        "resource_id": "e25f6309-c384-446e-bdc1-5241cb14890b"
                    }
                ], 
                "type": "value", 
                "value": "FILTER_10M-GA-UP-INET", 
                "param": "input_filter_name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "vrf_gw_sample-ha-router-downlink_1025_filter", 
                "param": "filter_term_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "198b93f2-006e-45b6-96d3-e7ef6f759501"
                    }
                ], 
                "type": "value", 
                "value": 830, 
                "param": "secondary_device_port"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "198b93f2-006e-45b6-96d3-e7ef6f759501"
                    }
                ], 
                "type": "value", 
                "value": "esiesi0000", 
                "param": "secondary_device_password"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "60", 
                "param": "heat_timeout"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "vrf_gw_sample-ha-router-downlink_1025", 
                "param": "vrf_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_service", 
                        "resource_id": "848e04de-733d-4f98-8971-bdb3b83e0296"
                    }
                ], 
                "type": "value", 
                "value": "InetGW1-VRRP", 
                "param": "primary_vrrp_config_group"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "198b93f2-006e-45b6-96d3-e7ef6f759501"
                    }
                ], 
                "type": "value", 
                "value": "esi", 
                "param": "secondary_device_username"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "9b82b55a-551e-4069-ae77-c972e30ab0cc"
                    }
                ], 
                "type": "value", 
                "value": 830, 
                "param": "primary_device_port"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "198b93f2-006e-45b6-96d3-e7ef6f759501"
                    }
                ], 
                "type": "value", 
                "value": "10.79.5.184", 
                "param": "secondary_device_ip"
            }
        ], 
        "resource_type": "internet_gateway", 
        "action": "create", 
        "is_last": false, 
        "on_failure": "fail", 
        "id": "create:heat_worker:internet_gateway:429e24b5-a2f0-4fb8-b467-e335857e9476:1:gt36x", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "secondary_logical_interface_name": "ae0.1025", 
            "name": "sample-internet-gateway", 
            "primary_logical_interface_name": "ae0.1025", 
            "downlink_interface_id": "1205d3f2-7568-412a-a554-012340ab3172", 
            "internet_service_id": "848e04de-733d-4f98-8971-bdb3b83e0296", 
            "qos_option_id": "e25f6309-c384-446e-bdc1-5241cb14890b", 
            "vrf_name": "vrf_gw_sample-ha-router-downlink_1025", 
            "maximum_static_routes": 32, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "id": "429e24b5-a2f0-4fb8-b467-e335857e9476", 
            "vlan_id": "1025", 
            "description": "Sample Internet-gateway"
        }
    }, 
    0
]
```

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:internet_gateway:429e24b5-a2f0-4fb8-b467-e335857e9476:1:fmke3
[
    "monitoring_worker", 
    {
        "is_first": false, 
        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476", 
        "handler": "monitoring_worker", 
        "job_name": "internet_gateway:429e24b5-a2f0-4fb8-b467-e335857e9476:1", 
        "dependency": [
            "create:heat_worker:internet_gateway:429e24b5-a2f0-4fb8-b467-e335857e9476:1:gt36x"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "9b82b55a-551e-4069-ae77-c972e30ab0cc"
                    }
                ], 
                "type": "value", 
                "value": "esi", 
                "param": "username"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "9b82b55a-551e-4069-ae77-c972e30ab0cc"
                    }
                ], 
                "type": "value", 
                "value": "esiesi0000", 
                "param": "password"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "vrf_gw_sample-ha-router-downlink_1025_OUT", 
                "param": "counter_name_out_secondary"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_service", 
                        "resource_id": "848e04de-733d-4f98-8971-bdb3b83e0296"
                    }
                ], 
                "type": "value", 
                "value": "INET_OUT", 
                "param": "inet_out_filter"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "9b82b55a-551e-4069-ae77-c972e30ab0cc"
                    }
                ], 
                "type": "value", 
                "value": 830, 
                "param": "ssh_port"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }
                ], 
                "type": "value", 
                "value": "1205d3f2-7568-412a-a554-012340ab3172", 
                "param": "downlink_interface_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "9b82b55a-551e-4069-ae77-c972e30ab0cc"
                    }
                ], 
                "type": "value", 
                "value": "10.79.5.185", 
                "param": "primary_server_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "vrf_gw_sample-ha-router-downlink_1025_IN", 
                "param": "counter_name_in_secondary"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "vrf_gw_sample-ha-router-downlink_1025_IN", 
                "param": "counter_name_in_primary"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "198b93f2-006e-45b6-96d3-e7ef6f759501"
                    }
                ], 
                "type": "value", 
                "value": "10.79.5.184", 
                "param": "secondary_server_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": null, 
                "param": "uplink_interface_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_service", 
                        "resource_id": "848e04de-733d-4f98-8971-bdb3b83e0296"
                    }
                ], 
                "type": "value", 
                "value": "INET_IN", 
                "param": "inet_in_filter"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "vrf_gw_sample-ha-router-downlink_1025_OUT", 
                "param": "counter_name_out_primary"
            }
        ], 
        "resource_type": "internet_gateway", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:internet_gateway:429e24b5-a2f0-4fb8-b467-e335857e9476:1:fmke3", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "secondary_logical_interface_name": "ae0.1025", 
            "name": "sample-internet-gateway", 
            "primary_logical_interface_name": "ae0.1025", 
            "downlink_interface_id": "1205d3f2-7568-412a-a554-012340ab3172", 
            "internet_service_id": "848e04de-733d-4f98-8971-bdb3b83e0296", 
            "qos_option_id": "e25f6309-c384-446e-bdc1-5241cb14890b", 
            "vrf_name": "vrf_gw_sample-ha-router-downlink_1025", 
            "maximum_static_routes": 32, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "id": "429e24b5-a2f0-4fb8-b467-e335857e9476", 
            "vlan_id": "1025", 
            "description": "Sample Internet-gateway"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/internet_gateways/429e24b5-a2f0-4fb8-b467-e335857e9476
{
    "stack_id": "internet_gateway_429e24b5-a2f0-4fb8-b467-e335857e9476", 
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "internet_gateway:429e24b5-a2f0-4fb8-b467-e335857e9476"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/internet_gateways/429e24b5-a2f0-4fb8-b467-e335857e9476
{
    "heat_outputs": []
}
```

### Checking stored data at the point of (5) in etcd

```
/esi-worker/job_state/v2.0/internet_gateways/429e24b5-a2f0-4fb8-b467-e335857e9476
{
    "state_monitoring": {
        "downlink": "ACTIVE", 
        "uplink": "ACTIVE"
    }, 
    "heat_outputs": []
}
```

### Checking stored data at the point of (6) in etcd

```
/state/v2.0/internet_gateways/429e24b5-a2f0-4fb8-b467-e335857e9476
{
    "state": {
        "state_monitoring": "{\"downlink\": \"ACTIVE\", \"uplink\": \"ACTIVE\"}", 
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[]"
    }, 
    "version": 1, 
    "error": ""
}
```
