# Stored data in etcd: Create Vpn Interface

```
/jobs/all/create:heat_worker:vpn_interface:07d4f1fc-5142-4fae-b115-627fc009e222:1:1r2cs
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222", 
        "handler": "heat_worker", 
        "job_name": "vpn_interface:07d4f1fc-5142-4fae-b115-627fc009e222:1", 
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
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "c50006de-8afe-48fc-b7b8-37dc7617764a"
                    }, 
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "2bc8e40d-ab01-4738-a4aa-e69d8fd30688"
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
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
                    }
                ], 
                "type": "value", 
                "value": "ge-0/0/1.122", 
                "param": "primary_device_logical_interface"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vpn_gateway", 
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "66bdfe91-b9e6-42f2-8942-bb4d4a67d5ba"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "8c233862-895f-4cca-b377-c353e733c768"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "7a35974a-a19f-49e2-b907-ad7fd8692975"
                    }
                ], 
                "type": "value", 
                "value": "esiesi0000", 
                "param": "primary_device_password"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "07d4f1fc-5142-4fae-b115-627fc009e222", 
                "param": "gohan_id"
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
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "66bdfe91-b9e6-42f2-8942-bb4d4a67d5ba"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "8c233862-895f-4cca-b377-c353e733c768"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "7a35974a-a19f-49e2-b907-ad7fd8692975"
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
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
                    }, 
                    {
                        "resource_type": "vpn_service", 
                        "resource_id": "c8d57f7e-b439-475e-a6fb-ee2594390177"
                    }
                ], 
                "type": "value", 
                "value": "VPNGW2-RI-EBGP", 
                "param": "secondary_ebgp_config_group"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": 1, 
                "param": "version"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vpn_gateway", 
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "66bdfe91-b9e6-42f2-8942-bb4d4a67d5ba"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "8c233862-895f-4cca-b377-c353e733c768"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "b7e6d8ad-5377-4380-bbb4-1a62566cbd6d"
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
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
                    }
                ], 
                "type": "value", 
                "value": "ge-0/0/1.122", 
                "param": "secondary_device_logical_interface"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vpn_gateway", 
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
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
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "c50006de-8afe-48fc-b7b8-37dc7617764a"
                    }, 
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "f3ecf585-5c3b-445a-97a7-d8e124c99e16"
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
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
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
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
                    }, 
                    {
                        "resource_type": "vpn_service", 
                        "resource_id": "c8d57f7e-b439-475e-a6fb-ee2594390177"
                    }
                ], 
                "type": "value", 
                "value": "VPNGW1-RI-EBGP", 
                "param": "primary_ebgp_config_group"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
                "param": "tenant_id"
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
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "66bdfe91-b9e6-42f2-8942-bb4d4a67d5ba"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "8c233862-895f-4cca-b377-c353e733c768"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "b7e6d8ad-5377-4380-bbb4-1a62566cbd6d"
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
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "66bdfe91-b9e6-42f2-8942-bb4d4a67d5ba"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "8c233862-895f-4cca-b377-c353e733c768"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "b7e6d8ad-5377-4380-bbb4-1a62566cbd6d"
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
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
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
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "66bdfe91-b9e6-42f2-8942-bb4d4a67d5ba"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "8c233862-895f-4cca-b377-c353e733c768"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "7a35974a-a19f-49e2-b907-ad7fd8692975"
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
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "66bdfe91-b9e6-42f2-8942-bb4d4a67d5ba"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "8c233862-895f-4cca-b377-c353e733c768"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "7a35974a-a19f-49e2-b907-ad7fd8692975"
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
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "66bdfe91-b9e6-42f2-8942-bb4d4a67d5ba"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "8c233862-895f-4cca-b377-c353e733c768"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "b7e6d8ad-5377-4380-bbb4-1a62566cbd6d"
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
        "id": "create:heat_worker:vpn_interface:07d4f1fc-5142-4fae-b115-627fc009e222:1:1r2cs", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "bgp_remote_as": "9598", 
            "description": "Sample Vpn-interface", 
            "name": "sample-vpn-interface", 
            "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
            "vpn_gw_id": "b1da850c-3344-4de2-aa18-d96a30b54f69", 
            "primary": {
                "bgp_peer_ip": "192.168.8.1", 
                "ip_address": "192.168.8.2/30", 
                "bgp_router_id": "192.168.8.2"
            }, 
            "operational_state": "NO_STATE", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "bgp_md5": "test", 
            "id": "07d4f1fc-5142-4fae-b115-627fc009e222", 
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
