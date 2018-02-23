# Stored data in etcd: Create Subnet (admin-net)

These are stored data for "heat_templates" in etcd.

* subnet

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/subnets/707847d0-89d9-4b98-93a2-8b376709c5f3
{
    "body": {
        "status": "PENDING_CREATE", 
        "description": "adminpod subnet", 
        "enable_dhcp": true, 
        "tags": {}, 
        "network_id": "168c1535-9001-49c7-bb05-21844570a83c", 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
        "dns_nameservers": [], 
        "dhcp_server_address": "100.64.193.2", 
        "ntp_servers": [], 
        "allocation_pools": [
            {
                "start": "100.64.193.2", 
                "end": "100.64.193.254"
            }
        ], 
        "gateway_ip": "100.64.193.1", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "ip_version": 4, 
        "host_routes": [
            {
                "nexthop": "100.64.193.1", 
                "destination": "172.26.10.0/24"
            }
        ], 
        "cidr": "100.64.193.0/24", 
        "id": "707847d0-89d9-4b98-93a2-8b376709c5f3", 
        "name": "adminpod-subnet"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/create:heat_worker:subnet:707847d0-89d9-4b98-93a2-8b376709c5f3:1:l7ka6
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "707847d0-89d9-4b98-93a2-8b376709c5f3", 
        "handler": "heat_worker", 
        "job_name": "subnet:707847d0-89d9-4b98-93a2-8b376709c5f3:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "707847d0-89d9-4b98-93a2-8b376709c5f3", 
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
                        "resource_id": "168c1535-9001-49c7-bb05-21844570a83c"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "168c1535-9001-49c7-bb05-21844570a83c"
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
                "value": "100.64.193.2", 
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
                        "start": "100.64.193.2", 
                        "end": "100.64.193.254"
                    }
                ], 
                "param": "allocation_pools"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "100.64.193.1", 
                "param": "gateway_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [
                    {
                        "destination": "172.26.10.0/24", 
                        "nexthop": "100.64.193.1"
                    }
                ], 
                "param": "host_routes"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "100.64.193.0/24", 
                "param": "cidr"
            }
        ], 
        "resource_type": "subnet", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:subnet:707847d0-89d9-4b98-93a2-8b376709c5f3:1:l7ka6", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "adminpod subnet", 
            "enable_dhcp": true, 
            "tags": {}, 
            "network_id": "168c1535-9001-49c7-bb05-21844570a83c", 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "dns_nameservers": [], 
            "dhcp_server_address": "100.64.193.2", 
            "ntp_servers": [], 
            "allocation_pools": [
                {
                    "start": "100.64.193.2", 
                    "end": "100.64.193.254"
                }
            ], 
            "gateway_ip": "100.64.193.1", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "ip_version": 4, 
            "host_routes": [
                {
                    "destination": "172.26.10.0/24", 
                    "nexthop": "100.64.193.1"
                }
            ], 
            "cidr": "100.64.193.0/24", 
            "id": "707847d0-89d9-4b98-93a2-8b376709c5f3", 
            "name": "adminpod-subnet"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/subnets/707847d0-89d9-4b98-93a2-8b376709c5f3
{
    "stack_id": "subnet_707847d0-89d9-4b98-93a2-8b376709c5f3", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "100.64.193.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "707847d0-89d9-4b98-93a2-8b376709c5f3", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "100.64.193.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "168c1535-9001-49c7-bb05-21844570a83c", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "a2fc1444-c7f4-4a72-8376-a920889c4a43", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "subnet:707847d0-89d9-4b98-93a2-8b376709c5f3"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/subnets/707847d0-89d9-4b98-93a2-8b376709c5f3
{
    "heat_outputs": [
        {
            "output_value": "100.64.193.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "707847d0-89d9-4b98-93a2-8b376709c5f3", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "100.64.193.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "168c1535-9001-49c7-bb05-21844570a83c", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "a2fc1444-c7f4-4a72-8376-a920889c4a43", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/subnets/707847d0-89d9-4b98-93a2-8b376709c5f3
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"100.64.193.0/24\", \"description\": \"IP prefix of local subnet.\", \"output_key\": \"ip_prefix\"}, {\"output_value\": \"707847d0-89d9-4b98-93a2-8b376709c5f3\", \"description\": \"The name of the local subnet.\", \"output_key\": \"name\"}, {\"output_value\": \"100.64.193.1\", \"description\": \"Default gateway of local subnet.\", \"output_key\": \"default_gateway\"}, {\"output_value\": \"168c1535-9001-49c7-bb05-21844570a83c\", \"description\": \"A unique id for the network.\", \"output_key\": \"network_id\"}, {\"output_value\": \"5a79909b-2bf3-4e26-8a9c-0bf6bb175457\", \"description\": \"IPAM this local subnet uses.\", \"output_key\": \"ipam\"}, {\"output_value\": \"a2fc1444-c7f4-4a72-8376-a920889c4a43\", \"description\": \"A unique id for the local subnet.\", \"output_key\": \"id\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
