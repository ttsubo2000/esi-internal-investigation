# Stored data in etcd: Create Subnet

```
/jobs/all/create:heat_worker:subnet:67877f2d-0547-4cea-a6ce-2e3b937aa31b:1:gqv2s
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "67877f2d-0547-4cea-a6ce-2e3b937aa31b", 
        "handler": "heat_worker", 
        "job_name": "subnet:67877f2d-0547-4cea-a6ce-2e3b937aa31b:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "67877f2d-0547-4cea-a6ce-2e3b937aa31b", 
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
                        "resource_id": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e"
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
        "id": "create:heat_worker:subnet:67877f2d-0547-4cea-a6ce-2e3b937aa31b:1:gqv2s", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "Sample Subnet", 
            "enable_dhcp": true, 
            "tags": {}, 
            "network_id": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e", 
            "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
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
            "id": "67877f2d-0547-4cea-a6ce-2e3b937aa31b", 
            "name": "sample-subnet"
        }
    }, 
    0
]
```
