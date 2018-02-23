# Stored data in etcd: Create Subnet

These are stored data for "heat_templates" in etcd.

* port
* port_monitoring

![scope](../../images/esi_interface.011.png)

These are stored data for "Create Subnet" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ports/3388400c-5e25-4b97-8210-2a796927f2e7
{
    "body": {
        "status": "ACTIVE", 
        "description": "DHCP Server Port", 
        "allowed_address_pairs": [], 
        "admin_state_up": true, 
        "network_id": "bb69041d-c654-4e9f-a763-afd4333275bc", 
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
                "subnet_id": "b4f0c956-2fe0-4634-b7c8-22bfd8095aaf", 
                "ip_address": "172.16.101.2"
            }
        ], 
        "id": "3388400c-5e25-4b97-8210-2a796927f2e7", 
        "tags": {}, 
        "device_id": "b4f0c956-2fe0-4634-b7c8-22bfd8095aaf"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/state/v2.0/ports/3388400c-5e25-4b97-8210-2a796927f2e7
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
