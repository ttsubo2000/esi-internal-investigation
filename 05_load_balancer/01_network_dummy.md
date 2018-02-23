[Return to Previous Page](00_load_balancer.md)

# 1. Clarification of interface in Sequence Diagram "Create Network for dummy-net"
You can see the relations of "Network" as following.

![Network](resource/gohan_investigate_for_loadbalancer.002.png)


## 1.1. Stored data in etcd after initinalizing gohan

![scope](../images/ESI_Sequence_diagram.002.png)

These are stored data for "heat_templates" in etcd.

* [Checking stored data for "network"](../heat_template/network.md)



## 1.2. HTTP Methods for RESTful between Gohan and Client

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
        "description": "dummy network for load_balancer",
        "name": "dummy-net",
        "plane": "data",
        "tags": {},
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c"
    }
}
```



## 1.3. Stored data in etcd after receiving HTTP Methods for RESTful

![scope](../images/ESI_Sequence_diagram.004.png)

These are stored data for "Create Network" in etcd.

* [Checking stored data for creating "network"](stored_in_etcd/CreateNetwork1_01.md)



## 1.4. Stored heat-stack via heat-api

![scope](../images/ESI_Sequence_diagram.005.png)

These are stored heat-stacks for "Create Network" in heat-engine.

* [Checking heat-stack of "network"](heat-stack/CreateNetwork1_01.md)



## 1.5. Stored resource in gohan
As a result, checking resources regarding of "Network" in gohan.

* Checking the target of resources via neutron client
```
$ neutron net-show ce9a7a92-d11a-4fc6-8ae7-18061b62c98f
+---------------------+--------------------------------------+
| Field               | Value                                |
+---------------------+--------------------------------------+
| admin_state_up      | True                                 |
| description         | dummy network for load_balancer      |
| id                  | ce9a7a92-d11a-4fc6-8ae7-18061b62c98f |
| name                | dummy-net                            |
| orchestration_state | CREATE_COMPLETE                      |
| plane               | data                                 |
| shared              | False                                |
| status              | ACTIVE                               |
| subnets             |                                      |
| tags                | {}                                   |
| tenant_id           | fe3a4a1a72c04479bb6c19c2c0ccba4c     |
+---------------------+--------------------------------------+
```
* Checking the target of resources via gohan client
```
$ gohan client network show --output-format json ce9a7a92-d11a-4fc6-8ae7-18061b62c98f
{
    "network": {
        "admin_state_up": true,
        "description": "dummy network for load_balancer",
        "id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f",
        "name": "dummy-net",
        "orchestration_state": "CREATE_COMPLETE",
        "plane": "data",
        "shared": false,
        "status": "ACTIVE",
        "subnets": [],
        "tags": {},
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c"
    }
}
```
* Checking billing_resource via gohan client
```
$ gohan client billing_resource list --output-format json
{
    "billing_resources": [
        {
            "config_version": 1,
            "ended": null,
            "id": "80c39f73-d70b-49db-b108-c690548b102c",
            "info": {},
            "parent_billing_id": null,
            "resource_id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f",
            "resource_type": "network",
            "started": 1.519017384e+09,
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c",
            "unique_resource_id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f"
        }
    ]
}
```


[Return to Previous Page](00_load_balancer.md)
