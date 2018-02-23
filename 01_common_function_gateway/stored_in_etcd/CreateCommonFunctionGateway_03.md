# Stored data in etcd: Create Common Function Gateway

These are stored data for "heat_templates" in etcd.

* subnet

![scope](../../images/esi_interface.009.png)

These are stored data for "Create Common Function Gateway" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/subnets/e1353d56-b05a-43a9-b924-383ab0d64d7b
{
    "body": {
        "status": "PENDING_CREATE", 
        "description": "", 
        "enable_dhcp": true, 
        "tags": {}, 
        "network_id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "dns_nameservers": [], 
        "dhcp_server_address": "169.254.0.2", 
        "ntp_servers": [], 
        "allocation_pools": [
            {
                "start": "169.254.0.2", 
                "end": "169.254.127.254"
            }
        ], 
        "gateway_ip": null, 
        "ip_version": 4, 
        "host_routes": [], 
        "cidr": "169.254.0.0/17", 
        "id": "e1353d56-b05a-43a9-b924-383ab0d64d7b", 
        "name": "common_function_gw_access_subnet_5c241c51-2003-407a-a239-689fabd19022"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:subnet:e1353d56-b05a-43a9-b924-383ab0d64d7b:1:junpn
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "e1353d56-b05a-43a9-b924-383ab0d64d7b", 
        "handler": "heat_worker", 
        "job_name": "subnet:e1353d56-b05a-43a9-b924-383ab0d64d7b:1", 
        "dependency": [
            "create:heat_worker:network:f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57:1:7vfno"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "e1353d56-b05a-43a9-b924-383ab0d64d7b", 
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
                        "resource_id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57"
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
                "value": "169.254.0.2", 
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
                        "start": "169.254.0.2", 
                        "end": "169.254.127.254"
                    }
                ], 
                "param": "allocation_pools"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": null, 
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
                "value": "169.254.0.0/17", 
                "param": "cidr"
            }
        ], 
        "resource_type": "subnet", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:subnet:e1353d56-b05a-43a9-b924-383ab0d64d7b:1:junpn", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "", 
            "enable_dhcp": true, 
            "tags": {}, 
            "network_id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "dns_nameservers": [], 
            "dhcp_server_address": "169.254.0.2", 
            "ntp_servers": [], 
            "allocation_pools": [
                {
                    "start": "169.254.0.2", 
                    "end": "169.254.127.254"
                }
            ], 
            "gateway_ip": null, 
            "ip_version": 4, 
            "host_routes": [], 
            "cidr": "169.254.0.0/17", 
            "id": "e1353d56-b05a-43a9-b924-383ab0d64d7b", 
            "name": "common_function_gw_access_subnet_5c241c51-2003-407a-a239-689fabd19022"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/subnets/e1353d56-b05a-43a9-b924-383ab0d64d7b
{
    "stack_id": "subnet_e1353d56-b05a-43a9-b924-383ab0d64d7b", 
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "169.254.0.0/17", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "e1353d56-b05a-43a9-b924-383ab0d64d7b", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "0.0.0.0", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "9e61b626-a866-4ba5-b1c7-01935fdac3f4", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "subnet:e1353d56-b05a-43a9-b924-383ab0d64d7b"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/subnets/e1353d56-b05a-43a9-b924-383ab0d64d7b
{
    "heat_outputs": [
        {
            "output_value": "169.254.0.0/17", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "e1353d56-b05a-43a9-b924-383ab0d64d7b", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "0.0.0.0", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "9e61b626-a866-4ba5-b1c7-01935fdac3f4", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ]
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/subnets/e1353d56-b05a-43a9-b924-383ab0d64d7b
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"169.254.0.0/17\", \"description\": \"IP prefix of local subnet.\", \"output_key\": \"ip_prefix\"}, {\"output_value\": \"e1353d56-b05a-43a9-b924-383ab0d64d7b\", \"description\": \"The name of the local subnet.\", \"output_key\": \"name\"}, {\"output_value\": \"0.0.0.0\", \"description\": \"Default gateway of local subnet.\", \"output_key\": \"default_gateway\"}, {\"output_value\": \"f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57\", \"description\": \"A unique id for the network.\", \"output_key\": \"network_id\"}, {\"output_value\": \"aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa\", \"description\": \"IPAM this local subnet uses.\", \"output_key\": \"ipam\"}, {\"output_value\": \"9e61b626-a866-4ba5-b1c7-01935fdac3f4\", \"description\": \"A unique id for the local subnet.\", \"output_key\": \"id\"}]"
    }, 
    "version": 1, 
    "error": ""
}
```
