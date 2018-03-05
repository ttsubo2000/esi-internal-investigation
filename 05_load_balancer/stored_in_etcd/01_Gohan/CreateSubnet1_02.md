# Stored data in etcd: Create Subnet (dummy-net)

```
/config/v2.0/ports/7864794a-fe4f-4aac-91a7-61c103f11f58
{
    "body": {
        "status": "ACTIVE", 
        "description": "DHCP Server Port", 
        "allowed_address_pairs": [], 
        "admin_state_up": true, 
        "network_id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
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
                "subnet_id": "6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a", 
                "ip_address": "10.121.232.2"
            }
        ], 
        "id": "7864794a-fe4f-4aac-91a7-61c103f11f58", 
        "security_groups": [], 
        "device_id": "6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
