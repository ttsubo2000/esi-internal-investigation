[Return to Previous Page](00_firewall.md)

# 8. Clarification of interface in Sequence Diagram "Create Firewall"
You can see the relations of "Firewall" as following.

![Firewall](resource/gohan_investigate_for_firewall.009.png)


## 8.1. Gohan

![scope](../images/ESI_Sequence_diagram.002.png)

### Outline
First of all, Gohan has received JSON data for "Create Firewall" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/firewalls
```
```
{
    "firewall": {
        "availability_zone": "nova",
        "default_gateway": "192.168.1.1",
        "firewall_plan_id": "40520774-4f10-4e8c-90fa-550bd4cdf101",
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099"
    }
}
```
After processing, Gohan has stored data for "Create Firewall" in etcd.

* [Checking stored data for creating "port (100.64.193.3 / device_owner:"")"](stored_in_etcd/01_Gohan/CreateFirewall_01.md)
* [Checking stored data for creating "port (10.121.232.3 / device_owner:"")"](stored_in_etcd/01_Gohan/CreateFirewall_02.md)
* [Checking stored data for creating "port (10.121.232.4 / device_owner:"")"](stored_in_etcd/01_Gohan/CreateFirewall_03.md)
* [Checking stored data for creating "vnf_instance"](stored_in_etcd/01_Gohan/CreateFirewall_04.md)
* [Checking stored data for creating "vnf_interface (slot_number:0)"](stored_in_etcd/01_Gohan/CreateFirewall_05.md)
* [Checking stored data for creating "vnf_interface (slot_number:1)"](stored_in_etcd/01_Gohan/CreateFirewall_06.md)
* [Checking stored data for creating "vnf_interface (slot_number:2)"](stored_in_etcd/01_Gohan/CreateFirewall_07.md)
* [Checking stored data for creating "firewall"](stored_in_etcd/01_Gohan/CreateFirewall_08.md)
* [Checking stored data for creating "firewall_interface (dp0s5 / slot_number:2)"](stored_in_etcd/01_Gohan/CreateFirewall_09.md)
* [Checking stored data for creating "firewall_interface (dp0s4 / slot_number:1)"](stored_in_etcd/01_Gohan/CreateFirewall_10.md)
* [Checking stored data for creating "firewall_interface (dp0s3 / slot_number:0)"](stored_in_etcd/01_Gohan/CreateFirewall_11.md)
* [Checking stored data for updating "port (100.64.193.3 / device_owner:"compute:nova" / attached:false)"](stored_in_etcd/01_Gohan/CreateFirewall_12.md)
* [Checking stored data for updating "port (100.64.193.3 / device_owner:"compute:nova" / attached:true)"](stored_in_etcd/01_Gohan/CreateFirewall_13.md)
* [Checking stored data for updating "port (10.121.232.3 / device_owner:"compute:nova" / attached:false)"](stored_in_etcd/01_Gohan/CreateFirewall_14.md)
* [Checking stored data for updating "port (10.121.232.3 / device_owner:"compute:nova" / attached:true)"](stored_in_etcd/01_Gohan/CreateFirewall_15.md)
* [Checking stored data for updating "port (10.121.232.4 / device_owner:"compute:nova" / attached:false)"](stored_in_etcd/01_Gohan/CreateFirewall_16.md)
* [Checking stored data for updating "port (10.121.232.4 / device_owner:"compute:nova" / attached:true)"](stored_in_etcd/01_Gohan/CreateFirewall_17.md)


## 8.2. ResourceReader
When ResourceReader has started, it gets all of schemas from Gohan.
After that, these schemas are converted as a template_mappings.
And then, ResourceReader keeps storing template_mappings for following processing.

### Reference
* [Checking schemas in ResourceReader](../memo/schemas.txt)
* [Checking template_mappings in ResourceReader](../memo/template_mappings.md)

![scope](../images/ESI_Sequence_diagram.003.png)

### Outline
After fetching resource_data for "Create Firewall" in etcd, ResourceReader has fetched heat_templates in etcd.

* [Checking stored data for "port"](../heat_template/port.md)
* [Checking stored data for "vnf_instance"](../heat_template/vnf_instance.md)
* [Checking stored data for "firewall_config"](../heat_template/firewall_config.md)
* [Checking stored data for "firewall_interface"](../heat_template/firewall_interface.md)


## 8.3. JobManager

![scope](../images/ESI_Sequence_diagram.004.png)

### Outline
After converting resource_data to job_data, JobManager has stored it in etcd.

* [Checking stored data for creating "port (100.64.193.3 / device_owner:"")"](stored_in_etcd/02_JobManager/CreateFirewall_01.md)
* [Checking stored data for creating "port (10.121.232.3 / device_owner:"")"](stored_in_etcd/02_JobManager/CreateFirewall_02.md)
* [Checking stored data for creating "port (10.121.232.4 / device_owner:"")"](stored_in_etcd/02_JobManager/CreateFirewall_03.md)
* [Checking stored data for creating "vnf_instance"](stored_in_etcd/02_JobManager/CreateFirewall_04.md)
* [Checking stored data for creating "firewall"](stored_in_etcd/02_JobManager/CreateFirewall_08.md)
* [Checking stored data for creating "firewall_interface (dp0s5 / slot_number:2)"](stored_in_etcd/02_JobManager/CreateFirewall_09.md)
* [Checking stored data for creating "firewall_interface (dp0s4 / slot_number:1)"](stored_in_etcd/02_JobManager/CreateFirewall_10.md)
* [Checking stored data for creating "firewall_interface (dp0s3 / slot_number:0)"](stored_in_etcd/02_JobManager/CreateFirewall_11.md)
* [Checking stored data for updating "port (100.64.193.3 / device_owner:"compute:nova" / attached:false)"](stored_in_etcd/02_JobManager/CreateFirewall_12.md)
* [Checking stored data for updating "port (100.64.193.3 / device_owner:"compute:nova" / attached:true)"](stored_in_etcd/02_JobManager/CreateFirewall_13.md)
* [Checking stored data for updating "port (10.121.232.3 / device_owner:"compute:nova" / attached:false)"](stored_in_etcd/02_JobManager/CreateFirewall_14.md)
* [Checking stored data for updating "port (10.121.232.3 / device_owner:"compute:nova" / attached:true)"](stored_in_etcd/02_JobManager/CreateFirewall_15.md)
* [Checking stored data for updating "port (10.121.232.4 / device_owner:"compute:nova" / attached:false)"](stored_in_etcd/02_JobManager/CreateFirewall_16.md)
* [Checking stored data for updating "port (10.121.232.4 / device_owner:"compute:nova" / attached:true)"](stored_in_etcd/02_JobManager/CreateFirewall_17.md)


## 8.4. HeatWorker

![scope](../images/ESI_Sequence_diagram.005.png)

### Outline
After fetching job_data, HeatWorker has handled job_data.
And then, HeatWorker has stored the result of handling job_data.

* [Checking stored data for creating "port (100.64.193.3 / device_owner:"")"](stored_in_etcd/03_HeatWorker/CreateFirewall_01.md)
* [Checking stored data for creating "port (10.121.232.3 / device_owner:"")"](stored_in_etcd/03_HeatWorker/CreateFirewall_02.md)
* [Checking stored data for creating "port (10.121.232.4 / device_owner:"")"](stored_in_etcd/03_HeatWorker/CreateFirewall_03.md)
* [Checking stored data for creating "vnf_instance"](stored_in_etcd/03_HeatWorker/CreateFirewall_04.md)
* [Checking stored data for creating "firewall"](stored_in_etcd/03_HeatWorker/CreateFirewall_08.md)
* [Checking stored data for creating "firewall_interface (dp0s5 / slot_number:2)"](stored_in_etcd/03_HeatWorker/CreateFirewall_09.md)
* [Checking stored data for creating "firewall_interface (dp0s4 / slot_number:1)"](stored_in_etcd/03_HeatWorker/CreateFirewall_10.md)
* [Checking stored data for creating "firewall_interface (dp0s3 / slot_number:0)"](stored_in_etcd/03_HeatWorker/CreateFirewall_11.md)
* [Checking stored data for updating "port (100.64.193.3 / device_owner:"compute:nova" / attached:false)"](stored_in_etcd/03_HeatWorker/CreateFirewall_12.md)
* [Checking stored data for updating "port (100.64.193.3 / device_owner:"compute:nova" / attached:true)"](stored_in_etcd/03_HeatWorker/CreateFirewall_13.md)
* [Checking stored data for updating "port (10.121.232.3 / device_owner:"compute:nova" / attached:false)"](stored_in_etcd/03_HeatWorker/CreateFirewall_14.md)
* [Checking stored data for updating "port (10.121.232.3 / device_owner:"compute:nova" / attached:true)"](stored_in_etcd/03_HeatWorker/CreateFirewall_15.md)
* [Checking stored data for updating "port (10.121.232.4 / device_owner:"compute:nova" / attached:false)"](stored_in_etcd/03_HeatWorker/CreateFirewall_16.md)
* [Checking stored data for updating "port (10.121.232.4 / device_owner:"compute:nova" / attached:true)"](stored_in_etcd/03_HeatWorker/CreateFirewall_17.md)


## 8.5. Heat

![scope](../images/ESI_Sequence_diagram.006.png)

### Outline
Heat has conducted some tasks for "Create Firewall".
As a result, Heat has stored heat-stacks for "Create Firewall".

* [Checking heat-stack of "vnf_instance"](heat-stack/CreateFirewall_01.md)
* [Checking heat-stack of "firewall"](heat-stack/CreateFirewall_02.md)
* [Checking heat-stack of "firewall_interface (dp0s3)"](heat-stack/CreateFirewall_03.md)
* [Checking heat-stack of "firewall_interface (dp0s4)"](heat-stack/CreateFirewall_04.md)
* [Checking heat-stack of "firewall_interface (dp0s5)"](heat-stack/CreateFirewall_05.md)
* [Checking heat-stack of "port (100.64.193.3)"](heat-stack/CreateFirewall_06.md)
* [Checking heat-stack of "port (10.121.232.3)"](heat-stack/CreateFirewall_07.md)
* [Checking heat-stack of "port (10.121.232.4)"](heat-stack/CreateFirewall_08.md)


## 8.6. ESI-Interface between Gohan/heat-engine and Nova-compute

![scope](sequence/gohan_esi_investigating_for_firewall.002.png)


### (1) Creating vnf-instance in nova-comoute
* from heat to nova
```
POST /v2/0f40dffa48614d9baa7eaac7e7532099/servers
```
```
{
    "server": {
        "name": "firewall-8e4c20be-d221-43f4-8325-0162c1f06166",
        "imageRef": "b2cb95f5-1f08-42ae-a1d2-d18b5da04f0c",
        "availability_zone": "nova",
        "flavorRef": "4",
        "max_count": 1,
        "min_count": 1,
        "networks": [
            {
                "port": "cdde9cfd-a898-4911-b812-b6849f611549"
            }
        ]
    }
}
```
* from nova to gohan
```
PUT /v2.0/ports/cdde9cfd-a898-4911-b812-b6849f611549.json
```
```
{
    "port": {
        "device_owner": "compute:nova",
        "device_id": "2e555b09-e0d7-4cce-8854-c481a2363917"
    }
}
```
### (2) Stopping vnf-instace in nova-comoute
* from heat to nova
```
POST /v2/0f40dffa48614d9baa7eaac7e7532099/servers/2e555b09-e0d7-4cce-8854-c481a2363917/action
```
```
{
    "os-stop": null
}
```
### (3) Attaching interface in nova-comoute
* from heat to nova
```
POST /v2/0f40dffa48614d9baa7eaac7e7532099/servers/2e555b09-e0d7-4cce-8854-c481a2363917/os-interface
```
```
{
    "interfaceAttachment": {
        "port_id": "dea87c7b-b43f-4936-8e32-8995b038b3f8"
    }
}
```
* from nova to gohan
```
PUT /v2.0/ports/dea87c7b-b43f-4936-8e32-8995b038b3f8.json
```
```
{
    "port": {
        "device_owner": "compute:nova",
        "device_id": "2e555b09-e0d7-4cce-8854-c481a2363917"
    }
}
```
### (4) Attaching interface in nova-comoute
* from heat to nova
```
POST /v2/0f40dffa48614d9baa7eaac7e7532099/servers/2e555b09-e0d7-4cce-8854-c481a2363917/os-interface
```
```
{
    "interfaceAttachment": {
        "port_id": "fd09eda4-10b1-4534-984a-7124c338c69d"
    }
}
```
* from nova to gohan
```
PUT /v2.0/ports/fd09eda4-10b1-4534-984a-7124c338c69d.json
```
```
{
    "port": {
        "device_owner": "compute:nova",
        "device_id": "2e555b09-e0d7-4cce-8854-c481a2363917"
    }
}
```
### (5) Starting vnf-instace in nova-comoute
* from heat to nova
```
POST /v2/0f40dffa48614d9baa7eaac7e7532099/servers/2e555b09-e0d7-4cce-8854-c481a2363917/action
```
```
{
    "os-start": null
}
```


## 8.7. CollectorAgent

![scope](../images/ESI_Sequence_diagram.007.png)

### Outline
CollectorAgent has conducted some tasks for "Create Firewall" based heat-stacks via Heat.
As a result, CollectorAgent has responded the result of status information as handling tasks.

* [Checking monitoring of "vnf_instance"](collector_agents/CreateFirewall_01.md)
* [Checking monitoring of "firewall_config"](collector_agents/CreateFirewall_02.md)
* [Checking monitoring of "firewall_interface (dp0s5)"](collector_agents/CreateFirewall_03.md)
* [Checking monitoring of "firewall_interface (dp0s3)"](collector_agents/CreateFirewall_04.md)
* [Checking monitoring of "firewall_interface (dp0s4)"](collector_agents/CreateFirewall_05.md)
* [Checking monitoring of "port"](collector_agents/CreateFirewall_06.md)
* [Checking monitoring of "port"](collector_agents/CreateFirewall_07.md)
* [Checking monitoring of "port"](collector_agents/CreateFirewall_08.md)

And then, CollectorAgent has stored the result of status information.

* [Checking stored data for creating "vnf_instance"](stored_in_etcd/04_CollectorAgent/CreateFirewall_04.md)
* [Checking stored data for creating "firewall"](stored_in_etcd/04_CollectorAgent/CreateFirewall_08.md)
* [Checking stored data for creating "firewall_interface (dp0s5 / slot_number:2)"](stored_in_etcd/04_CollectorAgent/CreateFirewall_09.md)
* [Checking stored data for creating "firewall_interface (dp0s4 / slot_number:1)"](stored_in_etcd/04_CollectorAgent/CreateFirewall_10.md)
* [Checking stored data for creating "firewall_interface (dp0s3 / slot_number:0)"](stored_in_etcd/04_CollectorAgent/CreateFirewall_11.md)
* [Checking stored data for updating "port (100.64.193.3 / device_owner:"compute:nova" / attached:true)"](stored_in_etcd/04_CollectorAgent/CreateFirewall_13.md)
* [Checking stored data for updating "port (10.121.232.3 / device_owner:"compute:nova" / attached:true)"](stored_in_etcd/04_CollectorAgent/CreateFirewall_15.md)
* [Checking stored data for updating "port (10.121.232.4 / device_owner:"compute:nova" / attached:true)"](stored_in_etcd/04_CollectorAgent/CreateFirewall_17.md)


## 8.8. Stored resource in gohan
As a result, checking resources regarding of "Firewall" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client firewall show --output-format json 8e4c20be-d221-43f4-8325-0162c1f06166
{
    "firewall": {
        "admin_username": "user-admin",
        "availability_zone": "nova",
        "default_gateway": "192.168.1.1",
        "description": "",
        "firewall_plan_id": "40520774-4f10-4e8c-90fa-550bd4cdf101",
        "id": "8e4c20be-d221-43f4-8325-0162c1f06166",
        "interfaces": [
            {
                "id": "1c351257-d185-40b7-b04a-6272de75d434",
                "ip_address": "100.64.193.3",
                "name": "dp0s3",
                "network_id": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554",
                "operational_state": "UP",
                "orchestration_state": "CREATE_COMPLETE",
                "slot_number": 0,
                "status": "ACTIVE",
                "type": "management",
                "virtual_ip_address": null,
                "virtual_ip_properties": null,
                "vnf_interface_id": "c8fef8f8-a7a1-448f-ae76-81992e598016"
            },
            {
                "id": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a",
                "ip_address": null,
                "name": "dp0s4",
                "network_id": null,
                "operational_state": "UP",
                "orchestration_state": "CREATE_COMPLETE",
                "slot_number": 1,
                "status": "ACTIVE",
                "type": "user",
                "virtual_ip_address": null,
                "virtual_ip_properties": null,
                "vnf_interface_id": "c6cf2771-be40-4d16-ba15-20a62f8b78f6"
            },
            {
                "id": "cdf30a48-8cf7-4935-9f8a-5b51f1177704",
                "ip_address": null,
                "name": "dp0s5",
                "network_id": null,
                "operational_state": "UP",
                "orchestration_state": "CREATE_COMPLETE",
                "slot_number": 2,
                "status": "ACTIVE",
                "type": "user",
                "virtual_ip_address": null,
                "virtual_ip_properties": null,
                "vnf_interface_id": "1e047117-2ca8-43dc-aa80-619b224bab4c"
            }
        ],
        "name": "",
        "networks": [
            {
                "ifname": "dp0s4",
                "type": "disable"
            },
            {
                "ifname": "dp0s5",
                "type": "disable"
            }
        ],
        "operational_state": "UP",
        "orchestration_state": "CREATE_COMPLETE",
        "other_username": "",
        "status": "ACTIVE",
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099",
        "user_username": "user-read",
        "vnf_instance_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb"
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
            "id": "613357ec-62d3-43d8-a1ee-146986f4ace3",
            "info": {},
            "parent_billing_id": null,
            "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166",
            "resource_type": "firewall",
            "started": 1.51842155e+09,
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099",
            "unique_resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
        },
        {
            "config_version": 1,
            "ended": null,
            "id": "b95d379f-4019-4396-8fdf-973d826db114",
            "info": {
                "plan_name": "Brocade_5600_vRouter_3.5R6S3_2CPU-8GB-2IF"
            },
            "parent_billing_id": "613357ec-62d3-43d8-a1ee-146986f4ace3",
            "resource_id": "40520774-4f10-4e8c-90fa-550bd4cdf101",
            "resource_type": "firewall_plan",
            "started": 1.51842155e+09,
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099",
            "unique_resource_id": null
        }
    ]
}
```
* Checking another resources via nova client
```
$ nova show 2e555b09-e0d7-4cce-8854-c481a2363917
+--------------------------------------+----------------------------------------------------------+
| Property                             | Value                                                    |
+--------------------------------------+----------------------------------------------------------+
| OS-DCF:diskConfig                    | MANUAL                                                   |
| OS-EXT-AZ:availability_zone          | nova                                                     |
| OS-EXT-SRV-ATTR:host                 | nova-server                                              |
| OS-EXT-SRV-ATTR:hypervisor_hostname  | nova-server                                              |
| OS-EXT-SRV-ATTR:instance_name        | instance-00000001                                        |
| OS-EXT-STS:power_state               | 1                                                        |
| OS-EXT-STS:task_state                | -                                                        |
| OS-EXT-STS:vm_state                  | active                                                   |
| OS-SRV-USG:launched_at               | 2018-02-12T07:40:10.000000                               |
| OS-SRV-USG:terminated_at             | -                                                        |
| accessIPv4                           |                                                          |
| accessIPv6                           |                                                          |
| adminpod-net network                 | 100.64.193.3                                             |
| config_drive                         |                                                          |
| created                              | 2018-02-12T07:40:09Z                                     |
| dummy-net network                    | 10.121.232.3, 10.121.232.4                               |
| flavor                               | m1.large (4)                                             |
| hostId                               | a1ada0b7af73f0f3e44a99d3a558afdaf2caf52e3fb9910565b4d755 |
| id                                   | 2e555b09-e0d7-4cce-8854-c481a2363917                     |
| image                                | vyatta-0108-2016 (b2cb95f5-1f08-42ae-a1d2-d18b5da04f0c)  |
| key_name                             | -                                                        |
| metadata                             | {}                                                       |
| name                                 | firewall-8e4c20be-d221-43f4-8325-0162c1f06166            |
| os-extended-volumes:volumes_attached | []                                                       |
| progress                             | 0                                                        |
| security_groups                      | default                                                  |
| status                               | ACTIVE                                                   |
| tenant_id                            | 0f40dffa48614d9baa7eaac7e7532099                         |
| updated                              | 2018-02-12T07:44:42Z                                     |
| user_id                              | 0c7ba6a7a9624837929c5953b2a54c93                         |
+--------------------------------------+----------------------------------------------------------+
```
```
$ nova interface-list 2e555b09-e0d7-4cce-8854-c481a2363917
+------------------------+--------------------------------------+--------------------------------------+--------------+-------------------+
| Port State             | Port ID                              | Net ID                               | IP addresses | MAC Addr          |
+------------------------+--------------------------------------+--------------------------------------+--------------+-------------------+
| MONITORING_UNAVAILABLE | cdde9cfd-a898-4911-b812-b6849f611549 | 75c2c3ec-7fe7-494c-a35c-db3f94d3a554 | 100.64.193.3 | fa:16:3e:2f:e8:a6 |
| MONITORING_UNAVAILABLE | dea87c7b-b43f-4936-8e32-8995b038b3f8 | 73b2c401-a1f3-49fb-8612-8c755b37a28d | 10.121.232.3 | fa:16:3e:99:1e:37 |
| ACTIVE                 | fd09eda4-10b1-4534-984a-7124c338c69d | 73b2c401-a1f3-49fb-8612-8c755b37a28d | 10.121.232.4 | fa:16:3e:8e:dd:05 |
+------------------------+--------------------------------------+--------------------------------------+--------------+-------------------+
```
* Checking another resources via neutron client
```
$ neutron port-list | grep -v dhcp-server-port
+--------------------------------------+--------------------------+-------------------+-------------------------------------------------------------------------------------+
| id                                   | name                     | mac_address       | fixed_ips                                                                           |
+--------------------------------------+--------------------------+-------------------+-------------------------------------------------------------------------------------+
| cdde9cfd-a898-4911-b812-b6849f611549 | firewall-management-port | fa:16:3e:2f:e8:a6 | {"subnet_id": "c8090497-34be-456b-9186-377e918f3d50", "ip_address": "100.64.193.3"} |
| dea87c7b-b43f-4936-8e32-8995b038b3f8 | firewall-user-port       | fa:16:3e:99:1e:37 | {"subnet_id": "1244d619-cc55-4bb7-b181-606776ba5e88", "ip_address": "10.121.232.3"} |
| fd09eda4-10b1-4534-984a-7124c338c69d | firewall-user-port       | fa:16:3e:8e:dd:05 | {"subnet_id": "1244d619-cc55-4bb7-b181-606776ba5e88", "ip_address": "10.121.232.4"} |
+--------------------------------------+--------------------------+-------------------+-------------------------------------------------------------------------------------+
```
```
$ neutron port-show cdde9cfd-a898-4911-b812-b6849f611549
+-----------------------+-------------------------------------------------------------------------------------+
| Field                 | Value                                                                               |
+-----------------------+-------------------------------------------------------------------------------------+
| admin_state_up        | True                                                                                |
| allowed_address_pairs |                                                                                     |
| attached              | True                                                                                |
| binding:vif_type      | vrouter                                                                             |
| description           |                                                                                     |
| device_id             | 2e555b09-e0d7-4cce-8854-c481a2363917                                                |
| device_owner          | compute:nova                                                                        |
| ese_logical_port_id   |                                                                                     |
| fake_delete           | True                                                                                |
| fixed_ips             | {"subnet_id": "c8090497-34be-456b-9186-377e918f3d50", "ip_address": "100.64.193.3"} |
| id                    | cdde9cfd-a898-4911-b812-b6849f611549                                                |
| mac_address           | fa:16:3e:2f:e8:a6                                                                   |
| managed_by_service    | False                                                                               |
| name                  | firewall-management-port                                                            |
| network_id            | 75c2c3ec-7fe7-494c-a35c-db3f94d3a554                                                |
| operational_state     | FAIL                                                                                |
| orchestration_state   | UPDATE_COMPLETE                                                                     |
| security_groups       |                                                                                     |
| segmentation_id       | 0                                                                                   |
| segmentation_type     | flat                                                                                |
| status                | MONITORING_UNAVAILABLE                                                              |
| tags                  | {}                                                                                  |
| tenant_id             | 0f40dffa48614d9baa7eaac7e7532099                                                    |
+-----------------------+-------------------------------------------------------------------------------------+
```
```
$ neutron port-show dea87c7b-b43f-4936-8e32-8995b038b3f8
+-----------------------+-------------------------------------------------------------------------------------+
| Field                 | Value                                                                               |
+-----------------------+-------------------------------------------------------------------------------------+
| admin_state_up        | False                                                                               |
| allowed_address_pairs |                                                                                     |
| attached              | True                                                                                |
| binding:vif_type      | vrouter                                                                             |
| description           |                                                                                     |
| device_id             | 2e555b09-e0d7-4cce-8854-c481a2363917                                                |
| device_owner          | compute:nova                                                                        |
| ese_logical_port_id   |                                                                                     |
| fake_delete           | True                                                                                |
| fixed_ips             | {"subnet_id": "1244d619-cc55-4bb7-b181-606776ba5e88", "ip_address": "10.121.232.3"} |
| id                    | dea87c7b-b43f-4936-8e32-8995b038b3f8                                                |
| mac_address           | fa:16:3e:99:1e:37                                                                   |
| managed_by_service    | False                                                                               |
| name                  | firewall-user-port                                                                  |
| network_id            | 73b2c401-a1f3-49fb-8612-8c755b37a28d                                                |
| operational_state     | FAIL                                                                                |
| orchestration_state   | UPDATE_COMPLETE                                                                     |
| security_groups       |                                                                                     |
| segmentation_id       | 0                                                                                   |
| segmentation_type     | flat                                                                                |
| status                | MONITORING_UNAVAILABLE                                                              |
| tags                  | {}                                                                                  |
| tenant_id             | 0f40dffa48614d9baa7eaac7e7532099                                                    |
+-----------------------+-------------------------------------------------------------------------------------+
```
```
$ neutron port-show fd09eda4-10b1-4534-984a-7124c338c69d
+-----------------------+-------------------------------------------------------------------------------------+
| Field                 | Value                                                                               |
+-----------------------+-------------------------------------------------------------------------------------+
| admin_state_up        | False                                                                               |
| allowed_address_pairs |                                                                                     |
| attached              | True                                                                                |
| binding:vif_type      | vrouter                                                                             |
| description           |                                                                                     |
| device_id             | 2e555b09-e0d7-4cce-8854-c481a2363917                                                |
| device_owner          | compute:nova                                                                        |
| ese_logical_port_id   |                                                                                     |
| fake_delete           | True                                                                                |
| fixed_ips             | {"subnet_id": "1244d619-cc55-4bb7-b181-606776ba5e88", "ip_address": "10.121.232.4"} |
| id                    | fd09eda4-10b1-4534-984a-7124c338c69d                                                |
| mac_address           | fa:16:3e:8e:dd:05                                                                   |
| managed_by_service    | False                                                                               |
| name                  | firewall-user-port                                                                  |
| network_id            | 73b2c401-a1f3-49fb-8612-8c755b37a28d                                                |
| operational_state     | UP                                                                                  |
| orchestration_state   | UPDATE_COMPLETE                                                                     |
| security_groups       |                                                                                     |
| segmentation_id       | 0                                                                                   |
| segmentation_type     | flat                                                                                |
| status                | ACTIVE                                                                              |
| tags                  | {}                                                                                  |
| tenant_id             | 0f40dffa48614d9baa7eaac7e7532099                                                    |
+-----------------------+-------------------------------------------------------------------------------------+
```
* Checking another resources via gohan client
```
$ gohan client vnf_instance show --output-format json 44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb
{
    "vnf_instance": {
        "availability_zone": "nova",
        "config_drive": false,
        "description": null,
        "id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb",
        "management_ip": "100.64.193.3",
        "name": "firewall-8e4c20be-d221-43f4-8325-0162c1f06166",
        "networks": [
            {
                "port": "cdde9cfd-a898-4911-b812-b6849f611549"
            },
            {
                "port": "dea87c7b-b43f-4936-8e32-8995b038b3f8"
            },
            {
                "port": "fd09eda4-10b1-4534-984a-7124c338c69d"
            }
        ],
        "operational_state": "UP",
        "orchestration_state": "CREATE_COMPLETE",
        "owner_tenant_id": "0f40dffa48614d9baa7eaac7e7532099",
        "reboot": "",
        "status": "ACTIVE",
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099",
        "user_data": "",
        "user_data_format": "RAW",
        "user_data_parameters": {},
        "vnf_plan_id": "60791395-2267-4553-b115-a38fad3ebf69",
        "vnf_template_id": "5a84974a-9d8b-4887-898b-8e3c095e744d"
    }
}
```
```
$ gohan client port list --output-format json
{
    "ports": [

        ... (snip)

        {
            "admin_state_up": true,
            "allowed_address_pairs": [],
            "attached": true,
            "binding:vif_type": "vrouter",
            "description": "",
            "device_id": "2e555b09-e0d7-4cce-8854-c481a2363917",
            "device_owner": "compute:nova",
            "ese_logical_port_id": null,
            "fake_delete": true,
            "fixed_ips": [
                {
                    "ip_address": "100.64.193.3",
                    "subnet_id": "c8090497-34be-456b-9186-377e918f3d50"
                }
            ],
            "id": "cdde9cfd-a898-4911-b812-b6849f611549",
            "mac_address": "fa:16:3e:2f:e8:a6",
            "managed_by_service": false,
            "name": "firewall-management-port",
            "network_id": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554",
            "operational_state": "FAIL",
            "orchestration_state": "UPDATE_COMPLETE",
            "security_groups": [],
            "segmentation_id": 0,
            "segmentation_type": "flat",
            "status": "MONITORING_UNAVAILABLE",
            "tags": {},
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099"
        },
        {
            "admin_state_up": false,
            "allowed_address_pairs": [],
            "attached": true,
            "binding:vif_type": "vrouter",
            "description": "",
            "device_id": "2e555b09-e0d7-4cce-8854-c481a2363917",
            "device_owner": "compute:nova",
            "ese_logical_port_id": null,
            "fake_delete": true,
            "fixed_ips": [
                {
                    "ip_address": "10.121.232.3",
                    "subnet_id": "1244d619-cc55-4bb7-b181-606776ba5e88"
                }
            ],
            "id": "dea87c7b-b43f-4936-8e32-8995b038b3f8",
            "mac_address": "fa:16:3e:99:1e:37",
            "managed_by_service": false,
            "name": "firewall-user-port",
            "network_id": "73b2c401-a1f3-49fb-8612-8c755b37a28d",
            "operational_state": "FAIL",
            "orchestration_state": "UPDATE_COMPLETE",
            "security_groups": [],
            "segmentation_id": 0,
            "segmentation_type": "flat",
            "status": "MONITORING_UNAVAILABLE",
            "tags": {},
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099"
        },
        {
            "admin_state_up": false,
            "allowed_address_pairs": [],
            "attached": true,
            "binding:vif_type": "vrouter",
            "description": "",
            "device_id": "2e555b09-e0d7-4cce-8854-c481a2363917",
            "device_owner": "compute:nova",
            "ese_logical_port_id": null,
            "fake_delete": true,
            "fixed_ips": [
                {
                    "ip_address": "10.121.232.4",
                    "subnet_id": "1244d619-cc55-4bb7-b181-606776ba5e88"
                }
            ],
            "id": "fd09eda4-10b1-4534-984a-7124c338c69d",
            "mac_address": "fa:16:3e:8e:dd:05",
            "managed_by_service": false,
            "name": "firewall-user-port",
            "network_id": "73b2c401-a1f3-49fb-8612-8c755b37a28d",
            "operational_state": "UP",
            "orchestration_state": "UPDATE_COMPLETE",
            "security_groups": [],
            "segmentation_id": 0,
            "segmentation_type": "flat",
            "status": "ACTIVE",
            "tags": {},
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099"
        }
    ]
}
```
```
$ gohan client vnf_interface list --output-format json
{
    "vnf_interfaces": [
        {
            "description": null,
            "id": "1e047117-2ca8-43dc-aa80-619b224bab4c",
            "ip_address": null,
            "name": "interface-2",
            "network_id": null,
            "port_id": "fd09eda4-10b1-4534-984a-7124c338c69d",
            "slot_number": 2,
            "status": "ACTIVE",
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099",
            "type": "user",
            "virtual_ip_address": null,
            "virtual_ip_properties": null,
            "vnf_instance_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb"
        },
        {
            "description": null,
            "id": "c6cf2771-be40-4d16-ba15-20a62f8b78f6",
            "ip_address": null,
            "name": "interface-1",
            "network_id": null,
            "port_id": "dea87c7b-b43f-4936-8e32-8995b038b3f8",
            "slot_number": 1,
            "status": "MONITORING_UNAVAILABLE",
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099",
            "type": "user",
            "virtual_ip_address": null,
            "virtual_ip_properties": null,
            "vnf_instance_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb"
        },
        {
            "description": null,
            "id": "c8fef8f8-a7a1-448f-ae76-81992e598016",
            "ip_address": "100.64.193.3",
            "name": "interface-0",
            "network_id": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554",
            "port_id": "cdde9cfd-a898-4911-b812-b6849f611549",
            "slot_number": 0,
            "status": "MONITORING_UNAVAILABLE",
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099",
            "type": "management",
            "virtual_ip_address": null,
            "virtual_ip_properties": null,
            "vnf_instance_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb"
        }
    ]
}
```
```
$ gohan client firewall_interface list --output-format json
{
    "firewall_interfaces": [
        {
            "description": null,
            "firewall_id": "8e4c20be-d221-43f4-8325-0162c1f06166",
            "id": "1c351257-d185-40b7-b04a-6272de75d434",
            "ip_address": "100.64.193.3",
            "name": "dp0s3",
            "network_id": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554",
            "operational_state": "UP",
            "orchestration_state": "CREATE_COMPLETE",
            "slot_number": 0,
            "status": "ACTIVE",
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099",
            "type": "management",
            "virtual_ip_address": null,
            "virtual_ip_properties": null,
            "vnf_interface_id": "c8fef8f8-a7a1-448f-ae76-81992e598016"
        },
        {
            "description": null,
            "firewall_id": "8e4c20be-d221-43f4-8325-0162c1f06166",
            "id": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a",
            "ip_address": null,
            "name": "dp0s4",
            "network_id": null,
            "operational_state": "UP",
            "orchestration_state": "CREATE_COMPLETE",
            "slot_number": 1,
            "status": "ACTIVE",
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099",
            "type": "user",
            "virtual_ip_address": null,
            "virtual_ip_properties": null,
            "vnf_interface_id": "c6cf2771-be40-4d16-ba15-20a62f8b78f6"
        },
        {
            "description": null,
            "firewall_id": "8e4c20be-d221-43f4-8325-0162c1f06166",
            "id": "cdf30a48-8cf7-4935-9f8a-5b51f1177704",
            "ip_address": null,
            "name": "dp0s5",
            "network_id": null,
            "operational_state": "UP",
            "orchestration_state": "CREATE_COMPLETE",
            "slot_number": 2,
            "status": "ACTIVE",
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099",
            "type": "user",
            "virtual_ip_address": null,
            "virtual_ip_properties": null,
            "vnf_interface_id": "1e047117-2ca8-43dc-aa80-619b224bab4c"
        }
    ]
}
```

[Return to Previous Page](00_firewall.md)
