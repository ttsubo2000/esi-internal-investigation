# Stored data in etcd: Create Vpn Interface

```
/config/v2.0/vpn_interfaces/07d4f1fc-5142-4fae-b115-627fc009e222
{
    "body": {
        "status": "PENDING_CREATE", 
        "bgp_remote_as": "9598", 
        "description": "Sample Vpn-interface", 
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
        "vpn_gw_id": "b1da850c-3344-4de2-aa18-d96a30b54f69", 
        "primary": {
            "bgp_peer_ip": "192.168.8.1", 
            "ip_address": "192.168.8.2/30", 
            "bgp_router_id": "192.168.8.2"
        }, 
        "operational_state": "NO_STATE", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "bgp_md5": "test", 
        "secondary": {
            "bgp_peer_ip": "192.168.8.5", 
            "ip_address": "192.168.8.6/30", 
            "bgp_router_id": "192.168.8.6"
        }, 
        "id": "07d4f1fc-5142-4fae-b115-627fc009e222", 
        "name": "sample-vpn-interface"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
