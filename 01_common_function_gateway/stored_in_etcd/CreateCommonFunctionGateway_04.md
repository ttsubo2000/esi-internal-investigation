# Stored data in etcd: Create Common Function Gateway

These are stored data for "heat_templates" in etcd.

* port
* port_monitoring

![scope](../../images/esi_interface.011.png)

These are stored data for "Create Common Function Gateway" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ports/bbaac433-1023-4660-88f0-ccd8c2c26c89
{
    "body": {
        "status": "ACTIVE", 
        "description": "DHCP Server Port", 
        "allowed_address_pairs": [], 
        "admin_state_up": true, 
        "network_id": "f2de53ae-bc76-46f2-b2ae-a7eefa9d6e57", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "managed_by_service": false, 
        "attached": false, 
        "name": "dhcp-server-port", 
        "binding:vif_type": "vrouter", 
        "device_owner": "network:dhcp", 
        "fake_delete": false, 
        "mac_address": "00:00:5e:00:01:00", 
        "host_routes": [], 
        "fixed_ips": [
            {
                "subnet_id": "e1353d56-b05a-43a9-b924-383ab0d64d7b", 
                "ip_address": "169.254.0.2"
            }
        ], 
        "id": "bbaac433-1023-4660-88f0-ccd8c2c26c89", 
        "tags": {}, 
        "device_id": "e1353d56-b05a-43a9-b924-383ab0d64d7b"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/state/v2.0/ports/bbaac433-1023-4660-88f0-ccd8c2c26c89
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
