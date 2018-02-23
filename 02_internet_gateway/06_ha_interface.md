[Return to Previous Page](00_internet_gateway.md)

# 6. Clarification of interface in Sequence Diagram "Create Ha Interface"
You can see the relations of "Ha Interface" as following.

![Ha Interface](resource/gohan_investigate_for_inetgw.007.png)

## 6.1. Sequence Diagram between gohan and etcd
This is a diagram that has been described as interfaces for "Ha Interface" between gohan and etcd.

* Initinalizing gohan ...
* Receiving HTTP Methods for Creating Resource ...

![Create Ha Interface](diag/ESI_Sequence_Diagram_for_Internet_Gateway.009.png)

## 6.2. Stored data in etcd after initinalizing gohan
These are stored data for "heat_templates" in etcd.

* [Checking stored data for "ha_interface_monitoring"](../heat_template/ha_interface_monitoring.md)


## 6.3. HTTP Methods for RESTful between Gohan and Client
This is JSON data for "Create Ha Interface" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/ha_interfaces
```
```
{
    "ha_interface": {
        "ha_router_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17",
        "link_type": "downlink",
        "maximum_be_bandwidth": 500,
        "maximum_ga_bandwidth": 500,
        "name": "sample-ha-router-downlink",
        "primary_interface_id": "1fda2a88-f7e9-4982-9ce2-d65c9611aae7",
        "secondary_interface_id": "469e4283-80e6-491c-830f-c483c1f7c695",
        "restricted_vlans": "0-1024,4094",
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f"
    }
}
```
![scope](../images/esi_interface.004.png)


## 6.4. Stored data in etcd after receiving HTTP Methods for RESTful
These are stored data for "Create Ha Interface" in etcd.

* [Checking stored data for creating "ha_interface"](stored_in_etcd/CreateHaInterface_01.md)

![scope](../images/esi_interface.005.png)


## 6.5. Stored resource in gohan
As a result, checking resources regarding of "Ha Interface" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client ha_interface show --output-format json 1205d3f2-7568-412a-a554-012340ab3172
{
    "ha_interface": {
        "admin_state_up": true,
        "available_be_bandwidth": 500,
        "available_ga_bandwidth": 500,
        "description": "",
        "gateway_instances_count": 0,
        "ha_router_id": "d4286c1d-86e7-42d3-9d84-a4d9daa3ae17",
        "id": "1205d3f2-7568-412a-a554-012340ab3172",
        "link_type": "downlink",
        "maximum_be_bandwidth": 500,
        "maximum_ga_bandwidth": 500,
        "name": "sample-ha-router-downlink",
        "primary_interface_id": "1fda2a88-f7e9-4982-9ce2-d65c9611aae7",
        "restricted_vlans": "0-1024,4094",
        "secondary_interface_id": "469e4283-80e6-491c-830f-c483c1f7c695",
        "status": "ACTIVE",
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f",
        "vlan_ids_available": 3069,
        "vlan_pool_state": "//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////+AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM="
    }
}
```

[Return to Previous Page](00_internet_gateway.md)
