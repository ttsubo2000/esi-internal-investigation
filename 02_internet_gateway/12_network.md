[Return to Previous Page](00_internet_gateway.md)

# 12. Clarification of interface in Sequence Diagram "Create Network"
You can see the relations of "Network" as following.

![Network](resource/gohan_investigate_for_inetgw.013.png)


## 12.1. Gohan

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
        "admin_state_up": true,
        "description": "Sample Network",
        "name": "sample-network",
        "plane": "data",
        "tags": {},
        "tenant_id": "06d6b792b31c40daa546fb0f4e35980d"
    }
}
```
After processing, Gohan has stored data for "Network" in etcd.

* [Checking stored data for creating "network"](stored_in_etcd/01_Gohan/CreateNetwork_01.md)


## 12.2. ResourceReader
When ResourceReader has started, it gets all of schemas from Gohan.
After that, these schemas are converted as a template_mappings.
And then, ResourceReader keeps storing template_mappings for following processing.

### Reference
* [Checking schemas in ResourceReader](../memo/schemas.txt)
* [Checking template_mappings in ResourceReader](../memo/template_mappings.md)

![scope](../images/ESI_Sequence_diagram.003.png)

### Outline
After fetching resource_data for "Network" in etcd, ResourceReader has fetched heat_templates in etcd.

* [Checking stored data for "network"](../heat_template/network.md)


## 12.3. JobManager

![scope](../images/ESI_Sequence_diagram.004.png)

### Outline
After converting resource_data to job_data, JobManager has stored it in etcd.

* [Checking stored data for creating "network"](stored_in_etcd/02_JobManager/CreateNetwork_01.md)


## 12.4. HeatWorker

![scope](../images/ESI_Sequence_diagram.005.png)

### Outline
After fetching job_data, HeatWorker has handled job_data.
And then, HeatWorker has stored the result of handling job_data.

* [Checking stored data for creating "network"](stored_in_etcd/03_HeatWorker/CreateNetwork_01.md)


## 12.5. Heat

![scope](../images/ESI_Sequence_diagram.006.png)

### Outline
Heat has conducted some tasks for "Create Network".
As a result, Heat has stored heat-stacks for "Create Network".

* [Checking heat-stack of "network"](heat-stack/CreateNetwork_01.md)


## 12.6. Stored resource in gohan
As a result, checking resources regarding of "Network" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client network show --output-format json 6e557507-1c2a-49b1-ba90-5f616a1f1f3e
{
    "network": {
        "admin_state_up": true,
        "description": "Sample Network",
        "id": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e",
        "name": "sample-network",
        "orchestration_state": "CREATE_COMPLETE",
        "plane": "data",
        "shared": false,
        "status": "ACTIVE",
        "subnets": [],
        "tags": {},
        "tenant_id": "06d6b792b31c40daa546fb0f4e35980d"
    }
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
            "id": "fc6dc454-4214-4573-9fbd-e2b5311a7d57",
            "info": {},
            "parent_billing_id": null,
            "resource_id": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e",
            "resource_type": "network",
            "started": 1.52281809e+09,
            "tenant_id": "06d6b792b31c40daa546fb0f4e35980d",
            "unique_resource_id": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e"
        }
    ]
}
```


[Return to Previous Page](00_internet_gateway.md)
