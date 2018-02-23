# Stored data in kafka: Create Vpn Interface

These are stored data for "Create Vpn Interface" in kafka.

### topic "monitor_vpn_interface"
```
{
    "gohan_resource_type": "vpn_interfaces",
    "name": "primary",
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f",
    "version": 1,
    "action": "create",
    "gohan_id": "0bea303d-b6eb-4edc-83ef-e32f915d3047",
    "properties": {
        "instance": "vrf_gw_sample-ha-router-downlink_1025",
        "host": "10.79.5.185",
        "peer_address": "192.168.8.1",
        "login": "esi",
        "password": "esiesi0000",
        "port": 830
    }
}
```
```
{
    "gohan_resource_type": "vpn_interfaces",
    "name": "secondary",
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f",
    "version": 1,
    "action": "create",
    "gohan_id": "0bea303d-b6eb-4edc-83ef-e32f915d3047",
    "properties": {
        "instance": "vrf_gw_sample-ha-router-downlink_1025",
        "host": "10.79.5.184",
        "peer_address": "192.168.8.5",
        "login": "esi",
        "password": "esiesi0000",
        "port": 830
    }
}
```
