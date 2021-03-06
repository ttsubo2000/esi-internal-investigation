[Return to Previous Page](00_logical_network.md)

# 3. Clarification of interface in Sequence Diagram "Create Ese Physical Port"
You can see the relations of "Ese Physical Port" as following.

![Ese Physical Port](resource/gohan_investigate_for_logicalnetwork.004.png)


## 3.1. Gohan

![scope](../images/ESI_Sequence_diagram.002.png)

### Outline
First of all, Gohan has received JSON data for "Create Ese Physical Port" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/ese_physical_ports
```
```
{
    "ese_physical_port": {
        "connected_port_owner": "physical_port",
        "tenant_id": "ae69b52f46ba480bb9636f62736436f4",
        "existing": "existing",
        "connected_port_id": "7ff183de-0188-46bf-b7d0-68d08ad2b54f",
        "ese_device_id": "718148aa-4483-47d5-bbd1-a0e0738dc018",
        "name": "xe-0/0/1"
    }
}
```
After processing, Gohan has stored data for "Create Ese Physical Port" in etcd.

* [Checking stored data for creating "ese_physical_port"](stored_in_etcd/01_Gohan/CreateEsePhysicalPort_01.md)


## 3.2. ResourceReader
When ResourceReader has started, it gets all of schemas from Gohan.
After that, these schemas are converted as a template_mappings.
And then, ResourceReader keeps storing template_mappings for following processing.

### Reference
* [Checking schemas in ResourceReader](../memo/schemas.txt)
* [Checking template_mappings in ResourceReader](../memo/template_mappings.md)

![scope](../images/ESI_Sequence_diagram.003.png)

### Outline
After fetching resource_data for "Create Ese Physical Port" in etcd, ResourceReader has fetched heat_templates in etcd.

* [Checking stored data for "ese_physical_port_existing"](../heat_template/ese_physical_port_existing.md)


## 3.3. JobManager

![scope](../images/ESI_Sequence_diagram.004.png)

### Outline
After converting resource_data to job_data, JobManager has stored it in etcd.

* [Checking stored data for creating "ese_physical_port"](stored_in_etcd/02_JobManager/CreateEsePhysicalPort_01.md)


## 3.4. HeatWorker

![scope](../images/ESI_Sequence_diagram.005.png)

### Outline
After fetching job_data, HeatWorker has handled job_data.
And then, HeatWorker has stored the result of handling job_data.

* [Checking stored data for creating "ese_physical_port"](stored_in_etcd/03_HeatWorker/CreateEsePhysicalPort_01.md)


## 3.5. Heat

![scope](../images/ESI_Sequence_diagram.006.png)

### Outline
Heat has conducted some tasks for "Create Ese Physical Port".
As a result, Heat has stored heat-stacks for "Create Ese Physical Port".

* [Checking heat-stack of "ese_physical_port"](heat-stack/CreateEsePhysicalPort_01.md)


## 3.6. CollectorAgent

![scope](../images/ESI_Sequence_diagram.007.png)

### Outline
CollectorAgent has conducted some tasks for "Create Ese Physical Port" based heat-stacks via Heat.
As a result, CollectorAgent has responded the result of status information as handling tasks.

* [Checking monitoring of "ese_physical_port"](collector_agents/CreateEsePhysicalPort_01.md)

And then, CollectorAgent has stored the result of status information.

* [Checking stored data for creating "ese_physical_port"](stored_in_etcd/04_CollectorAgent/CreateEsePhysicalPort_01.md)


## 3.7. Stored resource in gohan
As a result, checking resources regarding of "Ese Physical Port" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client ese_physical_port show --output-format json 24dd42cf-b343-47a9-966a-8f7486378c46
{
    "ese_physical_port": {
        "connected_port_id": "7ff183de-0188-46bf-b7d0-68d08ad2b54f",
        "connected_port_owner": "physical_port",
        "description": "",
        "ese_device_id": "718148aa-4483-47d5-bbd1-a0e0738dc018",
        "existing": "existing",
        "id": "24dd42cf-b343-47a9-966a-8f7486378c46",
        "name": "xe-0/0/1",
        "operational_state": "UP",
        "orchestration_state": "CREATE_COMPLETE",
        "status": "ACTIVE",
        "tags": {},
        "tenant_id": "ae69b52f46ba480bb9636f62736436f4"
    }
}
```


[Return to Previous Page](00_logical_network.md)
