# Stored data in etcd: Create Subnet (user-net)

```
/config/v2.0/subnets/a11785e2-0c2b-4131-9144-349155f958f5
{
    "body": {
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
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
