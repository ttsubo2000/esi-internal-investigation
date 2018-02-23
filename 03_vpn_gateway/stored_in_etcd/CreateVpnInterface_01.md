# Stored data in etcd: Create Vpn Interface

These are stored data for "heat_templates" in etcd.

* vpn_interface
* vpn_interface_monitoring

![scope](../../images/esi_interface.008.png)

These are stored data for "Create Vpn Interface" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/vpn_interfaces/0bea303d-b6eb-4edc-83ef-e32f915d3047
{
    "body": {
        "status": "PENDING_CREATE", 
        "bgp_remote_as": "9598", 
        "description": "Sample Vpn-interface", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "vpn_gw_id": "4fab887d-8f73-40e6-b2d8-2426255231bf", 
        "primary": {
            "bgp_peer_ip": "192.168.8.1", 
            "ip_address": "192.168.8.2/30", 
            "bgp_router_id": "192.168.8.2"
        }, 
        "bgp_md5": "test", 
        "secondary": {
            "bgp_peer_ip": "192.168.8.5", 
            "ip_address": "192.168.8.6/30", 
            "bgp_router_id": "192.168.8.6"
        }, 
        "id": "0bea303d-b6eb-4edc-83ef-e32f915d3047", 
        "name": "sample-vpn-interface"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:vpn_interface:0bea303d-b6eb-4edc-83ef-e32f915d3047:1:1iijb
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "0bea303d-b6eb-4edc-83ef-e32f915d3047", 
        "handler": "heat_worker", 
        "job_name": "vpn_interface:0bea303d-b6eb-4edc-83ef-e32f915d3047:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "192.168.8.6", 
                "param": "secondary_router_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }, 
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
                "param": "secondary_device_physical_interface"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "192.168.8.1", 
                "param": "primary_peer_ip"
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
                "value": "CloudGW1", 
                "param": "bgp_group_name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "9598", 
                "param": "remote_as"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "192.168.8.2/30", 
                "param": "jinja_primary_uplink_ip"
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
                        "resource_type": "vpn_service", 
                        "resource_id": "72b05fe5-88c6-4888-a6fb-feb793fffae8"
                    }
                ], 
                "type": "value", 
                "value": "VPNGW2-RI-EBGP", 
                "param": "secondary_ebgp_config_group"
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
                        "resource_id": "5e552b8f-cd5a-454c-a224-33f7da0afa24"
                    }, 
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "6e8f473f-47ec-4b54-8f0f-d459d440393b"
                    }
                ], 
                "type": "value", 
                "value": "ge-0/0/1", 
                "param": "primary_device_physical_interface"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }
                ], 
                "type": "value", 
                "value": "122", 
                "param": "uplink_vlan"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "test", 
                "param": "md5"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "192.168.8.5", 
                "param": "secondary_peer_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "192.168.8.2", 
                "param": "primary_router_id"
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
                "value": "VPNGW1-RI-EBGP", 
                "param": "primary_ebgp_config_group"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "192.168.8.6/30", 
                "param": "jinja_secondary_uplink_ip"
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
        "resource_type": "vpn_interface", 
        "action": "create", 
        "is_last": false, 
        "on_failure": "fail", 
        "id": "create:heat_worker:vpn_interface:0bea303d-b6eb-4edc-83ef-e32f915d3047:1:1iijb", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "bgp_remote_as": "9598", 
            "description": "Sample Vpn-interface", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "vpn_gw_id": "4fab887d-8f73-40e6-b2d8-2426255231bf", 
            "primary": {
                "bgp_peer_ip": "192.168.8.1", 
                "ip_address": "192.168.8.2/30", 
                "bgp_router_id": "192.168.8.2"
            }, 
            "name": "sample-vpn-interface", 
            "bgp_md5": "test", 
            "id": "0bea303d-b6eb-4edc-83ef-e32f915d3047", 
            "secondary": {
                "bgp_peer_ip": "192.168.8.5", 
                "ip_address": "192.168.8.6/30", 
                "bgp_router_id": "192.168.8.6"
            }
        }
    }, 
    0
]
```

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:vpn_interface:0bea303d-b6eb-4edc-83ef-e32f915d3047:1:rlv12
[
    "monitoring_worker", 
    {
        "is_first": false, 
        "resource_id": "0bea303d-b6eb-4edc-83ef-e32f915d3047", 
        "handler": "monitoring_worker", 
        "job_name": "vpn_interface:0bea303d-b6eb-4edc-83ef-e32f915d3047:1", 
        "dependency": [
            "create:heat_worker:vpn_interface:0bea303d-b6eb-4edc-83ef-e32f915d3047:1:1iijb"
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
                "resources": [], 
                "type": "value", 
                "value": "192.168.8.5", 
                "param": "secondary_peer_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "192.168.8.1", 
                "param": "primary_peer_ip"
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
                "resources": [], 
                "type": "value", 
                "value": "EDGE_ROUTER_COMMUNITY", 
                "param": "community_name"
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
                    }
                ], 
                "type": "value", 
                "value": "vrf_gw_sample-ha-router-downlink_1025", 
                "param": "vrf_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }
                ], 
                "type": "value", 
                "value": "ge-0/0/1.122", 
                "param": "secondary_port"
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
                "resources": [
                    {
                        "resource_type": "vpn_gateway", 
                        "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
                    }
                ], 
                "type": "value", 
                "value": "ge-0/0/1.122", 
                "param": "primary_port"
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
        "resource_type": "vpn_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:vpn_interface:0bea303d-b6eb-4edc-83ef-e32f915d3047:1:rlv12", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "bgp_remote_as": "9598", 
            "description": "Sample Vpn-interface", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "vpn_gw_id": "4fab887d-8f73-40e6-b2d8-2426255231bf", 
            "primary": {
                "bgp_peer_ip": "192.168.8.1", 
                "ip_address": "192.168.8.2/30", 
                "bgp_router_id": "192.168.8.2"
            }, 
            "name": "sample-vpn-interface", 
            "bgp_md5": "test", 
            "id": "0bea303d-b6eb-4edc-83ef-e32f915d3047", 
            "secondary": {
                "bgp_peer_ip": "192.168.8.5", 
                "ip_address": "192.168.8.6/30", 
                "bgp_router_id": "192.168.8.6"
            }
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/vpn_interfaces/0bea303d-b6eb-4edc-83ef-e32f915d3047
{
    "stack_id": "vpn_interface_0bea303d-b6eb-4edc-83ef-e32f915d3047", 
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "vpn_interface:0bea303d-b6eb-4edc-83ef-e32f915d3047"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/vpn_interfaces/0bea303d-b6eb-4edc-83ef-e32f915d3047
{
    "heat_outputs": []
}
```

### Checking stored data at the point of (5) in etcd

```
/esi-worker/job_state/v2.0/vpn_interfaces/0bea303d-b6eb-4edc-83ef-e32f915d3047
{
    "state_monitoring": {
        "primary_uplink": "ACTIVE", 
        "primary": "ESTABLISHED", 
        "secondary_uplink": "ACTIVE", 
        "secondary": "ESTABLISHED"
    }, 
    "heat_outputs": []
}
```

### Checking stored data at the point of (6) in etcd

```
/state/v2.0/vpn_interfaces/0bea303d-b6eb-4edc-83ef-e32f915d3047
{
    "state": {
        "state_monitoring": "{\"primary_uplink\": \"ACTIVE\", \"primary\": \"ESTABLISHED\", \"secondary_uplink\": \"ACTIVE\", \"secondary\": \"ESTABLISHED\"}", 
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[]"
    }, 
    "version": 1, 
    "error": ""
}
```

### Checking stored data at the point of (7) in etcd

```
/monitoring/v2.0/vpn_interfaces/0bea303d-b6eb-4edc-83ef-e32f915d3047
{
    "version": 1, 
    "primary": "ESTABLISHED", 
    "secondary": "ESTABLISHED"
}
```
