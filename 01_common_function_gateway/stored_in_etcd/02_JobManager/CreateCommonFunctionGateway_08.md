# Stored data in etcd: Create Common Function Gateway

```
/jobs/all/create:heat_worker:common_function_gateway:f649736d-1920-41eb-96af-d4e4fe192d0e:1:2n65z
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "f649736d-1920-41eb-96af-d4e4fe192d0e", 
        "handler": "heat_worker", 
        "job_name": "common_function_gateway:f649736d-1920-41eb-96af-d4e4fe192d0e:1", 
        "dependency": [
            "create:heat_worker:subnet:cf9356ae-b4e1-4a91-8193-089fdc12173d:1:7kdu4"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "common_function_pool", 
                        "resource_id": "2d4a700d-bf94-4217-9a3c-4217a16c951f"
                    }
                ], 
                "type": "value", 
                "value": [
                    41, 
                    42
                ], 
                "param": "jinja_vrids"
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
                        "resource_type": "common_function", 
                        "resource_id": "637aa51a-f54f-4723-bc5f-9fb8942dfc8b"
                    }, 
                    {
                        "resource_type": "common_function", 
                        "resource_id": "b7ff279d-a7ee-4714-b77c-bcd2f0e51996"
                    }
                ], 
                "type": "value", 
                "value": [
                    1, 
                    2
                ], 
                "param": "jinja_common_service_numbers"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "1025", 
                "param": "jinja_vlan_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "16f6433d-0864-4d24-809d-c1b8e878280c"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "e16529c4-ffb8-4346-b850-af3c93564604"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "f4f54175-93fe-406b-ae66-dbca4df99e03"
                    }
                ], 
                "type": "value", 
                "value": "esiesi0000", 
                "param": "primary_device_password"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "f649736d-1920-41eb-96af-d4e4fe192d0e", 
                "param": "gohan_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "common_function_pool", 
                        "resource_id": "2d4a700d-bf94-4217-9a3c-4217a16c951f"
                    }
                ], 
                "type": "value", 
                "value": "SHARED-RESOURCE", 
                "param": "jinja_service_vrf_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "common_function_pool", 
                        "resource_id": "2d4a700d-bf94-4217-9a3c-4217a16c951f"
                    }
                ], 
                "type": "value", 
                "value": "DNAT-RULE", 
                "param": "jinja_dnat_group_name"
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
                        "resource_type": "ha_interface", 
                        "resource_id": "16f6433d-0864-4d24-809d-c1b8e878280c"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "e16529c4-ffb8-4346-b850-af3c93564604"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "f4f54175-93fe-406b-ae66-dbca4df99e03"
                    }
                ], 
                "type": "value", 
                "value": "10.79.5.185", 
                "param": "primary_device_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "1025", 
                "param": "jinja_logical_tunnel_unit_user"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": 1, 
                "param": "version"
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
                        "resource_type": "ha_interface", 
                        "resource_id": "16f6433d-0864-4d24-809d-c1b8e878280c"
                    }, 
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "b9c7c1f4-1b90-4a7a-8161-34276bb2ed10"
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
                        "resource_id": "16f6433d-0864-4d24-809d-c1b8e878280c"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "e16529c4-ffb8-4346-b850-af3c93564604"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "2d056865-47a9-45cf-a890-ed10e3b5912a"
                    }
                ], 
                "type": "value", 
                "value": "esi", 
                "param": "secondary_device_username"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "common_function_pool", 
                        "resource_id": "2d4a700d-bf94-4217-9a3c-4217a16c951f"
                    }
                ], 
                "type": "value", 
                "value": "DNAT-POOL", 
                "param": "jinja_dnat_pool_group_name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "100.64.0.10", 
                "param": "jinja_nat_ip"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "subnet", 
                        "resource_id": "cf9356ae-b4e1-4a91-8193-089fdc12173d"
                    }
                ], 
                "type": "value", 
                "value": "cf9356ae-b4e1-4a91-8193-089fdc12173d", 
                "param": "jinja_dummy_dependency"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "vrf_gw_sample-ha-router-downlink_1025", 
                "param": "jinja_vrf_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "common_function_pool", 
                        "resource_id": "2d4a700d-bf94-4217-9a3c-4217a16c951f"
                    }
                ], 
                "type": "value", 
                "value": "IF-USER-VRRP-ACT", 
                "param": "jinja_vrrp_group_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "common_function_pool", 
                        "resource_id": "2d4a700d-bf94-4217-9a3c-4217a16c951f"
                    }
                ], 
                "type": "value", 
                "value": "SNAPT-RULE", 
                "param": "jinja_snapt_group_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "common_function_pool", 
                        "resource_id": "2d4a700d-bf94-4217-9a3c-4217a16c951f"
                    }
                ], 
                "type": "value", 
                "value": "lt-0/0/0", 
                "param": "jinja_logical_tunnel_interface_name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "c583ce78843344adbe5fd20f13620274", 
                "param": "tenant_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "16f6433d-0864-4d24-809d-c1b8e878280c"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "e16529c4-ffb8-4346-b850-af3c93564604"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "2d056865-47a9-45cf-a890-ed10e3b5912a"
                    }
                ], 
                "type": "value", 
                "value": 830, 
                "param": "secondary_device_port"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "11025", 
                "param": "jinja_logical_tunnel_unit_service"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "16f6433d-0864-4d24-809d-c1b8e878280c"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "e16529c4-ffb8-4346-b850-af3c93564604"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "2d056865-47a9-45cf-a890-ed10e3b5912a"
                    }
                ], 
                "type": "value", 
                "value": "esiesi0000", 
                "param": "secondary_device_password"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "common_function_pool", 
                        "resource_id": "2d4a700d-bf94-4217-9a3c-4217a16c951f"
                    }
                ], 
                "type": "value", 
                "value": "ms-0/2/0", 
                "param": "jinja_service_interface_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "16f6433d-0864-4d24-809d-c1b8e878280c"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "e16529c4-ffb8-4346-b850-af3c93564604"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "f4f54175-93fe-406b-ae66-dbca4df99e03"
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
                        "resource_id": "16f6433d-0864-4d24-809d-c1b8e878280c"
                    }, 
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "c2576120-00b0-461e-a2ae-f7bbff9465d0"
                    }
                ], 
                "type": "value", 
                "value": "ae0", 
                "param": "primary_device_physical_downlink_interface"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "common_function_pool", 
                        "resource_id": "2d4a700d-bf94-4217-9a3c-4217a16c951f"
                    }
                ], 
                "type": "value", 
                "value": "SNAPT-POOL", 
                "param": "jinja_snapt_pool_group_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "16f6433d-0864-4d24-809d-c1b8e878280c"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "e16529c4-ffb8-4346-b850-af3c93564604"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "f4f54175-93fe-406b-ae66-dbca4df99e03"
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
                        "resource_id": "16f6433d-0864-4d24-809d-c1b8e878280c"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "e16529c4-ffb8-4346-b850-af3c93564604"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "2d056865-47a9-45cf-a890-ed10e3b5912a"
                    }
                ], 
                "type": "value", 
                "value": "10.79.5.184", 
                "param": "secondary_device_ip"
            }
        ], 
        "resource_type": "common_function_gateway", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:common_function_gateway:f649736d-1920-41eb-96af-d4e4fe192d0e:1:2n65z", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "secondary_logical_interface_name": "ae0.1025", 
            "description": "", 
            "primary_logical_interface_name": "ae0.1025", 
            "logical_tunnel_unit_user": "1025", 
            "network_id": "fc8814a7-eb1e-4f59-8422-7de500e72782", 
            "downlink_interface_id": "16f6433d-0864-4d24-809d-c1b8e878280c", 
            "nat_ip": "100.64.0.10", 
            "operational_state": "NO_STATE", 
            "logical_tunnel_unit_service": "11025", 
            "subnet_id": "cf9356ae-b4e1-4a91-8193-089fdc12173d", 
            "common_function_pool_id": "2d4a700d-bf94-4217-9a3c-4217a16c951f", 
            "vrf_name": "vrf_gw_sample-ha-router-downlink_1025", 
            "common_functions": [
                {
                    "common_function_id": "637aa51a-f54f-4723-bc5f-9fb8942dfc8b"
                }, 
                {
                    "common_function_id": "b7ff279d-a7ee-4714-b77c-bcd2f0e51996"
                }
            ], 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "tenant_id": "c583ce78843344adbe5fd20f13620274", 
            "id": "f649736d-1920-41eb-96af-d4e4fe192d0e", 
            "vlan_id": "1025", 
            "name": "T0011CF000"
        }
    }, 
    0
]
```
