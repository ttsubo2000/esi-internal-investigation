# Stored data in etcd: Create Subnet (admin-net)

```
/config/v2.0/subnets/c8090497-34be-456b-9186-377e918f3d50
{
    "body": {
        "status": "PENDING_CREATE", 
        "description": "adminpod subnet", 
        "enable_dhcp": true, 
        "tags": {}, 
        "network_id": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
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
        "id": "c8090497-34be-456b-9186-377e918f3d50", 
        "name": "adminpod-subnet"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
