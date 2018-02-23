# Stored data in etcd: Create Loadbalancer

No stored data for "heat_templates" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/vnf_interfaces/848a926b-40ec-455a-a87c-e960c56b3dba
{
    "body": {
        "status": "PENDING_CREATE", 
        "type": "user", 
        "name": "interface-2", 
        "network_id": null, 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
        "vnf_instance_id": "398d65ba-0060-456e-b415-5bc954450717", 
        "slot_number": 2, 
        "port_id": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f", 
        "id": "848a926b-40ec-455a-a87c-e960c56b3dba"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/state/v2.0/vnf_interfaces/848a926b-40ec-455a-a87c-e960c56b3dba
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
