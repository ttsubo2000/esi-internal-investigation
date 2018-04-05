[Return to Previous Page](00_internet_gateway.md)

# 4. Clarification of interface in Sequence Diagram "Create Ha Router"
You can see the relations of "Ha Router" as following.

![Ha Router](resource/gohan_investigate_for_inetgw.005.png)


## 4.1. Gohan

![scope](../images/ESI_Sequence_diagram.002.png)

### Outline
First of all, Gohan has received JSON data for "Create Ha Router" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/ha_routers
```
```
{
    "ha_router": {
        "description": "sample_ha_router",
        "name": "sample-ha-router",
        "primary_router_id": "cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78",
        "secondary_router_id": "ca43aedb-bc30-4355-a931-7bb1d9040659",
        "tenant_id": "06d6b792b31c40daa546fb0f4e35980d"
    }
}
```
After processing, Gohan has stored data for "Create Ha Router" in etcd

* [Checking stored data for creating "ha_router"](stored_in_etcd/01_Gohan/CreateHaRouter_01.md)


## 4.2. ResourceReader
When ResourceReader has started, it gets all of schemas from Gohan.
After that, these schemas are converted as a template_mappings.
And then, ResourceReader keeps storing template_mappings for following processing.

### Reference
* [Checking schemas in ResourceReader](../memo/schemas.txt)
* [Checking template_mappings in ResourceReader](../memo/template_mappings.md)

![scope](../images/ESI_Sequence_diagram.003.png)

### Outline
After fetching resource_data for "Create Ha Router" in etcd, ResourceReader has not fetched heat_templates in etcd because of non_workable_resource.
And then, ResourceReader has stored data as finishing resource

* [Checking stored data for creating "ha_router"](stored_in_etcd/00_ResourceReader/CreateHaRouter_01.md)


## 4.3. Stored resource in gohan
As a result, checking resources regarding of "Ha Router" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client ha_router show --output-format json add04ae7-e48a-4583-a726-bed5f3b748c4
{
    "ha_router": {
        "available_gateways": 500,
        "description": "sample_ha_router",
        "id": "add04ae7-e48a-4583-a726-bed5f3b748c4",
        "maximum_gateways": 500,
        "name": "sample-ha-router",
        "primary_router_id": "cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78",
        "secondary_router_id": "ca43aedb-bc30-4355-a931-7bb1d9040659",
        "status": "ACTIVE",
        "tenant_id": "06d6b792b31c40daa546fb0f4e35980d"
    }
}
```

[Return to Previous Page](00_internet_gateway.md)
