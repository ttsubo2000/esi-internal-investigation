# Stored data in etcd: Create Subnet

```
/config/v2.0/subnets/e825f4e4-ba44-4d9e-9578-a31ad45bedda
{
    "body": {
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
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
