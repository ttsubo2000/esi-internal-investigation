# Stored data in etcd: Create Subnet (dummy-net)

```
/config/v2.0/subnets/1244d619-cc55-4bb7-b181-606776ba5e88
{
    "body": {
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
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
