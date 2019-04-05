[Return to Previous Page](00_firewall.md)

# 6. Clarification of interface in Sequence Diagram "Create Subnet for user-net"
You can see the relations of "Subnet" as following.

![Subnet](resource/gohan_investigate_for_firewall.007.png)


## 6.1. Gohan

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
        "description": "firewall subnet",
        "name": "sample-fw-subnet",
        "tenant_id": "d2a4608bbd28402196acdba7a1632daf",
        "tags": {},
        "ip_version": 4,
        "cidr": "10.98.77.0/24",
        "network_id": "0422f224-5da3-4f01-8ba5-2ae68f241774"
    }
}
```
After processing, Gohan has stored data for "Create Subnet" in etcd.

* [Checking stored data for creating "subnet"](stored_in_etcd/01_Gohan/CreateSubnet3_01.md)
* [Checking stored data for creating "port(dhcp)"](stored_in_etcd/01_Gohan/CreateSubnet3_02.md)


## 6.2. ResourceReader
When ResourceReader has started, it gets all of schemas from Gohan.
After that, these schemas are converted as a template_mappings.
And then, ResourceReader keeps storing template_mappings for following processing.

### Reference
* [Checking schemas in ResourceReader](../memo/schemas.txt)
* [Checking template_mappings in ResourceReader](../memo/template_mappings.md)
* [Checking _relations in ResourceReader](../memo/_relations.md)

![scope](../images/ESI_Sequence_diagram.003.png)

### Outline
After fetching resource_data for "Create Subnet" in etcd, ResourceReader has fetched heat_templates in etcd.

* [Checking stored data for "subnet"](../heat_template/subnet.md)

And then, ResourceReader has stored data as finishing resource

* [Checking stored data for creating "port(dhcp)"](stored_in_etcd/00_ResourceReader/CreateSubnet3_02.md)


## 6.3. JobManager

![scope](../images/ESI_Sequence_diagram.004.png)

### Outline
After converting resource_data to job_data, JobManager has stored it in etcd.

* [Checking stored data for creating "subnet"](stored_in_etcd/02_JobManager/CreateSubnet3_01.md)


## 6.4. HeatWorker

![scope](../images/ESI_Sequence_diagram.005.png)

### Outline
After fetching job_data, HeatWorker has handled job_data.
And then, HeatWorker has stored the result of handling job_data.

* [Checking stored data for creating "subnet"](stored_in_etcd/03_HeatWorker/CreateSubnet3_01.md)


## 6.5. Heat

![scope](../images/ESI_Sequence_diagram.006.png)

### Outline
Heat has conducted some tasks for "Create Subnet".
As a result, Heat has stored heat-stacks for "Create Subnet".

* [Checking heat-stack of "subnet"](heat-stack/CreateSubnet3_01.md)


## 6.6. Stored resource in gohan
As a result, checking resources regarding of "Subnet" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client subnet show --output-format json 8effd73d-925d-4ec9-9cee-8cffc9aafef3
{
    "subnet": {
        "allocation_pools": [
            {
                "end": "10.98.77.254",
                "start": "10.98.77.2"
            }
        ],
        "cidr": "10.98.77.0/24",
        "description": "firewall subnet",
        "dhcp_server_address": "10.98.77.2",
        "dns_nameservers": [
            "0.0.0.0"
        ],
        "enable_dhcp": true,
        "gateway_ip": "10.98.77.1",
        "host_routes": [],
        "id": "8effd73d-925d-4ec9-9cee-8cffc9aafef3",
        "ip_version": 4,
        "ipv6_address_mode": null,
        "ipv6_ra_mode": null,
        "name": "sample-fw-subnet",
        "network_id": "0422f224-5da3-4f01-8ba5-2ae68f241774",
        "ntp_servers": [],
        "orchestration_state": "CREATE_COMPLETE",
        "status": "ACTIVE",
        "tags": {},
        "tenant_id": "d2a4608bbd28402196acdba7a1632daf"
    }
}
```
* Checking another resources via gohan client
```
$ gohan client port show --output-format json f9fbeb5c-6769-43be-9269-f1c1cbb1248a
{
    "port": {
        "admin_state_up": true,
        "allowed_address_pairs": [],
        "attached": false,
        "binding:vif_type": "vrouter",
        "description": "DHCP Server Port",
        "device_id": "8effd73d-925d-4ec9-9cee-8cffc9aafef3",
        "device_owner": "network:dhcp",
        "ese_logical_port_id": null,
        "fake_delete": false,
        "fixed_ips": [
            {
                "ip_address": "10.98.77.2",
                "subnet_id": "8effd73d-925d-4ec9-9cee-8cffc9aafef3"
            }
        ],
        "id": "f9fbeb5c-6769-43be-9269-f1c1cbb1248a",
        "mac_address": "00:00:5e:00:01:00",
        "managed_by_service": false,
        "name": "dhcp-server-port",
        "network_id": "0422f224-5da3-4f01-8ba5-2ae68f241774",
        "operational_state": "",
        "orchestration_state": "SYNC_COMPLETE",
        "security_groups": [],
        "segmentation_id": null,
        "segmentation_type": null,
        "status": "ACTIVE",
        "tags": {},
        "tenant_id": "d2a4608bbd28402196acdba7a1632daf"
    }
}
```

[Return to Previous Page](00_firewall.md)
