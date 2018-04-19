[Return to Previous Page](00_vpn_gateway.md)

# 8. Clarification of interface in Sequence Diagram "Create Qos Option"
You can see the relations of "Qos Option" as following.

![Qos Option](resource/gohan_investigate_for_vpngw.009.png)


## 8.1. Gohan

![scope](../images/ESI_Sequence_diagram.002.png)

### Outline
First of all, Gohan has received JSON data for "Create Qos Option" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/qos_options
```
```
{
    "qos_option": {
        "bandwidth": "10",
        "incoming_policer_config": "action { loss-priority high then discard; } single-rate { color-blind; committed-information-rate 10m; committed-burst-size 187500000; excess-burst-size 187500000; }",
        "incoming_policer_name": "10M-GA-UP-VPN",
        "name": "10Mbps-Guaranteed",
        "outgoing_policer_config": "if-exceeding { bandwidth-limit 10m; burst-size-limit 187500000; } then discard;",
        "outgoing_policer_name": "10M-GA-DOWN-VPN",
        "qos_type": "guarantee",
        "service_type": "vpn",
        "vpn_service_id": "c8d57f7e-b439-475e-a6fb-ee2594390177",
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef"
    }
}
```
After processing, Gohan has stored data for "Create Qos Option" in etcd

* [Checking stored data for creating "qos_option"](stored_in_etcd/01_Gohan/CreateQosOption_01.md)


## 8.2. ResourceReader
When ResourceReader has started, it gets all of schemas from Gohan.
After that, these schemas are converted as a template_mappings.
And then, ResourceReader keeps storing template_mappings for following processing.

### Reference
* [Checking schemas in ResourceReader](../memo/schemas.txt)
* [Checking template_mappings in ResourceReader](../memo/template_mappings.md)

![scope](../images/ESI_Sequence_diagram.003.png)

### Outline
After fetching resource_data for "Create Qos Option" in etcd, ResourceReader has not fetched heat_templates in etcd because of non_workable_resource.
And then, ResourceReader has stored data as finishing resource

* [Checking stored data for creating "qos_option"](stored_in_etcd/00_ResourceReader/CreateQosOption_01.md)


## 8.3. Stored resource in gohan
As a result, checking resources regarding of "Qos Option" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client qos_option show --output-format json d35a3c95-8647-44d7-b32f-405b77d77f51
{
    "qos_option": {
        "aws_service_id": null,
        "azure_service_id": null,
        "bandwidth": "10",
        "charge_type": null,
        "description": "",
        "gcp_service_id": null,
        "ha_router_id": "8c233862-895f-4cca-b377-c353e733c768",
        "id": "d35a3c95-8647-44d7-b32f-405b77d77f51",
        "incoming_policer_config": "action { loss-priority high then discard; } single-rate { color-blind; committed-information-rate 10m; committed-burst-size 187500000; excess-burst-size 187500000; }",
        "incoming_policer_name": "10M-GA-UP-VPN",
        "interdc_service_id": null,
        "internet_service_id": null,
        "name": "10Mbps-Guaranteed",
        "orchestration_state": "SYNC_COMPLETE",
        "outgoing_policer_config": "if-exceeding { bandwidth-limit 10m; burst-size-limit 187500000; } then discard;",
        "outgoing_policer_name": "10M-GA-DOWN-VPN",
        "qos_type": "guarantee",
        "service_type": "vpn",
        "status": "ACTIVE",
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
        "vpn_service_id": "c8d57f7e-b439-475e-a6fb-ee2594390177"
    }
}
```

[Return to Previous Page](00_vpn_gateway.md)
