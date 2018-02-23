# Stored data in etcd: Create Static Route

These are stored data for "heat_templates" in etcd.

* static_route_internet

![scope](../../images/esi_interface.009.png)

These are stored data for "Create Static Route" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/static_routes/3ecf06a5-014e-48b0-841c-6ad812e69132
{
    "body": {
        "status": "PENDING_CREATE", 
        "destination": "203.0.112.0/28", 
        "description": "Sample Static-route", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "internet_gw_id": "8b9ba87a-5b28-4c67-ba04-4f1d436960f8", 
        "nexthop": "172.16.101.1", 
        "public_ip_id": "07ff3a4e-f968-481e-8ee2-378a73b8f2a2", 
        "service_type": "internet", 
        "id": "3ecf06a5-014e-48b0-841c-6ad812e69132", 
        "name": "sample-static-route"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:static_route:3ecf06a5-014e-48b0-841c-6ad812e69132:1:q6dcd
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "3ecf06a5-014e-48b0-841c-6ad812e69132", 
        "handler": "heat_worker", 
        "job_name": "static_route:3ecf06a5-014e-48b0-841c-6ad812e69132:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "8b9ba87a-5b28-4c67-ba04-4f1d436960f8"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "cecfbee0-beab-471a-a0e9-304b12bb9eac"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "0e3a382b-c27d-49c6-bc0c-735ad7ab005c"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "1dc05a10-0e16-4306-8ace-afab2352bbe9"
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
                        "resource_id": "07ff3a4e-f968-481e-8ee2-378a73b8f2a2"
                    }
                ], 
                "type": "value", 
                "value": "07ff3a4e-f968-481e-8ee2-378a73b8f2a2", 
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
                        "resource_id": "8b9ba87a-5b28-4c67-ba04-4f1d436960f8"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "cecfbee0-beab-471a-a0e9-304b12bb9eac"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "0e3a382b-c27d-49c6-bc0c-735ad7ab005c"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "f54c4933-bb4d-432d-b6fd-6c712937c1c0"
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
                        "resource_id": "8b9ba87a-5b28-4c67-ba04-4f1d436960f8"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "cecfbee0-beab-471a-a0e9-304b12bb9eac"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "0e3a382b-c27d-49c6-bc0c-735ad7ab005c"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "1dc05a10-0e16-4306-8ace-afab2352bbe9"
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
                        "resource_id": "8b9ba87a-5b28-4c67-ba04-4f1d436960f8"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "cecfbee0-beab-471a-a0e9-304b12bb9eac"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "0e3a382b-c27d-49c6-bc0c-735ad7ab005c"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "f54c4933-bb4d-432d-b6fd-6c712937c1c0"
                    }
                ], 
                "type": "value", 
                "value": "172.23.16.66", 
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
                        "resource_id": "8b9ba87a-5b28-4c67-ba04-4f1d436960f8"
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
                        "resource_id": "8b9ba87a-5b28-4c67-ba04-4f1d436960f8"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "cecfbee0-beab-471a-a0e9-304b12bb9eac"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "0e3a382b-c27d-49c6-bc0c-735ad7ab005c"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "f54c4933-bb4d-432d-b6fd-6c712937c1c0"
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
                        "resource_id": "8b9ba87a-5b28-4c67-ba04-4f1d436960f8"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "cecfbee0-beab-471a-a0e9-304b12bb9eac"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "0e3a382b-c27d-49c6-bc0c-735ad7ab005c"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "f54c4933-bb4d-432d-b6fd-6c712937c1c0"
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
                        "resource_id": "8b9ba87a-5b28-4c67-ba04-4f1d436960f8"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "cecfbee0-beab-471a-a0e9-304b12bb9eac"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "0e3a382b-c27d-49c6-bc0c-735ad7ab005c"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "1dc05a10-0e16-4306-8ace-afab2352bbe9"
                    }
                ], 
                "type": "value", 
                "value": "172.23.16.65", 
                "param": "secondary_device_ip"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "8b9ba87a-5b28-4c67-ba04-4f1d436960f8"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "cecfbee0-beab-471a-a0e9-304b12bb9eac"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "0e3a382b-c27d-49c6-bc0c-735ad7ab005c"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "1dc05a10-0e16-4306-8ace-afab2352bbe9"
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
        "id": "create:heat_worker:static_route:3ecf06a5-014e-48b0-841c-6ad812e69132:1:q6dcd", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "nexthop": "172.16.101.1", 
            "description": "Sample Static-route", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "internet_gw_id": "8b9ba87a-5b28-4c67-ba04-4f1d436960f8", 
            "destination": "203.0.112.0/28", 
            "public_ip_id": "07ff3a4e-f968-481e-8ee2-378a73b8f2a2", 
            "service_type": "internet", 
            "id": "3ecf06a5-014e-48b0-841c-6ad812e69132", 
            "name": "sample-static-route"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/static_routes/3ecf06a5-014e-48b0-841c-6ad812e69132
{
    "stack_id": "static_route_3ecf06a5-014e-48b0-841c-6ad812e69132", 
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "static_route:3ecf06a5-014e-48b0-841c-6ad812e69132"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/static_routes/3ecf06a5-014e-48b0-841c-6ad812e69132
{
    "heat_outputs": []
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/static_routes/3ecf06a5-014e-48b0-841c-6ad812e69132
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[]"
    }, 
    "version": 1, 
    "error": ""
}
```
