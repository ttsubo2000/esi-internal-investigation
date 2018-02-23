# Stored data in etcd: Create Firewall

No stored data for "heat_templates" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/vnf_interfaces/c6cf2771-be40-4d16-ba15-20a62f8b78f6
{
    "body": {
        "status": "PENDING_CREATE", 
        "type": "user", 
        "name": "interface-1", 
        "network_id": null, 
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
        "vnf_instance_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb", 
        "slot_number": 1, 
        "port_id": "dea87c7b-b43f-4936-8e32-8995b038b3f8", 
        "id": "c6cf2771-be40-4d16-ba15-20a62f8b78f6"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/vnf_interfaces/c6cf2771-be40-4d16-ba15-20a62f8b78f6
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
