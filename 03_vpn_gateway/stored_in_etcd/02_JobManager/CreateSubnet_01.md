# Stored data in etcd: Create Subnet

```
/jobs/all/create:heat_worker:subnet:e825f4e4-ba44-4d9e-9578-a31ad45bedda:1:89l4t
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "e825f4e4-ba44-4d9e-9578-a31ad45bedda", 
        "handler": "heat_worker", 
        "job_name": "subnet:e825f4e4-ba44-4d9e-9578-a31ad45bedda:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "e825f4e4-ba44-4d9e-9578-a31ad45bedda", 
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
                        "resource_id": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2"
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
        "id": "create:heat_worker:subnet:e825f4e4-ba44-4d9e-9578-a31ad45bedda:1:89l4t", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "Sample Subnet", 
            "enable_dhcp": true, 
            "tags": {}, 
            "network_id": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2", 
            "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
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
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "ip_version": 4, 
            "host_routes": [], 
            "cidr": "172.16.101.0/24", 
            "id": "e825f4e4-ba44-4d9e-9578-a31ad45bedda", 
            "name": "sample-subnet"
        }
    }, 
    0
]
```
