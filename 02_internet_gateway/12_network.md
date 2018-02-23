[Return to Previous Page](00_internet_gateway.md)

# 12. Clarification of interface in Sequence Diagram "Create Network"
You can see the relations of "Network" as following.

![Network](resource/gohan_investigate_for_inetgw.013.png)

## 12.1. Sequence Diagram between gohan and etcd
This is a diagram that has been described as interfaces for "Network" between gohan and etcd.

* Initinalizing gohan ...
* Receiving HTTP Methods for Creating Resource ...

![Create Network](diag/ESI_Sequence_Diagram_for_Internet_Gateway.015.png)

## 12.2. Stored data in etcd after initinalizing gohan
These are stored data for "heat_templates" in etcd.

* [Checking stored data for "network"](../heat_template/network.md)
* [Checking stored data for "network_monitoring"](../heat_template/network_monitoring.md)


## 12.3. HTTP Methods for RESTful between Gohan and Client
This is JSON data for "Create Network" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/networks
```
```
{
    "network": {
        "admin_state_up": true,
        "description": "Sample Network",
        "name": "sample-network",
        "plane": "data",
        "tags": {},
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f"
    }
}
```
![scope](../images/esi_interface.004.png)


## 12.4. Stored data in etcd after receiving HTTP Methods for RESTful
These are stored data for "Create Network" in etcd.

* [Checking stored data for creating "network"](stored_in_etcd/CreateNetwork_01.md)

![scope](../images/esi_interface.005.png)


## 12.5. Stored heat-stack via heat-api
These are stored heat-stacks for "Create Network" in heat-engine.

* [Checking heat-stack of "network"](heat-stack/CreateNetwork_01.md)

![scope](../images/esi_interface.006.png)


## 12.6. Stored resource for monitoring in Kafka
This is JSON data for "Create Network" between monitoring-worker and kafka

* [Checking the topic "monitor_virtual_network" for monitoring "network"](stored_in_kafka/CreateNetwork_01.md)

![scope](../images/esi_interface.007.png)


## 12.7. Stored resource in gohan
As a result, checking resources regarding of "Network" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client network show --output-format json 52d7bef8-aa17-45c3-b63e-6a0e504603f0
{
    "network": {
        "admin_state_up": true,
        "description": "Sample Network",
        "id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0",
        "name": "sample-network",
        "plane": "data",
        "shared": false,
        "status": "ACTIVE",
        "subnets": [],
        "tags": {},
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f"
    }
}
```
* Checking resource_mapping via gohan client
```
$ gohan client resource_mapping list --output-format json
{
    "resource_mappings": [

        ... (snip)

        {
            "created": 1.494476703e+09,
            "deleted": null,
            "id": "f6a5fc1b-695d-4921-923a-92af07f52c2b",
            "mapped_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0",
            "relation": "instance",
            "resource_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0",
            "resource_type": "network",
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f"
        }
    ]
}
```
* Checking billing_resource via gohan client
```
$ gohan client billing_resource list --output-format json
{
    "billing_resources": [

        ... (snip)

        {
            "config_version": 1,
            "ended": null,
            "id": "b4165f07-3b67-438d-a398-4add6a499a04",
            "info": {},
            "parent_billing_id": null,
            "resource_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0",
            "resource_type": "network",
            "started": 1.494476703e+09,
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f",
            "unique_resource_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0"
        }
    ]
}
```


[Return to Previous Page](00_internet_gateway.md)
