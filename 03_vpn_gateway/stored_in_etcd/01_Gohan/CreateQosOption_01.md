# Stored data in etcd: Create Qos Option

```
/config/v2.0/qos_options/d35a3c95-8647-44d7-b32f-405b77d77f51
{
    "body": {
        "status": "PENDING_CREATE", 
        "qos_type": "guarantee", 
        "outgoing_policer_name": "10M-GA-DOWN-VPN", 
        "description": "", 
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
        "incoming_policer_name": "10M-GA-UP-VPN", 
        "vpn_service_id": "c8d57f7e-b439-475e-a6fb-ee2594390177", 
        "bandwidth": "10", 
        "outgoing_policer_config": "if-exceeding { bandwidth-limit 10m; burst-size-limit 187500000; } then discard;", 
        "incoming_policer_config": "action { loss-priority high then discard; } single-rate { color-blind; committed-information-rate 10m; committed-burst-size 187500000; excess-burst-size 187500000; }", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "service_type": "vpn", 
        "ha_router_id": "8c233862-895f-4cca-b377-c353e733c768", 
        "id": "d35a3c95-8647-44d7-b32f-405b77d77f51", 
        "name": "10Mbps-Guaranteed"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
