# Stored data in etcd: Create Subnet

These are stored data for "heat_templates" in etcd.

* port
* port_monitoring

![scope](../../images/esi_interface.011.png)

These are stored data for "Create Subnet" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ports/0cd64eb2-32e8-4069-b5e4-9b718aa61b76
{
    "body": {
        "status": "ACTIVE", 
        "description": "DHCP Server Port", 
        "allowed_address_pairs": [], 
        "admin_state_up": true, 
        "network_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0", 
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
                "subnet_id": "a510f785-7758-4ce5-8fd4-c107d11b8e40", 
                "ip_address": "172.16.101.2"
            }
        ], 
        "id": "0cd64eb2-32e8-4069-b5e4-9b718aa61b76", 
        "tags": {}, 
        "device_id": "a510f785-7758-4ce5-8fd4-c107d11b8e40"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/state/v2.0/ports/0cd64eb2-32e8-4069-b5e4-9b718aa61b76
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
