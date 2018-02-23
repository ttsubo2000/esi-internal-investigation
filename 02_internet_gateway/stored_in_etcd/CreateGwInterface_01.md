# Stored data in etcd: Create Gw Interface

These are stored data for "heat_templates" in etcd.

* gw_interface_internet
* gw_interface_monitoring

![scope](../../images/esi_interface.008.png)

These are stored data for "Create Gw Interface" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/gw_interfaces/b9618566-14ea-4505-8eae-8fdb4b6a0ec1
{
    "body": {
        "status": "PENDING_CREATE", 
        "secondary_ipv4": "172.16.101.153", 
        "gw_vipv4": "172.16.101.151", 
        "description": "Sample Gw-interface", 
        "network_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "internet_gw_id": "429e24b5-a2f0-4fb8-b467-e335857e9476", 
        "vrid": 20, 
        "primary_ipv4": "172.16.101.152", 
        "netmask": 24, 
        "service_type": "internet", 
        "id": "b9618566-14ea-4505-8eae-8fdb4b6a0ec1", 
        "name": "sample-gw-interface"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:gw_interface:b9618566-14ea-4505-8eae-8fdb4b6a0ec1:1:ihknd
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "b9618566-14ea-4505-8eae-8fdb4b6a0ec1", 
        "handler": "heat_worker", 
        "job_name": "gw_interface:b9618566-14ea-4505-8eae-8fdb4b6a0ec1:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
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
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
                    {
                        "resource_type": "internet_service", 
                        "resource_id": "848e04de-733d-4f98-8971-bdb3b83e0296"
                    }
                ], 
                "type": "value", 
                "value": "InetGW1-RI-IBGP", 
                "param": "secondary_ibgp_config_group"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
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
                "resources": [], 
                "type": "value", 
                "value": "172.16.101.153", 
                "param": "secondary_device_gw_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "inet-gw-group", 
                "param": "bgp_group_name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "172.16.101.151", 
                "param": "gw_vip"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
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
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
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
                "resources": [], 
                "type": "value", 
                "value": "", 
                "param": "jinja_dummy_dependency"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }
                ], 
                "type": "value", 
                "value": "1025", 
                "param": "vlan"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
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
                "resources": [], 
                "type": "value", 
                "value": 24, 
                "param": "netmask"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "172.16.101.152", 
                "param": "primary_device_gw_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": 20, 
                "param": "vrrp_group"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "105", 
                "param": "primary_device_priority"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "network", 
                        "resource_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0"
                    }
                ], 
                "type": "value", 
                "value": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
                "param": "jinja_force_dependency"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
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
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
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
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }
                ], 
                "type": "value", 
                "value": "vrf_gw_sample-ha-router-downlink_1025", 
                "param": "vrf_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
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
                "value": "100", 
                "param": "secondary_device_priority"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
                    {
                        "resource_type": "internet_service", 
                        "resource_id": "848e04de-733d-4f98-8971-bdb3b83e0296"
                    }
                ], 
                "type": "value", 
                "value": "InetGW2-RI-IBGP", 
                "param": "primary_ibgp_config_group"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
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
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
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
        "resource_type": "gw_interface", 
        "action": "create", 
        "is_last": false, 
        "on_failure": "fail", 
        "id": "create:heat_worker:gw_interface:b9618566-14ea-4505-8eae-8fdb4b6a0ec1:1:ihknd", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "secondary_ipv4": "172.16.101.153", 
            "gw_vipv4": "172.16.101.151", 
            "description": "Sample Gw-interface", 
            "network_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "internet_gw_id": "429e24b5-a2f0-4fb8-b467-e335857e9476", 
            "vrid": 20, 
            "primary_ipv4": "172.16.101.152", 
            "netmask": 24, 
            "service_type": "internet", 
            "id": "b9618566-14ea-4505-8eae-8fdb4b6a0ec1", 
            "name": "sample-gw-interface"
        }
    }, 
    0
]
```

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:gw_interface:b9618566-14ea-4505-8eae-8fdb4b6a0ec1:1:zn1cr
[
    "monitoring_worker", 
    {
        "is_first": false, 
        "resource_id": "b9618566-14ea-4505-8eae-8fdb4b6a0ec1", 
        "handler": "monitoring_worker", 
        "job_name": "gw_interface:b9618566-14ea-4505-8eae-8fdb4b6a0ec1:1", 
        "dependency": [
            "create:heat_worker:gw_interface:b9618566-14ea-4505-8eae-8fdb4b6a0ec1:1:ihknd"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
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
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }
                ], 
                "type": "value", 
                "value": "ae0.1025", 
                "param": "secondary_logical_interface_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }
                ], 
                "type": "value", 
                "value": "ae0.1025", 
                "param": "primary_logical_interface_name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": 20, 
                "param": "vrid"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
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
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
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
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
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
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
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
                "param": "secondary_device_login"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "internet", 
                "param": "service_type"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
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
                "param": "primary_device_login"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
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
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
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
        "resource_type": "gw_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:gw_interface:b9618566-14ea-4505-8eae-8fdb4b6a0ec1:1:zn1cr", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "secondary_ipv4": "172.16.101.153", 
            "gw_vipv4": "172.16.101.151", 
            "description": "Sample Gw-interface", 
            "network_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "internet_gw_id": "429e24b5-a2f0-4fb8-b467-e335857e9476", 
            "vrid": 20, 
            "primary_ipv4": "172.16.101.152", 
            "netmask": 24, 
            "service_type": "internet", 
            "id": "b9618566-14ea-4505-8eae-8fdb4b6a0ec1", 
            "name": "sample-gw-interface"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/gw_interfaces/b9618566-14ea-4505-8eae-8fdb4b6a0ec1
{
    "stack_id": "gw_interface_b9618566-14ea-4505-8eae-8fdb4b6a0ec1", 
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "gw_interface:b9618566-14ea-4505-8eae-8fdb4b6a0ec1"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/gw_interfaces/b9618566-14ea-4505-8eae-8fdb4b6a0ec1
{
    "heat_outputs": []
}
```

### Checking stored data at the point of (5) in etcd

```
/esi-worker/job_state/v2.0/gw_interfaces/b9618566-14ea-4505-8eae-8fdb4b6a0ec1
{
    "state_monitoring": {
        "primary": "master", 
        "secondary": "backup"
    }, 
    "heat_outputs": []
}
```

### Checking stored data at the point of (6) in etcd

```
/state/v2.0/gw_interfaces/b9618566-14ea-4505-8eae-8fdb4b6a0ec1
{
    "state": {
        "state_monitoring": "{\"primary\": \"master\", \"secondary\": \"backup\"}", 
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[]"
    }, 
    "version": 1, 
    "error": ""
}
```

### Checking stored data at the point of (7) in etcd

```
/monitoring/v2.0/gw_interfaces/b9618566-14ea-4505-8eae-8fdb4b6a0ec1
{
    "version": 1, 
    "primary": "MASTER", 
    "secondary": "BACKUP"
}
```
