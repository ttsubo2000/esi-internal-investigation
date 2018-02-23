[Return to Previous Page](00_fire_wall.md)

# 7. Clarification of interface in Sequence Diagram "Create Firewall Plan"
You can see the relations of "Firewall Plan" as following.

![Firewall Plan](resource/gohan_investigate_for_firewall.008.png)



## 7.1. HTTP Methods for RESTful between Gohan and Client

![scope](../images/ESI_Sequence_diagram.003.png)

This is JSON data for "Create Firewall Plan" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/firewall_plans
```
```
{
    "firewall_plan": {
        "is_public": true,
        "name": "Brocade_5600_vRouter_3.5R6S3_2CPU-8GB-2IF",
        "vendor": "vyatta",
        "version": "3.5R6S3-test",
        "vnf_plan_id": "60791395-2267-4553-b115-a38fad3ebf69",
        "vnf_template_id": "5a84974a-9d8b-4887-898b-8e3c095e744d",
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099"
    }
}
```



## 7.2. Stored data in etcd after receiving HTTP Methods for RESTful

![scope](../images/ESI_Sequence_diagram.004.png)

These are stored data for "Create Firewall Plan" in etcd.

* [Checking stored data for creating "firewall_plan"](stored_in_etcd/CreateFirewallPlan_01.md)



## 7.3. Stored resource in gohan
As a result, checking resources regarding of "Firewall Plan" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client firewall_plan show --output-format json 40520774-4f10-4e8c-90fa-550bd4cdf101
{
    "firewall_plan": {
        "description": "",
        "enabled": true,
        "id": "40520774-4f10-4e8c-90fa-550bd4cdf101",
        "is_public": true,
        "name": "Brocade_5600_vRouter_3.5R6S3_2CPU-8GB-2IF",
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099",
        "vendor": "vyatta",
        "version": "3.5R6S3-test",
        "vnf_plan_id": "60791395-2267-4553-b115-a38fad3ebf69",
        "vnf_template_id": "5a84974a-9d8b-4887-898b-8e3c095e744d"
    }
}
```

[Return to Previous Page](00_fire_wall.md)