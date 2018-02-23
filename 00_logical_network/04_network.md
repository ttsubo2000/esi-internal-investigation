[Return to Previous Page](00_logical_network.md)

# 4. Clarification of interface in Sequence Diagram "Create Network"
You can see the relations of "Network" as following.

![Network](resource/gohan_investigate_for_logicalnetwork.005.png)


## 4.1. Stored data in etcd after initinalizing gohan

![scope](../images/ESI_Sequence_diagram.002.png)

These are stored data for "heat_templates" in etcd.

* [Checking stored data for "network"](../heat_template/network.md)



## 4.2. HTTP Methods for RESTful between Gohan and Client

![scope](../images/ESI_Sequence_diagram.003.png)

This is JSON data for "Create Network" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/networks
```
```
{
    "network": {
        "description": "sample network", 
        "tags": {}, 
        "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
        "admin_state_up": true, 
        "plane": "data", 
        "name": "sample-network"
    }
}
```



## 4.3. Stored data in etcd after receiving HTTP Methods for RESTful

![scope](../images/ESI_Sequence_diagram.004.png)

These are stored data for "Create Network" in etcd.

* [Checking stored data for creating "network"](stored_in_etcd/CreateNetwork_01.md)



## 4.4. Stored heat-stack via heat-api

![scope](../images/ESI_Sequence_diagram.005.png)

These are stored heat-stacks for "Create Network" in heat-engine.

* [Checking heat-stack of "network"](heat-stack/CreateNetwork_01.md)



## 4.5. Stored resource in gohan
As a result, checking resources regarding of "Network" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client network show --output-format json 35bc496f-3c0e-46b4-a5c0-33810e8e7263
{
    "network": {
        "admin_state_up": true,
        "description": "sample network",
        "id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263",
        "name": "sample-network",
        "orchestration_state": "CREATE_COMPLETE",
        "plane": "data",
        "shared": false,
        "status": "ACTIVE",
        "subnets": [],
        "tags": {},
        "tenant_id": "ae69b52f46ba480bb9636f62736436f4"
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
            "id": "0d9e8315-519b-4220-a751-9fcc0080c8a3",
            "info": {},
            "parent_billing_id": null,
            "resource_id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263",
            "resource_type": "network",
            "started": 1.518677706e+09,
            "tenant_id": "ae69b52f46ba480bb9636f62736436f4",
            "unique_resource_id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263"
        }
    ]
}
```


[Return to Previous Page](00_logical_network.md)
