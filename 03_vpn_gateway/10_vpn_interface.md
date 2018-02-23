[Return to Previous Page](00_vpn_gateway.md)

# 10. Clarification of interface in Sequence Diagram "Create Vpn Interface"
You can see the relations of "Vpn Interface" as following.

![Vpn Interface](resource/gohan_investigate_for_vpngw.011.png)

## 10.1. Sequence Diagram between gohan and etcd
This is a diagram that has been described as interfaces for "Vpn Interface" between gohan and etcd.

* Initinalizing gohan ...
* Receiving HTTP Methods for Creating Resource ...

![Create Vpn Interface](diag/ESI_Sequence_Diagram_for_VPN_Gateway.016.png)

## 10.2. Stored data in etcd after initinalizing gohan
These are stored data for "heat_templates" in etcd.

* [Checking stored data for "vpn_interface"](../heat_template/vpn_interface.md)
* [Checking stored data for "vpn_gateway"](../heat_template/vpn_gateway.md)
* [Checking stored data for "vpn_interface_monitoring"](../heat_template/vpn_interface_monitoring.md)
* [Checking stored data for "vpn_gateway_monitoring"](../heat_template/vpn_gateway_monitoring.md)


## 10.3. HTTP Methods for RESTful between Gohan and Client
This is JSON data for "Create Vpn Interface" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/vpn_interfaces
```
```
{
    "vpn_interface": {
        "bgp_md5": "test",
        "bgp_remote_as": "9598",
        "description": "Sample Vpn-interface",
        "name": "sample-vpn-interface",

        "primary": {
            "bgp_peer_ip": "192.168.8.1",
            "bgp_router_id": "192.168.8.2",
            "ip_address": "192.168.8.2/30"
        },
        "secondary": {
            "bgp_peer_ip": "192.168.8.5",
            "bgp_router_id": "192.168.8.6",
            "ip_address": "192.168.8.6/30"
        },
        "vpn_gw_id": "4fab887d-8f73-40e6-b2d8-2426255231bf",
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f"
    }
}
```
![scope](../images/esi_interface.004.png)


## 10.4. Stored data in etcd after receiving HTTP Methods for RESTful
These are stored data for "Create Vpn Interface" in etcd.

* [Checking stored data for creating "vpn_interface"](stored_in_etcd/CreateVpnInterface_01.md)
* [Checking stored data for creating "vpn_gateway"](stored_in_etcd/CreateVpnInterface_02.md)

![scope](../images/esi_interface.005.png)


## 10.5. Stored heat-stack via heat-api
These are stored heat-stacks for "Create Vpn Interface" in heat-engine.

* [Checking heat-stack of "vpn_interface" for creating at "(a)" in section "10.1."](heat-stack/CreateVpnInterface_01.md)
* [Checking heat-stack of "vpn_gateway" for updating at "(b)" in section "10.1."](heat-stack/CreateVpnInterface_02.md)

![scope](../images/esi_interface.006.png)


## 11.6. Applying JUNOS Configurations via netconf
Checking configuration in Edge Router

* MX-1
```
[edit interfaces ge-0/0/1 unit 122]
+     family inet {
+         address 192.168.8.6/30;
+     }

[edit routing-instances vrf_gw_sample-ha-router-downlink_1025]
+    routing-options {
+        router-id 192.168.8.6;
+        autonomous-system 65101;
+    }
+    protocols {
+        bgp {
+            group CloudGW1 {
+                apply-groups VPNGW2-RI-EBGP;
+                local-address 192.168.8.6;
+                peer-as 9598;
+                neighbor 192.168.8.5 {
+                    authentication-key "$9$-/d2aji.5z6qm"; ## SECRET-DATA
+                }
+            }
+        }
+    }

[edit]
```

* MX-2
```
[edit interfaces ge-0/0/1 unit 122]
+     family inet {
+         address 192.168.8.2/30;
+     }

[edit routing-instances vrf_gw_sample-ha-router-downlink_1025]
+    routing-options {
+        router-id 192.168.8.2;
+        autonomous-system 65101;
+    }
+    protocols {
+        bgp {
+            group CloudGW1 {
+                apply-groups VPNGW1-RI-EBGP;
+                local-address 192.168.8.2;
+                peer-as 9598;
+                neighbor 192.168.8.1 {
+                    authentication-key "$9$FNex3A0Ehrv87yl"; ## SECRET-DATA
+                }
+            }
+        }
+    }
```

## 10.7. Stored resource for monitoring in Kafka
This is JSON data for "Create Vpn Interface" between monitoring-worker and kafka

* [Checking the topic "monitor_logical_port" for monitoring "vpn_interface"](stored_in_kafka/CreateVpnInterface_01.md)
* [Checking the topic "monitor_vpn_interface" for monitoring "vpn_interface"](stored_in_kafka/CreateVpnInterface_02.md)

![scope](../images/esi_interface.007.png)


## 10.8. Stored resource in gohan
As a result, checking resources regarding of "Vpn Interface" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client vpn_interface show --output-format json 0bea303d-b6eb-4edc-83ef-e32f915d3047
{
    "vpn_interface": {
        "bgp_md5": "test",
        "bgp_remote_as": "9598",
        "description": "Sample Vpn-interface",
        "id": "0bea303d-b6eb-4edc-83ef-e32f915d3047",
        "name": "sample-vpn-interface",
        "primary": {
            "bgp_peer_ip": "192.168.8.1",
            "bgp_router_id": "192.168.8.2",
            "ip_address": "192.168.8.2/30"
        },
        "secondary": {
            "bgp_peer_ip": "192.168.8.5",
            "bgp_router_id": "192.168.8.6",
            "ip_address": "192.168.8.6/30"
        },
        "status": "ACTIVE",
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f",
        "vpn_gw_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
    }
}
```
* Checking resource_mapping via gohan client
```
$ gohan client resource_mapping list --output-format json
{
    "resource_mappings": [
        {
            "created": 1.494478858e+09,
            "deleted": null,
            "id": "1d5dcf8f-40f5-4780-8023-63bc1dd771ac",
            "mapped_id": "10.79.5.185-ge-0/0/1.122",
            "relation": "primary",
            "resource_id": "0bea303d-b6eb-4edc-83ef-e32f915d3047",
            "resource_type": "vpn_interface",
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f"
        },
        {
            "created": 1.494478864e+09,
            "deleted": null,
            "id": "2f46f2b3-81f2-45d7-9f66-e64d131bb20b",
            "mapped_id": "10.79.5.185-a3a62a37-5657-4822-98e0-991ab63f0e96",
            "relation": "instance",
            "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf",
            "resource_type": "vpn_gateway",
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f"
        },
        {
            "created": 1.494478858e+09,
            "deleted": null,
            "id": "4f69c6a1-e11b-4fae-bd0b-babe7df48380",
            "mapped_id": "10.79.5.184-ge-0/0/1.122",
            "relation": "secondary",
            "resource_id": "0bea303d-b6eb-4edc-83ef-e32f915d3047",
            "resource_type": "vpn_interface",
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f"
        },
        {
            "created": 1.494478827e+09,
            "deleted": 1.494478858e+09,
            "id": "7806e79c-7403-462f-abd4-57d4f4f20f54",
            "mapped_id": "10.79.5.185-a3a62a37-5657-4822-98e0-991ab63f0e96",
            "relation": "instance",
            "resource_id": "4fab887d-8f73-40e6-b2d8-2426255231bf",
            "resource_type": "vpn_gateway",
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f"
        }
    ]
}
```
* Checking another resources via gohan client
```
$ gohan client vpn_gateway show --output-format json 4fab887d-8f73-40e6-b2d8-2426255231bf
{
    "vpn_gateway": {
        "connected_vpn_interface": "0bea303d-b6eb-4edc-83ef-e32f915d3047",
        "description": "this resource is vpn-gateway",
        "downlink_interface_id": "a3a62a37-5657-4822-98e0-991ab63f0e96",
        "downlink_vlan_id": "1025",
        "id": "4fab887d-8f73-40e6-b2d8-2426255231bf",
        "local_as_number": "65101",
        "maximum_static_routes": 32,
        "name": "sample-vpn-gateway",
        "primary_logical_downlink_interface_name": "ae0.1025",
        "primary_logical_uplink_interface_name": "ge-0/0/1.122",
        "qos_option_id": "4f59680b-52b6-41da-b15a-09946c155efd",
        "secondary_logical_downlink_interface_name": "ae0.1025",
        "secondary_logical_uplink_interface_name": "ge-0/0/1.122",
        "status": "ACTIVE",
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f",
        "uplink_interface_id": "5e552b8f-cd5a-454c-a224-33f7da0afa24",
        "uplink_vlan_id": "122",
        "vpn_service_id": "72b05fe5-88c6-4888-a6fb-feb793fffae8",
        "vrf_name": "vrf_gw_sample-ha-router-downlink_1025"
    }
}
```

[Return to Previous Page](00_vpn_gateway.md)
