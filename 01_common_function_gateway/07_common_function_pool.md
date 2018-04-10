[Return to Previous Page](00_common_function_gateway.md)

# 7. Clarification of interface in Sequence Diagram "Create Common Function Pool"
You can see the relations of "Common Function Pool" as following.

![Common Function Tool](resource/gohan_investigate_for_commfuncgw.008.png)


## 7.1. Gohan

![scope](../images/ESI_Sequence_diagram.002.png)

### Outline
First of all, Gohan has received JSON data for "Create Common Function Pool" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/common_function_pools
```
```
{
    "common_function_pool": {
        "description": "sample common function pool",
        "dnat_group_name": "DNAT-RULE",
        "dnat_pool_group_name": "DNAT-POOL",
        "downlink_interfaces": [
            "16f6433d-0864-4d24-809d-c1b8e878280c"
        ],
        "link_local_cidr": "169.254.0.0/17",
        "logical_tunnel_interface_name": "lt-0/0/0",
        "name": "common_function_pool",
        "service_interface_name": "ms-0/2/0",
        "service_vrf_name": "SHARED-RESOURCE",
        "snapt_group_name": "SNAPT-RULE",
        "snapt_pool_group_name": "SNAPT-POOL",
        "tenant_id": "c583ce78843344adbe5fd20f13620274",
        "vrrp_config": [
            {
                "primary_ip": "169.254.1.251",
                "secondary_ip": "169.254.1.252",
                "vrid": 41
            },
            {
                "primary_ip": "169.254.1.253",
                "secondary_ip": "169.254.1.254",
                "vrid": 42
            }
        ],
        "vrrp_group_name": "IF-USER-VRRP-ACT"
    }
}
```
After processing, Gohan has stored data for "Create Common Function Pool" in etcd

* [Checking stored data for creating "common_function_pool"](stored_in_etcd/01_Gohan/CreateCommonFunctionPool_01.md)


## 7.2. ResourceReader
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

* [Checking stored data for creating "common_function_pool"](stored_in_etcd/00_ResourceReader/CreateCommonFunctionPool_01.md)


## 7.3. Stored resource in gohan
As a result, checking resources regarding of "Common Function Pool" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client common_function_pool show --output-format json 2d4a700d-bf94-4217-9a3c-4217a16c951f
{
    "common_function_pool": {
        "common_function_pool_state": "AAD//w==",
        "description": "sample common function pool",
        "dnat_group_name": "DNAT-RULE",
        "dnat_pool_group_name": "DNAT-POOL",
        "downlink_interfaces": [
            "16f6433d-0864-4d24-809d-c1b8e878280c"
        ],
        "id": "2d4a700d-bf94-4217-9a3c-4217a16c951f",
        "link_local_cidr": "169.254.0.0/17",
        "link_local_netmask": 17,
        "logical_tunnel_interface_name": "lt-0/0/0",
        "name": "common_function_pool",
        "service_interface_name": "ms-0/2/0",
        "service_vrf_name": "SHARED-RESOURCE",
        "snapt_group_name": "SNAPT-RULE",
        "snapt_pool_group_name": "SNAPT-POOL",
        "tenant_id": "c583ce78843344adbe5fd20f13620274",
        "vrrp_config": [
            {
                "primary_ip": "169.254.1.251",
                "secondary_ip": "169.254.1.252",
                "vrid": 41
            },
            {
                "primary_ip": "169.254.1.253",
                "secondary_ip": "169.254.1.254",
                "vrid": 42
            }
        ],
        "vrrp_group_name": "IF-USER-VRRP-ACT"
    }
}
```

[Return to Previous Page](00_common_function_gateway.md)
