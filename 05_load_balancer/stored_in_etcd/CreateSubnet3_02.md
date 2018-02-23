# Stored data in etcd: Create Subnet (user-net)

These are stored data for "heat_templates" in etcd.

* port

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ports/6b5b32b0-e1fc-430d-9ae0-57306fab7285
{
    "body": {
        "status": "ACTIVE", 
        "description": "DHCP Server Port", 
        "allowed_address_pairs": [], 
        "admin_state_up": true, 
        "network_id": "774acf45-316f-4431-b31b-08770b76d761", 
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
                "subnet_id": "c2c9520b-026d-444a-8db9-c1cb9d71c130", 
                "ip_address": "10.225.225.2"
            }
        ], 
        "id": "6b5b32b0-e1fc-430d-9ae0-57306fab7285", 
        "security_groups": [], 
        "device_id": "c2c9520b-026d-444a-8db9-c1cb9d71c130"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/ports/6b5b32b0-e1fc-430d-9ae0-57306fab7285
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
