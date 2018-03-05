# Stored data in etcd: Create Subnet (admin-net)

```
/config/v2.0/subnets/707847d0-89d9-4b98-93a2-8b376709c5f3
{
    "body": {
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
                "nexthop": "100.64.193.1", 
                "destination": "172.26.10.0/24"
            }
        ], 
        "cidr": "100.64.193.0/24", 
        "id": "707847d0-89d9-4b98-93a2-8b376709c5f3", 
        "name": "adminpod-subnet"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
