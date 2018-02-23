# Stored data in etcd: Create Firewall

No stored data for "heat_templates" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/vnf_interfaces/c8fef8f8-a7a1-448f-ae76-81992e598016
{
    "body": {
        "status": "PENDING_CREATE", 
        "type": "user", 
        "name": "interface-0", 
        "network_id": null, 
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
        "vnf_instance_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb", 
        "slot_number": 0, 
        "port_id": "cdde9cfd-a898-4911-b812-b6849f611549", 
        "id": "c8fef8f8-a7a1-448f-ae76-81992e598016"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/vnf_interfaces/c8fef8f8-a7a1-448f-ae76-81992e598016
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
