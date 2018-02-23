# Stored data in etcd: Create Common Function Gateway

These are stored data for "heat_templates" in etcd.

* common_function_gateway
* common_function_gateway_monitoring

![scope](../../images/esi_interface.008.png)

These are stored data for "Create Common Function Gateway" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/common_function_gateways/5c241c51-2003-407a-a239-689fabd19022
{
    "body": {
        "status": "PENDING_CREATE", 
        "secondary_logical_interface_name": "ae0.1025", 
        "description": "", 
        "primary_logical_interface_name": "ae0.1025", 
        "logical_tunnel_unit_user": "1025", 
        "network_id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
        "downlink_interface_id": "372ed357-e622-41fb-a613-076d332838e2", 
        "nat_ip": "100.64.0.10", 
        "logical_tunnel_unit_service": "11025", 
        "subnet_id": "e1353d56-b05a-43a9-b924-383ab0d64d7b", 
        "common_function_pool_id": "cca32fd7-2430-4acc-87e9-a7b527e9918d", 
        "vrf_name": "vrf_gw_sample-ha-router-downlink_1025", 
        "common_functions": [
            {
                "common_function_id": "18c64ec9-78c2-43ac-ae0d-48fa9b6c0858"
            }, 
            {
                "common_function_id": "c1be08ee-7cf2-4c84-8fe7-7e891d17bc71"
            }
        ], 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "id": "5c241c51-2003-407a-a239-689fabd19022", 
        "vlan_id": "1025", 
        "name": "T0011CF000"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:common_function_gateway:5c241c51-2003-407a-a239-689fabd19022:1:6q0nj
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "5c241c51-2003-407a-a239-689fabd19022", 
        "handler": "heat_worker", 
        "job_name": "common_function_gateway:5c241c51-2003-407a-a239-689fabd19022:1", 
        "dependency": [
            "create:heat_worker:subnet:e1353d56-b05a-43a9-b924-383ab0d64d7b:1:junpn"
        ], 
        "version": 1, 
        "params": [
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
                        "resource_id": "18c64ec9-78c2-43ac-ae0d-48fa9b6c0858"
                    }, 
                    {
                        "resource_type": "common_function", 
                        "resource_id": "c1be08ee-7cf2-4c84-8fe7-7e891d17bc71"
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
                        "resource_id": "372ed357-e622-41fb-a613-076d332838e2"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "8aba84f9-4675-4d22-a231-e9eabde80818"
                    }
                ], 
                "type": "value", 
                "value": "esiesi0000", 
                "param": "primary_device_password"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "common_function_pool", 
                        "resource_id": "cca32fd7-2430-4acc-87e9-a7b527e9918d"
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
                        "resource_id": "cca32fd7-2430-4acc-87e9-a7b527e9918d"
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
                        "resource_id": "372ed357-e622-41fb-a613-076d332838e2"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "8aba84f9-4675-4d22-a231-e9eabde80818"
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
                "value": "ae0.1025", 
                "param": "secondary_device_logical_downlink_interface"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "372ed357-e622-41fb-a613-076d332838e2"
                    }, 
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "96c3629b-9bfb-4d54-adc1-750d024c2858"
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
                        "resource_id": "372ed357-e622-41fb-a613-076d332838e2"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "769b5e3b-3320-41ec-9be0-4567b50f1aab"
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
                        "resource_id": "cca32fd7-2430-4acc-87e9-a7b527e9918d"
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
                        "resource_id": "e1353d56-b05a-43a9-b924-383ab0d64d7b"
                    }
                ], 
                "type": "value", 
                "value": "e1353d56-b05a-43a9-b924-383ab0d64d7b", 
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
                        "resource_id": "cca32fd7-2430-4acc-87e9-a7b527e9918d"
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
                        "resource_id": "cca32fd7-2430-4acc-87e9-a7b527e9918d"
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
                        "resource_id": "cca32fd7-2430-4acc-87e9-a7b527e9918d"
                    }
                ], 
                "type": "value", 
                "value": "lt-0/0/0", 
                "param": "jinja_logical_tunnel_interface_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "372ed357-e622-41fb-a613-076d332838e2"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "769b5e3b-3320-41ec-9be0-4567b50f1aab"
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
                        "resource_id": "372ed357-e622-41fb-a613-076d332838e2"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "769b5e3b-3320-41ec-9be0-4567b50f1aab"
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
                        "resource_id": "cca32fd7-2430-4acc-87e9-a7b527e9918d"
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
                        "resource_id": "372ed357-e622-41fb-a613-076d332838e2"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "8aba84f9-4675-4d22-a231-e9eabde80818"
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
                        "resource_id": "372ed357-e622-41fb-a613-076d332838e2"
                    }, 
                    {
                        "resource_type": "er_physical_interface", 
                        "resource_id": "a752c6c0-2075-4e7f-9040-5fcefcad0252"
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
                        "resource_id": "cca32fd7-2430-4acc-87e9-a7b527e9918d"
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
                        "resource_id": "372ed357-e622-41fb-a613-076d332838e2"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "8aba84f9-4675-4d22-a231-e9eabde80818"
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
                        "resource_id": "372ed357-e622-41fb-a613-076d332838e2"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "769b5e3b-3320-41ec-9be0-4567b50f1aab"
                    }
                ], 
                "type": "value", 
                "value": "10.79.5.184", 
                "param": "secondary_device_ip"
            }
        ], 
        "resource_type": "common_function_gateway", 
        "action": "create", 
        "is_last": false, 
        "on_failure": "fail", 
        "id": "create:heat_worker:common_function_gateway:5c241c51-2003-407a-a239-689fabd19022:1:6q0nj", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "secondary_logical_interface_name": "ae0.1025", 
            "description": "", 
            "primary_logical_interface_name": "ae0.1025", 
            "logical_tunnel_unit_user": "1025", 
            "network_id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
            "downlink_interface_id": "372ed357-e622-41fb-a613-076d332838e2", 
            "nat_ip": "100.64.0.10", 
            "logical_tunnel_unit_service": "11025", 
            "subnet_id": "e1353d56-b05a-43a9-b924-383ab0d64d7b", 
            "common_function_pool_id": "cca32fd7-2430-4acc-87e9-a7b527e9918d", 
            "vrf_name": "vrf_gw_sample-ha-router-downlink_1025", 
            "common_functions": [
                {
                    "common_function_id": "18c64ec9-78c2-43ac-ae0d-48fa9b6c0858"
                }, 
                {
                    "common_function_id": "c1be08ee-7cf2-4c84-8fe7-7e891d17bc71"
                }
            ], 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "id": "5c241c51-2003-407a-a239-689fabd19022", 
            "vlan_id": "1025", 
            "name": "T0011CF000"
        }
    }, 
    0
]
```

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:common_function_gateway:5c241c51-2003-407a-a239-689fabd19022:1:q0km3
[
    "monitoring_worker", 
    {
        "is_first": false, 
        "resource_id": "5c241c51-2003-407a-a239-689fabd19022", 
        "handler": "monitoring_worker", 
        "job_name": "common_function_gateway:5c241c51-2003-407a-a239-689fabd19022:1", 
        "dependency": [
            "create:heat_worker:common_function_gateway:5c241c51-2003-407a-a239-689fabd19022:1:6q0nj"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "372ed357-e622-41fb-a613-076d332838e2"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "769b5e3b-3320-41ec-9be0-4567b50f1aab"
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
                        "resource_id": "cca32fd7-2430-4acc-87e9-a7b527e9918d"
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
                "param": "primary_logical_interface_name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "ae0.1025", 
                "param": "secondary_logical_interface_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "372ed357-e622-41fb-a613-076d332838e2"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "769b5e3b-3320-41ec-9be0-4567b50f1aab"
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
                        "resource_id": "372ed357-e622-41fb-a613-076d332838e2"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "8aba84f9-4675-4d22-a231-e9eabde80818"
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
                        "resource_id": "372ed357-e622-41fb-a613-076d332838e2"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "8aba84f9-4675-4d22-a231-e9eabde80818"
                    }
                ], 
                "type": "value", 
                "value": "esiesi0000", 
                "param": "primary_device_password"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "372ed357-e622-41fb-a613-076d332838e2"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "769b5e3b-3320-41ec-9be0-4567b50f1aab"
                    }
                ], 
                "type": "value", 
                "value": "esi", 
                "param": "secondary_device_login"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "372ed357-e622-41fb-a613-076d332838e2"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "8aba84f9-4675-4d22-a231-e9eabde80818"
                    }
                ], 
                "type": "value", 
                "value": "esi", 
                "param": "primary_device_login"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ha_interface", 
                        "resource_id": "372ed357-e622-41fb-a613-076d332838e2"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "8aba84f9-4675-4d22-a231-e9eabde80818"
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
                        "resource_id": "372ed357-e622-41fb-a613-076d332838e2"
                    }, 
                    {
                        "resource_type": "ha_router", 
                        "resource_id": "3a3d7a43-d749-44e8-90bc-de7b37d1d258"
                    }, 
                    {
                        "resource_type": "edge_router", 
                        "resource_id": "769b5e3b-3320-41ec-9be0-4567b50f1aab"
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
        "id": "create:monitoring_worker:common_function_gateway:5c241c51-2003-407a-a239-689fabd19022:1:q0km3", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "secondary_logical_interface_name": "ae0.1025", 
            "description": "", 
            "primary_logical_interface_name": "ae0.1025", 
            "logical_tunnel_unit_user": "1025", 
            "network_id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
            "downlink_interface_id": "372ed357-e622-41fb-a613-076d332838e2", 
            "nat_ip": "100.64.0.10", 
            "logical_tunnel_unit_service": "11025", 
            "subnet_id": "e1353d56-b05a-43a9-b924-383ab0d64d7b", 
            "common_function_pool_id": "cca32fd7-2430-4acc-87e9-a7b527e9918d", 
            "vrf_name": "vrf_gw_sample-ha-router-downlink_1025", 
            "common_functions": [
                {
                    "common_function_id": "18c64ec9-78c2-43ac-ae0d-48fa9b6c0858"
                }, 
                {
                    "common_function_id": "c1be08ee-7cf2-4c84-8fe7-7e891d17bc71"
                }
            ], 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "id": "5c241c51-2003-407a-a239-689fabd19022", 
            "vlan_id": "1025", 
            "name": "T0011CF000"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/common_function_gateways/5c241c51-2003-407a-a239-689fabd19022
{
    "stack_id": "common_function_gateway_5c241c51-2003-407a-a239-689fabd19022", 
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "common_function_gateway:5c241c51-2003-407a-a239-689fabd19022"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/common_function_gateways/5c241c51-2003-407a-a239-689fabd19022
{
    "heat_outputs": []
}
```

### Checking stored data at the point of (5) in etcd

```
/esi-worker/job_state/v2.0/common_function_gateways/5c241c51-2003-407a-a239-689fabd19022
{
    "state_monitoring": {
        "secondary_41": "backup", 
        "primary_42": "master", 
        "primary_41": "master", 
        "secondary_42": "backup"
    }, 
    "heat_outputs": []
}
```

### Checking stored data at the point of (6) in etcd

```
/state/v2.0/common_function_gateways/5c241c51-2003-407a-a239-689fabd19022
{
    "state": {
        "state_monitoring": "{\"secondary_41\": \"backup\", \"primary_42\": \"master\", \"primary_41\": \"master\", \"secondary_42\": \"backup\"}", 
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[]"
    }, 
    "version": 1, 
    "error": ""
}
```

### Checking stored data at the point of (7) in etcd

```
/monitoring/v2.0/common_function_gateways/5c241c51-2003-407a-a239-689fabd19022
{
    "version": 1, 
    "secondary_41": "BACKUP", 
    "primary_42": "MASTER", 
    "primary_41": "MASTER", 
    "secondary_42": "BACKUP"
}
```
