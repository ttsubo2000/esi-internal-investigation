# Stored data in etcd: Create Vpn Gateway

These are stored data for "heat_templates" in etcd.

* vpn_gateway
* vpn_gateway_monitoring

![scope](../../images/esi_interface.008.png)

These are stored data for "Create Vpn Gateway" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/vpn_gateways/4fab887d-8f73-40e6-b2d8-2426255231bf
{
    "body": {
        "downlink_vlan_id": "1025", 
        "status": "PENDING_CREATE", 
        "vpn_service_id": "72b05fe5-88c6-4888-a6fb-feb793fffae8", 
        "description": "this resource is vpn-gateway", 
        "secondary_logical_downlink_interface_name": "ae0.1025", 
        "downlink_interface_id": "a3a62a37-5657-4822-98e0-991ab63f0e96", 
        "qos_option_id": "4f59680b-52b6-41da-b15a-09946c155efd", 
        "name": "sample-vpn-gateway", 
        "uplink_vlan_id": "122", 
        "primary_logical_downlink_interface_name": "ae0.1025", 
        "local_as_number": "65101", 
        "uplink_interface_id": "5e552b8f-cd5a-454c-a224-33f7da0afa24", 
        "maximum_static_routes": 32, 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "secondary_logical_uplink_interface_name": "ge-0/0/1.122", 
        "primary_logical_uplink_interface_name": "ge-0/0/1.122", 
        "vrf_name": "vrf_gw_sample-ha-router-downlink_1025", 
        "id": "4fab887d-8f73-40e6-b2d8-2426255231bf", 
        "connected_vpn_interface": ""
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:vpn_gateway:4fab887d-8f73-40e6-b2d8-2426255231bf:1:6zudv
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf", 
        "handler": "heat_worker", 
        "job_name": "vpn_gateway:4fab887d-8f73-40e6-b2d8-2426255231bf:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "ge-0/0/1.122", 
                "param": "primary_device_logical_uplink_interface"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "ae0.1025", 
                "param": "primary_device_logical_downlink_interface"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "a3a62a37-5657-4822-98e0-991ab63f0e96"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "f01ed0a6-7094-4e54-b14b-94657fff1efb"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "792c7a6d-19b5-4d6f-b9f6-1e5b1eb45198"
                    }
                ], 
                "type": "value", 
                "value": "esiesi0000", 
                "param": "primary_device_password"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "qos_option", 
                        "resource_id": "4f59680b-52b6-41da-b15a-09946c155efd"
                    }
                ], 
                "type": "value", 
                "value": "FILTER_10M-GA-DOWN-VPN", 
                "param": "output_filter_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "a3a62a37-5657-4822-98e0-991ab63f0e96"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "f01ed0a6-7094-4e54-b14b-94657fff1efb"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "792c7a6d-19b5-4d6f-b9f6-1e5b1eb45198"
                    }
                ], 
                "type": "value", 
                "value": "10.79.5.185", 
                "param": "primary_device_ip"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "a3a62a37-5657-4822-98e0-991ab63f0e96"
                    }, 
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "6b160a8d-fdad-4fe7-aaed-3ff5f729d6c8"
                    }
                ], 
                "type": "value", 
                "value": "ae0", 
                "param": "secondary_device_physical_downlink_interface"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "a3a62a37-5657-4822-98e0-991ab63f0e96"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "f01ed0a6-7094-4e54-b14b-94657fff1efb"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "3ca3a59a-4f92-4a8a-9ec1-1c55a97c794e"
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
                        "resource_id": "5e552b8f-cd5a-454c-a224-33f7da0afa24"
                    }, 
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "6e8f473f-47ec-4b54-8f0f-d459d440393b"
                    }
                ], 
                "type": "value", 
                "value": "ge-0/0/1", 
                "param": "primary_device_physical_uplink_interface"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "ge-0/0/1.122", 
                "param": "secondary_device_logical_uplink_interface"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "1025", 
                "param": "downlink_vlan"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "ae0.1025", 
                "param": "secondary_device_logical_downlink_interface"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "qos_option", 
                        "resource_id": "4f59680b-52b6-41da-b15a-09946c155efd"
                    }
                ], 
                "type": "value", 
                "value": "FILTER_10M-GA-UP-VPN", 
                "param": "input_filter_name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "122", 
                "param": "uplink_vlan"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "a3a62a37-5657-4822-98e0-991ab63f0e96"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "f01ed0a6-7094-4e54-b14b-94657fff1efb"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "3ca3a59a-4f92-4a8a-9ec1-1c55a97c794e"
                    }
                ], 
                "type": "value", 
                "value": 830, 
                "param": "secondary_device_port"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vpn_service", 
                        "resource_id": "72b05fe5-88c6-4888-a6fb-feb793fffae8"
                    }
                ], 
                "type": "value", 
                "value": "VPNGW1-VRRP", 
                "param": "primary_downlink_vrrp_config_group"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "a3a62a37-5657-4822-98e0-991ab63f0e96"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "f01ed0a6-7094-4e54-b14b-94657fff1efb"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "3ca3a59a-4f92-4a8a-9ec1-1c55a97c794e"
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
                        "resource_type": "ha_interface", 
                        "resource_id": "a3a62a37-5657-4822-98e0-991ab63f0e96"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "f01ed0a6-7094-4e54-b14b-94657fff1efb"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "792c7a6d-19b5-4d6f-b9f6-1e5b1eb45198"
                    }
                ], 
                "type": "value", 
                "value": "esi", 
                "param": "primary_device_username"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "a3a62a37-5657-4822-98e0-991ab63f0e96"
                    }, 
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "8ff57ce4-55f9-40d4-82ed-1f00c9051678"
                    }
                ], 
                "type": "value", 
                "value": "ae0", 
                "param": "primary_device_physical_downlink_interface"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vpn_service", 
                        "resource_id": "72b05fe5-88c6-4888-a6fb-feb793fffae8"
                    }
                ], 
                "type": "value", 
                "value": "VPNGW2-VRRP", 
                "param": "secondary_downlink_vrrp_config_group"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "a3a62a37-5657-4822-98e0-991ab63f0e96"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "f01ed0a6-7094-4e54-b14b-94657fff1efb"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "792c7a6d-19b5-4d6f-b9f6-1e5b1eb45198"
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
                        "resource_id": "5e552b8f-cd5a-454c-a224-33f7da0afa24"
                    }, 
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "f87c6efe-f590-4c29-8fc9-2f914e1eb362"
                    }
                ], 
                "type": "value", 
                "value": "ge-0/0/1", 
                "param": "secondary_device_physical_uplink_interface"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "a3a62a37-5657-4822-98e0-991ab63f0e96"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "f01ed0a6-7094-4e54-b14b-94657fff1efb"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "3ca3a59a-4f92-4a8a-9ec1-1c55a97c794e"
                    }
                ], 
                "type": "value", 
                "value": "10.79.5.184", 
                "param": "secondary_device_ip"
            }
        ], 
        "resource_type": "vpn_gateway", 
        "action": "create", 
        "is_last": false, 
        "on_failure": "fail", 
        "id": "create:heat_worker:vpn_gateway:4fab887d-8f73-40e6-b2d8-2426255231bf:1:6zudv", 
        "resource_input": {
            "downlink_vlan_id": "1025", 
            "status": "PENDING_CREATE", 
            "vpn_service_id": "72b05fe5-88c6-4888-a6fb-feb793fffae8", 
            "description": "this resource is vpn-gateway", 
            "maximum_static_routes": 32, 
            "secondary_logical_downlink_interface_name": "ae0.1025", 
            "downlink_interface_id": "a3a62a37-5657-4822-98e0-991ab63f0e96", 
            "qos_option_id": "4f59680b-52b6-41da-b15a-09946c155efd", 
            "secondary_logical_uplink_interface_name": "ge-0/0/1.122", 
            "uplink_vlan_id": "122", 
            "primary_logical_downlink_interface_name": "ae0.1025", 
            "local_as_number": "65101", 
            "vrf_name": "vrf_gw_sample-ha-router-downlink_1025", 
            "uplink_interface_id": "5e552b8f-cd5a-454c-a224-33f7da0afa24", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "primary_logical_uplink_interface_name": "ge-0/0/1.122", 
            "connected_vpn_interface": "", 
            "id": "4fab887d-8f73-40e6-b2d8-2426255231bf", 
            "name": "sample-vpn-gateway"
        }
    }, 
    0
]
```

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:vpn_gateway:4fab887d-8f73-40e6-b2d8-2426255231bf:1:hps74
[
    "monitoring_worker", 
    {
        "is_first": false, 
        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf", 
        "handler": "monitoring_worker", 
        "job_name": "vpn_gateway:4fab887d-8f73-40e6-b2d8-2426255231bf:1", 
        "dependency": [
            "create:heat_worker:vpn_gateway:4fab887d-8f73-40e6-b2d8-2426255231bf:1:6zudv"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "a3a62a37-5657-4822-98e0-991ab63f0e96"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "f01ed0a6-7094-4e54-b14b-94657fff1efb"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "792c7a6d-19b5-4d6f-b9f6-1e5b1eb45198"
                    }
                ], 
                "type": "value", 
                "value": "10.79.5.185", 
                "param": "primary_device_ip"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "a3a62a37-5657-4822-98e0-991ab63f0e96"
                    }
                ], 
                "type": "value", 
                "value": "a3a62a37-5657-4822-98e0-991ab63f0e96", 
                "param": "downlink_interface_id"
            }
        ], 
        "resource_type": "vpn_gateway", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:vpn_gateway:4fab887d-8f73-40e6-b2d8-2426255231bf:1:hps74", 
        "resource_input": {
            "downlink_vlan_id": "1025", 
            "status": "PENDING_CREATE", 
            "vpn_service_id": "72b05fe5-88c6-4888-a6fb-feb793fffae8", 
            "description": "this resource is vpn-gateway", 
            "maximum_static_routes": 32, 
            "secondary_logical_downlink_interface_name": "ae0.1025", 
            "downlink_interface_id": "a3a62a37-5657-4822-98e0-991ab63f0e96", 
            "qos_option_id": "4f59680b-52b6-41da-b15a-09946c155efd", 
            "secondary_logical_uplink_interface_name": "ge-0/0/1.122", 
            "uplink_vlan_id": "122", 
            "primary_logical_downlink_interface_name": "ae0.1025", 
            "local_as_number": "65101", 
            "vrf_name": "vrf_gw_sample-ha-router-downlink_1025", 
            "uplink_interface_id": "5e552b8f-cd5a-454c-a224-33f7da0afa24", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "primary_logical_uplink_interface_name": "ge-0/0/1.122", 
            "connected_vpn_interface": "", 
            "id": "4fab887d-8f73-40e6-b2d8-2426255231bf", 
            "name": "sample-vpn-gateway"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/vpn_gateways/4fab887d-8f73-40e6-b2d8-2426255231bf
{
    "stack_id": "vpn_gateway_4fab887d-8f73-40e6-b2d8-2426255231bf", 
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "vpn_gateway:4fab887d-8f73-40e6-b2d8-2426255231bf"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/vpn_gateways/4fab887d-8f73-40e6-b2d8-2426255231bf
{
    "heat_outputs": []
}
```

### Checking stored data at the point of (5) in etcd

```
/esi-worker/job_state/v2.0/vpn_gateways/4fab887d-8f73-40e6-b2d8-2426255231bf
{
    "state_monitoring": {
        "downlink": "ACTIVE"
    }, 
    "heat_outputs": []
}
```

### Checking stored data at the point of (6) in etcd

```
/state/v2.0/vpn_gateways/4fab887d-8f73-40e6-b2d8-2426255231bf
{
    "state": {
        "state_monitoring": "{\"downlink\": \"ACTIVE\"}", 
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[]"
    }, 
    "version": 1, 
    "error": ""
}
```
