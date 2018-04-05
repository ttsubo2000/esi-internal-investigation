# Stored data in etcd: Create Internet Service

```
/config/v2.0/internet_services/986a140f-81da-4e5c-afc3-26f463a85786
{
    "body": {
        "vrf_export_policy": "INSTANCE-USER_OUT", 
        "primary_ibgp_config_group": "InetGW2-RI-IBGP", 
        "description": "", 
        "zone": "jp1-zone1", 
        "default_static_routes_per_gateway": 32, 
        "ga_forwarding_class": "FC-INET-GA", 
        "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
        "inet_out_filter": "INET_OUT", 
        "secondary_ibgp_config_group": "InetGW1-RI-IBGP", 
        "vrf_config": "", 
        "name": "sample-internet-service", 
        "secondary_vrrp_config_group": "InetGW2-VRRP", 
        "uplink_import_policy": "INSTANCE-MASTER_IN", 
        "primary_vrrp_config_group": "InetGW1-VRRP", 
        "downlink_interfaces": [
            "2595e193-84a8-49dc-aa2e-7a68c60ea11e"
        ], 
        "be_forwarding_class": "FC-INET-BE", 
        "neighbour_prefix": "BGP-VIRTUAL-ROUTER-PEERS", 
        "inet_in_filter": "INET_IN", 
        "id": "986a140f-81da-4e5c-afc3-26f463a85786", 
        "vrf_import_policy": "INSTANCE-USER_IN", 
        "minimal_submask_length": 26
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
