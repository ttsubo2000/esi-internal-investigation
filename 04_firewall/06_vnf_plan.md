[Return to Previous Page](00_fire_wall.md)

# 6. Clarification of interface in Sequence Diagram "Create Vnf Plan"
You can see the relations of "Vnf Plan" as following.

![Vnf Plan](resource/gohan_investigate_for_firewall.007.png)



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
        "description": "vyatta-2CPU-2IF",
        "flavor": "m1.large",
        "function": "firewall",
        "interface_limit": 3,
        "name": "vyatta-2CPU-2IF",
        "vendor": "vyatta",
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099"
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
$ gohan client vnf_plan show --output-format json 60791395-2267-4553-b115-a38fad3ebf69
{
    "vnf_plan": {
        "default_interface_number": 3,
        "description": "vyatta-2CPU-2IF",
        "flavor": "m1.large",
        "function": "firewall",
        "id": "60791395-2267-4553-b115-a38fad3ebf69",
        "interface_limit": 3,
        "name": "vyatta-2CPU-2IF",
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099",
        "vendor": "vyatta"
    }
}
```

[Return to Previous Page](00_fire_wall.md)
