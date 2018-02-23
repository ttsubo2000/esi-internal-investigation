[Return to Previous Page](00_fire_wall.md)

# 3. Clarification of interface in Sequence Diagram "Create Network for admin-net"
You can see the relations of "Network" as following.

![Network](resource/gohan_investigate_for_firewall.004.png)


## 3.1. Stored data in etcd after initinalizing gohan

![scope](../images/ESI_Sequence_diagram.002.png)

These are stored data for "heat_templates" in etcd.

* [Checking stored data for "network"](../heat_template/network.md)



## 3.2. HTTP Methods for RESTful between Gohan and Client

![scope](../images/ESI_Sequence_diagram.003.png)

This is JSON data for "Create Network" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/networks
```
```
{
    "network": {
        "admin_state_up": true,
        "description": "adminpod network",
        "name": "adminpod-net",
        "plane": "data",
        "tags": {},
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099"
    }
}
```



## 3.3. Stored data in etcd after receiving HTTP Methods for RESTful

![scope](../images/ESI_Sequence_diagram.004.png)

These are stored data for "Create Network" in etcd.

* [Checking stored data for creating "network"](stored_in_etcd/CreateNetwork2_01.md)



## 3.4. Stored heat-stack via heat-api

![scope](../images/ESI_Sequence_diagram.005.png)

These are stored heat-stacks for "Create Network" in heat-engine.

* [Checking heat-stack of "network"](heat-stack/CreateNetwork2_01.md)



## 3.5. Stored resource in gohan
As a result, checking resources regarding of "Network" in gohan.

* Checking the target of resources via neutron client
```
$ neutron net-show 75c2c3ec-7fe7-494c-a35c-db3f94d3a554
+---------------------+--------------------------------------+
| Field               | Value                                |
+---------------------+--------------------------------------+
| admin_state_up      | True                                 |
| description         | adminpod network                     |
| id                  | 75c2c3ec-7fe7-494c-a35c-db3f94d3a554 |
| name                | adminpod-net                         |
| orchestration_state | CREATE_COMPLETE                      |
| plane               | data                                 |
| shared              | False                                |
| status              | ACTIVE                               |
| subnets             |                                      |
| tags                | {}                                   |
| tenant_id           | 0f40dffa48614d9baa7eaac7e7532099     |
+---------------------+--------------------------------------+
```
* Checking the target of resources via gohan client
```
$ gohan client network show --output-format json 75c2c3ec-7fe7-494c-a35c-db3f94d3a554
{   
    "network": {
        "admin_state_up": true,
        "description": "adminpod network",
        "id": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554",
        "name": "adminpod-net",
        "orchestration_state": "CREATE_COMPLETE",
        "plane": "data",
        "shared": false,
        "status": "ACTIVE",
        "subnets": [],
        "tags": {},
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099"
    }
}
```
* Checking billing_resource via gohan client
```
$ gohan client billing_resource list --output-format json
{
    "billing_resources": [

        ... (snip)

        {
            "config_version": 1,
            "ended": null,
            "id": "3e5f3bcf-2af7-4b06-9092-afb0b3944a2f",
            "info": {},
            "parent_billing_id": null,
            "resource_id": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554",
            "resource_type": "network",
            "started": 1.518421185e+09,
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099",
            "unique_resource_id": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554"
        }
    ]
}
```

[Return to Previous Page](00_fire_wall.md)
