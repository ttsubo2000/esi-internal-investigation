# Stored data in etcd: Create Subnet

```
/config/v2.0/subnets/67877f2d-0547-4cea-a6ce-2e3b937aa31b
{
    "body": {
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
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
