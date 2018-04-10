[Return to Previous Page](00_common_function_gateway.md)

# 6. Clarification of interface in Sequence Diagram "Create Ha Interface"
You can see the relations of "Ha Interface" as following.

![Ha Interface](resource/gohan_investigate_for_commfuncgw.007.png)


## 6.1. Gohan

![scope](../images/ESI_Sequence_diagram.002.png)

### Outline
First of all, Gohan has received JSON data for "Create Ha Interface" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/ha_interfaces
```
```
{
    "ha_interface": {
        "ha_router_id": "e16529c4-ffb8-4346-b850-af3c93564604",
        "link_type": "downlink",
        "name": "sample-ha-router-downlink",
        "primary_interface_id": "c2576120-00b0-461e-a2ae-f7bbff9465d0",
        "secondary_interface_id": "b9c7c1f4-1b90-4a7a-8161-34276bb2ed10",
        "restricted_vlans": "0-1024,4094",
        "tenant_id": "c583ce78843344adbe5fd20f13620274"
    }
}
```
After processing, Gohan has stored data for "Create Ha Interface" in etcd

* [Checking stored data for creating "ha_interface"](stored_in_etcd/01_Gohan/CreateHaInterface_01.md)


## 6.2. ResourceReader
When ResourceReader has started, it gets all of schemas from Gohan.
After that, these schemas are converted as a template_mappings.
And then, ResourceReader keeps storing template_mappings for following processing.

### Reference
* [Checking schemas in ResourceReader](../memo/schemas.txt)
* [Checking template_mappings in ResourceReader](../memo/template_mappings.md)

![scope](../images/ESI_Sequence_diagram.003.png)

### Outline
After fetching resource_data for "Create Ha Interface" in etcd, ResourceReader has not fetched heat_templates in etcd because of non_workable_resource.
And then, ResourceReader has stored data as finishing resource

* [Checking stored data for creating "ha_interface"](stored_in_etcd/00_ResourceReader/CreateHaInterface_01.md)


## 6.3. Stored resource in gohan
As a result, checking resources regarding of "Ha Interface" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client ha_interface show --output-format json 16f6433d-0864-4d24-809d-c1b8e878280c
{
    "ha_interface": {
        "admin_state_up": true,
        "available_be_bandwidth": 0,
        "available_ga_bandwidth": 0,
        "description": "",
        "gateway_instances_count": 0,
        "ha_router_id": "e16529c4-ffb8-4346-b850-af3c93564604",
        "id": "16f6433d-0864-4d24-809d-c1b8e878280c",
        "link_type": "downlink",
        "maximum_be_bandwidth": 0,
        "maximum_ga_bandwidth": 0,
        "name": "sample-ha-router-downlink",
        "primary_interface_id": "c2576120-00b0-461e-a2ae-f7bbff9465d0",
        "restricted_vlans": "0-1024,4094",
        "secondary_interface_id": "b9c7c1f4-1b90-4a7a-8161-34276bb2ed10",
        "status": "ACTIVE",
        "tenant_id": "c583ce78843344adbe5fd20f13620274",
        "vlan_ids_available": 3069,
        "vlan_pool_state": "//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////+AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM="
    }
}
```

[Return to Previous Page](00_common_function_gateway.md)
