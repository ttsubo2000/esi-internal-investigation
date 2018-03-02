[Return to Previous Page](00_firewall.md)

# 6. Clarification of interface in Sequence Diagram "Create Vnf Plan"
You can see the relations of "Vnf Plan" as following.

![Vnf Plan](resource/gohan_investigate_for_firewall.007.png)


## 6.1. Gohan

![scope](../images/ESI_Sequence_diagram.002.png)

### Outline
First of all, Gohan has received JSON data for "Create Vnf Plan" in HTTP Methods from client.

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
After processing, Gohan has stored data for "Create Vnf Plan" in etcd

* [Checking stored data for creating "vnf_plan"](stored_in_etcd/01_Gohan/CreateVnfPlan_01.md)


## 6.2. ResourceReader
When ResourceReader has started, it gets all of schemas from Gohan.
After that, these schemas are converted as a template_mappings.
And then, ResourceReader keeps storing template_mappings for following processing.

### Reference
* [Checking schemas in ResourceReader](../memo/schemas.txt)
* [Checking template_mappings in ResourceReader](../memo/template_mappings.md)

![scope](../images/ESI_Sequence_diagram.003.png)

### Outline
After fetching resource_data for "Create Vnf Plan" in etcd, ResourceReader has not fetched heat_templates in etcd because of non_workable_resource.
And then, ResourceReader has stored data as finishing resource

* [Checking stored data for creating "vnf_plan"](stored_in_etcd/00_ResourceReader/CreateVnfPlan_01.md)


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

[Return to Previous Page](00_firewall.md)
