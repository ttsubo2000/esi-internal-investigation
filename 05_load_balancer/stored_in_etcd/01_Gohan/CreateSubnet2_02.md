# Stored data in etcd: Create Subnet (admin-net)

```
/config/v2.0/ports/ff724cd0-02ef-42e0-9510-1ea784ddaa8c
{
    "body": {
        "status": "ACTIVE", 
        "description": "DHCP Server Port", 
        "allowed_address_pairs": [], 
        "admin_state_up": true, 
        "network_id": "168c1535-9001-49c7-bb05-21844570a83c", 
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
                "subnet_id": "707847d0-89d9-4b98-93a2-8b376709c5f3", 
                "ip_address": "100.64.193.2"
            }
        ], 
        "id": "ff724cd0-02ef-42e0-9510-1ea784ddaa8c", 
        "security_groups": [], 
        "device_id": "707847d0-89d9-4b98-93a2-8b376709c5f3"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
