# Stored data in etcd: Create Gw Interface

```
/jobs/all/create:heat_worker:gw_interface:3dbcfce5-bca5-4182-991a-c23de685fcf1:1:2qwyd
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "3dbcfce5-bca5-4182-991a-c23de685fcf1", 
        "handler": "heat_worker", 
        "job_name": "gw_interface:3dbcfce5-bca5-4182-991a-c23de685fcf1:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
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
                        "resource_type": "er_physical_interface", 
                        "resource_id": "c8e2d558-02ee-4bf3-ba5b-958821a21043"
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
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
                    }, 
                    {
                        "resource_type": "vpn_service", 
                        "resource_id": "c8d57f7e-b439-475e-a6fb-ee2594390177"
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
                "value": "172.16.101.153", 
                "param": "secondary_device_gw_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "3dbcfce5-bca5-4182-991a-c23de685fcf1", 
                "param": "gohan_id"
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
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
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
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
                    }
                ], 
                "type": "value", 
                "value": "ae0.1025", 
                "param": "primary_logical_interface_name"
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
                        "resource_id": "66bdfe91-b9e6-42f2-8942-bb4d4a67d5ba"
                    }, 
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "3118d6be-b1cb-472a-805f-7e1ec46aa5e7"
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
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
                    }, 
                    {
                        "resource_type": "vpn_interface", 
                        "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222"
                    }
                ], 
                "type": "value", 
                "value": "07d4f1fc-5142-4fae-b115-627fc009e222", 
                "param": "jinja_force_dependency"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
                "param": "tenant_id"
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
                        "resource_type": "network", 
                        "resource_id": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2"
                    }
                ], 
                "type": "value", 
                "value": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2", 
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
                        "resource_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
                    }, 
                    {
                        "resource_type": "vpn_service", 
                        "resource_id": "c8d57f7e-b439-475e-a6fb-ee2594390177"
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
        "resource_type": "gw_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:gw_interface:3dbcfce5-bca5-4182-991a-c23de685fcf1:1:2qwyd", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "secondary_ipv4": "172.16.101.153", 
            "gw_vipv4": "172.16.101.151", 
            "description": "Sample Gw-interface", 
            "network_id": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2", 
            "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
            "vpn_gw_id": "b1da850c-3344-4de2-aa18-d96a30b54f69", 
            "vrid": 20, 
            "primary_ipv4": "172.16.101.152", 
            "operational_state": "NO_STATE", 
            "netmask": 24, 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "service_type": "vpn", 
            "id": "3dbcfce5-bca5-4182-991a-c23de685fcf1", 
            "name": "sample-gw-interface"
        }
    }, 
    0
]
```
