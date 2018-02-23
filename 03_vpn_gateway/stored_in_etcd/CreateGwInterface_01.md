# Stored data in etcd: Create Gw Interface

These are stored data for "heat_templates" in etcd.

* gw_interface_vpn
* gw_interface_monitoring

![scope](../../images/esi_interface.008.png)

These are stored data for "Create Gw Interface" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/gw_interfaces/fbd7d07e-9e84-4ad7-ab85-36d46adb9435
{
    "body": {
        "status": "PENDING_CREATE", 
        "secondary_ipv4": "172.16.101.153", 
        "gw_vipv4": "172.16.101.151", 
        "description": "Sample Gw-interface", 
        "network_id": "bb69041d-c654-4e9f-a763-afd4333275bc", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "vpn_gw_id": "4fab887d-8f73-40e6-b2d8-2426255231bf", 
        "vrid": 20, 
        "primary_ipv4": "172.16.101.152", 
        "netmask": 24, 
        "service_type": "vpn", 
        "id": "fbd7d07e-9e84-4ad7-ab85-36d46adb9435", 
        "name": "sample-gw-interface"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:gw_interface:fbd7d07e-9e84-4ad7-ab85-36d46adb9435:1:3r1tj
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "fbd7d07e-9e84-4ad7-ab85-36d46adb9435", 
        "handler": "heat_worker", 
        "job_name": "gw_interface:fbd7d07e-9e84-4ad7-ab85-36d46adb9435:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
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
                "param": "secondary_device_physical_interface"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
                    {
                        "resource_type": "vpn_service", 
                        "resource_id": "72b05fe5-88c6-4888-a6fb-feb793fffae8"
                    }
                ], 
                "type": "value", 
                "value": "VPNGW2-RI-IBGP", 
                "param": "secondary_ibgp_config_group"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
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
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
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
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
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
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
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
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }
                ], 
                "type": "value", 
                "value": "1025", 
                "param": "downlink_vlan_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }
                ], 
                "type": "value", 
                "value": "65101", 
                "param": "local_as"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
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
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
                    {
                        "resource_type": "vpn_interface", 
                        "resource_id": "0bea303d-b6eb-4edc-83ef-e32f915d3047"
                    }
                ], 
                "type": "value", 
                "value": "0bea303d-b6eb-4edc-83ef-e32f915d3047", 
                "param": "jinja_force_dependency"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
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
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
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
                "resources": [
                    {
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }
                ], 
                "type": "value", 
                "value": "vrf_gw_sample-ha-router-downlink_1025", 
                "param": "vrf_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "network", 
                        "resource_id": "bb69041d-c654-4e9f-a763-afd4333275bc"
                    }
                ], 
                "type": "value", 
                "value": "bb69041d-c654-4e9f-a763-afd4333275bc", 
                "param": "jinja_force_dependency2"
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
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
                    {
                        "resource_type": "vpn_service", 
                        "resource_id": "72b05fe5-88c6-4888-a6fb-feb793fffae8"
                    }
                ], 
                "type": "value", 
                "value": "VPNGW1-RI-IBGP", 
                "param": "primary_ibgp_config_group"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
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
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
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
        "resource_type": "gw_interface", 
        "action": "create", 
        "is_last": false, 
        "on_failure": "fail", 
        "id": "create:heat_worker:gw_interface:fbd7d07e-9e84-4ad7-ab85-36d46adb9435:1:3r1tj", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "secondary_ipv4": "172.16.101.153", 
            "gw_vipv4": "172.16.101.151", 
            "description": "Sample Gw-interface", 
            "network_id": "bb69041d-c654-4e9f-a763-afd4333275bc", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "vpn_gw_id": "4fab887d-8f73-40e6-b2d8-2426255231bf", 
            "vrid": 20, 
            "primary_ipv4": "172.16.101.152", 
            "netmask": 24, 
            "service_type": "vpn", 
            "id": "fbd7d07e-9e84-4ad7-ab85-36d46adb9435", 
            "name": "sample-gw-interface"
        }
    }, 
    0
]
```

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:gw_interface:fbd7d07e-9e84-4ad7-ab85-36d46adb9435:1:6o5m6
[
    "monitoring_worker", 
    {
        "is_first": false, 
        "resource_id": "fbd7d07e-9e84-4ad7-ab85-36d46adb9435", 
        "handler": "monitoring_worker", 
        "job_name": "gw_interface:fbd7d07e-9e84-4ad7-ab85-36d46adb9435:1", 
        "dependency": [
            "create:heat_worker:gw_interface:fbd7d07e-9e84-4ad7-ab85-36d46adb9435:1:3r1tj"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
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
                "resources": [
                    {
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }
                ], 
                "type": "value", 
                "value": "ae0.1025", 
                "param": "secondary_logical_interface_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
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
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
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
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
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
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
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
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
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
                "param": "secondary_device_login"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "vpn", 
                "param": "service_type"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
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
                "param": "primary_device_login"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
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
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
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
        "resource_type": "gw_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:gw_interface:fbd7d07e-9e84-4ad7-ab85-36d46adb9435:1:6o5m6", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "secondary_ipv4": "172.16.101.153", 
            "gw_vipv4": "172.16.101.151", 
            "description": "Sample Gw-interface", 
            "network_id": "bb69041d-c654-4e9f-a763-afd4333275bc", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "vpn_gw_id": "4fab887d-8f73-40e6-b2d8-2426255231bf", 
            "vrid": 20, 
            "primary_ipv4": "172.16.101.152", 
            "netmask": 24, 
            "service_type": "vpn", 
            "id": "fbd7d07e-9e84-4ad7-ab85-36d46adb9435", 
            "name": "sample-gw-interface"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/gw_interfaces/fbd7d07e-9e84-4ad7-ab85-36d46adb9435
{
    "stack_id": "gw_interface_fbd7d07e-9e84-4ad7-ab85-36d46adb9435", 
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "gw_interface:fbd7d07e-9e84-4ad7-ab85-36d46adb9435"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/gw_interfaces/fbd7d07e-9e84-4ad7-ab85-36d46adb9435
{
    "heat_outputs": []
}
```

### Checking stored data at the point of (5) in etcd

```
/esi-worker/job_state/v2.0/gw_interfaces/fbd7d07e-9e84-4ad7-ab85-36d46adb9435
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
/state/v2.0/gw_interfaces/fbd7d07e-9e84-4ad7-ab85-36d46adb9435
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
/monitoring/v2.0/gw_interfaces/fbd7d07e-9e84-4ad7-ab85-36d46adb9435
{
    "version": 1, 
    "primary": "MASTER", 
    "secondary": "BACKUP"
}
```
