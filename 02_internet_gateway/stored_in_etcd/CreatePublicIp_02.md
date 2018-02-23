# Stored data in etcd: Create Public Ip

These are stored data for "heat_templates" in etcd.

* public_ip

![scope](../../images/esi_interface.009.png)

These are stored data for "Create Public Ip" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/public_ips/bc6f2c6d-59be-4f56-a2d7-96ab578c0735
{
    "body": {
        "status": "PENDING_CREATE", 
        "description": "Sample Public-Ip", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "ip_pool_id": "5cd14f90-cf3c-4aeb-b30a-227b3c936761", 
        "id": "bc6f2c6d-59be-4f56-a2d7-96ab578c0735", 
        "cidr": "203.0.112.0", 
        "submask_length": 28, 
        "internet_gw_id": "429e24b5-a2f0-4fb8-b467-e335857e9476", 
        "name": "sample-public_ip"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:public_ip:bc6f2c6d-59be-4f56-a2d7-96ab578c0735:1:rpxah
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "bc6f2c6d-59be-4f56-a2d7-96ab578c0735", 
        "handler": "heat_worker", 
        "job_name": "public_ip:bc6f2c6d-59be-4f56-a2d7-96ab578c0735:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "198b93f2-006e-45b6-96d3-e7ef6f759501"
                    }
                ], 
                "type": "value", 
                "value": "esiesi0000", 
                "param": "secondary_device_password"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "9b82b55a-551e-4069-ae77-c972e30ab0cc"
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
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "198b93f2-006e-45b6-96d3-e7ef6f759501"
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
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "9b82b55a-551e-4069-ae77-c972e30ab0cc"
                    }
                ], 
                "type": "value", 
                "value": "10.79.5.185", 
                "param": "primary_device_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": 28, 
                "param": "ip_mask"
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
                "value": "203.0.112.0", 
                "param": "ip_cidr"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "internet_gateway", 
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "9b82b55a-551e-4069-ae77-c972e30ab0cc"
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
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "198b93f2-006e-45b6-96d3-e7ef6f759501"
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
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "9b82b55a-551e-4069-ae77-c972e30ab0cc"
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
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }, 
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "1205d3f2-7568-412a-a554-012340ab3172"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "198b93f2-006e-45b6-96d3-e7ef6f759501"
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
                        "resource_id": "429e24b5-a2f0-4fb8-b467-e335857e9476"
                    }
                ], 
                "type": "value", 
                "value": "vrf_gw_sample-ha-router-downlink_1025_prefix", 
                "param": "prefix_list_name"
            }
        ], 
        "resource_type": "public_ip", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:public_ip:bc6f2c6d-59be-4f56-a2d7-96ab578c0735:1:rpxah", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "Sample Public-Ip", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "ip_pool_id": "5cd14f90-cf3c-4aeb-b30a-227b3c936761", 
            "internet_gw_id": "429e24b5-a2f0-4fb8-b467-e335857e9476", 
            "cidr": "203.0.112.0", 
            "submask_length": 28, 
            "id": "bc6f2c6d-59be-4f56-a2d7-96ab578c0735", 
            "name": "sample-public_ip"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/public_ips/bc6f2c6d-59be-4f56-a2d7-96ab578c0735
{
    "stack_id": "public_ip_bc6f2c6d-59be-4f56-a2d7-96ab578c0735", 
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "public_ip:bc6f2c6d-59be-4f56-a2d7-96ab578c0735"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/public_ips/bc6f2c6d-59be-4f56-a2d7-96ab578c0735
{
    "heat_outputs": []
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/public_ips/bc6f2c6d-59be-4f56-a2d7-96ab578c0735
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[]"
    }, 
    "version": 1, 
    "error": ""
}
```
