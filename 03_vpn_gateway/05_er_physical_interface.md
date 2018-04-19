[Return to Previous Page](00_vpn_gateway.md)

# 5. Clarification of interface in Sequence Diagram "Create Er Physical Interface"
You can see the relations of "Create Er Physical Interface" as following.

![Er Physical Interface](resource/gohan_investigate_for_vpngw.006.png)


## 5.1. Gohan

![scope](../images/ESI_Sequence_diagram.002.png)

### Outline
First of all, Gohan has received JSON data for "Create Er Physical Interface" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/er_physical_interfaces
```
```
{
    "er_physical_interface": {
        "device_id": "7a35974a-a19f-49e2-b907-ad7fd8692975",
        "name": "ge-0/0/1",
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef"
    }
}
```
* Checking JSON data at post method
```
POST /v2.0/er_physical_interfaces
```
```
{
    "er_physical_interface": {
        "connected_ese_port_id": "0078808a-c28e-46e1-887d-8ec65f90c446",
        "device_id": "7a35974a-a19f-49e2-b907-ad7fd8692975",
        "name": "ae0",
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef"
    }
}
```
* Checking JSON data at post method
```
POST /v2.0/er_physical_interfaces
```
```
{
    "er_physical_interface": {
        "connected_ese_port_id": "a6e70af1-386b-4d79-943f-6f44e87f95b3",
        "device_id": "b7e6d8ad-5377-4380-bbb4-1a62566cbd6d",
        "name": "ae0",
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef"
    }
}
```
* Checking JSON data at post method
```
POST /v2.0/er_physical_interfaces
```
```
{
    "er_physical_interface": {
        "device_id": "b7e6d8ad-5377-4380-bbb4-1a62566cbd6d",
        "name": "ge-0/0/1",
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef"
    }
}
```
After processing, Gohan has stored data for "Create Er Physical Interface" in etcd.

* [Checking stored data for creating "ge-0/0/1"](stored_in_etcd/01_Gohan/CreateErPhysicalInterface_01.md)
* [Checking stored data for creating "ae0"](stored_in_etcd/01_Gohan/CreateErPhysicalInterface_02.md)
* [Checking stored data for creating "ae0"](stored_in_etcd/01_Gohan/CreateErPhysicalInterface_03.md)
* [Checking stored data for creating "ge-0/0/1"](stored_in_etcd/01_Gohan/CreateErPhysicalInterface_04.md)


## 5.2. ResourceReader
When ResourceReader has started, it gets all of schemas from Gohan.
After that, these schemas are converted as a template_mappings.
And then, ResourceReader keeps storing template_mappings for following processing.

### Reference
* [Checking schemas in ResourceReader](../memo/schemas.txt)
* [Checking template_mappings in ResourceReader](../memo/template_mappings.md)

![scope](../images/ESI_Sequence_diagram.003.png)

### Outline
After fetching resource_data for "Create Er Physical Interface" in etcd, ResourceReader has fetched heat_templates in etcd.

* [Checking stored data for "er_physical_interface"](../heat_template/er_physical_interface.md)


## 5.3. JobManager

![scope](../images/ESI_Sequence_diagram.004.png)

### Outline
After converting resource_data to job_data, JobManager has stored it in etcd.

* [Checking stored data for creating "ge-0/0/1"](stored_in_etcd/02_JobManager/CreateErPhysicalInterface_01.md)
* [Checking stored data for creating "ae0"](stored_in_etcd/02_JobManager/CreateErPhysicalInterface_02.md)
* [Checking stored data for creating "ae0"](stored_in_etcd/02_JobManager/CreateErPhysicalInterface_03.md)
* [Checking stored data for creating "ge-0/0/1"](stored_in_etcd/02_JobManager/CreateErPhysicalInterface_04.md)


## 5.4. HeatWorker

![scope](../images/ESI_Sequence_diagram.005.png)

### Outline
After fetching job_data, HeatWorker has handled job_data.
And then, HeatWorker has stored the result of handling job_data.

* [Checking stored data for creating "ge-0/0/1"](stored_in_etcd/03_HeatWorker/CreateErPhysicalInterface_01.md)
* [Checking stored data for creating "ae0"](stored_in_etcd/03_HeatWorker/CreateErPhysicalInterface_02.md)
* [Checking stored data for creating "ae0"](stored_in_etcd/03_HeatWorker/CreateErPhysicalInterface_03.md)
* [Checking stored data for creating "ge-0/0/1"](stored_in_etcd/03_HeatWorker/CreateErPhysicalInterface_04.md)


## 5.5. Heat

![scope](../images/ESI_Sequence_diagram.006.png)

### Outline
Heat has conducted some tasks for "Create Er Physical Interface".
As a result, Heat has stored heat-stacks for "Create Er Physical Interface".

* [Checking heat-stack of "ge-0/0/1"](heat-stack/CreateErPhysicalInterface_01.md)
* [Checking heat-stack of "ae0"](heat-stack/CreateErPhysicalInterface_02.md)
* [Checking heat-stack of "ae0"](heat-stack/CreateErPhysicalInterface_03.md)
* [Checking heat-stack of "ge-0/0/1"](heat-stack/CreateErPhysicalInterface_04.md)


## 5.6. CollectorAgent

![scope](../images/ESI_Sequence_diagram.007.png)

### Outline
CollectorAgent has conducted some tasks for "Create Er Physical Interface" based heat-stacks via Heat.
As a result, CollectorAgent has responded the result of status information as handling tasks.

* [Checking monitoring of "ge-0/0/1"](collector_agents/CreateErPhysicalInterface_01.md)
* [Checking monitoring of "ae0"](collector_agents/CreateErPhysicalInterface_02.md)
* [Checking monitoring of "ae0"](collector_agents/CreateErPhysicalInterface_03.md)
* [Checking monitoring of "ge-0/0/1"](collector_agents/CreateErPhysicalInterface_04.md)

And then, CollectorAgent has stored the result of status information.

* [Checking stored data for creating "ge-0/0/1"](stored_in_etcd/04_CollectorAgent/CreateErPhysicalInterface_01.md)
* [Checking stored data for creating "ae0"](stored_in_etcd/04_CollectorAgent/CreateErPhysicalInterface_02.md)
* [Checking stored data for creating "ae0"](stored_in_etcd/04_CollectorAgent/CreateErPhysicalInterface_03.md)
* [Checking stored data for creating "ge-0/0/1"](stored_in_etcd/04_CollectorAgent/CreateErPhysicalInterface_04.md)


## 5.7. Stored resource in gohan
As a result, checking resources regarding of "Er Physical Interface" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client er_physical_interface show --output-format json f3ecf585-5c3b-445a-97a7-d8e124c99e16
{
    "er_physical_interface": {
        "connected_ese_port_id": null,
        "description": "",
        "device_id": "7a35974a-a19f-49e2-b907-ad7fd8692975",
        "id": "f3ecf585-5c3b-445a-97a7-d8e124c99e16",
        "name": "ge-0/0/1",
        "operational_state": "UP",
        "orchestration_state": "CREATE_COMPLETE",
        "status": "ACTIVE",
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef"
    }
}
```
```
$ gohan client er_physical_interface show --output-format json 3118d6be-b1cb-472a-805f-7e1ec46aa5e7
{
    "er_physical_interface": {
        "connected_ese_port_id": "0078808a-c28e-46e1-887d-8ec65f90c446",
        "description": "",
        "device_id": "7a35974a-a19f-49e2-b907-ad7fd8692975",
        "id": "3118d6be-b1cb-472a-805f-7e1ec46aa5e7",
        "name": "ae0",
        "operational_state": "UP",
        "orchestration_state": "CREATE_COMPLETE",
        "status": "ACTIVE",
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef"
    }
}
```
```
$ gohan client er_physical_interface show --output-format json c8e2d558-02ee-4bf3-ba5b-958821a21043
{
    "er_physical_interface": {
        "connected_ese_port_id": "a6e70af1-386b-4d79-943f-6f44e87f95b3",
        "description": "",
        "device_id": "b7e6d8ad-5377-4380-bbb4-1a62566cbd6d",
        "id": "c8e2d558-02ee-4bf3-ba5b-958821a21043",
        "name": "ae0",
        "operational_state": "UP",
        "orchestration_state": "CREATE_COMPLETE",
        "status": "ACTIVE",
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef"
    }
}
```
```
$ gohan client er_physical_interface show --output-format json 2bc8e40d-ab01-4738-a4aa-e69d8fd30688
{
    "er_physical_interface": {
        "connected_ese_port_id": null,
        "description": "",
        "device_id": "b7e6d8ad-5377-4380-bbb4-1a62566cbd6d",
        "id": "2bc8e40d-ab01-4738-a4aa-e69d8fd30688",
        "name": "ge-0/0/1",
        "operational_state": "UP",
        "orchestration_state": "CREATE_COMPLETE",
        "status": "ACTIVE",
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef"
    }
}
```


[Return to Previous Page](00_vpn_gateway.md)
