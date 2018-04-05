# Stored data in etcd: Create Gw Interface

```
/jobs/all/create:heat_worker:gw_interface:ce8831fd-d30c-41e3-95de-feaee0b95405:1:y9zyx
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "ce8831fd-d30c-41e3-95de-feaee0b95405", 
        "handler": "heat_worker", 
        "job_name": "gw_interface:ce8831fd-d30c-41e3-95de-feaee0b95405:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "2595e193-84a8-49dc-aa2e-7a68c60ea11e"
                    }, 
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "d108a472-81ab-43a0-8c49-e0d1a46e6128"
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
                        "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
                    }, 
                    {
                        "resource_type": "internet_service", 
                        "resource_id": "986a140f-81da-4e5c-afc3-26f463a85786"
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
                        "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "2595e193-84a8-49dc-aa2e-7a68c60ea11e"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "add04ae7-e48a-4583-a726-bed5f3b748c4"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78"
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
                "value": "ce8831fd-d30c-41e3-95de-feaee0b95405", 
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
                        "resource_type": "internet_gateway", 
                        "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "2595e193-84a8-49dc-aa2e-7a68c60ea11e"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "add04ae7-e48a-4583-a726-bed5f3b748c4"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78"
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
                        "resource_type": "internet_gateway", 
                        "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "2595e193-84a8-49dc-aa2e-7a68c60ea11e"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "add04ae7-e48a-4583-a726-bed5f3b748c4"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "ca43aedb-bc30-4355-a931-7bb1d9040659"
                    }
                ], 
                "type": "value", 
                "value": "esi", 
                "param": "secondary_device_username"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
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
                        "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
                    }
                ], 
                "type": "value", 
                "value": "ae0.1025", 
                "param": "primary_logical_interface_name"
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
                        "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
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
                        "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "2595e193-84a8-49dc-aa2e-7a68c60ea11e"
                    }, 
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "53712736-354c-4374-be82-6f07bea9d1bd"
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
                        "resource_id": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e"
                    }
                ], 
                "type": "value", 
                "value": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e", 
                "param": "jinja_force_dependency"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "06d6b792b31c40daa546fb0f4e35980d", 
                "param": "tenant_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "2595e193-84a8-49dc-aa2e-7a68c60ea11e"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "add04ae7-e48a-4583-a726-bed5f3b748c4"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "ca43aedb-bc30-4355-a931-7bb1d9040659"
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
                        "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "2595e193-84a8-49dc-aa2e-7a68c60ea11e"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "add04ae7-e48a-4583-a726-bed5f3b748c4"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "ca43aedb-bc30-4355-a931-7bb1d9040659"
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
                        "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
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
                        "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "2595e193-84a8-49dc-aa2e-7a68c60ea11e"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "add04ae7-e48a-4583-a726-bed5f3b748c4"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78"
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
                        "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
                    }, 
                    {
                        "resource_type": "internet_service", 
                        "resource_id": "986a140f-81da-4e5c-afc3-26f463a85786"
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
                        "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "2595e193-84a8-49dc-aa2e-7a68c60ea11e"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "add04ae7-e48a-4583-a726-bed5f3b748c4"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78"
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
                        "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "2595e193-84a8-49dc-aa2e-7a68c60ea11e"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "add04ae7-e48a-4583-a726-bed5f3b748c4"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "ca43aedb-bc30-4355-a931-7bb1d9040659"
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
        "id": "create:heat_worker:gw_interface:ce8831fd-d30c-41e3-95de-feaee0b95405:1:y9zyx", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "secondary_ipv4": "172.16.101.153", 
            "gw_vipv4": "172.16.101.151", 
            "description": "Sample Gw-interface", 
            "network_id": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e", 
            "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
            "internet_gw_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9", 
            "vrid": 20, 
            "primary_ipv4": "172.16.101.152", 
            "operational_state": "NO_STATE", 
            "netmask": 24, 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "service_type": "internet", 
            "id": "ce8831fd-d30c-41e3-95de-feaee0b95405", 
            "name": "sample-gw-interface"
        }
    }, 
    0
]
```
