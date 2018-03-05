# Stored data in etcd: Create Subnet (user-net)

```
/config/v2.0/subnets/c2c9520b-026d-444a-8db9-c1cb9d71c130
{
    "body": {
        "status": "PENDING_CREATE", 
        "description": "load_balancer subnet", 
        "enable_dhcp": true, 
        "tags": {}, 
        "network_id": "774acf45-316f-4431-b31b-08770b76d761", 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
        "dns_nameservers": [], 
        "dhcp_server_address": "10.225.225.2", 
        "ntp_servers": [], 
        "allocation_pools": [
            {
                "start": "10.225.225.2", 
                "end": "10.225.225.254"
            }
        ], 
        "gateway_ip": "10.225.225.1", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "ip_version": 4, 
        "host_routes": [], 
        "cidr": "10.225.225.0/24", 
        "id": "c2c9520b-026d-444a-8db9-c1cb9d71c130", 
        "name": "sample-lb-subnet"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
