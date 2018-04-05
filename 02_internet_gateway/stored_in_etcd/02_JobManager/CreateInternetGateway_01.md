# Stored data in etcd: Create Internet Gateway

```
/jobs/all/create:heat_worker:internet_gateway:f6e8c695-c4c1-4a93-9b7e-1663aee6dec9:1:5duk4
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9", 
        "handler": "heat_worker", 
        "job_name": "internet_gateway:f6e8c695-c4c1-4a93-9b7e-1663aee6dec9:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "internet_service", 
                        "resource_id": "986a140f-81da-4e5c-afc3-26f463a85786"
                    }
                ], 
                "type": "value", 
                "value": "INSTANCE-USER_OUT", 
                "param": "vrf_export_policy"
            }, 
            {
                "resources": [
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
                "resources": [], 
                "type": "value", 
                "value": "vrf_gw_sample-ha-router-downlink_1025_OUT", 
                "param": "counter_name_out"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "ae0.1025", 
                "param": "primary_device_logical_interface"
            }, 
            {
                "resources": [
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
                "value": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9", 
                "param": "gohan_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_service", 
                        "resource_id": "986a140f-81da-4e5c-afc3-26f463a85786"
                    }
                ], 
                "type": "value", 
                "value": "INSTANCE-USER_IN", 
                "param": "vrf_import_policy"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "vrf_gw_sample-ha-router-downlink_1025_prefix", 
                "param": "prefix_list_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_service", 
                        "resource_id": "986a140f-81da-4e5c-afc3-26f463a85786"
                    }
                ], 
                "type": "value", 
                "value": "", 
                "param": "jinja_vrf_config"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "qos_option", 
                        "resource_id": "0e6b35d9-d74d-4d3a-922a-d79b9df9b78c"
                    }
                ], 
                "type": "value", 
                "value": "FILTER_10M-GA-DOWN-INET", 
                "param": "output_filter_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_service", 
                        "resource_id": "986a140f-81da-4e5c-afc3-26f463a85786"
                    }
                ], 
                "type": "value", 
                "value": "InetGW2-VRRP", 
                "param": "secondary_vrrp_config_group"
            }, 
            {
                "resources": [
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
                        "resource_type": "internet_service", 
                        "resource_id": "986a140f-81da-4e5c-afc3-26f463a85786"
                    }
                ], 
                "type": "value", 
                "value": "INET_IN", 
                "param": "inet_in_filter"
            }, 
            {
                "resources": [
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
                "value": "ae0.1025", 
                "param": "secondary_device_logical_interface"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "vrf_gw_sample-ha-router-downlink_1025_IN", 
                "param": "counter_name_in"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_service", 
                        "resource_id": "986a140f-81da-4e5c-afc3-26f463a85786"
                    }
                ], 
                "type": "value", 
                "value": "INET_OUT", 
                "param": "inet_out_filter"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "1025", 
                "param": "vlan"
            }, 
            {
                "resources": [
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
                "resources": [
                    {
                        "resource_type": "internet_service", 
                        "resource_id": "986a140f-81da-4e5c-afc3-26f463a85786"
                    }
                ], 
                "type": "value", 
                "value": "INSTANCE-MASTER_IN", 
                "param": "uplink_import_policy"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "qos_option", 
                        "resource_id": "0e6b35d9-d74d-4d3a-922a-d79b9df9b78c"
                    }
                ], 
                "type": "value", 
                "value": "FILTER_10M-GA-UP-INET", 
                "param": "input_filter_name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "vrf_gw_sample-ha-router-downlink_1025_filter", 
                "param": "filter_term_name"
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
                "resources": [], 
                "type": "value", 
                "value": "vrf_gw_sample-ha-router-downlink_1025", 
                "param": "vrf_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_service", 
                        "resource_id": "986a140f-81da-4e5c-afc3-26f463a85786"
                    }
                ], 
                "type": "value", 
                "value": "InetGW1-VRRP", 
                "param": "primary_vrrp_config_group"
            }, 
            {
                "resources": [
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
        "resource_type": "internet_gateway", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:internet_gateway:f6e8c695-c4c1-4a93-9b7e-1663aee6dec9:1:5duk4", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "secondary_logical_interface_name": "ae0.1025", 
            "name": "sample-internet-gateway", 
            "primary_logical_interface_name": "ae0.1025", 
            "downlink_interface_id": "2595e193-84a8-49dc-aa2e-7a68c60ea11e", 
            "internet_service_id": "986a140f-81da-4e5c-afc3-26f463a85786", 
            "qos_option_id": "0e6b35d9-d74d-4d3a-922a-d79b9df9b78c", 
            "vrf_name": "vrf_gw_sample-ha-router-downlink_1025", 
            "maximum_static_routes": 32, 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
            "id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9", 
            "vlan_id": "1025", 
            "description": "Sample Internet-gateway"
        }
    }, 
    0
]
```
