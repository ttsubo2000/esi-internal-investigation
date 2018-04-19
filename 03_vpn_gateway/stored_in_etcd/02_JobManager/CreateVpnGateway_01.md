# Stored data in etcd: Create Vpn Gateway

```
/jobs/all/create:heat_worker:vpn_gateway:b1da850c-3344-4de2-aa18-d96a30b54f69:1:hhmut
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69", 
        "handler": "heat_worker", 
        "job_name": "vpn_gateway:b1da850c-3344-4de2-aa18-d96a30b54f69:1", 
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
                "resources": [
                    {
                        "resource_type": "qos_option", 
                        "resource_id": "d35a3c95-8647-44d7-b32f-405b77d77f51"
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
                        "resource_type": "ha_interface", 
                        "resource_id": "66bdfe91-b9e6-42f2-8942-bb4d4a67d5ba"
                    }, 
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "c8e2d558-02ee-4bf3-ba5b-958821a21043"
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
                        "resource_id": "d35a3c95-8647-44d7-b32f-405b77d77f51"
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
                        "resource_type": "vpn_service", 
                        "resource_id": "c8d57f7e-b439-475e-a6fb-ee2594390177"
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
                "resources": [], 
                "type": "value", 
                "value": "vrf_gw_sample-ha-router-downlink_1025", 
                "param": "vrf_name"
            }, 
            {
                "resources": [
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
                        "resource_type": "ha_interface", 
                        "resource_id": "66bdfe91-b9e6-42f2-8942-bb4d4a67d5ba"
                    }, 
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "3118d6be-b1cb-472a-805f-7e1ec46aa5e7"
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
                        "resource_id": "c8d57f7e-b439-475e-a6fb-ee2594390177"
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
                "param": "secondary_device_physical_uplink_interface"
            }, 
            {
                "resources": [
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
        "resource_type": "vpn_gateway", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:vpn_gateway:b1da850c-3344-4de2-aa18-d96a30b54f69:1:hhmut", 
        "resource_input": {
            "downlink_vlan_id": "1025", 
            "status": "PENDING_CREATE", 
            "vpn_service_id": "c8d57f7e-b439-475e-a6fb-ee2594390177", 
            "description": "this resource is vpn-gateway", 
            "maximum_static_routes": 32, 
            "secondary_logical_downlink_interface_name": "ae0.1025", 
            "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
            "qos_option_id": "d35a3c95-8647-44d7-b32f-405b77d77f51", 
            "secondary_logical_uplink_interface_name": "ge-0/0/1.122", 
            "uplink_vlan_id": "122", 
            "primary_logical_downlink_interface_name": "ae0.1025", 
            "local_as_number": "65101", 
            "vrf_name": "vrf_gw_sample-ha-router-downlink_1025", 
            "uplink_interface_id": "c50006de-8afe-48fc-b7b8-37dc7617764a", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "downlink_interface_id": "66bdfe91-b9e6-42f2-8942-bb4d4a67d5ba", 
            "primary_logical_uplink_interface_name": "ge-0/0/1.122", 
            "connected_vpn_interface": "", 
            "id": "b1da850c-3344-4de2-aa18-d96a30b54f69", 
            "name": "sample-vpn-gateway"
        }
    }, 
    0
]
```
