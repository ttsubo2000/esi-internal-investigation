# Stored data in etcd: Create Subnet (user-net)

```
/jobs/all/create:heat_worker:subnet:a11785e2-0c2b-4131-9144-349155f958f5:1:5gauj
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "a11785e2-0c2b-4131-9144-349155f958f5", 
        "handler": "heat_worker", 
        "job_name": "subnet:a11785e2-0c2b-4131-9144-349155f958f5:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "a11785e2-0c2b-4131-9144-349155f958f5", 
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
                        "resource_id": "82712b89-c35c-4276-83cb-818860d41f9e"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "82712b89-c35c-4276-83cb-818860d41f9e"
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
                "value": "10.98.76.2", 
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
                        "start": "10.98.76.2", 
                        "end": "10.98.76.254"
                    }
                ], 
                "param": "allocation_pools"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "10.98.76.1", 
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
                "value": "10.98.76.0/24", 
                "param": "cidr"
            }
        ], 
        "resource_type": "subnet", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:subnet:a11785e2-0c2b-4131-9144-349155f958f5:1:5gauj", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "firewall subnet", 
            "enable_dhcp": true, 
            "tags": {}, 
            "network_id": "82712b89-c35c-4276-83cb-818860d41f9e", 
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
            "dns_nameservers": [], 
            "dhcp_server_address": "10.98.76.2", 
            "ntp_servers": [], 
            "allocation_pools": [
                {
                    "start": "10.98.76.2", 
                    "end": "10.98.76.254"
                }
            ], 
            "gateway_ip": "10.98.76.1", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "ip_version": 4, 
            "host_routes": [], 
            "cidr": "10.98.76.0/24", 
            "id": "a11785e2-0c2b-4131-9144-349155f958f5", 
            "name": "sample-fw-subnet"
        }
    }, 
    0
]
```
