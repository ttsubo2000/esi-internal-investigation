# Stored data in etcd: Create Subnet

```
/config/v2.0/ports/3836f376-21ad-4ec2-975b-b7f0c671c5c8
{
    "body": {
        "status": "ACTIVE", 
        "description": "DHCP Server Port", 
        "allowed_address_pairs": [], 
        "admin_state_up": true, 
        "network_id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
        "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
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
                "subnet_id": "3cfa93ac-251a-4a60-9434-ff4c88bf3655", 
                "ip_address": "192.168.200.2"
            }
        ], 
        "id": "3836f376-21ad-4ec2-975b-b7f0c671c5c8", 
        "security_groups": [], 
        "device_id": "3cfa93ac-251a-4a60-9434-ff4c88bf3655"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
