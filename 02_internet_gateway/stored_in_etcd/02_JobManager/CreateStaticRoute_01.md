# Stored data in etcd: Create Static Route

```
/jobs/all/create:heat_worker:static_route:d0aa20b1-9302-4b43-a3c1-9edce0811af8:1:jnu3v
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "d0aa20b1-9302-4b43-a3c1-9edce0811af8", 
        "handler": "heat_worker", 
        "job_name": "static_route:d0aa20b1-9302-4b43-a3c1-9edce0811af8:1", 
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
                "resources": [
                    {
                        "resource_type": "public_ip", 
                        "resource_id": "d5622781-f06a-4fad-b800-b577a05ad8b2"
                    }
                ], 
                "type": "value", 
                "value": "d5622781-f06a-4fad-b800-b577a05ad8b2", 
                "param": "jinja_dummy_dependency"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "203.0.112.0/28", 
                "param": "route"
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
            }
        ], 
        "resource_type": "static_route", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:static_route:d0aa20b1-9302-4b43-a3c1-9edce0811af8:1:jnu3v", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "nexthop": "172.16.101.1", 
            "description": "Sample Static-route", 
            "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
            "internet_gw_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9", 
            "destination": "203.0.112.0/28", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "public_ip_id": "d5622781-f06a-4fad-b800-b577a05ad8b2", 
            "service_type": "internet", 
            "id": "d0aa20b1-9302-4b43-a3c1-9edce0811af8", 
            "name": "sample-static-route"
        }
    }, 
    0
]
```
