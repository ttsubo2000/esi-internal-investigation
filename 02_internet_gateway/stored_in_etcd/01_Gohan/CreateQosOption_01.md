# Stored data in etcd: Create Qos Option

```
/config/v2.0/qos_options/0e6b35d9-d74d-4d3a-922a-d79b9df9b78c
{
    "body": {
        "status": "PENDING_CREATE", 
        "qos_type": "guarantee", 
        "outgoing_policer_name": "10M-GA-DOWN-INET", 
        "description": "", 
        "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
        "internet_service_id": "986a140f-81da-4e5c-afc3-26f463a85786", 
        "incoming_policer_name": "10M-GA-UP-INET", 
        "bandwidth": "10", 
        "outgoing_policer_config": "if-exceeding { bandwidth-limit 10m; burst-size-limit 187500000; } then discard;", 
        "incoming_policer_config": "action { loss-priority high then discard; } single-rate { color-blind; committed-information-rate 10m; committed-burst-size 187500000; excess-burst-size 187500000; }", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "service_type": "internet", 
        "ha_router_id": "add04ae7-e48a-4583-a726-bed5f3b748c4", 
        "id": "0e6b35d9-d74d-4d3a-922a-d79b9df9b78c", 
        "name": "10Mbps-Guaranteed"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
