[Return to Previous Page](00_internet_gateway.md)

# 6. Clarification of interface in Sequence Diagram "Create Ha Interface"
You can see the relations of "Ha Interface" as following.

![Ha Interface](resource/gohan_investigate_for_inetgw.007.png)


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
        "ha_router_id": "add04ae7-e48a-4583-a726-bed5f3b748c4",
        "link_type": "downlink",
        "maximum_be_bandwidth": 500,
        "maximum_ga_bandwidth": 500,
        "name": "sample-ha-router-downlink",
        "primary_interface_id": "53712736-354c-4374-be82-6f07bea9d1bd",
        "secondary_interface_id": "d108a472-81ab-43a0-8c49-e0d1a46e6128",
        "restricted_vlans": "0-1024,4094",
        "tenant_id": "06d6b792b31c40daa546fb0f4e35980d"
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
gohan client ha_interface show --output-format json 2595e193-84a8-49dc-aa2e-7a68c60ea11e
{
    "ha_interface": {
        "admin_state_up": true,
        "available_be_bandwidth": 500,
        "available_ga_bandwidth": 500,
        "description": "",
        "gateway_instances_count": 0,
        "ha_router_id": "add04ae7-e48a-4583-a726-bed5f3b748c4",
        "id": "2595e193-84a8-49dc-aa2e-7a68c60ea11e",
        "link_type": "downlink",
        "maximum_be_bandwidth": 500,
        "maximum_ga_bandwidth": 500,
        "name": "sample-ha-router-downlink",
        "primary_interface_id": "53712736-354c-4374-be82-6f07bea9d1bd",
        "restricted_vlans": "0-1024,4094",
        "secondary_interface_id": "d108a472-81ab-43a0-8c49-e0d1a46e6128",
        "status": "ACTIVE",
        "tenant_id": "06d6b792b31c40daa546fb0f4e35980d",
        "vlan_ids_available": 3069,
        "vlan_pool_state": "//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////+AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM="
    }
}
```

[Return to Previous Page](00_internet_gateway.md)
