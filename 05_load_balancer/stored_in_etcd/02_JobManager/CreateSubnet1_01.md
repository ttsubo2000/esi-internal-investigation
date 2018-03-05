# Stored data in etcd: Create Subnet (dummy-net)

```
/jobs/all/create:heat_worker:subnet:6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a:1:hxcet
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a", 
        "handler": "heat_worker", 
        "job_name": "subnet:6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a", 
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
                        "resource_id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f"
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
        "id": "create:heat_worker:subnet:6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a:1:hxcet", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "dummy subnet for load_balancer", 
            "enable_dhcp": true, 
            "tags": {}, 
            "network_id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
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
            "id": "6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a", 
            "name": "dummy-subnet"
        }
    }, 
    0
]
```
