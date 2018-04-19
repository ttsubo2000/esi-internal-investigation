[Return to Previous Page](00_internet_gateway.md)

# 2. Clarification of interface in Sequence Diagram "Create Ese Physical Port"
You can see the relations of "Ese Physical Port" as following.

![Ese Physical Port](resource/gohan_investigate_for_inetgw.003.png)


## 2.1. Gohan

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
        "name": "xe-0/0/3",
        "ese_device_id": "3fb53223-b614-46b6-92e8-25c3bcbed214",
        "connected_port_id": "",
        "connected_port_owner": "mx_downlink",
        "tenant_id": "06d6b792b31c40daa546fb0f4e35980d"
    }
}
```
* Checking JSON data at post method
```
POST /v2.0/ese_physical_ports
```
```
{
    "ese_physical_port": {
        "name": "xe-0/0/4",
        "ese_device_id": "3fb53223-b614-46b6-92e8-25c3bcbed214",
        "connected_port_id": "",
        "connected_port_owner": "mx_downlink",
        "tenant_id": "06d6b792b31c40daa546fb0f4e35980d"
    }
}
```
After processing, Gohan has stored data for "Create Ese Physical Port" in etcd.

* [Checking stored data for creating "xe-0/0/3"](stored_in_etcd/01_Gohan/CreateEsePhysicalPort_01.md)
* [Checking stored data for creating "xe-0/0/4"](stored_in_etcd/01_Gohan/CreateEsePhysicalPort_02.md)


## 2.2. ResourceReader
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


## 2.3. JobManager

![scope](../images/ESI_Sequence_diagram.004.png)

### Outline
After converting resource_data to job_data, JobManager has stored it in etcd.

* [Checking stored data for creating "xe-0/0/3"](stored_in_etcd/02_JobManager/CreateEsePhysicalPort_01.md)
* [Checking stored data for creating "xe-0/0/4"](stored_in_etcd/02_JobManager/CreateEsePhysicalPort_02.md)


## 2.4. HeatWorker

![scope](../images/ESI_Sequence_diagram.005.png)

### Outline
After fetching job_data, HeatWorker has handled job_data.
And then, HeatWorker has stored the result of handling job_data.

* [Checking stored data for creating "xe-0/0/3"](stored_in_etcd/03_HeatWorker/CreateEsePhysicalPort_01.md)
* [Checking stored data for creating "xe-0/0/4"](stored_in_etcd/03_HeatWorker/CreateEsePhysicalPort_02.md)


## 2.5. Heat

![scope](../images/ESI_Sequence_diagram.006.png)

### Outline
Heat has conducted some tasks for "Create Ese Physical Port".
As a result, Heat has stored heat-stacks for "Create Ese Physical Port".

* [Checking heat-stack of "xe-0/0/3"](heat-stack/CreateEsePhysicalPort_01.md)
* [Checking heat-stack of "xe-0/0/4"](heat-stack/CreateEsePhysicalPort_02.md)


## 2.6. CollectorAgent

![scope](../images/ESI_Sequence_diagram.007.png)

### Outline
CollectorAgent has conducted some tasks for "Create Ese Physical Port" based heat-stacks via Heat.
As a result, CollectorAgent has responded the result of status information as handling tasks.

* [Checking monitoring of "xe-0/0/3"](collector_agents/CreateEsePhysicalPort_01.md)
* [Checking monitoring of "xe-0/0/4"](collector_agents/CreateEsePhysicalPort_02.md)

And then, CollectorAgent has stored the result of status information.

* [Checking stored data for creating "xe-0/0/3"](stored_in_etcd/04_CollectorAgent/CreateEsePhysicalPort_01.md)
* [Checking stored data for creating "xe-0/0/4"](stored_in_etcd/04_CollectorAgent/CreateEsePhysicalPort_02.md)


## 2.7. Stored resource in gohan
As a result, checking resources regarding of "Ese Physical Port" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client ese_physical_port show --output-format json 887fecdd-956b-47fa-a348-8940c53a5bf9
{   
    "ese_physical_port": {
        "connected_port_id": "",
        "connected_port_owner": "mx_downlink",
        "description": "",
        "ese_device_id": "3fb53223-b614-46b6-92e8-25c3bcbed214",
        "existing": "new",
        "id": "887fecdd-956b-47fa-a348-8940c53a5bf9",
        "name": "xe-0/0/3",
        "operational_state": "UP",
        "orchestration_state": "CREATE_COMPLETE",
        "status": "ACTIVE",
        "tags": {},
        "tenant_id": "06d6b792b31c40daa546fb0f4e35980d"
    }
}
```
```
$ gohan client ese_physical_port show --output-format json 6b29894f-8694-4865-92c1-2e78360e65a6
{
    "ese_physical_port": {
        "connected_port_id": "",
        "connected_port_owner": "mx_downlink",
        "description": "",
        "ese_device_id": "3fb53223-b614-46b6-92e8-25c3bcbed214",
        "existing": "new",
        "id": "6b29894f-8694-4865-92c1-2e78360e65a6",
        "name": "xe-0/0/4",
        "operational_state": "UP",
        "orchestration_state": "CREATE_COMPLETE",
        "status": "ACTIVE",
        "tags": {},
        "tenant_id": "06d6b792b31c40daa546fb0f4e35980d"
    }
}
```


[Return to Previous Page](00_internet_gateway.md)
