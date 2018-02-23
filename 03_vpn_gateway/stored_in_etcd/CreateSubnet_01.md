# Stored data in etcd: Create Subnet

These are stored data for "heat_templates" in etcd.

* subnet

![scope](../../images/esi_interface.009.png)

These are stored data for "Create Subnet" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/subnets/b4f0c956-2fe0-4634-b7c8-22bfd8095aaf
{
    "body": {
        "status": "PENDING_CREATE", 
        "description": "Sample Subnet", 
        "enable_dhcp": true, 
        "tags": {}, 
        "network_id": "bb69041d-c654-4e9f-a763-afd4333275bc", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "dns_nameservers": [], 
        "dhcp_server_address": "172.16.101.2", 
        "ntp_servers": [], 
        "allocation_pools": [
            {
                "start": "172.16.101.2", 
                "end": "172.16.101.254"
            }
        ], 
        "gateway_ip": "172.16.101.1", 
        "ip_version": 4, 
        "host_routes": [], 
        "cidr": "172.16.101.0/24", 
        "id": "b4f0c956-2fe0-4634-b7c8-22bfd8095aaf", 
        "name": "sample-subnet"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:subnet:b4f0c956-2fe0-4634-b7c8-22bfd8095aaf:1:7upde
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "b4f0c956-2fe0-4634-b7c8-22bfd8095aaf", 
        "handler": "heat_worker", 
        "job_name": "subnet:b4f0c956-2fe0-4634-b7c8-22bfd8095aaf:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "b4f0c956-2fe0-4634-b7c8-22bfd8095aaf", 
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
                        "resource_id": "bb69041d-c654-4e9f-a763-afd4333275bc"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "bb69041d-c654-4e9f-a763-afd4333275bc"
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
                "value": "172.16.101.2", 
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
                        "start": "172.16.101.2", 
                        "end": "172.16.101.254"
                    }
                ], 
                "param": "allocation_pools"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "172.16.101.1", 
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
                "value": "172.16.101.0/24", 
                "param": "cidr"
            }
        ], 
        "resource_type": "subnet", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:subnet:b4f0c956-2fe0-4634-b7c8-22bfd8095aaf:1:7upde", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "Sample Subnet", 
            "enable_dhcp": true, 
            "tags": {}, 
            "network_id": "bb69041d-c654-4e9f-a763-afd4333275bc", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "dns_nameservers": [], 
            "dhcp_server_address": "172.16.101.2", 
            "ntp_servers": [], 
            "allocation_pools": [
                {
                    "start": "172.16.101.2", 
                    "end": "172.16.101.254"
                }
            ], 
            "gateway_ip": "172.16.101.1", 
            "ip_version": 4, 
            "host_routes": [], 
            "cidr": "172.16.101.0/24", 
            "id": "b4f0c956-2fe0-4634-b7c8-22bfd8095aaf", 
            "name": "sample-subnet"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/subnets/b4f0c956-2fe0-4634-b7c8-22bfd8095aaf
{
    "stack_id": "subnet_b4f0c956-2fe0-4634-b7c8-22bfd8095aaf", 
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "172.16.101.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "b4f0c956-2fe0-4634-b7c8-22bfd8095aaf", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "172.16.101.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "bb69041d-c654-4e9f-a763-afd4333275bc", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "8f9e2ede-c3b4-438e-888d-55e326ec29a9", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "subnet:b4f0c956-2fe0-4634-b7c8-22bfd8095aaf"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/subnets/b4f0c956-2fe0-4634-b7c8-22bfd8095aaf
{
    "heat_outputs": [
        {
            "output_value": "172.16.101.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "b4f0c956-2fe0-4634-b7c8-22bfd8095aaf", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "172.16.101.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "bb69041d-c654-4e9f-a763-afd4333275bc", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "8f9e2ede-c3b4-438e-888d-55e326ec29a9", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ]
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/subnets/b4f0c956-2fe0-4634-b7c8-22bfd8095aaf
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"172.16.101.0/24\", \"description\": \"IP prefix of local subnet.\", \"output_key\": \"ip_prefix\"}, {\"output_value\": \"b4f0c956-2fe0-4634-b7c8-22bfd8095aaf\", \"description\": \"The name of the local subnet.\", \"output_key\": \"name\"}, {\"output_value\": \"172.16.101.1\", \"description\": \"Default gateway of local subnet.\", \"output_key\": \"default_gateway\"}, {\"output_value\": \"bb69041d-c654-4e9f-a763-afd4333275bc\", \"description\": \"A unique id for the network.\", \"output_key\": \"network_id\"}, {\"output_value\": \"aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa\", \"description\": \"IPAM this local subnet uses.\", \"output_key\": \"ipam\"}, {\"output_value\": \"8f9e2ede-c3b4-438e-888d-55e326ec29a9\", \"description\": \"A unique id for the local subnet.\", \"output_key\": \"id\"}]"
    }, 
    "version": 1, 
    "error": ""
}
```
