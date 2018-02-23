# Stored data in etcd: Create Subnet (user-net)

These are stored data for "heat_templates" in etcd.

* subnet

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/subnets/c2c9520b-026d-444a-8db9-c1cb9d71c130
{
    "body": {
        "status": "PENDING_CREATE", 
        "description": "load_balancer subnet", 
        "enable_dhcp": true, 
        "tags": {}, 
        "network_id": "774acf45-316f-4431-b31b-08770b76d761", 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
        "dns_nameservers": [], 
        "dhcp_server_address": "10.225.225.2", 
        "ntp_servers": [], 
        "allocation_pools": [
            {
                "start": "10.225.225.2", 
                "end": "10.225.225.254"
            }
        ], 
        "gateway_ip": "10.225.225.1", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "ip_version": 4, 
        "host_routes": [], 
        "cidr": "10.225.225.0/24", 
        "id": "c2c9520b-026d-444a-8db9-c1cb9d71c130", 
        "name": "sample-lb-subnet"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/create:heat_worker:subnet:c2c9520b-026d-444a-8db9-c1cb9d71c130:1:qqsdr
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "c2c9520b-026d-444a-8db9-c1cb9d71c130", 
        "handler": "heat_worker", 
        "job_name": "subnet:c2c9520b-026d-444a-8db9-c1cb9d71c130:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "c2c9520b-026d-444a-8db9-c1cb9d71c130", 
                "param": "name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": true, 
                "param": "enable_dhcp"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "network", 
                        "resource_id": "774acf45-316f-4431-b31b-08770b76d761"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "774acf45-316f-4431-b31b-08770b76d761"
                }, 
                "param": "network_id"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "default-domain:default-project:default-network-ipam", 
                "param": "ipam"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [], 
                "param": "dns_nameservers"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "3", 
                "param": "heat_timeout"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "10.225.225.2", 
                "param": "dhcp_server_address"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [], 
                "param": "ntp_servers"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [
                    {
                        "start": "10.225.225.2", 
                        "end": "10.225.225.254"
                    }
                ], 
                "param": "allocation_pools"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "10.225.225.1", 
                "param": "gateway_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [], 
                "param": "host_routes"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "10.225.225.0/24", 
                "param": "cidr"
            }
        ], 
        "resource_type": "subnet", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:subnet:c2c9520b-026d-444a-8db9-c1cb9d71c130:1:qqsdr", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "load_balancer subnet", 
            "enable_dhcp": true, 
            "tags": {}, 
            "network_id": "774acf45-316f-4431-b31b-08770b76d761", 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "dns_nameservers": [], 
            "dhcp_server_address": "10.225.225.2", 
            "ntp_servers": [], 
            "allocation_pools": [
                {
                    "start": "10.225.225.2", 
                    "end": "10.225.225.254"
                }
            ], 
            "gateway_ip": "10.225.225.1", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "ip_version": 4, 
            "host_routes": [], 
            "cidr": "10.225.225.0/24", 
            "id": "c2c9520b-026d-444a-8db9-c1cb9d71c130", 
            "name": "sample-lb-subnet"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/subnets/c2c9520b-026d-444a-8db9-c1cb9d71c130
{
    "stack_id": "subnet_c2c9520b-026d-444a-8db9-c1cb9d71c130", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "10.225.225.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "c2c9520b-026d-444a-8db9-c1cb9d71c130", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "10.225.225.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "774acf45-316f-4431-b31b-08770b76d761", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "43f081ee-2527-4821-90b9-5560459c95a0", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "subnet:c2c9520b-026d-444a-8db9-c1cb9d71c130"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/subnets/c2c9520b-026d-444a-8db9-c1cb9d71c130
{
    "heat_outputs": [
        {
            "output_value": "10.225.225.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "c2c9520b-026d-444a-8db9-c1cb9d71c130", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "10.225.225.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "774acf45-316f-4431-b31b-08770b76d761", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "43f081ee-2527-4821-90b9-5560459c95a0", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/subnets/c2c9520b-026d-444a-8db9-c1cb9d71c130
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"10.225.225.0/24\", \"description\": \"IP prefix of local subnet.\", \"output_key\": \"ip_prefix\"}, {\"output_value\": \"c2c9520b-026d-444a-8db9-c1cb9d71c130\", \"description\": \"The name of the local subnet.\", \"output_key\": \"name\"}, {\"output_value\": \"10.225.225.1\", \"description\": \"Default gateway of local subnet.\", \"output_key\": \"default_gateway\"}, {\"output_value\": \"774acf45-316f-4431-b31b-08770b76d761\", \"description\": \"A unique id for the network.\", \"output_key\": \"network_id\"}, {\"output_value\": \"5a79909b-2bf3-4e26-8a9c-0bf6bb175457\", \"description\": \"IPAM this local subnet uses.\", \"output_key\": \"ipam\"}, {\"output_value\": \"43f081ee-2527-4821-90b9-5560459c95a0\", \"description\": \"A unique id for the local subnet.\", \"output_key\": \"id\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
