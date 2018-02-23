# Stored data in etcd: Create Subnet (admin-net)

These are stored data for "heat_templates" in etcd.

* port

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ports/10de1073-2a60-4bbc-810b-642537ad19bf
{
    "body": {
        "status": "ACTIVE", 
        "description": "DHCP Server Port", 
        "allowed_address_pairs": [], 
        "admin_state_up": true, 
        "network_id": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
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
                "subnet_id": "c8090497-34be-456b-9186-377e918f3d50", 
                "ip_address": "100.64.193.2"
            }
        ], 
        "id": "10de1073-2a60-4bbc-810b-642537ad19bf", 
        "security_groups": [], 
        "device_id": "c8090497-34be-456b-9186-377e918f3d50"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/ports/10de1073-2a60-4bbc-810b-642537ad19bf
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
