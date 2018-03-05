# Stored data in etcd: Create Subnet (dummy-net)

```
/config/v2.0/subnets/6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a
{
    "body": {
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
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
