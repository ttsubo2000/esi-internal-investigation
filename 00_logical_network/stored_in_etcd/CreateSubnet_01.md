# Stored data in etcd: Create Subnet

These are stored data for "heat_templates" in etcd.

* subnet

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/subnets/3cfa93ac-251a-4a60-9434-ff4c88bf3655
{
    "body": {
        "status": "PENDING_CREATE", 
        "description": "sample subnet", 
        "enable_dhcp": true, 
        "tags": {}, 
        "network_id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
        "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
        "dns_nameservers": [], 
        "dhcp_server_address": "192.168.200.2", 
        "ntp_servers": [], 
        "allocation_pools": [
            {
                "start": "192.168.200.2", 
                "end": "192.168.200.254"
            }
        ], 
        "gateway_ip": "192.168.200.1", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "ip_version": 4, 
        "host_routes": [], 
        "cidr": "192.168.200.0/24", 
        "id": "3cfa93ac-251a-4a60-9434-ff4c88bf3655", 
        "name": "sample-subnet"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/create:heat_worker:subnet:3cfa93ac-251a-4a60-9434-ff4c88bf3655:1:igwm1
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "3cfa93ac-251a-4a60-9434-ff4c88bf3655", 
        "handler": "heat_worker", 
        "job_name": "subnet:3cfa93ac-251a-4a60-9434-ff4c88bf3655:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "3cfa93ac-251a-4a60-9434-ff4c88bf3655", 
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
                        "resource_id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263"
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
                "value": "192.168.200.2", 
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
                        "start": "192.168.200.2", 
                        "end": "192.168.200.254"
                    }
                ], 
                "param": "allocation_pools"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "192.168.200.1", 
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
                "value": "192.168.200.0/24", 
                "param": "cidr"
            }
        ], 
        "resource_type": "subnet", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:subnet:3cfa93ac-251a-4a60-9434-ff4c88bf3655:1:igwm1", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "sample subnet", 
            "enable_dhcp": true, 
            "tags": {}, 
            "network_id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
            "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
            "dns_nameservers": [], 
            "dhcp_server_address": "192.168.200.2", 
            "ntp_servers": [], 
            "allocation_pools": [
                {
                    "start": "192.168.200.2", 
                    "end": "192.168.200.254"
                }
            ], 
            "gateway_ip": "192.168.200.1", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "ip_version": 4, 
            "host_routes": [], 
            "cidr": "192.168.200.0/24", 
            "id": "3cfa93ac-251a-4a60-9434-ff4c88bf3655", 
            "name": "sample-subnet"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/subnets/3cfa93ac-251a-4a60-9434-ff4c88bf3655
{
    "stack_id": "subnet_3cfa93ac-251a-4a60-9434-ff4c88bf3655", 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "192.168.200.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "3cfa93ac-251a-4a60-9434-ff4c88bf3655", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "192.168.200.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "15711909-5d0a-46c8-83f5-c739380ebbb9", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "subnet:3cfa93ac-251a-4a60-9434-ff4c88bf3655"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/subnets/3cfa93ac-251a-4a60-9434-ff4c88bf3655
{
    "heat_outputs": [
        {
            "output_value": "192.168.200.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "3cfa93ac-251a-4a60-9434-ff4c88bf3655", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "192.168.200.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "15711909-5d0a-46c8-83f5-c739380ebbb9", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/subnets/3cfa93ac-251a-4a60-9434-ff4c88bf3655
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"192.168.200.0/24\", \"description\": \"IP prefix of local subnet.\", \"output_key\": \"ip_prefix\"}, {\"output_value\": \"3cfa93ac-251a-4a60-9434-ff4c88bf3655\", \"description\": \"The name of the local subnet.\", \"output_key\": \"name\"}, {\"output_value\": \"192.168.200.1\", \"description\": \"Default gateway of local subnet.\", \"output_key\": \"default_gateway\"}, {\"output_value\": \"35bc496f-3c0e-46b4-a5c0-33810e8e7263\", \"description\": \"A unique id for the network.\", \"output_key\": \"network_id\"}, {\"output_value\": \"5a79909b-2bf3-4e26-8a9c-0bf6bb175457\", \"description\": \"IPAM this local subnet uses.\", \"output_key\": \"ipam\"}, {\"output_value\": \"15711909-5d0a-46c8-83f5-c739380ebbb9\", \"description\": \"A unique id for the local subnet.\", \"output_key\": \"id\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
