# Stored data in etcd: Create Qos Option

These are stored data for "heat_templates" in etcd.

* qos_option_vpn (no use)

![scope](../../images/esi_interface.009.png)

These are stored data for "Create Qos Option" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/qos_options/4f59680b-52b6-41da-b15a-09946c155efd
{
    "body": {
        "status": "PENDING_CREATE", 
        "qos_type": "guarantee", 
        "description": "", 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "incoming_policer_name": "10M-GA-UP-VPN", 
        "vpn_service_id": "72b05fe5-88c6-4888-a6fb-feb793fffae8", 
        "bandwidth": "10", 
        "outgoing_policer_config": "if-exceeding { bandwidth-limit 10m; burst-size-limit 187500000; } then discard;", 
        "incoming_policer_config": "action { loss-priority high then discard; } single-rate { color-blind; committed-information-rate 10m; committed-burst-size 187500000; excess-burst-size 187500000; }", 
        "outgoing_policer_name": "10M-GA-DOWN-VPN", 
        "service_type": "vpn", 
        "ha_router_id": "f01ed0a6-7094-4e54-b14b-94657fff1efb", 
        "id": "4f59680b-52b6-41da-b15a-09946c155efd", 
        "name": "10Mbps-Guaranteed"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/state/v2.0/qos_options/4f59680b-52b6-41da-b15a-09946c155efd
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
