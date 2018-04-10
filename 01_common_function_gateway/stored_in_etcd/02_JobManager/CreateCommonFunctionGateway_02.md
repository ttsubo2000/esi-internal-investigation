# Stored data in etcd: Create Common Function Gateway

```
/jobs/all/create:heat_worker:subnet:cf9356ae-b4e1-4a91-8193-089fdc12173d:1:7kdu4
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "cf9356ae-b4e1-4a91-8193-089fdc12173d", 
        "handler": "heat_worker", 
        "job_name": "subnet:cf9356ae-b4e1-4a91-8193-089fdc12173d:1", 
        "dependency": [
            "create:heat_worker:network:fc8814a7-eb1e-4f59-8422-7de500e72782:1:oodvi"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "cf9356ae-b4e1-4a91-8193-089fdc12173d", 
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
                        "resource_id": "fc8814a7-eb1e-4f59-8422-7de500e72782"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "fc8814a7-eb1e-4f59-8422-7de500e72782"
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
        "id": "create:heat_worker:subnet:cf9356ae-b4e1-4a91-8193-089fdc12173d:1:7kdu4", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "", 
            "enable_dhcp": true, 
            "tags": {}, 
            "network_id": "fc8814a7-eb1e-4f59-8422-7de500e72782", 
            "tenant_id": "c583ce78843344adbe5fd20f13620274", 
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
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "ip_version": 4, 
            "host_routes": [], 
            "cidr": "169.254.0.0/17", 
            "id": "cf9356ae-b4e1-4a91-8193-089fdc12173d", 
            "name": "common_function_gw_access_subnet_f649736d-1920-41eb-96af-d4e4fe192d0e"
        }
    }, 
    0
]
```
