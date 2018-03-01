# Stored data in etcd: Create Subnet

```
/config/v2.0/subnets/3cfa93ac-251a-4a60-9434-ff4c88bf3655
{
    "body": {
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
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
