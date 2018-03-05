# Stored data in etcd: Create Subnet (admin-net)

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
