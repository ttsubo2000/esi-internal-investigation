# Stored data in etcd: Create Qos Option

These are stored data for "heat_templates" in etcd.

* qos_option_internet (no use)

![scope](../../images/esi_interface.011.png)

These are stored data for "Create Qos Option" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/qos_options/e25f6309-c384-446e-bdc1-5241cb14890b
{
    "body": {
        "status": "PENDING_CREATE", 
        "qos_type": "guarantee", 
        "description": "", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "internet_service_id": "848e04de-733d-4f98-8971-bdb3b83e0296", 
        "incoming_policer_name": "10M-GA-UP-INET", 
        "bandwidth": "10", 
        "outgoing_policer_config": "if-exceeding { bandwidth-limit 10m; burst-size-limit 187500000; } then discard;", 
        "incoming_policer_config": "action { loss-priority high then discard; } single-rate { color-blind; committed-information-rate 10m; committed-burst-size 187500000; excess-burst-size 187500000; }", 
        "outgoing_policer_name": "10M-GA-DOWN-INET", 
        "service_type": "internet", 
        "ha_router_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17", 
        "id": "e25f6309-c384-446e-bdc1-5241cb14890b", 
        "name": "10Mbps-Guaranteed"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/state/v2.0/qos_options/e25f6309-c384-446e-bdc1-5241cb14890b
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
