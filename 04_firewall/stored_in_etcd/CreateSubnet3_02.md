# Stored data in etcd: Create Subnet (user-net)

These are stored data for "heat_templates" in etcd.

* port

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ports/c18705d5-e40a-4bb7-94da-3dc9a93b32e5
{
    "body": {
        "status": "ACTIVE", 
        "description": "DHCP Server Port", 
        "allowed_address_pairs": [], 
        "admin_state_up": true, 
        "network_id": "82712b89-c35c-4276-83cb-818860d41f9e", 
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
                "subnet_id": "a11785e2-0c2b-4131-9144-349155f958f5", 
                "ip_address": "10.98.76.2"
            }
        ], 
        "id": "c18705d5-e40a-4bb7-94da-3dc9a93b32e5", 
        "security_groups": [], 
        "device_id": "a11785e2-0c2b-4131-9144-349155f958f5"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/ports/c18705d5-e40a-4bb7-94da-3dc9a93b32e5
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
