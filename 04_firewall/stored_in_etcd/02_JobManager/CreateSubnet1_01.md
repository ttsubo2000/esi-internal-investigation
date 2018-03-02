# Stored data in etcd: Create Subnet (dummy-net)

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
