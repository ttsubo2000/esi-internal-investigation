# Stored data in etcd: Create Subnet

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
