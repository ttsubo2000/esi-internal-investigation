[Return to Previous Page](00_load_balancer.md)

# 3. Clarification of interface in Sequence Diagram "Create Network for admin-net"
You can see the relations of "Network" as following.

![Network](resource/gohan_investigate_for_loadbalancer.004.png)


## 3.1. Gohan

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
        "description": "adminpod network",
        "name": "adminpod-net",
        "plane": "data",
        "tags": {},
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c"
    }
}
```
After processing, Gohan has stored data for "Network" in etcd.

* [Checking stored data for creating "network"](stored_in_etcd/01_Gohan/CreateNetwork2_01.md)


## 3.2. ResourceReader
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


## 3.3. JobManager

![scope](../images/ESI_Sequence_diagram.004.png)

### Outline
After converting resource_data to job_data, JobManager has stored it in etcd.

* [Checking stored data for creating "network"](stored_in_etcd/02_JobManager/CreateNetwork2_01.md)


## 3.4. HeatWorker

![scope](../images/ESI_Sequence_diagram.005.png)

### Outline
After fetching job_data, HeatWorker has handled job_data.
And then, HeatWorker has stored the result of handling job_data.

* [Checking stored data for creating "network"](stored_in_etcd/03_HeatWorker/CreateNetwork2_01.md)


## 3.5. Heat

![scope](../images/ESI_Sequence_diagram.006.png)

### Outline
Heat has conducted some tasks for "Create Network".
As a result, Heat has stored heat-stacks for "Create Network".

* [Checking heat-stack of "network"](heat-stack/CreateNetwork2_01.md)


## 3.6. Stored resource in gohan
As a result, checking resources regarding of "Network" in gohan.

* Checking the target of resources via neutron client
```
$ neutron net-show 168c1535-9001-49c7-bb05-21844570a83c
+---------------------+--------------------------------------+
| Field               | Value                                |
+---------------------+--------------------------------------+
| admin_state_up      | True                                 |
| description         | adminpod network                     |
| id                  | 168c1535-9001-49c7-bb05-21844570a83c |
| name                | adminpod-net                         |
| orchestration_state | CREATE_COMPLETE                      |
| plane               | data                                 |
| shared              | False                                |
| status              | ACTIVE                               |
| subnets             |                                      |
| tags                | {}                                   |
| tenant_id           | fe3a4a1a72c04479bb6c19c2c0ccba4c     |
+---------------------+--------------------------------------+
```
* Checking the target of resources via gohan client
```
$ gohan client network show --output-format json 168c1535-9001-49c7-bb05-21844570a83c
{
    "network": {
        "admin_state_up": true,
        "description": "adminpod network",
        "id": "168c1535-9001-49c7-bb05-21844570a83c",
        "name": "adminpod-net",
        "orchestration_state": "CREATE_COMPLETE",
        "plane": "data",
        "shared": false,
        "status": "ACTIVE",
        "subnets": [],
        "tags": {},
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c"
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
            "id": "25ee24b6-7113-427d-b7a1-a87cb5884a9e",
            "info": {},
            "parent_billing_id": null,
            "resource_id": "168c1535-9001-49c7-bb05-21844570a83c",
            "resource_type": "network",
            "started": 1.5190174e+09,
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c",
            "unique_resource_id": "168c1535-9001-49c7-bb05-21844570a83c"
        }
    ]
}
```

[Return to Previous Page](00_load_balancer.md)
