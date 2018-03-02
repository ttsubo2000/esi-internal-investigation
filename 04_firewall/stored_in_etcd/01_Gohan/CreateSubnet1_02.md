# Stored data in etcd: Create Subnet (dummy-net)

```
/config/v2.0/ports/db7b07e7-5fb8-4400-9a64-f3b1df8038f2
{
    "body": {
        "status": "ACTIVE", 
        "description": "DHCP Server Port", 
        "allowed_address_pairs": [], 
        "admin_state_up": true, 
        "network_id": "73b2c401-a1f3-49fb-8612-8c755b37a28d", 
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
        "managed_by_service": false, 
        "attached": false, 
        "name": "dhcp-server-port", 
        "binding:vif_type": "vrouter", 
        "device_owner": "network:dhcp", 
        "tags": {}, 
        "fake_delete": false, 
        "orchestration_state": "NO_STATE", 
        "mac_address": "00:00:5e:00:01:00", 
        "host_routes": [], 
        "fixed_ips": [
            {
                "subnet_id": "1244d619-cc55-4bb7-b181-606776ba5e88", 
                "ip_address": "10.121.232.2"
            }
        ], 
        "id": "db7b07e7-5fb8-4400-9a64-f3b1df8038f2", 
        "security_groups": [], 
        "device_id": "1244d619-cc55-4bb7-b181-606776ba5e88"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
