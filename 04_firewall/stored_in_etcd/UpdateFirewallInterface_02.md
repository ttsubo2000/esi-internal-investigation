# Stored data in etcd: Update Firewall Interface

No stored data for "heat_templates" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/vnf_interfaces/c6cf2771-be40-4d16-ba15-20a62f8b78f6
{
    "body": {
        "status": "PENDING_UPDATE", 
        "type": "user", 
        "description": null, 
        "network_id": "82712b89-c35c-4276-83cb-818860d41f9e", 
        "ip_address": "10.98.76.3", 
        "vnf_instance_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb", 
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
        "slot_number": 1, 
        "virtual_ip_address": null, 
        "virtual_ip_properties": null, 
        "port_id": "472879c4-4611-4762-a069-293e0081bcbf", 
        "id": "c6cf2771-be40-4d16-ba15-20a62f8b78f6", 
        "name": "interface-1"
    }, 
    "version": 2, 
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
    "version": 2, 
    "error": ""
}
```
