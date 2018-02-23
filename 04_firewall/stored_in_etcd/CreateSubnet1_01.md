# Stored data in etcd: Create Subnet (dummy-net)

These are stored data for "heat_templates" in etcd.

* subnet

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/subnets/1244d619-cc55-4bb7-b181-606776ba5e88
{
    "body": {
        "status": "PENDING_CREATE", 
        "description": "dummy subnet for firewall", 
        "enable_dhcp": true, 
        "tags": {}, 
        "network_id": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
        "dns_nameservers": [], 
        "dhcp_server_address": "10.121.232.2", 
        "ntp_servers": [], 
        "allocation_pools": [
            {
                "start": "10.121.232.2", 
                "end": "10.121.232.254"
            }
        ], 
        "gateway_ip": "10.121.232.1", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "ip_version": 4, 
        "host_routes": [], 
        "cidr": "10.121.232.0/24", 
        "id": "1244d619-cc55-4bb7-b181-606776ba5e88", 
        "name": "dummy-subnet"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/create:heat_worker:subnet:1244d619-cc55-4bb7-b181-606776ba5e88:1:hid71
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "1244d619-cc55-4bb7-b181-606776ba5e88", 
        "handler": "heat_worker", 
        "job_name": "subnet:1244d619-cc55-4bb7-b181-606776ba5e88:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "1244d619-cc55-4bb7-b181-606776ba5e88", 
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
                        "resource_id": "73b2c401-a1f3-49fb-8612-8c755b37a28d"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "73b2c401-a1f3-49fb-8612-8c755b37a28d"
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
                "value": "10.121.232.2", 
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
                        "start": "10.121.232.2", 
                        "end": "10.121.232.254"
                    }
                ], 
                "param": "allocation_pools"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "10.121.232.1", 
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
                "value": "10.121.232.0/24", 
                "param": "cidr"
            }
        ], 
        "resource_type": "subnet", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:subnet:1244d619-cc55-4bb7-b181-606776ba5e88:1:hid71", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "dummy subnet for firewall", 
            "enable_dhcp": true, 
            "tags": {}, 
            "network_id": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
            "dns_nameservers": [], 
            "dhcp_server_address": "10.121.232.2", 
            "ntp_servers": [], 
            "allocation_pools": [
                {
                    "start": "10.121.232.2", 
                    "end": "10.121.232.254"
                }
            ], 
            "gateway_ip": "10.121.232.1", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "ip_version": 4, 
            "host_routes": [], 
            "cidr": "10.121.232.0/24", 
            "id": "1244d619-cc55-4bb7-b181-606776ba5e88", 
            "name": "dummy-subnet"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/subnets/1244d619-cc55-4bb7-b181-606776ba5e88
{
    "stack_id": "subnet_1244d619-cc55-4bb7-b181-606776ba5e88", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "10.121.232.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "1244d619-cc55-4bb7-b181-606776ba5e88", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "10.121.232.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "6cac8ad5-636a-4b97-91e8-9dfc09559ed1", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "subnet:1244d619-cc55-4bb7-b181-606776ba5e88"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/subnets/1244d619-cc55-4bb7-b181-606776ba5e88
{
    "heat_outputs": [
        {
            "output_value": "10.121.232.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "1244d619-cc55-4bb7-b181-606776ba5e88", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "10.121.232.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "6cac8ad5-636a-4b97-91e8-9dfc09559ed1", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/subnets/1244d619-cc55-4bb7-b181-606776ba5e88
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"10.121.232.0/24\", \"description\": \"IP prefix of local subnet.\", \"output_key\": \"ip_prefix\"}, {\"output_value\": \"1244d619-cc55-4bb7-b181-606776ba5e88\", \"description\": \"The name of the local subnet.\", \"output_key\": \"name\"}, {\"output_value\": \"10.121.232.1\", \"description\": \"Default gateway of local subnet.\", \"output_key\": \"default_gateway\"}, {\"output_value\": \"73b2c401-a1f3-49fb-8612-8c755b37a28d\", \"description\": \"A unique id for the network.\", \"output_key\": \"network_id\"}, {\"output_value\": \"5a79909b-2bf3-4e26-8a9c-0bf6bb175457\", \"description\": \"IPAM this local subnet uses.\", \"output_key\": \"ipam\"}, {\"output_value\": \"6cac8ad5-636a-4b97-91e8-9dfc09559ed1\", \"description\": \"A unique id for the local subnet.\", \"output_key\": \"id\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
