[Return to Previous Page](00_internet_gateway.md)

# 13. Clarification of interface in Sequence Diagram "Create Subnet"
You can see the relations of "Subnet" as following.

![Subnet](resource/gohan_investigate_for_inetgw.014.png)


## 13.1. Gohan

![scope](../images/ESI_Sequence_diagram.002.png)

### Outline
First of all, Gohan has received JSON data for "Create Subnet" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/subnets
```
```
{
    "subnet": {
        "description": "Sample Subnet",
        "name": "sample-subnet",
        "tenant_id": "06d6b792b31c40daa546fb0f4e35980d",
        "tags": {},
        "ip_version": 4,
        "cidr": "172.16.101.0/24",
        "network_id": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e"
    }
}
```
After processing, Gohan has stored data for "Create Subnet" in etcd.

* [Checking stored data for creating "subnet"](stored_in_etcd/01_Gohan/CreateSubnet_01.md)
* [Checking stored data for creating "port(dhcp)"](stored_in_etcd/01_Gohan/CreateSubnet_02.md)


## 13.2. ResourceReader
When ResourceReader has started, it gets all of schemas from Gohan.
After that, these schemas are converted as a template_mappings.
And then, ResourceReader keeps storing template_mappings for following processing.

### Reference
* [Checking schemas in ResourceReader](../memo/schemas.txt)
* [Checking template_mappings in ResourceReader](../memo/template_mappings.md)

![scope](../images/ESI_Sequence_diagram.003.png)

### Outline
After fetching resource_data for "Create Subnet" in etcd, ResourceReader has fetched heat_templates in etcd.

* [Checking stored data for "subnet"](../heat_template/subnet.md)

And then, ResourceReader has stored data as finishing resource

* [Checking stored data for creating "port(dhcp)"](stored_in_etcd/00_ResourceReader/CreateSubnet_02.md)


## 13.3. JobManager

![scope](../images/ESI_Sequence_diagram.004.png)

### Outline
After converting resource_data to job_data, JobManager has stored it in etcd.

* [Checking stored data for creating "subnet"](stored_in_etcd/02_JobManager/CreateSubnet_01.md) 


## 13.4. HeatWorker

![scope](../images/ESI_Sequence_diagram.005.png)

### Outline
After fetching job_data, HeatWorker has handled job_data.
And then, HeatWorker has stored the result of handling job_data.

* [Checking stored data for creating "subnet"](stored_in_etcd/03_HeatWorker/CreateSubnet_01.md) 


## 13.5. Heat

![scope](../images/ESI_Sequence_diagram.006.png)

### Outline
Heat has conducted some tasks for "Create Subnet".
As a result, Heat has stored heat-stacks for "Create Subnet".

* [Checking heat-stack of "subnet"](heat-stack/CreateSubnet_01.md)


## 13.6. Stored resource in gohan
As a result, checking resources regarding of "Subnet" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client subnet show --output-format json 67877f2d-0547-4cea-a6ce-2e3b937aa31b
{
    "subnet": {
        "allocation_pools": [
            {
                "end": "172.16.101.254",
                "start": "172.16.101.2"
            }
        ],
        "cidr": "172.16.101.0/24",
        "description": "Sample Subnet",
        "dhcp_server_address": "172.16.101.2",
        "dns_nameservers": [],
        "enable_dhcp": true,
        "gateway_ip": "172.16.101.1",
        "host_routes": [],
        "id": "67877f2d-0547-4cea-a6ce-2e3b937aa31b",
        "ip_version": 4,
        "ipv6_address_mode": null,
        "ipv6_ra_mode": null,
        "name": "sample-subnet",
        "network_id": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e",
        "ntp_servers": [],
        "orchestration_state": "CREATE_COMPLETE",
        "status": "ACTIVE",
        "tags": {},
        "tenant_id": "06d6b792b31c40daa546fb0f4e35980d"
    }
}
```
* Checking another resources via gohan client
```
$ gohan client port show --output-format json 9dc6550a-f4a0-4be0-9e52-f780501926a8
{
    "port": {
        "admin_state_up": true,
        "allowed_address_pairs": [],
        "attached": false,
        "binding:vif_type": "vrouter",
        "description": "DHCP Server Port",
        "device_id": "67877f2d-0547-4cea-a6ce-2e3b937aa31b",
        "device_owner": "network:dhcp",
        "ese_logical_port_id": null,
        "fake_delete": false,
        "fixed_ips": [
            {
                "ip_address": "172.16.101.2",
                "subnet_id": "67877f2d-0547-4cea-a6ce-2e3b937aa31b"
            }
        ],
        "id": "9dc6550a-f4a0-4be0-9e52-f780501926a8",
        "mac_address": "00:00:5e:00:01:00",
        "managed_by_service": false,
        "name": "dhcp-server-port",
        "network_id": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e",
        "operational_state": "",
        "orchestration_state": "SYNC_COMPLETE",
        "security_groups": [],
        "segmentation_id": null,
        "segmentation_type": null,
        "status": "ACTIVE",
        "tags": {},
        "tenant_id": "06d6b792b31c40daa546fb0f4e35980d"
    }
}
```

[Return to Previous Page](00_internet_gateway.md)
