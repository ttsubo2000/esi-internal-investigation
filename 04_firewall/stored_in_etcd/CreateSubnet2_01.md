# Stored data in etcd: Create Subnet (admin-net)

These are stored data for "heat_templates" in etcd.

* subnet

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/subnets/c8090497-34be-456b-9186-377e918f3d50
{
    "body": {
        "status": "PENDING_CREATE", 
        "description": "adminpod subnet", 
        "enable_dhcp": true, 
        "tags": {}, 
        "network_id": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
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
        "id": "c8090497-34be-456b-9186-377e918f3d50", 
        "name": "adminpod-subnet"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/create:heat_worker:subnet:c8090497-34be-456b-9186-377e918f3d50:1:du1dc
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "c8090497-34be-456b-9186-377e918f3d50", 
        "handler": "heat_worker", 
        "job_name": "subnet:c8090497-34be-456b-9186-377e918f3d50:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "c8090497-34be-456b-9186-377e918f3d50", 
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
                        "resource_id": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554"
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
        "id": "create:heat_worker:subnet:c8090497-34be-456b-9186-377e918f3d50:1:du1dc", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "adminpod subnet", 
            "enable_dhcp": true, 
            "tags": {}, 
            "network_id": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
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
            "id": "c8090497-34be-456b-9186-377e918f3d50", 
            "name": "adminpod-subnet"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/subnets/c8090497-34be-456b-9186-377e918f3d50
{
    "stack_id": "subnet_c8090497-34be-456b-9186-377e918f3d50", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "100.64.193.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "c8090497-34be-456b-9186-377e918f3d50", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "100.64.193.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "48f25db3-49e2-4bad-90d9-3fa333911d36", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "subnet:c8090497-34be-456b-9186-377e918f3d50"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/subnets/c8090497-34be-456b-9186-377e918f3d50
{
    "heat_outputs": [
        {
            "output_value": "100.64.193.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "c8090497-34be-456b-9186-377e918f3d50", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "100.64.193.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "48f25db3-49e2-4bad-90d9-3fa333911d36", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/subnets/c8090497-34be-456b-9186-377e918f3d50
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"100.64.193.0/24\", \"description\": \"IP prefix of local subnet.\", \"output_key\": \"ip_prefix\"}, {\"output_value\": \"c8090497-34be-456b-9186-377e918f3d50\", \"description\": \"The name of the local subnet.\", \"output_key\": \"name\"}, {\"output_value\": \"100.64.193.1\", \"description\": \"Default gateway of local subnet.\", \"output_key\": \"default_gateway\"}, {\"output_value\": \"75c2c3ec-7fe7-494c-a35c-db3f94d3a554\", \"description\": \"A unique id for the network.\", \"output_key\": \"network_id\"}, {\"output_value\": \"5a79909b-2bf3-4e26-8a9c-0bf6bb175457\", \"description\": \"IPAM this local subnet uses.\", \"output_key\": \"ipam\"}, {\"output_value\": \"48f25db3-49e2-4bad-90d9-3fa333911d36\", \"description\": \"A unique id for the local subnet.\", \"output_key\": \"id\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
