# Stored data in etcd: Create Loadbalancer

No stored data for "heat_templates" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/vnf_interfaces/9cf64483-bbf1-4e82-ae07-33febf43dbbf
{
    "body": {
        "status": "PENDING_CREATE", 
        "type": "management", 
        "name": "interface-0", 
        "network_id": "168c1535-9001-49c7-bb05-21844570a83c", 
        "ip_address": "100.64.193.3", 
        "vnf_instance_id": "398d65ba-0060-456e-b415-5bc954450717", 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
        "slot_number": 0, 
        "port_id": "ddc14be4-3480-4e97-a978-817b18f9904c", 
        "id": "9cf64483-bbf1-4e82-ae07-33febf43dbbf"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/vnf_interfaces/9cf64483-bbf1-4e82-ae07-33febf43dbbf
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
