# Stored data in etcd: Update Loadbalancer Interface

No stored data for "heat_templates" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/vnf_interfaces/3f1be05a-6cae-4f5e-9985-15f6f714d8dc
{
    "body": {
        "status": "PENDING_UPDATE", 
        "type": "user", 
        "description": null, 
        "network_id": "774acf45-316f-4431-b31b-08770b76d761", 
        "ip_address": "10.225.225.3", 
        "vnf_instance_id": "398d65ba-0060-456e-b415-5bc954450717", 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
        "slot_number": 1, 
        "virtual_ip_address": null, 
        "virtual_ip_properties": null, 
        "port_id": "23464cbc-d910-430a-93f7-3776ea07f992", 
        "id": "3f1be05a-6cae-4f5e-9985-15f6f714d8dc", 
        "name": "interface-1"
    }, 
    "version": 2, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/state/v2.0/vnf_interfaces/3f1be05a-6cae-4f5e-9985-15f6f714d8dc
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 2, 
    "error": ""
}
```
