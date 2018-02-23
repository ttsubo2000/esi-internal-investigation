[Return to Previous Page](00_vpn_gateway.md)

# 8. Clarification of interface in Sequence Diagram "Create Qos Option"
You can see the relations of "Qos Option" as following.

![Qos Option](resource/gohan_investigate_for_vpngw.009.png)

## 8.1. Sequence Diagram between gohan and etcd
This is a diagram that has been described as interfaces for "Qos Option" between gohan and etcd.

* Initinalizing gohan (but no use) ...
* Receiving HTTP Methods for Creating Resource ...

![Create Qos Option](diag/ESI_Sequence_Diagram_for_VPN_Gateway.014.png)


## 8.2. HTTP Methods for RESTful between Gohan and Client
This is JSON data for "Create Qos Option" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/qos_options
```
```
{
    "qos_option": {
        "bandwidth": "10",
        "incoming_policer_config": "action { loss-priority high then discard; } single-rate { color-blind; committed-information-rate 10m; committed-burst-size 187500000; excess-burst-size 187500000; }",
        "incoming_policer_name": "10M-GA-UP-VPN",
        "name": "10Mbps-Guaranteed",
        "outgoing_policer_config": "if-exceeding { bandwidth-limit 10m; burst-size-limit 187500000; } then discard;",
        "outgoing_policer_name": "10M-GA-DOWN-VPN",
        "qos_type": "guarantee",
        "service_type": "vpn",
        "vpn_service_id": "72b05fe5-88c6-4888-a6fb-feb793fffae8",
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f"
    }
}
```
![scope](../images/esi_interface.004.png)


## 8.3. Stored data in etcd after receiving HTTP Methods for RESTful
These are stored data for "Create Qos Option" in etcd.

* [Checking stored data for creating "qos_option"](stored_in_etcd/CreateQosOption_01.md)

![scope](../images/esi_interface.005.png)


## 8.4. Stored resource in gohan
As a result, checking resources regarding of "Qos Option" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client qos_option show --output-format json 4f59680b-52b6-41da-b15a-09946c155efd
{
    "qos_option": {
        "aws_service_id": null,
        "bandwidth": "10",
        "charge_type": null,
        "description": "",
        "ha_router_id": "f01ed0a6-7094-4e54-b14b-94657fff1efb",
        "id": "4f59680b-52b6-41da-b15a-09946c155efd",
        "incoming_policer_config": "action { loss-priority high then discard; } single-rate { color-blind; committed-information-rate 10m; committed-burst-size 187500000; excess-burst-size 187500000; }",
        "incoming_policer_name": "10M-GA-UP-VPN",
        "interdc_service_id": null,
        "internet_service_id": null,
        "name": "10Mbps-Guaranteed",
        "outgoing_policer_config": "if-exceeding { bandwidth-limit 10m; burst-size-limit 187500000; } then discard;",
        "outgoing_policer_name": "10M-GA-DOWN-VPN",
        "qos_type": "guarantee",
        "service_type": "vpn",
        "status": "ACTIVE",
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f",
        "vpn_service_id": "72b05fe5-88c6-4888-a6fb-feb793fffae8"
    }
}
```

[Return to Previous Page](00_vpn_gateway.md)
