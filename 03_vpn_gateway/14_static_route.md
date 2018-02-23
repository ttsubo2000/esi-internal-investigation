[Return to Previous Page](00_vpn_gateway.md)

# 14. Clarification of interface in Sequence Diagram "Create Static Route"
You can see the relations of "Static Route" as following.

![Static Route](resource/gohan_investigate_for_vpngw.015.png)

## 14.1. Sequence Diagram between gohan and etcd
This is a diagram that has been described as interfaces for "Static Route" between gohan and etcd.

* Initinalizing gohan ...
* Receiving HTTP Methods for Creating Resource ...

![Create Static Route](diag/ESI_Sequence_Diagram_for_VPN_Gateway.021.png)

## 14.2. Stored data in etcd after initinalizing gohan
These are stored data for "heat_templates" in etcd.

* [Checking stored data for "static_route_vpn"](../heat_template/static_route_vpn.md)


## 14.3. HTTP Methods for RESTful between Gohan and Client
This is JSON data for "Create Static Route" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/static_routes
```
```
{
    "static_route": {
        "description": "Sample Static-route",
        "destination": "192.168.0.0/24",
        "name": "sample-static-route",
        "nexthop": "172.16.101.1",
        "service_type": "vpn",
        "vpn_gw_id": "4fab887d-8f73-40e6-b2d8-2426255231bf",
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f"
    }
}
```
![scope](../images/esi_interface.004.png)


## 14.4. Stored data in etcd after receiving HTTP Methods for RESTful
These are stored data for "Create Static Route" in etcd.

* [Checking stored data for creating "static_route"](stored_in_etcd/CreateStaticRoute_01.md)

![scope](../images/esi_interface.005.png)


## 14.5. Stored heat-stack via heat-api
These are stored heat-stacks for "Create Static Route" in heat-engine.

* [Checking heat-stack of "static_route"](heat-stack/CreateStaticRoute_01.md)

![scope](../images/esi_interface.006.png)

## 14.6. Applying JUNOS Configurations via netconf
Checking configuration in Edge Router

* MX-1
```
[edit routing-instances vrf_gw_sample-ha-router-downlink_1025 routing-options]
+     static {
+         route 192.168.0.0/24 next-hop 172.16.101.1;
+     }

[edit]
```

* MX-2
```
[edit routing-instances vrf_gw_sample-ha-router-downlink_1025 routing-options]
+     static {
+         route 192.168.0.0/24 next-hop 172.16.101.1;
+     }

[edit]
```


## 14.7. Stored resource in gohan
As a result, checking resources regarding of "Static Route" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client static_route show --output-format json 1db45c0a-46cd-40af-a87e-718092df68b3
{
    "static_route": {
        "aws_gw_id": null,
        "description": "Sample Static-route",
        "destination": "192.168.0.0/24",
        "id": "1db45c0a-46cd-40af-a87e-718092df68b3",
        "interdc_gw_id": null,
        "internet_gw_id": null,
        "name": "sample-static-route",
        "nexthop": "172.16.101.1",
        "public_ip_id": null,
        "service_type": "vpn",
        "status": "ACTIVE",
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f",
        "vpn_gw_id": "4fab887d-8f73-40e6-b2d8-2426255231bf"
    }
}
```

[Return to Previous Page](00_vpn_gateway.md)
