# Stored data in etcd: Create Static Route

These are stored data for "heat_templates" in etcd.

* static_route_internet

![scope](../../images/esi_interface.009.png)

These are stored data for "Create Static Route" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/static_routes/1db45c0a-46cd-40af-a87e-718092df68b3
{
    "body": {
        "status": "PENDING_CREATE", 
        "destination": "192.168.0.0/24", 
        "description": "Sample Static-route", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "vpn_gw_id": "4fab887d-8f73-40e6-b2d8-2426255231bf", 
        "nexthop": "172.16.101.1", 
        "service_type": "vpn", 
        "id": "1db45c0a-46cd-40af-a87e-718092df68b3", 
        "name": "sample-static-route"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:static_route:1db45c0a-46cd-40af-a87e-718092df68b3:1:5xin5
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "1db45c0a-46cd-40af-a87e-718092df68b3", 
        "handler": "heat_worker", 
        "job_name": "static_route:1db45c0a-46cd-40af-a87e-718092df68b3:1", 
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
                "value": "192.168.0.0/24", 
                "param": "route"
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
            }
        ], 
        "resource_type": "static_route", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:static_route:1db45c0a-46cd-40af-a87e-718092df68b3:1:5xin5", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "nexthop": "172.16.101.1", 
            "description": "Sample Static-route", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "vpn_gw_id": "4fab887d-8f73-40e6-b2d8-2426255231bf", 
            "destination": "192.168.0.0/24", 
            "service_type": "vpn", 
            "id": "1db45c0a-46cd-40af-a87e-718092df68b3", 
            "name": "sample-static-route"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/static_routes/1db45c0a-46cd-40af-a87e-718092df68b3
{
    "stack_id": "static_route_1db45c0a-46cd-40af-a87e-718092df68b3", 
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "static_route:1db45c0a-46cd-40af-a87e-718092df68b3"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/static_routes/1db45c0a-46cd-40af-a87e-718092df68b3
{
    "heat_outputs": []
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/static_routes/1db45c0a-46cd-40af-a87e-718092df68b3
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[]"
    }, 
    "version": 1, 
    "error": ""
}
```
