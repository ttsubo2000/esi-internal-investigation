[Return to Previous Page](00_logical_network.md)

# 4. Clarification of interface in Sequence Diagram "Create Network"
You can see the relations of "Network" as following.

![Network](resource/gohan_investigate_for_logicalnetwork.005.png)


## 4.1. Gohan

![scope](../images/ESI_Sequence_diagram.002.png)

### Outline
First of all, Gohan has received JSON data for "Create Network" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/networks
```
```
{
    "network": {
        "description": "sample network",
        "tags": {},
        "tenant_id": "ae69b52f46ba480bb9636f62736436f4",
        "admin_state_up": true,
        "plane": "data",
        "name": "sample-network"
    }
}
```
After processing, Gohan has stored data for "Create Network" in etcd.

* [Checking stored data for creating "network"](stored_in_etcd/01_Gohan/CreateNetwork_01.md)


## 4.2. ResourceReader
When ResourceReader has started, it gets all of schemas from Gohan.
After that, these schemas are converted as a template_mappings.
And then, ResourceReader keeps storing template_mappings for following processing.

### Reference
* [Checking schemas in ResourceReader](../memo/schemas.txt)
* [Checking template_mappings in ResourceReader](../memo/template_mappings.md)

![scope](../images/ESI_Sequence_diagram.003.png)

### Outline
After fetching resource_data for "Create Network" in etcd, ResourceReader has fetched heat_templates in etcd.

* [Checking stored data for "network"](../heat_template/network.md)


## 4.3. JobManager

![scope](../images/ESI_Sequence_diagram.004.png)

### Outline
After converting resource_data to job_data, JobManager has stored it in etcd.

* [Checking stored data for creating "network"](stored_in_etcd/02_JobManager/CreateNetwork_01.md)


## 4.4. HeatWorker

![scope](../images/ESI_Sequence_diagram.005.png)

### Outline
After fetching job_data, HeatWorker has handled job_data.
And then, HeatWorker has stored the result of handling job_data.

* [Checking stored data for creating "network"](stored_in_etcd/03_HeatWorker/CreateNetwork_01.md)


## 4.5. Heat

![scope](../images/ESI_Sequence_diagram.006.png)

### Outline
Heat has conducted some tasks for "Create Network".
As a result, Heat has stored heat-stacks for "Create Network".

* [Checking heat-stack of "network"](heat-stack/CreateNetwork_01.md)


## 4.6. Stored resource in gohan
As a result, checking resources regarding of "Network" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client network show --output-format json 35bc496f-3c0e-46b4-a5c0-33810e8e7263
{
    "network": {
        "admin_state_up": true,
        "description": "sample network",
        "id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263",
        "name": "sample-network",
        "orchestration_state": "CREATE_COMPLETE",
        "plane": "data",
        "shared": false,
        "status": "ACTIVE",
        "subnets": [],
        "tags": {},
        "tenant_id": "ae69b52f46ba480bb9636f62736436f4"
    }
}
```
* Checking billing_resource via gohan client
```
$ gohan client billing_resource list --output-format json
{
    "billing_resources": [
        {
            "config_version": 1,
            "ended": null,
            "id": "0d9e8315-519b-4220-a751-9fcc0080c8a3",
            "info": {},
            "parent_billing_id": null,
            "resource_id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263",
            "resource_type": "network",
            "started": 1.518677706e+09,
            "tenant_id": "ae69b52f46ba480bb9636f62736436f4",
            "unique_resource_id": "35bc496f-3c0e-46b4-a5c0-33810e8e7263"
        }
    ]
}
```


[Return to Previous Page](00_logical_network.md)
