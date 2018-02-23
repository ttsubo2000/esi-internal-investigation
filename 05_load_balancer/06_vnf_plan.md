[Return to Previous Page](00_load_balancer.md)

# 6. Clarification of interface in Sequence Diagram "Create Vnf Plan"
You can see the relations of "Vnf Plan" as following.

![Vnf Plan](resource/gohan_investigate_for_loadbalancer.007.png)



## 6.1. HTTP Methods for RESTful between Gohan and Client

![scope](../images/ESI_Sequence_diagram.003.png)

This is JSON data for "Create Vnf Plan" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/vnf_plans
```
```
{
    "vnf_plan": {
        "default_interface_number": 3,
        "description": "dummy_vnf_plans",
        "flavor": "m1.xlarge",
        "function": "load_balancer",
        "interface_limit": 5,
        "name": "vLB_plan",
        "vendor": "citrix",
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c"
    }
}
```



## 6.2. Stored data in etcd after receiving HTTP Methods for RESTful

![scope](../images/ESI_Sequence_diagram.004.png)

These are stored data for "Create Vnf Plan" in etcd.

* [Checking stored data for creating "vnf_plan"](stored_in_etcd/CreateVnfPlan_01.md)



## 6.3. Stored resource in gohan
As a result, checking resources regarding of "Vnf Plan" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client vnf_plan show --output-format json 043fed11-ce3d-48fb-aa8d-13aad5804d83
{
    "vnf_plan": {
        "default_interface_number": 3,
        "description": "dummy_vnf_plans",
        "flavor": "m1.xlarge",
        "function": "load_balancer",
        "id": "043fed11-ce3d-48fb-aa8d-13aad5804d83",
        "interface_limit": 5,
        "name": "vLB_plan",
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c",
        "vendor": "citrix"
    }
}
```

[Return to Previous Page](00_load_balancer.md)
