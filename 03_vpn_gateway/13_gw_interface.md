[Return to Previous Page](00_vpn_gateway.md)

# 13. Clarification of interface in Sequence Diagram "Create Gw Interface"
You can see the relations of "Gw Interface" as following.

![Gw Interface](resource/gohan_investigate_for_vpngw.014.png)


## 13.1. Gohan

![scope](../images/ESI_Sequence_diagram.002.png)

### Outline
First of all, Gohan has received JSON data for "Create Gw Interface" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/gw_interfaces
```
```
{
    "gw_interface": {
        "description": "Sample Gw-interface",
        "gw_vipv4": "172.16.101.151",
        "name": "sample-gw-interface",
        "netmask": 24,
        "network_id": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2",
        "primary_ipv4": "172.16.101.152",
        "secondary_ipv4": "172.16.101.153",
        "service_type": "vpn",
        "vrid": 20,
        "vpn_gw_id": "b1da850c-3344-4de2-aa18-d96a30b54f69",
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef"
    }
}
```
After processing, Gohan has stored data for "Create Gw Interface" in etcd.

* [Checking stored data for creating "gw_interface"](stored_in_etcd/01_Gohan/CreateGwInterface_01.md)
* [Checking stored data for creating "port (172.16.101.151,152 / device_owner:"network:gw_interface" / attached:false)"](stored_in_etcd/01_Gohan/CreateGwInterface_02.md)
* [Checking stored data for creating "ese_logical_port (xe-0/0/3.1025)"](stored_in_etcd/01_Gohan/CreateGwInterface_03.md)
* [Checking stored data for creating "port (172.16.101.153 / device_owner:"network:gw_interface" / attached:false)"](stored_in_etcd/01_Gohan/CreateGwInterface_04.md)
* [Checking stored data for creating "ese_logical_port (xe-0/0/4.1025)"](stored_in_etcd/01_Gohan/CreateGwInterface_05.md)
* [Checking stored data for creating "port (172.16.101.153 / device_owner:"network:gw_interface" / attached:true)"](stored_in_etcd/01_Gohan/CreateGwInterface_06.md)
* [Checking stored data for creating "port (172.16.101.151,152 / device_owner:"network:gw_interface" / attached:true)"](stored_in_etcd/01_Gohan/CreateGwInterface_07.md)


## 13.2. ResourceReader
When ResourceReader has started, it gets all of schemas from Gohan.
After that, these schemas are converted as a template_mappings.
And then, ResourceReader keeps storing template_mappings for following processing.

### Reference
* [Checking schemas in ResourceReader](../memo/schemas.txt)
* [Checking template_mappings in ResourceReader](../memo/template_mappings.md)

![scope](../images/ESI_Sequence_diagram.003.png)

### Outline
After fetching resource_data for "Create Gw Interface" in etcd, ResourceReader has fetched heat_templates in etcd.

* [Checking stored data for "gw_interface_internet"](../heat_template/gw_interface_internet.md)
* [Checking stored data for "port"](../heat_template/port.md)
* [Checking stored data for "ese_logical_port"](../heat_template/ese_logical_port.md)


## 13.3. JobManager

![scope](../images/ESI_Sequence_diagram.004.png)

### Outline
After converting resource_data to job_data, JobManager has stored it in etcd.

* [Checking stored data for creating "gw_interface"](stored_in_etcd/02_JobManager/CreateGwInterface_01.md)
* [Checking stored data for creating "port (172.16.101.151,152 / device_owner:"network:gw_interface" / attached:false)"](stored_in_etcd/02_JobManager/CreateGwInterface_02.md)
* [Checking stored data for creating "ese_logical_port (xe-0/0/3.1025)"](stored_in_etcd/02_JobManager/CreateGwInterface_03.md)
* [Checking stored data for creating "port (172.16.101.153 / device_owner:"network:gw_interface" / attached:false)"](stored_in_etcd/02_JobManager/CreateGwInterface_04.md)
* [Checking stored data for creating "ese_logical_port (xe-0/0/4.1025)"](stored_in_etcd/02_JobManager/CreateGwInterface_05.md)
* [Checking stored data for creating "port (172.16.101.153 / device_owner:"network:gw_interface" / attached:true)"](stored_in_etcd/02_JobManager/CreateGwInterface_06.md)
* [Checking stored data for creating "port (172.16.101.151,152 / device_owner:"network:gw_interface" / attached:true)"](stored_in_etcd/02_JobManager/CreateGwInterface_07.md)


## 13.4. HeatWorker

![scope](../images/ESI_Sequence_diagram.005.png)

### Outline
After fetching job_data, HeatWorker has handled job_data.
And then, HeatWorker has stored the result of handling job_data.

* [Checking stored data for creating "gw_interface"](stored_in_etcd/03_HeatWorker/CreateGwInterface_01.md)
* [Checking stored data for creating "port (172.16.101.151,152 / device_owner:"network:gw_interface" / attached:false)"](stored_in_etcd/03_HeatWorker/CreateGwInterface_02.md)
* [Checking stored data for creating "ese_logical_port (xe-0/0/3.1025)"](stored_in_etcd/03_HeatWorker/CreateGwInterface_03.md)
* [Checking stored data for creating "port (172.16.101.153 / device_owner:"network:gw_interface" / attached:false)"](stored_in_etcd/03_HeatWorker/CreateGwInterface_04.md)
* [Checking stored data for creating "ese_logical_port (xe-0/0/4.1025)"](stored_in_etcd/03_HeatWorker/CreateGwInterface_05.md)
* [Checking stored data for creating "port (172.16.101.153 / device_owner:"network:gw_interface" / attached:true)"](stored_in_etcd/03_HeatWorker/CreateGwInterface_06.md)
* [Checking stored data for creating "port (172.16.101.151,152 / device_owner:"network:gw_interface" / attached:true)"](stored_in_etcd/03_HeatWorker/CreateGwInterface_07.md)


## 13.5. Heat

![scope](../images/ESI_Sequence_diagram.006.png)

### Outline
Heat has conducted some tasks for "Create Gw Interface".
As a result, Heat has stored heat-stacks for "Create Gw Interface".

* [Checking heat-stack of "gw_interface"](heat-stack/CreateGwInterface_01.md)
* [Checking heat-stack of "ese_logical_port"](heat-stack/CreateGwInterface_02.md)
* [Checking heat-stack of "ese_logical_port"](heat-stack/CreateGwInterface_03.md)
* [Checking heat-stack of "port"](heat-stack/CreateGwInterface_04.md)
* [Checking heat-stack of "port"](heat-stack/CreateGwInterface_05.md)


## 13.6. CollectorAgent

![scope](../images/ESI_Sequence_diagram.007.png)

### Outline
CollectorAgent has conducted some tasks for "Create Gw Interface" based heat-stacks via Heat.
As a result, CollectorAgent has responded the result of status information as handling tasks.

* [Checking monitoring of "gw_interface"](collector_agents/CreateGwInterface_01.md)
* [Checking monitoring of "ese_logical_port"](collector_agents/CreateGwInterface_02.md)
* [Checking monitoring of "ese_logical_port"](collector_agents/CreateGwInterface_03.md)
* [Checking monitoring of "port"](collector_agents/CreateGwInterface_04.md)
* [Checking monitoring of "port"](collector_agents/CreateGwInterface_05.md)

And then, CollectorAgent has stored the result of status information.

* [Checking stored data for creating "gw_interface"](stored_in_etcd/04_CollectorAgent/CreateGwInterface_01.md)
* [Checking stored data for creating "ese_logical_port (xe-0/0/3.1025)"](stored_in_etcd/04_CollectorAgent/CreateGwInterface_03.md)
* [Checking stored data for creating "ese_logical_port (xe-0/0/4.1025)"](stored_in_etcd/04_CollectorAgent/CreateGwInterface_05.md)
* [Checking stored data for creating "port (172.16.101.153 / device_owner:"network:gw_interface" / attached:true)"](stored_in_etcd/04_CollectorAgent/CreateGwInterface_06.md)
* [Checking stored data for creating "port (172.16.101.151,152 / device_owner:"network:gw_interface" / attached:true)"](stored_in_etcd/04_CollectorAgent/CreateGwInterface_07.md)


## 13.7. Applying JUNOS Configurations via netconf
Checking configuration in Edge Router

* MX-1
```
[edit interfaces ae0 unit 1025 family inet]
+       address 172.16.101.153/24 {
+           vrrp-group 20 {
+               virtual-address 172.16.101.151;
+               priority 100;
+           }
+       }
```
```
[edit routing-instances vrf_gw_sample-ha-router-downlink_1025 protocols bgp]
       group CloudGW1 { ... }
+      group inet-gw-group {
+          apply-groups VPNGW2-RI-IBGP;
+          local-address 172.16.101.153;
+          peer-as 65101;
+          neighbor 172.16.101.152;
+      }

[edit]
```

* MX-2
```
[edit interfaces ae0 unit 1025 family inet]
+       address 172.16.101.152/24 {
+           vrrp-group 20 {
+               virtual-address 172.16.101.151;
+               priority 105;
+           }
+       }
```
```
[edit routing-instances vrf_gw_sample-ha-router-downlink_1025 protocols bgp]
       group CloudGW1 { ... }
+      group inet-gw-group {
+          apply-groups VPNGW1-RI-IBGP;
+          local-address 172.16.101.152;
+          peer-as 65101;
+          neighbor 172.16.101.153;
+      }

[edit]
```

## 13.8. Stored resource in gohan
As a result, checking resources regarding of "Gw Interface" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client gw_interface show --output-format json 3dbcfce5-bca5-4182-991a-c23de685fcf1
{
    "gw_interface": {
        "aws_gw_id": null,
        "azure_gw_id": null,
        "description": "Sample Gw-interface",
        "gcp_gw_id": null,
        "gw_vipv4": "172.16.101.151",
        "gw_vipv6": null,
        "id": "3dbcfce5-bca5-4182-991a-c23de685fcf1",
        "interdc_gw_id": null,
        "internet_gw_id": null,
        "name": "sample-gw-interface",
        "netmask": 24,
        "network_id": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2",
        "operational_state": "UP",
        "orchestration_state": "CREATE_COMPLETE",
        "primary_ipv4": "172.16.101.152",
        "primary_ipv6": null,
        "public_ip_id": null,
        "secondary_ipv4": "172.16.101.153",
        "secondary_ipv6": null,
        "service_type": "vpn",
        "status": "ACTIVE",
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
        "vpn_gw_id": "b1da850c-3344-4de2-aa18-d96a30b54f69",
        "vrid": 20
    }
}
```
* Checking another resources via gohan client
```
$ gohan client ese_logical_port show --output-format json 257d0a9f-d5ae-4a93-9af4-81ad611e1b0d
{
    "ese_logical_port": {
        "common_function_gateway_id": null,
        "connected_resource": "gw_interface",
        "description": "ESE Logical port for Port 53eeb091-3297-4b9b-a200-b6568567e387",
        "ese_physical_port_id": "a6e70af1-386b-4d79-943f-6f44e87f95b3",
        "gw_interface_id": "3dbcfce5-bca5-4182-991a-c23de685fcf1",
        "id": "257d0a9f-d5ae-4a93-9af4-81ad611e1b0d",
        "name": "xe-0/0/4.1025",
        "network_id": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2",
        "operational_state": "UP",
        "orchestration_state": "CREATE_COMPLETE",
        "port_ids": [
            "53eeb091-3297-4b9b-a200-b6568567e387"
        ],
        "status": "ACTIVE",
        "tags": {},
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
        "type": "L2",
        "vlan_id": 1025
    }
}
```
```
$ gohan client port show --output-format json 53eeb091-3297-4b9b-a200-b6568567e387
{
    "port": {
        "admin_state_up": true,
        "allowed_address_pairs": [],
        "attached": true,
        "binding:vif_type": "vrouter",
        "description": "",
        "device_id": "3dbcfce5-bca5-4182-991a-c23de685fcf1",
        "device_owner": "network:gw_interface",
        "ese_logical_port_id": "257d0a9f-d5ae-4a93-9af4-81ad611e1b0d",
        "fake_delete": false,
        "fixed_ips": [
            {
                "ip_address": "172.16.101.153",
                "subnet_id": "e825f4e4-ba44-4d9e-9578-a31ad45bedda"
            }
        ],
        "id": "53eeb091-3297-4b9b-a200-b6568567e387",
        "mac_address": "fa:16:3e:7b:6f:90",
        "managed_by_service": true,
        "name": "Port for : a6e70af1-386b-4d79-943f-6f44e87f95b3",
        "network_id": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2",
        "operational_state": "FAIL",
        "orchestration_state": "UPDATE_COMPLETE",
        "security_groups": [],
        "segmentation_id": 1025,
        "segmentation_type": "vlan",
        "status": "MONITORING_UNAVAILABLE",
        "tags": {},
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef"
    }
}
```
```
$ gohan client ese_logical_port show --output-format json e30fdd19-2f48-422e-9c68-7c59a0e2fae8
{
    "ese_logical_port": {
        "common_function_gateway_id": null,
        "connected_resource": "gw_interface",
        "description": "ESE Logical port for Port 5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b",
        "ese_physical_port_id": "0078808a-c28e-46e1-887d-8ec65f90c446",
        "gw_interface_id": "3dbcfce5-bca5-4182-991a-c23de685fcf1",
        "id": "e30fdd19-2f48-422e-9c68-7c59a0e2fae8",
        "name": "xe-0/0/3.1025",
        "network_id": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2",
        "operational_state": "UP",
        "orchestration_state": "CREATE_COMPLETE",
        "port_ids": [
            "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b"
        ],
        "status": "ACTIVE",
        "tags": {},
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
        "type": "L2",
        "vlan_id": 1025
    }
}
```
```
$ gohan client port show --output-format json 5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b
{
    "port": {
        "admin_state_up": true,
        "allowed_address_pairs": [],
        "attached": true,
        "binding:vif_type": "vrouter",
        "description": "",
        "device_id": "3dbcfce5-bca5-4182-991a-c23de685fcf1",
        "device_owner": "network:gw_interface",
        "ese_logical_port_id": "e30fdd19-2f48-422e-9c68-7c59a0e2fae8",
        "fake_delete": false,
        "fixed_ips": [
            {
                "ip_address": "172.16.101.151",
                "subnet_id": "e825f4e4-ba44-4d9e-9578-a31ad45bedda"
            },
            {
                "ip_address": "172.16.101.152",
                "subnet_id": "e825f4e4-ba44-4d9e-9578-a31ad45bedda"
            }
        ],
        "id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b",
        "mac_address": "fa:16:3e:7b:eb:e8",
        "managed_by_service": true,
        "name": "Port for : 0078808a-c28e-46e1-887d-8ec65f90c446",
        "network_id": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2",
        "operational_state": "UP",
        "orchestration_state": "UPDATE_COMPLETE",
        "security_groups": [],
        "segmentation_id": 1025,
        "segmentation_type": "vlan",
        "status": "ACTIVE",
        "tags": {},
        "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef"
    }
}
```
* Checking another resources via neutron client
```
$ neutron port-list
+--------------------------------------+-------------------------------------------------+-------------------+---------------------------------------------------------------------------------------+
| id                                   | name                                            | mac_address       | fixed_ips                                                                             |
+--------------------------------------+-------------------------------------------------+-------------------+---------------------------------------------------------------------------------------+
| 53eeb091-3297-4b9b-a200-b6568567e387 | Port for : a6e70af1-386b-4d79-943f-6f44e87f95b3 | fa:16:3e:7b:6f:90 | {"subnet_id": "e825f4e4-ba44-4d9e-9578-a31ad45bedda", "ip_address": "172.16.101.153"} |
| 5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b | Port for : 0078808a-c28e-46e1-887d-8ec65f90c446 | fa:16:3e:7b:eb:e8 | {"subnet_id": "e825f4e4-ba44-4d9e-9578-a31ad45bedda", "ip_address": "172.16.101.151"} |
|                                      |                                                 |                   | {"subnet_id": "e825f4e4-ba44-4d9e-9578-a31ad45bedda", "ip_address": "172.16.101.152"} |
  ...
+--------------------------------------+-------------------------------------------------+-------------------+---------------------------------------------------------------------------------------+
```
```
$ neutron port-show 53eeb091-3297-4b9b-a200-b6568567e387
+-----------------------+---------------------------------------------------------------------------------------+
| Field                 | Value                                                                                 |
+-----------------------+---------------------------------------------------------------------------------------+
| admin_state_up        | True                                                                                  |
| allowed_address_pairs |                                                                                       |
| attached              | True                                                                                  |
| binding:vif_type      | vrouter                                                                               |
| description           |                                                                                       |
| device_id             | 3dbcfce5-bca5-4182-991a-c23de685fcf1                                                  |
| device_owner          | network:gw_interface                                                                  |
| ese_logical_port_id   | 257d0a9f-d5ae-4a93-9af4-81ad611e1b0d                                                  |
| fake_delete           | False                                                                                 |
| fixed_ips             | {"subnet_id": "e825f4e4-ba44-4d9e-9578-a31ad45bedda", "ip_address": "172.16.101.153"} |
| id                    | 53eeb091-3297-4b9b-a200-b6568567e387                                                  |
| mac_address           | fa:16:3e:7b:6f:90                                                                     |
| managed_by_service    | True                                                                                  |
| name                  | Port for : a6e70af1-386b-4d79-943f-6f44e87f95b3                                       |
| network_id            | afa0d9d6-84dc-4755-9c6e-db2f23f9dde2                                                  |
| operational_state     | FAIL                                                                                  |
| orchestration_state   | UPDATE_COMPLETE                                                                       |
| security_groups       |                                                                                       |
| segmentation_id       | 1025                                                                                  |
| segmentation_type     | vlan                                                                                  |
| status                | MONITORING_UNAVAILABLE                                                                |
| tags                  | {}                                                                                    |
| tenant_id             | b3e3095c0a5b4383805efe9cf2a6b5ef                                                      |
+-----------------------+---------------------------------------------------------------------------------------+
```
```
$ neutron port-show 5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b
+-----------------------+---------------------------------------------------------------------------------------+
| Field                 | Value                                                                                 |
+-----------------------+---------------------------------------------------------------------------------------+
| admin_state_up        | True                                                                                  |
| allowed_address_pairs |                                                                                       |
| attached              | True                                                                                  |
| binding:vif_type      | vrouter                                                                               |
| description           |                                                                                       |
| device_id             | 3dbcfce5-bca5-4182-991a-c23de685fcf1                                                  |
| device_owner          | network:gw_interface                                                                  |
| ese_logical_port_id   | e30fdd19-2f48-422e-9c68-7c59a0e2fae8                                                  |
| fake_delete           | False                                                                                 |
| fixed_ips             | {"subnet_id": "e825f4e4-ba44-4d9e-9578-a31ad45bedda", "ip_address": "172.16.101.151"} |
|                       | {"subnet_id": "e825f4e4-ba44-4d9e-9578-a31ad45bedda", "ip_address": "172.16.101.152"} |
| id                    | 5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b                                                  |
| mac_address           | fa:16:3e:7b:eb:e8                                                                     |
| managed_by_service    | True                                                                                  |
| name                  | Port for : 0078808a-c28e-46e1-887d-8ec65f90c446                                       |
| network_id            | afa0d9d6-84dc-4755-9c6e-db2f23f9dde2                                                  |
| operational_state     | UP                                                                                    |
| orchestration_state   | UPDATE_COMPLETE                                                                       |
| security_groups       |                                                                                       |
| segmentation_id       | 1025                                                                                  |
| segmentation_type     | vlan                                                                                  |
| status                | ACTIVE                                                                                |
| tags                  | {}                                                                                    |
| tenant_id             | b3e3095c0a5b4383805efe9cf2a6b5ef                                                      |
+-----------------------+---------------------------------------------------------------------------------------+
```


[Return to Previous Page](00_vpn_gateway.md)
