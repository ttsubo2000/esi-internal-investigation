[Return to Previous Page](00_vpn_gateway.md)

# 14. Clarification of interface in Sequence Diagram "Create Static Route"
You can see the relations of "Static Route" as following.

![Static Route](resource/gohan_investigate_for_vpngw.015.png)


## 14.1. Gohan

![scope](../images/ESI_Sequence_diagram.002.png)

### Outline
First of all, Gohan has received JSON data for "Create Static Route" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/static_routes
```
```
{
    "static_route": {
        "description": "Sample Static-route",
        "destination": "192.168.0.0/24",
        "name": "sample-static-route",
        "nexthop": "172.16.101.1",
        "service_type": "vpn",
        "vpn_gw_id": "b1da850c-3344-4de2-aa18-d96a30b54f69",
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef"
    }
}
```
After processing, Gohan has stored data for "Create Static Route" in etcd.

* [Checking stored data for creating "static_route"](stored_in_etcd/01_Gohan/CreateStaticRoute_01.md)


## 14.2. ResourceReader
When ResourceReader has started, it gets all of schemas from Gohan.
After that, these schemas are converted as a template_mappings.
And then, ResourceReader keeps storing template_mappings for following processing.

### Reference
* [Checking schemas in ResourceReader](../memo/schemas.txt)
* [Checking template_mappings in ResourceReader](../memo/template_mappings.md)

![scope](../images/ESI_Sequence_diagram.003.png)

### Outline
After fetching resource_data for "Create Static Route" in etcd, ResourceReader has fetched heat_templates in etcd.

* [Checking stored data for "static_route_internet"](../heat_template/static_route_vpn.md)


## 14.3. JobManager

![scope](../images/ESI_Sequence_diagram.004.png)

### Outline
After converting resource_data to job_data, JobManager has stored it in etcd.

* [Checking stored data for creating "static_route"](stored_in_etcd/02_JobManager/CreateStaticRoute_01.md)


## 14.4. HeatWorker

![scope](../images/ESI_Sequence_diagram.005.png)

### Outline
After fetching job_data, HeatWorker has handled job_data.
And then, HeatWorker has stored the result of handling job_data.

* [Checking stored data for creating "static_route"](stored_in_etcd/03_HeatWorker/CreateStaticRoute_01.md)


## 14.5. Heat

![scope](../images/ESI_Sequence_diagram.006.png)

### Outline
Heat has conducted some tasks for "Create Static Route".
As a result, Heat has stored heat-stacks for "Create Static Route".

* [Checking heat-stack of "static_route"](heat-stack/CreateStaticRoute_01.md)


## 14.6. Applying JUNOS Configurations via netconf
Checking configuration in Edge Router

* MX-1
```
[edit routing-instances vrf_gw_sample-ha-router-downlink_1025 routing-options]
+     static {
+         route 192.168.0.0/24 next-hop 172.16.101.1;
+     }

[edit]
```

* MX-2
```
[edit routing-instances vrf_gw_sample-ha-router-downlink_1025 routing-options]
+     static {
+         route 192.168.0.0/24 next-hop 172.16.101.1;
+     }

[edit]
```


## 14.7. Stored resource in gohan
As a result, checking resources regarding of "Static Route" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client static_route show --output-format json 31980341-9bef-4f05-8df7-674dea343884
{
    "static_route": {
        "aws_gw_id": null,
        "azure_gw_id": null,
        "description": "Sample Static-route",
        "destination": "192.168.0.0/24",
        "gcp_gw_id": null,
        "id": "31980341-9bef-4f05-8df7-674dea343884",
        "interdc_gw_id": null,
        "internet_gw_id": null,
        "name": "sample-static-route",
        "nexthop": "172.16.101.1",
        "orchestration_state": "CREATE_COMPLETE",
        "public_ip_id": null,
        "service_type": "vpn",
        "status": "ACTIVE",
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
        "vpn_gw_id": "b1da850c-3344-4de2-aa18-d96a30b54f69"
    }
}
```

[Return to Previous Page](00_vpn_gateway.md)
