[Return to Previous Page](00_firewall.md)

# 4. Clarification of interface in Sequence Diagram "Create Subnet for dummy-net"
You can see the relations of "Subnet" as following.

![Subnet](resource/gohan_investigate_for_firewall.003.png)


## 4.1. Gohan

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
        "description": "dummy subnet for firewall",
        "name": "dummy-subnet",
        "tenant_id": "d2a4608bbd28402196acdba7a1632daf",
        "tags": {},
        "ip_version": 4,
        "cidr": "10.121.233.0/24",
        "network_id": "3ad67159-9f73-404a-94da-582bda1641fb"
    }
}
```
After processing, Gohan has stored data for "Create Subnet" in etcd.

* [Checking stored data for creating "subnet"](stored_in_etcd/01_Gohan/CreateSubnet1_01.md)
* [Checking stored data for creating "port(dhcp)"](stored_in_etcd/01_Gohan/CreateSubnet1_02.md)


## 4.2. ResourceReader
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

* [Checking stored data for creating "port(dhcp)"](stored_in_etcd/00_ResourceReader/CreateSubnet1_02.md)


## 4.3. JobManager

![scope](../images/ESI_Sequence_diagram.004.png)

### Outline
After converting resource_data to job_data, JobManager has stored it in etcd.

* [Checking stored data for creating "subnet"](stored_in_etcd/02_JobManager/CreateSubnet1_01.md)


## 4.4. HeatWorker

![scope](../images/ESI_Sequence_diagram.005.png)

### Outline
After fetching job_data, HeatWorker has handled job_data.
And then, HeatWorker has stored the result of handling job_data.

* [Checking stored data for creating "subnet"](stored_in_etcd/03_HeatWorker/CreateSubnet1_01.md)


## 4.5. Heat

![scope](../images/ESI_Sequence_diagram.006.png)

### Outline
Heat has conducted some tasks for "Create Subnet".
As a result, Heat has stored heat-stacks for "Create Subnet".

* [Checking heat-stack of "subnet"](heat-stack/CreateSubnet1_01.md)


## 4.6. Stored resource in gohan
As a result, checking resources regarding of "Subnet" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client subnet show --output-format json 0479131c-e828-4721-abaa-a46265518b89
{
    "subnet": {
        "allocation_pools": [
            {
                "end": "10.121.233.254",
                "start": "10.121.233.2"
            }
        ],
        "cidr": "10.121.233.0/24",
        "description": "dummy subnet for firewall",
        "dhcp_server_address": "10.121.233.2",
        "dns_nameservers": [
            "0.0.0.0"
        ],
        "enable_dhcp": true,
        "gateway_ip": "10.121.233.1",
        "host_routes": [],
        "id": "0479131c-e828-4721-abaa-a46265518b89",
        "ip_version": 4,
        "ipv6_address_mode": null,
        "ipv6_ra_mode": null,
        "name": "dummy-subnet",
        "network_id": "3ad67159-9f73-404a-94da-582bda1641fb",
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
$ gohan client port show --output-format json e7894df1-b287-4494-bfe4-d6f989a448d1
{
    "port": {
        "admin_state_up": true,
        "allowed_address_pairs": [],
        "attached": false,
        "binding:vif_type": "vrouter",
        "description": "DHCP Server Port",
        "device_id": "0479131c-e828-4721-abaa-a46265518b89",
        "device_owner": "network:dhcp",
        "ese_logical_port_id": null,
        "fake_delete": false,
        "fixed_ips": [
            {
                "ip_address": "10.121.233.2",
                "subnet_id": "0479131c-e828-4721-abaa-a46265518b89"
            }
        ],
        "id": "e7894df1-b287-4494-bfe4-d6f989a448d1",
        "mac_address": "00:00:5e:00:01:00",
        "managed_by_service": false,
        "name": "dhcp-server-port",
        "network_id": "3ad67159-9f73-404a-94da-582bda1641fb",
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
