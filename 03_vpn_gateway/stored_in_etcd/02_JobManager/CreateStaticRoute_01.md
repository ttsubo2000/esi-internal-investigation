# Stored data in etcd: Create Static Route

```
/jobs/all/create:heat_worker:static_route:31980341-9bef-4f05-8df7-674dea343884:1:qyuh9
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "31980341-9bef-4f05-8df7-674dea343884", 
        "handler": "heat_worker", 
        "job_name": "static_route:31980341-9bef-4f05-8df7-674dea343884:1", 
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
                "value": "192.168.0.0/24", 
                "param": "route"
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
                "value": "60", 
                "param": "heat_timeout"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "172.16.101.1", 
                "param": "next_hop"
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
            }
        ], 
        "resource_type": "static_route", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:static_route:31980341-9bef-4f05-8df7-674dea343884:1:qyuh9", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "nexthop": "172.16.101.1", 
            "description": "Sample Static-route", 
            "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
            "vpn_gw_id": "b1da850c-3344-4de2-aa18-d96a30b54f69", 
            "destination": "192.168.0.0/24", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "service_type": "vpn", 
            "id": "31980341-9bef-4f05-8df7-674dea343884", 
            "name": "sample-static-route"
        }
    }, 
    0
]
```
